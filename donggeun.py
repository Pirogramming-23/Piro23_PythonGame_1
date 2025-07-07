import time
import random

def count_claps(number):
    # 3, 6, 9가 몇 개 들어있는지 세는 함수
    return sum(1 for digit in str(number) if digit in ['3', '6', '9'])

def gamegeun(players, user_name):
    print("🎮 3,6,9 게임 시작!")
    print("삼 육구삼육구~ 삼 육구삼육구~")
    print(f"플레이어: {', '.join([p['name'] if isinstance(p, dict) else p for p in players])} (사용자: {user_name})")
    print("-" * 50)

    number = 1
    cur_idx = 0
    num_players = len(players)
    
    # 각 플레이어별 실력 설정 (컴퓨터는 95-98% 정답률)
    player_skills = {}
    for player in players:
        if isinstance(player, dict):
            name = player['name']
        else:
            name = player
        if name == user_name:
            player_skills[name] = 1.0
        else:
            player_skills[name] = random.uniform(0.95, 0.98)

    while True:
        cur_player = players[cur_idx]['name'] if isinstance(players[cur_idx], dict) else players[cur_idx]
        expected = "짝" * count_claps(number) if count_claps(number) > 0 else str(number)
        
        print(f"\n👉 {cur_player} 차례! (숫자: {number})")

        # 사용자 차례인지 컴퓨터 차례인지 확인
        if cur_player == user_name:
            start_time = time.time()
            response = input("당신의 응답: ").strip()
            elapsed_time = time.time() - start_time
            
            if elapsed_time > 4:
                print("⏱️박자는 생명 생명 생명!")
                print(f"❌ 누가 술을 마셔 {cur_player}(이)가 술을 마셔~! 원~샷!")
                return cur_player
        else:
            # 컴퓨터 차례 - 실력에 따라 정답/오답 결정
            time.sleep(0.8)  # 컴퓨터가 생각하는 시간
            
            if random.random() < player_skills[cur_player]:
                # 컴퓨터가 정답을 말함
                response = expected
                print(f"{cur_player}: {response}")
            else:
                # 컴퓨터가 실수
                if count_claps(number) > 0:
                    # 3,6,9가 있는데 실수하는 경우
                    if random.random() < 0.5:
                        response = str(number)  # 숫자를 그대로 말함
                    else:
                        wrong_claps = random.randint(1, count_claps(number) + 2)
                        response = "짝" * wrong_claps  # 짝 개수를 틀림
                else:
                    # 3,6,9가 없는데 "짝"을 말함
                    response = "짝"
                print(f"{cur_player}: {response}")

        # 정답인지 확인하고 틀렸으면 게임 종료
        if response != expected:
            print(f"❌ 틀렸습니다! 정답은 '{expected}' 였습니다.")
            print(f"❌ 누가 술을 마셔 {cur_player}(이)가 술을 마셔~! 원~샷!")
            return cur_player

        # 다음 사람 차례로 넘어가기
        number += 1
        cur_idx = (cur_idx + 1) % num_players
        time.sleep(0.5)

    print("\n🎯 게임 종료!")
    print(f"최종 숫자: {number-1}")

