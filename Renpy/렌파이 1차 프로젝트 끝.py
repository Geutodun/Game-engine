define jh = Character("박준혁", color = "#00ebf7")
define ih = Character("임한", color = "#fce303")
define narrator = Character(None, kind = nvl)
define ch_narrator = Character(None)
define sc = Character("김세찬", color = "#f70000")
define hang1 = Character("빡빡이 아저씨", color = "#62fc03")
define fz = Character("필재", color = "#f5e642")
define yj = Character("지욱밥", color = "#ae00ff")
define right = Position(xalign = 0.96, yalign = 0.4)
define left = Position(xalign = 0.05, yalign = 0.4)


image background = "bg/self.jpg"
image background1 = "bg/scary.jpg"
image backgroundclass = "bg/classroom.jpg"
image backgroundtree = "bg/tree1.jpg"
image ch_jh = "character/jh/jh.png"
image ch_jh scary = "character/jh/jhscary.png"
image ch_jh scary1 = "character/jh/jhscary1.png"
image ch_ih = "character/ih/ih.png"
image ch_ih love = "character/ih/ihlove.png"
image hang1 = "character/char/2.jpg"
image backgroundwine = "bg/wine.jpg"
image backgroundwine1 = "bg/wine1.jpg"
image black = "bg/black.png"
image ch_fz = "character/fz/ff.png"
image ch_fz angry = "character/fz/fz.png"
image ch_fz love = "character/fz/fzlove.jpg"
image ch_yj = "character/yj/yj3.png"
image ch_yj sad = "character/yj/yj4.png"
image ch_yj cheerup = "character/yj/cheer up.jpg"


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

    scene backgroundtree with dissolve
    jh "여기는...도대체 어디지?..."
    "\n"
    "\n"
    "1장 끝"
    "2장 시작"
    nvl clear

    ch_narrator "이곳은 준혁이가 살던 곳과는 매우 다른 곳이었다. 사람들이 있는 건 준혁이가 살던 곳과 같았지만 사람과 동물이 합쳐진 것처럼 보이는 수인들, 귀가 뾰족한 엘프들 등 현실세계에서는 볼 수 없는 풍경이 펼쳐지고 있었다."
    ch_narrator "마침 준혁이 옆을 지나가는 머리가 맨들맨들한 아저씨를 붙잡아 그에게 질문했다."
    show hang1 at truecenter with dissolve
    jh "여기가 어디죠?"
    hang1 "잉???여기가 어딘지도 모르고 여길 왔단 말인가?"
    ch_narrator "그러고는 준혁이의 몸을 보더니 혼잣말로 조금만하게 중얼거렸다"
    hang1 "기억을 잃은 모험가인가? 몸이 좋구만....할짝 아주 좋구만 좋아.."
    jh "뭐가 좋다는 거죠? \n 이상한 말좀 그만하고 여기가 어디인지나 알려주세요?"
    hang1 "아! 아무것도 아닐세. 여기는 너처럼 기억을 잃어버린? 모험가들을 도와주는 즙무소가 있다네. 거기에 한번 가보게나. 참고로 즙무소는 저기 바로 앞에 있는 건물이란다."
    hang1 "번 가보게나. 참고로 즙무소는 저기 바로 앞에 있는 건물이란다. 아 그리고 여기는 이시스 왕국의 헨렌다 마을 이란다. 그럼 난 바빠서 이만.  전☆속☆전☆진 이다."
    hide hang1 with dissolve
    jh "아쉽다 할짝"
    jh "그럼 가볼까?"

    scene backgroundwine with dissolve
    ch_narrator "준혁이가 즙무소 앞에서 혼잣말로 크게 말했다."
    show ch_jh at truecenter
    jh "여기는 이세계인건가? 그럼 현실세계에서의 나는 죽은건가?"
    jh "아직 많은 남자들을 만나보지 못했는데...젠자아아앙!!!!!"
    jh "그래!!!! 그런거야!! 이건 신의 계시가 틀리없어!!!! 현실에서 만나지 못한 남자들을 여기서 만나라는 거야!!!!"
    jh "내가 왜 이런 신의 큰 뜻을 진작 이해하지 못한 거지? 정말 멍청하군. 하늘과 신의 뜻이 이러하다면....난 그 뜻을 받들어 반☆드☆시 모든 남자를 내 것으로  만들겠어!!!"
    ch_narrator "굳세게 다짐하며 즙무소 안으로 들어갔다"
    hide ch_jh with dissolve


    scene black with dissolve
    ch_narrator "“짤-랑-짤-랑”"
    ch_narrator "즙무소의 문에 있는 종이울리며 준혁이가 들어간다."

    scene backgroundwine1 with dissolve
    ch_narrator "즙무소에 들어가자 즙무소의 안내 직원인 필재가 다가온다"
    show ch_fz at truecenter with dissolve
    fz "“어서오세요. 무엇을 도와드릴까요?"
    fz "음...가만 보니 모험가이신 것 같네요. 미션을 받으러 오셨나요?"

    menu:
        "모험가요??? 아뇨":
            jump office
        "네 미션을 받으러 왔습니다":
            fz "모험가 카드를 보여주세요"
            jh "여기 있습니다"
            show ch_fz love at truecenter with dissolve
            fz "(어멋 이 너무나 휼룡한 근육 어멋!!!)"
            ch_narrator "필재가 사진을 챙기며"
            show ch_fz at truecenter with dissolve
            fz "이건 모험가 카드가 아님니다."
            jh "그전에 카드를 돌려주...."
            fz "지금 모험가 카드도 아닌 것을 주신 것을 보면 지금 절 놀리시는 걸로 봐도 되겠습니까?"
            jump office


