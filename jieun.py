# 아파트 게임
import random
import time

######## 아파트 게임 함수 ########
# 총 player를 list로 받음 - 추후 수정 가능
def gameJieun(invited_names, user_name, host):
    
    player_list = invited_names.copy()
    if user_name not in player_list:
        player_list.append(user_name)
    
    print("아 파트 아파트~🎶 아 파트 아파트~~🎶🎶")
    
    # input 받기
    if host == user_name:
        while True:
            try:
                floor = int(input("층 수를 입력해주세요(5 이상 30 이하의 정수) : "))
                if floor < 5:
                    print("5 이상의 숫자를 입력해주세요")
                elif floor > 30:
                    print("30 이하의 숫자를 입력해주세요")
                else:
                    break
            except ValueError:
                print("5 이상 30 이하의 정수를 입력해주세요!")
    else:
        # 컴퓨터는 랜덤으로 층 수 결정
        floor = random.randint(5, 30)
        
    print(f"{floor}층!")
    time.sleep(1)
    
    # player의 손 순서 정하기(player마다 손 2개)
    hands_list = []
    for p in player_list:
        hands_list.append(f"{p} (손1)")
        hands_list.append(f"{p} (손2)")
    random.shuffle(hands_list)
    
    call_num = 0
    while call_num < floor :
        for hand in hands_list:
            call_num += 1
            time.sleep(0.5)
            if call_num >= floor :
                print(f"{hand} : {call_num} ..")
                target = hand.split(" ")[0]
                break
            print(f"{hand} : {call_num}!")
    
    return target
    
if __name__ == "__main__":
    player_list = [2, 3, 4]
    #gameJieun(player_list, 1, 3) # 컴퓨터 진행 게임
    gameJieun(player_list, 1, 1) # 사용자 진행 게임
    