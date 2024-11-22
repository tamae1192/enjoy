import os
from PIL import Image

def resize_images(input_dir, output_dir, resolutions):
    """
    指定ディレクトリ内のJPG画像を指定の解像度にリサイズして保存する
    :param input_dir: 入力画像が格納されているディレクトリ
    :param output_dir: リサイズした画像を保存するディレクトリ
    :param resolutions: リサイズする解像度のリスト（例: [(2688, 1512), (2592, 1944)]）
    """
    # 入力ディレクトリを確認
    if not os.path.exists(input_dir):
        print(f"入力ディレクトリ {input_dir} が存在しません。")
        return

    # 出力ディレクトリを作成
    os.makedirs(output_dir, exist_ok=True)

    # ディレクトリ内のファイルをリスト
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".jpg"):
            input_path = os.path.join(input_dir, file_name)

            try:
                # 画像を開く
                with Image.open(input_path) as img:
                    for width, height in resolutions:
                        # リサイズ
                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                        
                        # 保存ファイル名の作成
                        output_subdir = os.path.join(output_dir, f"{width}x{height}")
                        os.makedirs(output_subdir, exist_ok=True)
                        output_path = os.path.join(output_subdir, file_name)

                        # 保存
                        resized_img.save(output_path)
                        print(f"画像 {file_name} を {width}x{height} にリサイズして保存しました: {output_path}")

            except Exception as e:
                print(f"画像 {file_name} の処理中にエラーが発生しました: {e}")

if __name__ == "__main__":
    # 入力ディレクトリ、出力ディレクトリ、および解像度を指定
    input_directory = "./input_images"  # JPGファイルが格納されているディレクトリ
    output_directory = "./output_images"  # リサイズした画像を保存するディレクトリ
    target_resolutions = [(2688, 1512), (2592, 1944)]  # 目的の解像度

    resize_images(input_directory, output_directory, target_resolutions)
