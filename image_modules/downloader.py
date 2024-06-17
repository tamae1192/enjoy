import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import shutil

def download_images(url:str,  download_dir:str):
    # 指定ディレクトリが存在しない場合は作成
    os.makedirs(download_dir,exist_ok=True)

    # ウェブページのHTMLを取得
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 画像URLの取得
    img_tags = soup.find_all('img')
    
    # もし画像が存在しなければメッセージを出して終了
    if len(img_tags) == 0:
        print("no image found")

    
    img_urls = [urljoin(url, img['src']) for img in img_tags]

    for img_url in img_urls:
        try:
            # 画像のダウンロード
            img_response = requests.get(img_url, stream=True)
            if img_response.status_code == 200:
                img_name = os.path.join(download_dir, os.path.basename(img_url))
                with open(img_name, 'wb') as f:
                    for chunk in img_response.iter_content(1024):
                        f.write(chunk)
            else:
                print(f"Failed to download {img_url}")
        except Exception as e:
            print(f"An error occurred while downloading {img_url}: {e}")

def delete_all_files_in_directory(directory:str):
    """
    指定されたディレクトリ内の全てのファイルを削除します。

    Args:
        directory (str): ファイルを削除するディレクトリのパス。
    """
    # ディレクトリが存在するかチェック
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # ディレクトリ内の全てのファイルとサブディレクトリを処理
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        try:
            # ファイルまたはシンボリックリンクを削除
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            # ディレクトリを削除
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
