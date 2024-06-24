import os
import shutil

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
                os.remove(file_path)
            # ディレクトリを削除
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
