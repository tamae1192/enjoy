import os

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests


def download_notion_images(url:str,  download_dir:str):
    # 指定ディレクトリが存在しない場合は作成
    os.makedirs(download_dir,exist_ok=True)

    # ウェブページのHTMLを取得
    soup = get_dynamic_soup(url)

    # 画像URLの取得
    img_tags = soup.find_all('img')
    
    # もし画像が存在しなければメッセージを出して終了
    if len(img_tags) == 0:
        print("no image found")

    
    img_urls = [urljoin(url, img['src']) for img in img_tags]

    for img_url in img_urls:

        img_url_name = img_url.split('?')[0]

        try:
            # 画像のダウンロード
            img_response = requests.get(img_url, stream=True)
            if img_response.status_code == 200:
               
                img_name = os.path.join(download_dir, os.path.basename(img_url_name))
                with open(img_name, 'wb') as f:
                    for chunk in img_response.iter_content(1024):
                        f.write(chunk)
            else:
                print(f"Failed to download {img_url}")
        except Exception as e:
            print(f"An error occurred while downloading {img_url}: {e}")


def get_dynamic_soup(url:str, wait_time = 2) -> BeautifulSoup:
    """動的なjavascriptが生成するimgタグを取得する場合の関数（notionなど）

    Args:
        url (str): 
        wait_time (int, optional): . Defaults to 3.

    Returns:
        BeautifulSoup: 
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    import time
    from webdriver_manager.chrome import ChromeDriverManager

    # WebDriver Managerを使用してchromedriverを設定
    service = Service(ChromeDriverManager().install())

    # ブラウザのオプション
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモードで実行

    # ブラウザを起動
    driver = webdriver.Chrome(service=service, options=options)

    # Notionの公開ページを開く
    driver.get(url)
    
    # ページが完全に読み込まれるまで待機
    time.sleep(wait_time)  # 必要に応じて調整

    # ページのソースを取得
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_static_soup(url:str) -> BeautifulSoup:
    """静的htmlリソースのimgタグを取得する場合の関数

    Args:
        url (str): 

    Returns:
        BeautifulSoup: 
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup