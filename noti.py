import os
from collections import defaultdict

# 최상위 디렉터리 경로
base_dir = './'  # 실제 디렉터리 경로로 바꾸세요

def count_updates_per_user(weeks):
    # 사용자별 문제 업데이트 수를 저장할 딕셔너리
    user_problem_count = defaultdict(lambda: defaultdict(int))

    for week in weeks:
        week_dir = os.path.join(base_dir, week)

        if os.path.exists(week_dir):
            print(f"Processing {week_dir}")
            for problem in os.listdir(week_dir):
                problem_dir = os.path.join(week_dir, problem)

                if os.path.isdir(problem_dir):
                    for file in os.listdir(problem_dir):
                        username = file.split('.')[0]  # 파일 이름에서 사용자 이름 추출
                        user_problem_count[week][username] += 1

    return user_problem_count

def print_user_updates(user_problem_count):
    for week, users in user_problem_count.items():
        print(f"\n{week}:")
        for user, count in users.items():
            print(f"{user}: {count} 문제")

def main():
    weeks = input("주차를 입력하세요 (예: 1,2,3): ")
    week_list = [f'week-0{week.strip()}' for week in weeks.split(',')]
    user_problem_count = count_updates_per_user(week_list)
    print_user_updates(user_problem_count)

if __name__ == "__main__":
    main()
