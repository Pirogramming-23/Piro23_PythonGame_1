import random
import time

#응답이 옳은지 체크하는 함수
def checkResponse(response, fruit):
    answer = {"딸기" : "딸기", "당근" : "딸기당근", "수박" : "딸기당근수박", "참외" : "딸기당근수박참외", "메론" : "딸기당근수박참외메론"}
    if response == answer[fruit]:
        return True
    return False

#컴퓨터의 응답을 출력하는 함수
#컴퓨터가 옳게 차례를 넘겼다면 True, 그렇지 않다면 False를 반환
def printResponse(computer, fruit, weight):
    answer = {"딸기" : "딸기", "당근" : "딸기당근", "수박" : "딸기당근수박", "참외" : "딸기당근수박참외", "메론" : "딸기당근수박참외메론"}
    fruits = ["딸기", "당근", "수박", "참외", "메론"]
    if random.random() + weight <= 0.85:
        print(f'{computer} : {answer[fruit]}!')
        return True
    else:
        error_response = answer[fruits[random.randint(0, 4)]]
        while error_response == answer[fruit]:
            error_response = answer[fruits[random.randint(0, 4)]]
        print(f'{computer} : {error_response}!')
        return False
    
#플레이어 리스트, 게임을 선택한 사람, 유저의 이름(컴퓨터가 아닌 사람)
def gameDongsu(players, host, user_name):
    if user_name not in players:
        players.append(user_name)
    tempo = 1 #게임의 템포를 나타내는 변수. 게임이 진행될수록 점점 빨라짐
    fruits = ["딸기", "당근", "수박", "참외", "메론"]
    print("🍓딸기당근수박참외메론게임~! 지목!")
    time.sleep(1)
    print("🍓딸기당근수박참외메론게임~! 지목!")
    time.sleep(1)
    print("====== 참여하는 인원 =======")
    for i in range(len(players)):
        print(f'{i+1}. {players[i]}')
    print("============================")
    time.sleep(1)
    
    cur_player = host #지금 말하는 사람의 이름
    next_player = ""
    next_player_idx = -1
    cur_fruit = ""
    next_fruit = ""

    #게임을 시작하기 위해 입력을 받는 과정
    #게임을 시작하는 사람이 유저인 경우
    if host == user_name:
        cur_input = input("현재 사람들 중 한명의 이름과 과일(딸기, 당근, 수박, 참외, 메론)을 입력해주세요! ex) 동수 수박: ").split(" ")
        time.sleep(tempo)
        try:
            next_player = cur_input[0]
            next_player_idx = players.index(next_player)
            next_fruit = cur_input[1]
        #아예 입력을 잘못한 경우 바로 고로시(?)
        except:
            print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
            time.sleep(1)
            return cur_player

        #본인을 다음 사람으로 지목한 경우 or 다음 사람 이름을 잘못 입력한 경우 or 과일을 잘못 입력한 경우 -> 패배
        if (next_player == cur_player) or (next_player not in players) or (next_fruit not in fruits):
            print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
            time.sleep(1)
            return cur_player
    
    #게임을 시작하는 사람이 컴퓨터인 경우
    else:
        next_player_idx = random.randint(0, len(players)-1) #랜덤으로 지목할 사람을 고름
        next_player = players[next_player_idx]
        #본인이 아닌 다음 사람이 나올때까지 랜덤을 돌림
        while next_player == cur_player:
            next_player_idx = random.randint(0, len(players)-1)
            next_player = players[next_player_idx]
        next_fruit = fruits[random.randint(0, 4)] #과일도 랜덤으로 고름
        print(f'{cur_player} : {next_player} {next_fruit}!')
        time.sleep(tempo)
    

    #여기부터 본격적으로 게임 플레이

    #컴퓨터는 85% 확률로 자기 차례에 성공을 하는데, 이러면 유저가 한번도 입력하지 않고도 컴퓨터끼리 싸워서 게임이 끝날 때가 있음.
    #때문에 가중치를 더해주다가 유저가 한번이라도 입력하고 나면 가중치를 0으로 바꿈
    weight = -1
    while True:
        cur_player = next_player #이전에 next_player 으로 지목 받은 사람이 cur_player가 됨
        cur_fruit = next_fruit #이전에 next_fruit 이었던 과일이 cur_fruit 이 됨
        tempo = max(0.3, tempo - 0.05) #게임 템포를 점점 올림
        #유저(컴퓨터가 아닌 사람)이 cur_player인 경우
        if cur_player == user_name:
            weight = 0 #유저가 한 번 차례를 맞이했으므로 컴퓨터가 실패할 확률을 만듦
            start_time = time.time()
            response = input("당신의 차례입니다!: ")
            end_time = time.time()
            elapsed_time = end_time - start_time
            time.sleep(tempo)

            if elapsed_time >= 4.5:
                print("박자는 생명!🎵 박자는 생명!🎵")
                time.sleep(1)
                print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
                time.sleep(1)
                return cur_player
            if not checkResponse(response, cur_fruit):
                print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
                time.sleep(1)
                return cur_player
            
            start_time = time.time()
            cur_input = input("현재 사람들 중 한명의 이름과 과일(딸기, 당근, 수박, 참외, 메론)을 입력해주세요! ex) 동수 수박: ").split(" ")
            end_time = time.time()
            elapsed_time = end_time - start_time
            time.sleep(tempo)
            if elapsed_time >= 4.5:
                print("박자는 생명!🎵 박자는 생명!🎵")
                time.sleep(1)
                print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
                time.sleep(1)
                return cur_player
            
            try:
                next_player = cur_input[0]
                next_player_idx = players.index(next_player)
                next_fruit = cur_input[1]
            #아예 입력을 잘못한 경우 바로 고로시(??)
            except:
                print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
                time.sleep(1)
                return cur_player
            #본인을 다음 사람으로 지목한 경우 or 다음 사람 이름을 잘못 입력한 경우 or 과일을 잘못 입력한 경우 -> 패배
            if (next_player == cur_player) or (next_player not in players) or (next_fruit not in fruits):
                print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
                time.sleep(1)
                return cur_player
        
        #컴퓨터가 cur_player인 경우
        else:
            #20% 확률로 응답에 실패했을 경우 고로시 + 게임 종료
            if not printResponse(cur_player, cur_fruit, weight):
                print(f'아 누가누가 술을 마셔🤨 {cur_player}(이)가 술을 마셔🥴 원~~~샷❗🥤')
                time.sleep(1)
                return cur_player

            time.sleep(tempo)
            next_player_idx = random.randint(0, len(players)-1) #랜덤으로 지목할 사람을 고름
            next_player = players[next_player_idx]
            #본인이 아닌 다음 사람이 나올때까지 랜덤을 돌림
            while next_player == cur_player:
                next_player_idx = random.randint(0, len(players)-1)
                next_player = players[next_player_idx]
            next_fruit = fruits[random.randint(0, 4)] #과일도 랜덤으로 고름
            print(f'{cur_player} : {next_player} {next_fruit}!')
            time.sleep(tempo)