from donggeun import *
from gichan import *
from jieun import *
from Jueun import *
from dongsu import *

#플레이어 설정
#동수,지은,기찬,주은,동근에 대한 이름과 치사량 저장
friends_pool = [
    {"name": "동수", "capacity": 6, "drank": 0},
    {"name": "동근", "capacity": 8, "drank": 0},
    {"name": "기찬", "capacity": 2, "drank": 0},
    {"name": "주은", "capacity": 2, "drank": 0},
    {"name": "지은", "capacity": 4, "drank": 0},
]
# =======================
# Main Game Logic
# =======================
def main():
    print("""                                                           
  ##   ##     #### ##  #  ###  ##       ####   ##   #    # #### 
  ##   ##    ### # ##  # ##  # ##      ###     ##   ##  ## ##   
 # ##  ##    ##    ##  # ##  # ##      ##     # ##  ###### ##   
 # ##  ##    ##    ##### ##  # ##      ##  #  # ##  ###### #### 
###### ##    ##    ##  # ##  # ##      ##  # ###### # # ## ##   
#   ## ##    ###   ##  # ##  # ##      ### # #   ## # # ## ##   
#   ## #####  #### ##  #  ###  #####    #### #   ## #   ## ####""")
    print("================================================================")
    print("                  🍺 ALCOHOL GAME 시작합니다! 🍺")
    print("================================================================")
    
    # 게임 시작 여부 확인
    start = input("게임을 진행할까요? (y/n) : ").strip().lower()
    if start != 'y':
        print("게임을 종료합니다.")
        return

    # 사용자 이름 받기
    user_name = input("오늘 거하게 취해볼 당신의 이름은? : ").strip()

    # 사용자 주량 선택
    while True:
        print("\n🍺 소주 기준 당신의 주량은? 🍺")
        print("1. 소주 반병 (2잔)")
        print("2. 소주 반병에서 한병 (4잔)")
        print("3. 소주 한병에서 한병 반 (6잔)")
        print("4. 소주 한병 반에서 두병 (8잔)")
        print("5. 소주 두병 이상 (10잔)")
        try:
            choice = int(input("당신의 치사량(주량)은 얼마만큼 인가요? (1~5 선택) : "))
            if 1 <= choice <= 5:
                break
            else:
                print("1~5 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

    user_capacity = choice * 2  # 잔 수로 환산
    user_data = {"name": user_name, "capacity": user_capacity, "drank": 0}
    
    # 초대할 친구 수 선택
    friends_name_pool = ["동수", "동근", "기찬", "주은", "지은"]
    while True:
        try:
            invite_num = int(input("\n함께 취할 친구들은 얼마나 필요하신가요?(최대 3명) : "))
            if 1 <= invite_num <= 3:
                break
            else:
                print("1~3 사이 숫자를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

    invited_names = random.sample(friends_name_pool, invite_num)
    players = [user_data]
    for friend in friends_pool:
        if friend["name"] in invited_names:
            players.append(friend)

    # 상태 출력
    print("\n현재 상태:")
    for p in players:
        print(f"{p['name']}은(는) 지금까지 🍺 {p['drank']} | 치사량까지 {p['capacity']}잔")
        time.sleep(1)

    # 게임 리스트 출력
    print("\n🍺 오늘의 ALCOHOL GAME 🍺")
    print("1. 시장에 가면 게임")
    print("2. 딸기당근수박참외메론 게임")
    print("3. 369 게임")
    print("4. 아파트 게임")
    print("5. 지하철 게임")
    time.sleep(1)

    # 게임 루프
    turn = 0
    while True:
        current_player = players[turn % len(players)]
        name = current_player['name']
        if name == user_name:
            try:
                game_choice = int(input(f"\n{name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? (1~5 입력) : "))
                if game_choice < 1 or game_choice > 5:
                    print("1~5 사이의 숫자를 입력해주세요.")
                    continue
            except ValueError:
                print("잘못된 입력입니다. 1~5 숫자를 입력해주세요.")
                continue
        else:
            game_choice = random.randint(1, 5)
            print(f"\n{name} 님이 게임을 선택하셨습니다! 😊 ({game_choice}번 게임)")
            time.sleep(1)

        # 선택된 게임 실행
        if game_choice == 1:
            drinker = gamegichan(players, user_name)
        elif game_choice == 2:
            drinker = gameDongsu(invited_names, current_player["name"], user_name)
        elif game_choice == 3:
            drinker = gamegeun(players, user_name)
        elif game_choice == 4:
            drinker = gameJieun(invited_names, user_name, name)
        elif game_choice == 5:
            drinker = gameJueun(invite_num+1, 0, players)

        # 게임 결과 시뮬레이션
        print("""                                                                                                            
                 ___   ___                                                                                  
    /|    / /       / /        //   ) )     //   / /       //   ) )     // | |     /|    //| |     //   / / 
   //|   / /       / /        //           //____         //           //__| |    //|   // | |    //____    
  // |  / /       / /        //           / ____         //  ____     / ___  |   // |  //  | |   / ____     
 //  | / /       / /        //           //             //    / /    //    | |  //  | //   | |  //          
//   |/ /     __/ /___     ((____/ /    //____/ /      ((____/ /    //     | | //   |//    | | //____/ / """) 
        time.sleep(1)
        if not drinker:
            drinker = random.choice(players)
        elif isinstance(drinker, str):
            drinker = next((p for p in players if p["name"] == drinker), None)
        if drinker:
            drinker["drank"] += 1
            if game_choice == 1:
                print(f"\n아 누가누가 술을 마셔🤨 {drinker['name']}(가) 술을 마셔🥴 원~~~샷❗🥤")
                time.sleep(1)

        # 상태 갱신
        print("\n현재 상태:")
        time.sleep(1)
        for p in players:
            remain = max(p["capacity"] - p["drank"], 0)
            print(f"{p['name']}은(는) 지금까지 🍺 {p['drank']} | 치사량까지 {remain}잔")
            time.sleep(1)

        # 치사량 도달 검사
        for p in players:
            if p["drank"] >= p["capacity"]:
                print("\n" + "="*40)
                print(f"{p['name']}(가) 전사했습니다... 꿈나라에서는 편히 쉬시길 ..zzz")
                time.sleep(1)
                print("🍺 다음에 술마시면 또 불러주세요~ 안녕 ! 🍺")
                return

        turn += 1

if __name__ == "__main__":
    main()