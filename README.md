# 前準備-Preparation
このgitからソースコードをダウンロード

cdコマンド等でenjoy/image_modulesへ移動

以下コマンドでrequirements.txt指定のライブラリをinstall
pip install -r requirements.txt

# 使い方-How to use
image_modulesディレクトリのresize_downloader.pyを実行
だいたい3パターンだと思うので3パターンを記載


# コマンド例-Command example
パターン1 特定のURL上の画像をダウンロードし圧縮
python main.py --url https://iret.media/***** --src_dir download_test --compressed_dir compress_test 

パターン2 特定のディレクトリの画像を圧縮:サイズ縮小
python compress_image.py  --src_dir download_test --compressed_dir compresse_test --resize True --scale 0.7

パターン3 特定のディレクトリの画像を圧縮:クオリティ下げ
python compress_image.py  --src_dir download_test --compressed_dir compress_test --requality True --quality 80


# 引数紹介-Argument introduction
--url targetURL
画像を引っ張ってくる対象のサイトURL

--src_dir 
画像をダウンロードするディレクトリ

--compressed_dir
画像が圧縮されたディレクトリ
