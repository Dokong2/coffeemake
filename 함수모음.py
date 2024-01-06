import pickle
import random
jinsang = False
GULL = False
DON = 0
Goodorjinsang = (random.randint(1, 2))

def save():
    with open("DON.pickle", 'wb') as f:
        pickle.dump([DON], f)


def oder():
    global jinsang
    GoodOder = ["커피 하나 주세요! 맛있어 보이네요.", "커피 하나요~!", "맛있겠네요~ 커피 하나만 주세요~."
                "커피가 최고죠! 커피 하나 주세요.","커피~ 커피~","커피  주세요~  잘  부탁드립니다앙~  "
                , "커피 하나 꿀 추가 ㅇㅋ ?", "커피 노 꿀 콜?"]

    BadOder = ["커피내놔 주인넘아.맛없는 꿀은 빼고.뭐, 이미 없지만.",
               "커피 1개 주세요...어...음...그냥 주지 말아주세요..어....음...걍 주ㅅ", ]

    GoodBedSay = ["왜요? 너무하시네요...", "예? 진짜로요? 네.. 님이 먼저 그러신 겁니다! 후회하지 마세요...", "뭐야 사장님이 미쳤어요",
                  "응 더이상 안와 꺼져", "응 다신 이가게 안와 더이상 말 붙히지 마", "사장 인성 ㄷㄷ 사탄이네", "사장님이 정신이 나갔어요!"]

    jinsangBadsay = ["(떼잉...여기도 안받네...커피좀 멋지게 못먹나..)", "아니 아무리 진상이여도 ㄲㅈ는 좀..마상...", "뭐야 정신이 나갔냐?",
                     "에엥? 왱 주문을 안바드실깡?? 정말 화 나 냉~~~~~~~~(아 쪽팔려 이거 맞냐..)", "진상은 막대한다..뭐 이런건가?",
                     "홀리몰리", "응 안와 수익 나락 나락 나락 락 락 락"]



    with open("DON.pickle", 'wb') as f:  #
        pickle.dump([DON], f)

    if Goodorjinsang == 1:
        jinsang = False
    else:
        jinsang = True

    print("주문 :")
    if jinsang == False:
        print(random.choice(GoodOder))
    else:
        print(random.choice(BadOder))

def OkOrNotOk():
    global jinsang
    print("주문 받기 [1] ㅣ 꺼져 [2]")
    OderOK = input(">>")
    if (OderOK == 1):
        if jinsang == False:
            print("손님 : 감사합니다!")
        else:
            print("진상 : 네. 응 ^^")
    elif jinsang == False:
        print(random.choice(GoodBedSay))
    else:
        print(random.choice(jinsangBadsay))
def Made():
    global jinsang
    print("커피를 만들자!")
    print("무엇을 할까?")
    print("바로 제작 [1] ㅣ 메뉴얼 보고 제작 [2]")
    menualorstart = input(">>")
    if menualorstart == 2:
        print("커피 레시피 :")
        print('원두를 갈자!      가는 방법   : "갉갉갉갉갉갉갉갉갉갉"을 입력한다.')
        print('커피 가루를 두자!  두는 방법   : "푸슑푸슑푸슑푸슑푸슑"을 입력한다.')
        print('물을 붓자!        붓는 방법   : "조롥조롥조롥조롥조롥"을 입력한다.')
        print('손잡이를 돌리자!   돌리는 방법  : "슈슉슈슉슈슉슈슉슈슉"를 입력한다. ')
        print('커피를 따르자!     세팅 방법   : "조르르르르르르르르륵"을 입력한다.')
        print("")
        print('옵션 : 꿀을 따르자! 따르는 방법 : "뿌루룱"을 입력한다. [추후 추가]')
    elif menualorstart == 1:
        print("")
    else:
        print("하겠다는거야 뭐라는거야;;")
    print("제작 시작!")
    while True:
        print("현재 단계 : 원두 갈기")
        wundu = input(">>")
        if wundu == "갉갉갉갉갉갉갉갉갉갉":
            print("원두 갈기 성공!")
            break
        else:
            print("다시 해보세요! 오타가 있는 것 같아요.")
    while True:
        print("현재 단계 : 커피 가루 두기")
        dugi = input(">>")
        if dugi == "푸슑푸슑푸슑푸슑푸슑":
            print("가루 두기 성공!")
            break
        else:
            print("다시 해보세요! 오타가 있는 것 같아요.")
    while True:
        print("현재 단계 : 물 붓기")
        Waterout = input(">>")
        if Waterout == "조롥조롥조롥조롥조롥":
            print("물 붓기 성공!")
            break
        else:
            print("다시 해보세요! 오타가 있는 것 같아요.")
    while True:
        print("현재 단계 : 손잡이 돌리기")
        Turn = input(">>")
        if Turn == "슈슉슈슉슈슉슈슉슈슉":
            print("손잡이 돌리기 성공!")
            break
        else:
            print("다시 해보세요! 오타가 있는 것 같아요.")
        #아 참된 ro동의 맛이란.... While 문 겁나 힘드네..어우
        #최종수정일 : 2024.1.6 20:55
