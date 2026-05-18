from vpython import *

# 팀 온보딩 샘플: 무지개 정원 구조대
# 고1 초보용 포인트:
# - sphere, box, label로 장면 만들기
# - while True + rate()로 움직임 만들기
# - if 조건문으로 문제를 고치기
# - 키보드 없이도 마우스 클릭/드래그로 상호작용하기

scene_background(color.cyan)

label(pos=vector(0, 3.2, 0), text="무지개 정원 구조대", height=18, color=color.white)
label(pos=vector(0, 2.8, 0), text="구름 클릭: 비 · 땅의 공 클릭: 소리 · 드래그: 공 부르기", height=8, color=color.black)

# 1. 기본 무대
box(pos=vector(0, -0.1, 0), size=vector(8, 0.2, 5), color=color.green)

# 2. 무지개 꽃 만들기
colors = [color.red, color.orange, color.yellow, color.green, color.cyan, color.blue, color.magenta]
flowers = []

for i in range(7):
    x = -3 + i
    stem = box(pos=vector(x, 0.15, 0), size=vector(0.08, 0.6, 0.08), color=color.green)
    head = sphere(pos=vector(x, 0.55, 0), radius=0.28, color=colors[i])
    flowers.append(head)

# 3. 구름: 같은 코드를 조금씩 위치만 바꿔 반복
clouds = []
for x in [-2.5, 0, 2.5]:
    sphere(pos=vector(x, 2.1, -1.5), radius=0.28, color=color.white)
    sphere(pos=vector(x + 0.25, 2.15, -1.5), radius=0.35, color=color.white)
    sphere(pos=vector(x + 0.55, 2.1, -1.5), radius=0.28, color=color.white)
    clouds.append(vector(x + 0.25, 2.12, -1.5))

# 구름을 클릭하면 떨어질 빗방울
raindrops = []
for i in range(28):
    x = -3.8 + (i % 14) * 0.58
    y = 2.6 - (i // 14) * 0.25
    drop = sphere(pos=vector(x, y, 1.4), radius=0.035, color=color.cyan, visible=False)
    raindrops.append(drop)
rain_timer = 0

# 4. 움직이는 정원 구조대 공
hero = sphere(pos=vector(-3.5, 0.45, 1.3), radius=0.25, color=color.white)
hero.velocity = vector(0.05, 0, 0)
hero.attach_trail(color=color.white, retain=50)
click_marker = sphere(pos=vector(0, 0.85, 1.3), radius=0.04, color=color.yellow)

# 5. 소리 + 마우스 이벤트: 구름은 비, 땅의 공은 소리, 드래그는 이동
garden_notes = ['도4', '미4', '솔4', '높은도4']
note_index = 0

# 5. 시행착오 포인트:
# 처음에는 벽 조건을 안 넣으면 공이 화면 밖으로 사라진다.
# 그래서 if 조건문으로 방향을 바꾸도록 수정했다.

while True:
    rate(60)

    # 마우스 클릭/드래그: 구름은 비, 땅의 공은 소리, 나머지는 공 부르기
    mouse = scene.mouse
    if mouse:
        target_x = max(-3.7, min(3.7, mouse.pos.x))
        target_y = mouse.pos.y

        if mouse.clicked:
            # 구름 클릭: 비 내리기
            cloud_clicked = False
            for cloud in clouds:
                if abs(target_x - cloud.x) < 0.8 and abs(target_y - cloud.y) < 0.7:
                    rain_timer = 150
                    cloud_clicked = True
                    play_sfx('pop')

            # 땅에 있는 구조대 공 클릭: 소리 내기
            if not cloud_clicked and abs(target_x - hero.pos.x) < 0.65 and abs(target_y - hero.pos.y) < 0.65:
                play_note(garden_notes[note_index], duration=0.35, type='triangle', volume=0.35)
                note_index = (note_index + 1) % len(garden_notes)
                click_marker.pos = vector(hero.pos.x, hero.pos.y + 0.45, 1.3)
                click_marker.radius = 0.25

        if mouse.down and target_y < 1.5:
            hero.velocity.x = 0.08 if target_x > hero.pos.x else -0.08
            click_marker.pos = vector(target_x, 0.85, 1.3)
            click_marker.radius = 0.18
            nearest = int(round(target_x + 3))
            if 0 <= nearest < len(flowers):
                flowers[nearest].color = colors[(nearest + note_index) % len(colors)]
        elif not mouse.down:
            click_marker.radius = 0.04

    # 비 애니메이션
    if rain_timer > 0:
        rain_timer -= 1
        for i in range(len(raindrops)):
            drop = raindrops[i]
            drop.visible = True
            drop.pos.y -= 0.12
            if drop.pos.y < 0.15:
                drop.pos.y = 2.6
                drop.pos.x = -3.8 + (i % 14) * 0.58
    else:
        for drop in raindrops:
            drop.visible = False

    hero.pos = hero.pos + hero.velocity

    # 공이 정원 끝에 닿으면 반대 방향으로 돌아오기
    if hero.pos.x > 3.7 or hero.pos.x < -3.7:
        hero.velocity.x = -hero.velocity.x
        play_note(garden_notes[note_index], duration=0.18, type='sine', volume=0.25)
        note_index = (note_index + 1) % len(garden_notes)

    # 꽃이 살짝살짝 숨 쉬는 효과
    for i in range(7):
        flowers[i].radius = 0.28 + 0.04 * abs(hero.pos.x - (-3 + i)) / 7

# 다음 팀원이 해볼 TODO
# - 클릭할 때 점수 올리기
# - 꽃에 이름표 붙이기
# - 나비를 추가하고 꽃 주변을 돌게 만들기
# - 공이 꽃에 닿으면 색이 바뀌게 만들기
# - 음표 리스트를 바꿔 우리 팀만의 멜로디 만들기
