
import os
from PIL import Image
import argparse

def recompress_images_in_directory(src_dir:str, new_dir:str, quality=70):
    """
    ディレクトリ内の全ての画像を指定されたスケールでリサイズします。

    Args:
        directory (str): 画像が保存されているディレクトリのパス。
        scale (float): 画像をリサイズするスケール。0.5で半分のサイズになります。

    """

    os.makedirs(src_dir,exist_ok=True)
    os.makedirs(new_dir,exist_ok=True)

    # サポートされている画像の拡張子
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

    # ディレクトリ内の全てのファイルを処理
    for filename in os.listdir(src_dir):
        if filename.lower().endswith(supported_extensions):
            src_filepath = os.path.join(src_dir, filename)
            new_filepath = os.path.join(new_dir, filename)

            with Image.open(src_filepath) as img:
                img.save(new_filepath, quality=quality, optimize=True)

           
def check_float_range(value:str) -> float:
    """
    0.5以上0.95以下の浮動小数点数であることをチェックする関数。

    Args:
        value (str): コマンドライン引数としての値。

    Returns:
        float: 浮動小数点数値。

    Raises:
        argparse.ArgumentTypeError: 引数が0.5から0.95の範囲外である場合。
    """
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid float value.")

    if fvalue < 0.5 or fvalue > 0.95:
        raise argparse.ArgumentTypeError(f"{value} is an invalid float value. It must be between 0.5 and 0.95.")
    
    return fvalue

def resize_images_in_directory(src_dir:str, new_dir:str, scale=0.5):
    """
    ディレクトリ内の全ての画像を指定されたスケールでリサイズします。

    Args:
        directory (str): 画像が保存されているディレクトリのパス。
        scale (float): 画像をリサイズするスケール。0.5で半分のサイズになります。

    """

    os.makedirs(src_dir,exist_ok=True)
    os.makedirs(new_dir,exist_ok=True)

    # サポートされている画像の拡張子
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

    # ディレクトリ内の全てのファイルを処理
    for filename in os.listdir(src_dir):
        if filename.lower().endswith(supported_extensions):
            src_filepath = os.path.join(src_dir, filename)
            new_filepath = os.path.join(new_dir, filename)

            # 画像を開く
            with Image.open(src_filepath) as img:
                # 現在のサイズを取得
                width, height = img.size

                # 新しいサイズを計算
                new_width = int(width * scale)
                new_height = int(height * scale)

                # 画像をリサイズ
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # 画像を保存（同じファイル名で上書き）
                resized_img.save(new_filepath)
                print(f"Resized {filename} from ({width}, {height}) to ({new_width}, {new_height})")

def check_range(value:str) -> int:
    """
    0から100の整数であることをチェックする関数。

    Args:
        value (str): コマンドライン引数としての値。

    Returns:
        int: 整数値。

    Raises:
        argparse.ArgumentTypeError: 引数が0から100の範囲外である場合。
    """
    ivalue = int(value)
    if ivalue < 0 or ivalue > 100:
        raise argparse.ArgumentTypeError(f"{value} is an invalid integer value. It must be between 0 and 100.")
    return ivalue

def convert_to_png(input_dir:str, output_dir:str) -> None:
    
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 入力フォルダ内のすべてのJPEGファイルを変換
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')

            # 画像を読み込み
            image = Image.open(input_path)

            # PNG形式で保存
            image.save(output_path, 'PNG')

            print(f"Converted {input_path} to {output_path}")
    return 


def get_argument():
    parser = argparse.ArgumentParser(description="Process two named arguments.")
    parser.add_argument("--src_dir", required=False, help="")
    parser.add_argument("--resize", required=False, help="")
    parser.add_argument("--requality", required=False, help="")
    parser.add_argument("--scale", type=check_float_range, required=False, help="")
    parser.add_argument("--quality", type=check_range, required=False, help="An integer between 0 and 100.")
    
    return parser.parse_args()

if __name__ == "__main__":
    
    args = get_argument()

    src_dir = args.src_dir
    compressed_dir = "compress"

    if args.resize:
        resize_images_in_directory(src_dir,compressed_dir,args.scale)
    
    if args.requality:
        recompress_images_in_directory(src_dir,compressed_dir,args.quality)
