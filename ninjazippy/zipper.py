import py7zr
import os
import sys

def zip_content(source_path: str, output_archive: str):
    """Zips a single file or an entire folder into a .7z archive."""
    print(f"🌀 Attempting to create archive '{output_archive}' from '{source_path}'...")
    
    if not os.path.exists(source_path):
        print(f"❌ Error: Source file or directory not found at '{source_path}'")
        sys.exit(1)

    # Create parent directory for the archive if it doesn't exist
    parent_dir = os.path.dirname(output_archive)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    try:
        with py7zr.SevenZipFile(output_archive, 'w') as z:
            # writeall handles both files and directories correctly
            z.writeall(source_path, os.path.basename(source_path))
        print(f"✅ Successfully created archive '{output_archive}'")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)