from vpython import *

# 팀 온보딩 샘플: 무지개 정원 구조대
# 고1 초보용 포인트:
# - sphere, box, label로 장면 만들기
# - while True + rate()로 움직임 만들기
# - if 조건문으로 문제를 고치기
# - TODO를 남겨 팀원이 이어서 개발하기

scene_background(color.cyan)

label(pos=vector(0, 3.2, 0), text="무지개 정원 구조대", height=18, color=color.white)
label(pos=vector(0, 2.8, 0), text="꽃을 지키는 공이 좌우로 움직입니다. 팀원이 이어서 구름/나비/점수를 추가해보세요!", height=8, color=color.black)

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
for x in [-2.5, 0, 2.5]:
    sphere(pos=vector(x, 2.1, -1.5), radius=0.28, color=color.white)
    sphere(pos=vector(x + 0.25, 2.15, -1.5), radius=0.35, color=color.white)
    sphere(pos=vector(x + 0.55, 2.1, -1.5), radius=0.28, color=color.white)

# 4. 움직이는 정원 구조대 공
hero = sphere(pos=vector(-3.5, 0.45, 1.3), radius=0.25, color=color.white)
hero.velocity = vector(0.05, 0, 0)
hero.attach_trail(color=color.white, radius=0.03, retain=50)

# 5. 시행착오 포인트:
# 처음에는 벽 조건을 안 넣으면 공이 화면 밖으로 사라진다.
# 그래서 if 조건문으로 방향을 바꾸도록 수정했다.

while True:
    rate(60)

    hero.pos = hero.pos + hero.velocity

    # 공이 정원 끝에 닿으면 반대 방향으로 돌아오기
    if hero.pos.x > 3.7 or hero.pos.x < -3.7:
        hero.velocity.x = -hero.velocity.x

    # 꽃이 살짝살짝 숨 쉬는 효과
    for i in range(7):
        flowers[i].radius = 0.28 + 0.04 * abs(hero.pos.x - (-3 + i)) / 7

# 다음 팀원이 해볼 TODO
# - 방향키로 hero 조종하기
# - 꽃에 이름표 붙이기
# - 나비를 추가하고 꽃 주변을 돌게 만들기
# - 공이 꽃에 닿으면 색이 바뀌게 만들기
