define jh = Character("박준혁", color = "#fc0303")
define yj = Character("즙지욱", color = "#fc038c") # 캐릭터 설정법
define kc = Character("김세찬", color = "#03fc20")
                                           #대화창 캐릭터 이름 색깔

                                    #대사 출력 방식 설정
define narrator = Character(None, kind = nvl)
                                          #화면 전체를 써서 출력

image background = "bg/class1.jpg"  #이미지 불러오기  
image c_jh = "character/jh.png"
image c_yj = "character/yj1.png"                              

label start:
    scene background  #배경으로 설정

    "캐릭터 소개"
    "즙지욱:히로인"
    "박준혁:주인공"
    "김세찬:라이벌"
    nvl clear # 이전 나레이션 제거

    "원작 소개"
    "책 이름:현실세계에서는 찐따였던 내가 이세계에서는 지욱밥 남친이라닛?! 너무 행복할 수 밖에 없다"
    "작가:김민종"
    "일러스트 작가:긍정의 참치"
    "출시연도:2020년"
    nvl clear


    show c_yj #캐릭터 이미지 불러오기
    yj "준혁이와 지욱이의 두근두근 이세계 러브"
    kc "시작~~~~~~~~~~~~~~~~하겠습니다."            
    kc "재미있게 즐겨주세요"

    
    return
