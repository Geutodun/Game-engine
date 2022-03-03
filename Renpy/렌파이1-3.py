define jh = Character("박준혁", color = "#fc0303")
define yj = Character("즙지욱", color = "#fc038c") # 캐릭터 설정법
define kc = Character("김세찬", color = "#03fc20")
                                           #대화창 캐릭터 이름 색깔

                                    #대사 출력 방식 설정
define narrator = Character(None, kind = nvl)
                                          #화면 전체를 써서 출력


image background = "bg/class1.jpg"  #이미지 불러오기  
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
    kc "나 김세찬 지욱이는 내꺼다!" 
    show c_jh at truecenter with dissolve #사진 y좌표도 가운데로 조정   # 사진을 가운데 정렬        
    jh "난 둘다 좋아"
    
   
    
    return
