import os
import sys
import zlib
import struct
import time

# -----------------------------
# Minimal RPA writer (RPAv3)
# -----------------------------
def write_rpa(archive_path, input_folder):
    """
    Creates a .rpa archive from all files in input_folder.
    """
    if not os.path.isdir(input_folder):
        raise ValueError(f"Input folder '{input_folder}' does not exist.")

    # Collect files
    file_entries = {}
    for root, _, files in os.walk(input_folder):
        for fname in files:
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, input_folder).replace("\\", "/")
            with open(full_path, "rb") as f:
                data = f.read()
            compressed = zlib.compress(data)
            file_entries[rel_path] = compressed

    # Write archive
    with open(archive_path, "wb") as out:
        # Write header
        out.write(b"RPA-3.0 ")  # RPAv3 magic
        index_offset_pos = out.tell()
        out.write(b"00000000")  # placeholder for index offset
        out.write(b"\n")

        # Write file data
        index = {}
        for rel_path, compressed in file_entries.items():
            offset = out.tell()
            out.write(compressed)
            index[rel_path] = (offset, len(compressed), len(zlib.decompress(compressed)), time.time())

        # Write index
        index_offset = out.tell()
        import json
        out.write(zlib.compress(json.dumps(index).encode("utf-8")))

        # Go back and write index offset
        out.seek(index_offset_pos)
        out.write(f"{index_offset:08d}".encode("ascii"))

    print(f"✅ Created archive: {archive_path} with {len(file_entries)} files.")


# -----------------------------
# CLI entry point
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python make_rpa.py <input_folder> <output.rpa>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_rpa = sys.argv[2]

    try:
        write_rpa(output_rpa, input_folder)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)