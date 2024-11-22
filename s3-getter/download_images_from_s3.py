import boto3
import os

def download_images_from_s3(bucket_name, prefix, download_dir):
    """
    S3の特定のディレクトリ内の画像をローカルにダウンロードする
    :param bucket_name: S3バケット名
    :param prefix: ダウンロードするディレクトリのパス（例: "images/"）
    :param download_dir: ローカルのダウンロード先ディレクトリ
    """
    # S3クライアントを作成
    s3 = boto3.client('s3')

    # プレフィックスに一致するオブジェクトをリストする
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    if 'Contents' not in response:
        print("指定されたディレクトリにはファイルが存在しません。")
        return

    # ダウンロードディレクトリを作成
    os.makedirs(download_dir, exist_ok=True)

    for obj in response['Contents']:
        file_key = obj['Key']
        if file_key.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # 画像拡張子をチェック
            file_name = os.path.basename(file_key)
            local_file_path = os.path.join(download_dir, file_name)
            print(f"Downloading {file_key} to {local_file_path}...")
            
            # ファイルをダウンロード
            s3.download_file(bucket_name, file_key, local_file_path)
    print("ダウンロード完了！")

if __name__ == "__main__":
    bucket_name = "your-bucket-name"
    prefix = "your/directory/path/"  # 例: "images/"
    download_dir = "./downloads"

    download_images_from_s3(bucket_name, prefix, download_dir)