return

label office:

    jh "전 그게 아니라 뿌쓩 빠쑝(앞에 일을 설명하는 소리)"
    show ch_fz angry at truecenter
    fz "썩 꺼지지 못해!!! 여기서 지욱밥님의 사랑을 받을 수 있는 건 오직 나 하나뿐 이라고!!!"
    fz "너가  몸이 아무리 좋아도 지욱밥님은 니 녀석이 탐낼 수 없어!!!"
    jh "지욱밥님이라...좋아 지욱밥이라는 남자를 내것으로 만들겠어!!!!"
    ch_narrator "그때 즙무소에 누군가가 들어온다"
    hide ch_fz
    yj "필재. 왜 이리 즙무소가 소란스럽지?"
    jh "내 생각이 맞다면 저 남자가 바로!!!!"
    show ch_yj at truecenter with dissolve
    yj "음...당신은 아마도 여기가 처음 이겠죠? 저희 직원이 무례했던 점은 제가 대신 사과드리죠. 아...그런데 당신의 이름은"
    jh "박☆준☆혁이라고 합니다"
    yj "아. 준혁씨 만나서 반가워요. 그러고 보니 제 소개가 늦었군요. 저는"
    jh "자기!!! 아니 지욱씨!!! 아니 지욱밥님이 맞으시죠?"
    yj "하 하 하 맞습니다. 제가 그렇게나 유명하던가요? 저를 알아봐주시다니. 정말 감사합니다. 네 제가 바로 즙무소의 관리인인 윤지욱이라고 합니다."
    yj "근데 준혁씨는 여긴 무슨일로 오셨나요?"
    jh "당신!!!그러니 윤지욱 당신을 내것으로 만들기위해 왔다!!!"
    hide ch_yj 
    show ch_yj at right with dissolve
    show ch_fz at left with dissolve
    fz "지욱밥님은 나만의 것이야!"
    ch_narrator "필재에게 다가가는 지욱이의 팔을 준혁이가 붙잡고"
    jh "어딜가는거야. 이제 넌 내꺼라고!"
    ch_narrator "이 모습을 본 필재는 지욱이에게서 준혁이를 떨어뜨리려 했지만 준혁이가 휘두른 왼팔에 가볍게 즙무소의 구석으로 날라가 버렸다."
    fz "이...런...힘 이라면 분명 지욱밥님을 행복하게 해드릴수있을거야"
    fz "앞으로 지욱밥님을 부탁한다"
    ch_narrator "필재가 쓰러지며 눈을 감았다."
    hide ch_fz with dissolve
    hide ch_yj with dissolve
    show ch_yj at truecenter with dissolve
    yj "안돼 필재 여기서 죽으면 흑흑 평생 행복하게 같이 살기로 했잖아"
    ch_narrator "준혁이가 지욱이를 껴안으며"
    jh "지욱밥 내가 당신을 행복하게 해주겠어"
    show ch_yj sad at truecenter with dissolve
    yj "크..흐...흡흑"
    yj "필재 그는 좋은 친구였고 좋은 남친이었어~!!!!"
    jh "내가 더 행복하게 만들어 줄 수 있어!!"
    yj "정말?"
    jh "물론이야"
    yj "한번 믿어볼게"
    ch_narrator "그 고백을 받아주며 주위 사람들의 박수와 환호를 받으며 새로운 커플의 탄생을 알렸다."
    show ch_yj cheerup at truecenter with dissolve
    "주위 사람들" "정말 축하해"
    "주위 사람들" "정말 잘 됐다"
    "주위 사람들" "꼭 행복해야해"

    "\n"
    "\n"
    "2장끝"








return
