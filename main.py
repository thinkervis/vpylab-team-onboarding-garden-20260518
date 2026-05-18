from vpython import *

# 팀 온보딩 샘플 3단계: 화면 밖으로 사라지는 문제 해결
# 핵심: if 조건문으로 공이 정원 끝에 닿았는지 확인합니다.

scene_background(color.cyan)

label(pos=vector(0, 3, 0), text="우리 팀의 무지개 정원", height=18, color=color.white)
box(pos=vector(0, -0.1, 0), size=vector(8, 0.2, 5), color=color.green)

colors = [color.red, color.orange, color.yellow, color.green, color.cyan, color.blue, color.magenta]
for i in range(7):
    x = -3 + i
    sphere(pos=vector(x, 0.55, 0), radius=0.28, color=colors[i])
    box(pos=vector(x, 0.15, 0), size=vector(0.08, 0.6, 0.08), color=color.green)

hero = sphere(pos=vector(-3.5, 0.45, 1.3), radius=0.25, color=color.white)
hero.velocity = vector(0.05, 0, 0)
hero.attach_trail(color=color.white, radius=0.03, retain=50)

while True:
    rate(60)
    hero.pos = hero.pos + hero.velocity

    # 문제 해결!
    # x 좌표가 오른쪽 끝(3.7)보다 커지거나 왼쪽 끝(-3.7)보다 작아지면 방향을 바꿉니다.
    if hero.pos.x > 3.7 or hero.pos.x < -3.7:
        hero.velocity.x = -hero.velocity.x

# 배운 점:
# - 움직임은 위치를 조금씩 바꾸는 것
# - 문제 해결은 조건을 관찰하고 if로 규칙을 만드는 것
