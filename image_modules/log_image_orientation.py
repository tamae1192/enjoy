import os
from PIL import Image, ExifTags

def log_image_orientation(input_dir):
    """
    指定ディレクトリ内の画像について、EXIF情報で画像の向きを判定してログを出力する
    :param input_dir: 画像が格納されているディレクトリ
    """
    # 入力ディレクトリの確認
    if not os.path.exists(input_dir):
        print(f"入力ディレクトリ {input_dir} が存在しません。")
        return

    # EXIFのOrientationタグを取得
    orientation_tag = next(
        (key for key, value in ExifTags.TAGS.items() if value == "Orientation"), None
    )
    if not orientation_tag:
        print("EXIF Orientation タグが見つかりませんでした。")
        return

    # ディレクトリ内の画像ファイルを処理
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(input_dir, file_name)
            try:
                with Image.open(file_path) as img:
                    # EXIF情報を取得
                    exif_data = img._getexif()
                    if exif_data and orientation_tag in exif_data:
                        orientation = exif_data[orientation_tag]
                        if orientation in [1, 2, 3, 4]:  # 上向き（または回転なし）
                            print(f"{file_name}: 上向き")
                        elif orientation in [5, 6, 7, 8]:  # 横向き
                            print(f"{file_name}: 横向き")
                        else:
                            print(f"{file_name}: 不明なOrientation値({orientation})")
                    else:
                        print(f"{file_name}: EXIF情報がありません（デフォルトは上向きとみなす）")
            except Exception as e:
                print(f"{file_name}: エラーが発生しました - {e}")

if __name__ == "__main__":
    # 画像が格納されているディレクトリを指定
    input_directory = ""  # 例: "./input_images"
    log_image_orientation(input_directory)
