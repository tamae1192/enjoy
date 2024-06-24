import argparse
import downloader 
import delete_file
import compress_image

def get_argument():
    parser = argparse.ArgumentParser(description="Process two named arguments.")
    parser.add_argument("--url", required=False, help="")
    parser.add_argument("--src_dir", required=False, help="")
    parser.add_argument("--compressed_dir", required=False, help="")
    parser.add_argument("--delete_dir", required=False, help="")
    
    return parser.parse_args()

if __name__ == "__main__":
    
    args = get_argument()

    src_dir = args.src_dir

    url = args.url
    compressed_dir = args.compressed_dir
    if args.delete_dir:
        delete_file.delete_all_files_in_directory(src_dir)
        delete_file.delete_all_files_in_directory(compressed_dir)    


    downloader.download_notion_images(url, src_dir)

    compress_image.resize_images_in_directory(src_dir,compressed_dir)