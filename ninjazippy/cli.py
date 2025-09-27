import argparse
# Make sure these imports are correct
from .zipper import zip_content
from .unzipper import unzip_archive

# The error means this function is likely missing or misspelled
def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="NinjaZipPy 🥷: A fast Python utility for .7z archives.",
        epilog="Example: ninjazippy zip my_folder archive.7z"
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # --- Unzip command ---
    parser_unzip = subparsers.add_parser("unzip", help="Unzip a .7z archive.")
    parser_unzip.add_argument("archive_path", type=str, help="Path to the .7z archive.")
    parser_unzip.add_argument("output_path", type=str, help="Directory for extracted files.")

    # --- Zip command ---
    parser_zip = subparsers.add_parser("zip", help="Zip a file or folder into a .7z archive.")
    parser_zip.add_argument("source_path", type=str, help="Path to the source file or folder.")
    parser_zip.add_argument("output_archive", type=str, help="Path for the output .7z archive.")

    args = parser.parse_args()

    if args.command == "unzip":
        unzip_archive(args.archive_path, args.output_path)
    elif args.command == "zip":
        zip_content(args.source_path, args.output_archive)

if __name__ == "__main__":
    main()