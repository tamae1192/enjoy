import argparse
import downloader 
import compress_image

def get_argument():
    parser = argparse.ArgumentParser(description="Process two named arguments.")
    parser.add_argument("--url", required=False, help="")
    parser.add_argument("--src_dir", required=False, help="")
    parser.add_argument("--compressed_dir", required=False, help="")
    
    return parser.parse_args()

if __name__ == "__main__":
    
    args = get_argument()

    src_dir = args.src_dir

    url = args.url
    downloader.delete_all_files_in_directory(src_dir)
    downloader.download_images(url, src_dir)
    
    compressed_dir = args.compressed_dir
    downloader.delete_all_files_in_directory(compressed_dir)    
    compress_image.resize_images_in_directory(src_dir,compressed_dir)