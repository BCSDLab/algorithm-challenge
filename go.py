import os

# 최상위 디렉터리 경로
base_dir = './week-01/'  # 실제 디렉터리 경로로 바꾸세요

def rename_md_v2_files():
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if 'mdv2' in file:
                old_file_path = os.path.join(root, file)
                new_file_path = old_file_path.replace('mdv2', 'md')
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} to {new_file_path}')

if __name__ == "__main__":
    rename_md_v2_files()
