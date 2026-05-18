from vpython import *

# 팀 온보딩 샘플 2단계: 움직이는 구조대 공 추가
# 시행착오: 아직 벽에서 튕기는 조건이 없어서 공이 화면 밖으로 사라집니다.

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

# 관찰 기록:
# - 공이 움직이는 건 성공!
# - 하지만 계속 오른쪽으로만 가서 화면 밖으로 사라진다.
# 다음 팀원이 해볼 일:
# - if 조건문으로 정원 끝에서 방향을 바꾸기
