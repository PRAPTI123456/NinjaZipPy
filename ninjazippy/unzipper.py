import py7zr
import os
import sys

def unzip_archive(archive_path: str, output_path: str):
    """Unzips a .7z archive to a specified output directory."""
    print(f"🌀 Attempting to extract '{archive_path}' to '{output_path}'...")
    
    if not os.path.exists(archive_path):
        print(f"❌ Error: Archive file not found at '{archive_path}'")
        sys.exit(1)
        
    os.makedirs(output_path, exist_ok=True)
    
    try:
        with py7zr.SevenZipFile(archive_path, mode='r') as z:
            z.extractall(path=output_path)
        print(f"✅ Successfully extracted archive to '{output_path}'")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)