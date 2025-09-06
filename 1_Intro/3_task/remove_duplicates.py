import os
import hashlib
from PIL import Image


def get_file_hash(filepath, block_size=65536):
    """Compute SHA256 hash of a file."""
    sha = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(block_size):
            sha.update(chunk)
    return sha.hexdigest()


def find_and_remove_duplicates(directory):
    """
    Find and remove duplicate image files in a directory,
    keeping only one copy of each.
    """
    hashes = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                # Only process image files
                with Image.open(filepath) as img:
                    img.verify()  # Verify it's an image
                file_hash = get_file_hash(filepath)
                if file_hash in hashes:
                    print("Removing duplicate:")
                    print(filepath)
                    os.remove(filepath)
                else:
                    hashes[file_hash] = filepath
            except Exception:
                # Not an image or unreadable file
                continue


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicates.py <directory>")
        sys.exit(1)
    find_and_remove_duplicates(sys.argv[1])
