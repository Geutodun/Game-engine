define jh = Character("박준혁", color = "#fc0303")
define yj = Character("즙지욱", color = "#fc038c") # 캐릭터 설정법
define kc = Character("김세찬", color = "#03fc20")
                                           #대화창 캐릭터 이름 색깔

                                    #대사 출력 방식 설정
define narrator = Character(None, kind = nvl)
                                          #화면 전체를 써서 출력
define ch_narrator = Character(None)                                   
                            #독백을 대화창으로 출력 하는 캐릭터 정의

image background = "bg/class1.jpg"  #이미지 불러오기 
image background1 = "bg/tree1.jpg"
image c_jh = im.FactorScale("character/jh.png", 1.2) #캐릭터 크기 조절
image c_yj:  
    "character/yj3.png" #이미지 불러오기
    yalign 0.4        #y좌표 조정                     
image c_kc: 
    "character/kc1.jpg"
    yalign 0.4


define right = Position(xalign = 0.96)
define left = Position(xalign = 0.05)


label start:
    scene background with fade #배경으로 설정

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



    show c_yj at right with dissolve    # 캐릭터 이미지 불러오기
    yj "내 이름은 즙벌렁 강태현이 될 남자다."
    show c_kc at left with dissolve   # 캐릭터 왼쪽 정렬
    kc "나 김세찬 준혁이는 내꺼다!" 
    show c_jh at truecenter with dissolve #사진 y좌표도 가운데로 조정   # 사진을 가운데 정렬        
    jh "난 둘다 좋아"
    
    menu:                              #선택지 만드는 명령어
        "그렇지만 난 지욱이가 좋아":
            yj "준혁아 난 널 믿고 있었어"
            kc "쉬익쉬익"
        
        "하지만 세찬이가 조금 더 좋아":
            kc "준혁 역시 너야"
            yj "(부들부들)"

    #위 선택지가 다 끝나면 여기로 온다.
    jh "상심하지마 너희 둘다 임한은 이길 수 없어"       
    
    hide c_jh 
    hide c_kc 
    hide c_yj 
    with dissolve

    "지금 시작합니다."
    nvl clear

    scene background1 with dissolve
    jh "여긴 어디지?"
    show c_jh at truecenter with dissolve
    jh "처음 보는 곳인데?"


    return
