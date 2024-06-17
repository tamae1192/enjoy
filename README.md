# 前準備-Preparation
このgitからソースコードをダウンロード

enjoy/image_modulesへ移動
```bash
cd image_modules
```

以下コマンドでrequirements.txt指定のライブラリをinstall
```bash
pip install -r requirements.txt
```

# 検証済み環境
MacBook Air M2 2022

# 使い方-How to use
以下に具体的なコマンド例を3点記載


# コマンド例-Command example
パターン1 特定のURL上の画像をダウンロードし圧縮
```bash
python main.py --url https://iret.media/***** --src_dir download_test --compressed_dir compress_test 
```
※ディレクトリやURLの指定は自由。ない場合は新たに作成される。絶対パス指定ではない場合はpythonの実行ディレクトリをルートとした位置に作成される


パターン2 特定のディレクトリの画像を圧縮:サイズ縮小
```bash
python compress_image.py  --src_dir download_test --compressed_dir compresse_test --resize True --scale 0.7
```
※0.9倍の場合は --scale 0.9指定をする

パターン3 特定のディレクトリの画像を圧縮:クオリティ下げ
```bash
python compress_image.py  --src_dir download_test --compressed_dir compress_test --requality True --quality 80
```
※60%指定の場合は --scale 60指定をする

# 引数紹介-Argument introduction
--url targetURL
画像を引っ張ってくる対象のサイトURL

--src_dir 
画像をダウンロードするディレクトリ

--compressed_dir
画像が圧縮されたディレクトリ
