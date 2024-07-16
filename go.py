import os
import shutil

# 최상위 디렉터리 경로
base_dir = './week-01/'  # 실제 디렉터리 경로로 바꾸세요

def rename_solution_files_and_clean_directories():
    for root, dirs, files in os.walk(base_dir):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            print(dir_path)
            if os.path.isdir(dir_path):
                for sub_root, sub_dirs, sub_files in os.walk(dir_path):
                    if os.path.basename(sub_root) == os.path.basename(sub_root):
                        for sub_file in sub_files:
                            sub_file_path = os.path.join(sub_root, sub_file)
                            new_file_path = os.path.join(base_dir, sub_file)
                            shutil.move(sub_file_path, new_file_path)
                            print(f"Moved: {sub_file_path} -> {new_file_path}")
                        os.rmdir(sub_root)
                        print(f"Removed directory: {sub_root}")

if __name__ == "__main__":
    rename_solution_files_and_clean_directories()
