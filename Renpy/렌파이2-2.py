define jh = Character("박준혁", color = "#00ebf7")
define ih = Character("임한", color = "#fce303")
define narrator = Character(None, kind = nvl)
define ch_narrator = Character(None)
define sc = Character("김세찬", color = "#f70000")


image background = "bg/self.jpg"
image background1 = "bg/scary.jpg"
image backgroundclass = "bg/classroom.jpg"
image backgroundtree = "bg/tree1.jpg"
image ch_jh = "character/jh/jh.png"
image ch_jh scary = "character/jh/jhscary.png"
image ch_jh scary1 = "character/jh/jhscary1.png"
image ch_ih = "character/ih/ih.png"
image ch_ih love = "character/ih/ihlove.png"



label start:
    scene background with fade 
    "\n"
    "게임 제목:준혁이의 이세계 미연시"
    "게임 원작:현실세계에서는 찐따였던 내가 이세게에서는 지욱밥 남친이라닛?! 너무 행복 할 수 밖에 없다."
    "원작자:김민종"
    "원작 일러스터:긍정의 참치"
    "게발자:Geutodun"
    nvl clear

    show ch_jh at truecenter with dissolve
    jh "안녕 나는 이 게임의 주인공이야"
    jh "앞으로 너와 함께 이 게임을 함께 해져 나갈 생각을 하니 두근거려!"
    jh "너도 그렇지?"
    

    $self_point = 0


    menu:
        "나도 두근거려":
            $self_point = self_point + 1
            jh "좋아"
        "전혀":
            $self_point = self_point - 1
            jh "진짜로?"


    if self_point > 0:
        jh "그럼 게임을 즐기러 가자"
        jump class
    else:
        jh "장난이지?"


    menu:
        "미안 장난이었어":
            jh "역시~"
            $self_point = self_point + 1
        "미친거 아니니?":
            jh ". . . . . . "

    if self_point == 0:
        jh "그럴줄 알았어 우리 게임을 즐기러 가보자"
        jump class
    else:
        jh ". . . . . . . . ."


    hide ch_jh with dissolve
    "나" "뭐야 어디 갔어?"
    
    scene background1 with dissolve
    "나" "여긴 어디야!!"
    jh "두근거리지 않다면 두근거리게 만들어 주지!!"
    show ch_jh scary at truecenter 
    jh "엄첨 두근거리지?"
    show ch_jh scary1 at truecenter 
    jh "하하항항항핳핳핳하하"
    "나" "이새끼 미쳤어!!!!!!!!!!!!!!!!!!!!!!"



    return


label class:
    scene backgroundclass with dissolve
    ih "준혁아 준혁아!!"
    jh "음냐음냐 임한 넌 내꺼야!! 음냐 음냐"
    show ch_ih at truecenter with dissolve
    ih "야 박준혁 야!!!"
    jh "읏☆흥"
    jh "아 뭐야 벌써 점심시간인가. 오 반장 깨워줘서 고마워~"
    show ch_ih love at truecenter
    ih "어 뭐야 저 녀석 정말 매력있잖...아! 아닛! 이게 아니라 빨리 밥이나 쳐 먹으라 가!!!"
    hide ch_ih love with dissolve
    jh "벌써 가버린 건가? 깜짝 놀라게 만들어 쥬지."
    ch_narrator "준혁이는 이 말을 하자마자 바로 5층임에도 불구하고 한치의 망설임 없이 창문으로 뛰어내렸다."
    ch_narrator "그 순간 이상한 빛이 준혁이의 몸을 감싸더니 준혁이는 정신을 잃고 말았다."
    sc "준혁아 안돼!!!!"
    ih "01035004265"

    scene backgroundtree with dissolve
    jh "여기는...도대체 어디지?..."
    "\n"
    "\n"
    "1장 끝"
    "2장 시작"
    nvl clear

return
