import random
import time
import signal

#시간초과 예외처리
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

sequence = []  # 전체 아이템 시퀀스
item_pool = ["사과", "배", "수박", "책", "모자", "바지", "치약", "우산", "신발", "귤"]
#유저 차례
def user_turn():
    print("지금까지의 물건을 순서대로 입력하세요.")
    for i, item in enumerate(sequence):

        start_time = time.time()  # 3초 제한
        answer = input(f"{i+1}번째 물건 (3초 내 입력): ")
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time >= 3:
            print("\n⏰ 시간 초과! 게임 오버.")
            return False
        if answer.strip() != item:
            print("틀렸습니다! 게임 오버.")
            return False
    # 새로운 아이템 추가
    while True:
        new_item = input("새로운 물건을 입력하세요: ").strip()
        if new_item and new_item not in sequence:
            sequence.append(new_item)
            break
        else:
            print("이미 입력된 물건이거나 잘못된 입력입니다.")
    return True
#컴퓨터 차례(미리 정의 된 물건들 이름 다쓰면 out)
def cpu_turn(cpu_name):
    print(f"{cpu_name}의 차례입니다...")
    time.sleep(1)
    # 기존 시퀀스 암기 시뮬레이션
    for i, item in enumerate(sequence):
        time.sleep(0.5)
        # 메모리 실패 확률 계산 및 실패 시 처리
        failure_chance = min(0.05 + 0.02 * len(sequence), 0.3)  # 길어질수록 실패 확률 증가 (최대 30%)
        if random.random() < failure_chance:
            print(f"{cpu_name}이(가) '{item}' 대신 틀린 말을 했습니다! 😵")
            return False
        print(f"{cpu_name}: {item}")
    # 새로운 아이템 추가
    remaining_items = list(set(item_pool) - set(sequence))
    if not remaining_items:
        print("아이템 풀이 모두 소진되었습니다!")
        return False
    new_item = random.choice(remaining_items)
    print(f"{cpu_name}: {new_item}")
    sequence.append(new_item)
    return True
#게임 실행함수
def gamegichan(players, user_name):
    print("시장에 가면~ 🎵")
    round_num = 1
    sequence.clear()  # 이전 게임의 아이템 시퀀스 초기화
    while True:
        print(f"\n===== Round {round_num} =====")
        for player in players:
            print(f"\n{player['name']}의 차례입니다.")
            if player['name'] == user_name:
                if not user_turn():
                    print(f"{player['name']}님이 틀렸습니다!")
                    print(f"아 누가누가 술을 마셔🤨 {player['name']}(가) 술을 마셔🥴 원~~~샷❗🥤")
                    return player['name']
            else:
                if not cpu_turn(player['name']):
                    print(f"{player['name']}의 차례에서 아이템 풀이 소진되었습니다!")
                    print(f"아 누가누가 술을 마셔🤨 {player['name']}(가) 술을 마셔🥴 원~~~샷❗🥤")
                    return player['name']
        round_num += 1