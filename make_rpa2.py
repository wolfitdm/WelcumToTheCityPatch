import os
import sys
import zlib
import time
import pickle  # RPA-2.0 uses Python pickles for the index

def write_rpa2(archive_path, input_folder):
    """
    Creates an RPA-2.0 archive from all files in input_folder.
    """
    if not os.path.isdir(input_folder):
        raise ValueError(f"Input folder '{input_folder}' does not exist.")

    # Collect files
    file_entries = {}
    file_data = b""
    offset = 0

    for root, _, files in os.walk(input_folder):
        for fname in files:
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, input_folder).replace("\\", "/")

            with open(full_path, "rb") as f:
                data = f.read()

            length = len(data)
            mtime = int(os.path.getmtime(full_path))

            file_entries[rel_path] = (offset, length, mtime)
            file_data += data
            offset += length

    # Pickle + compress index
    index_pickle = pickle.dumps(file_entries, protocol=2)
    index_compressed = zlib.compress(index_pickle)

    # Write archive
    with open(archive_path, "wb") as out:
        # Header
        out.write(b"RPA-2.0 ")
        out.write(f"{len(index_compressed):08d}".encode("ascii"))
        out.write(b"\n")

        # Index
        out.write(index_compressed)

        # File data
        out.write(file_data)

    print(f"✅ Created RPA-2.0 archive: {archive_path} with {len(file_entries)} files.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python make_rpa2.py <input_folder> <output.rpa>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_rpa = sys.argv[2]

    try:
        write_rpa2(output_rpa, input_folder)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)