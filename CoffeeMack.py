import pickle
import random
jinsang = False # 박지완천재
Oder = ["커피 하나 주세요! 맛있어 보이네요.", "커피 하나요! 꿀 추가로요~", "맛있겠네요~ 커피 하나만 주세요~.아! 꿀은 빼주세요."                                          
       "커피엔 꿀이 최고죠! 커피 하나 주세요.","꿀만 주실 수 있나요? 저의 이름은 곰돌이 푸입니ㄷ","커피~ 커피~ 꿀도 있게~~~",
        "커피내놔 주인넘아. 안그럼 쏜다.", "커피에 꿀 넣어주세요...어...음...그냥 넣지 말아주세요..어....음...걍 넣어주ㅅ",
        "커피      주세요~~~~ 꿀도       추가해서요~~~~~ 잘     부탁드립니다앙~~~~~~~~~","커피 하나 꿀 추가 ㅇㅋ ?"]

with (open("DON.pickle", "rb") as f):
    DON = pickle.load(f)
    print("주문 :")
    print(random.choice(Oder))
    print("주문 받기 [1] ㅣ 꺼져 [2]")
    OderOK = input(">>")
    if (OderOK == 1):
        if jinsang == False:
            print("손님 : 감사합니다!")
        else:
            print("제대로 해라...")
    elif jinsang == False:
        print("손님 : ??왜요??요즘같은 시대에 이런 가게가 다 있네요!")
    else:
        print("진상 : (떼잉...여기도 안받네...커피좀 멋지게 못먹나..)")