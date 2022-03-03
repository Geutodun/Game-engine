define jh = Character("박준혁", color = "#00ebf7")
define narrator = Character(None, kind = nvl)


image background = "bg/self.jpg"
image background1 = "bg/scary.jpg"
image backgroundclass = "bg/classroom.jpg"
image ch_jh = "character/jh.png"
image ch_jhscary = "character/jhscary.png"
image ch_jhscary1 = "character/jhscary1.png"


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
    show ch_jhscary at truecenter with dissolve
    jh "엄첨 두근거리지?"
    hide ch_jhscary
    show ch_jhscary1 at truecenter
    jh "하하항항항핳핳핳하하"
    "나" "이새끼 미쳤어!!!!!!!!!!!!!!!!!!!!!!"



    return


label class:
    scene backgroundclass with dissolve

    


return
