import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#이미지 가져오기
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

keys = [False, False, False, False]
playerpos = [100,100]

#계속 화면이 보이도록 한다.
while True:
    #화면 깨끗하게
    screen.fill((0,0,0)) #R,G,B 값
    
    #모든요소 다시 그리기
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass, (x*grass.get_width(),y*grass.get_height())) #배경은 플레이어코드 위에다가 쓴다.
    screen.blit(castle, (0,30))
    screen.blit(castle, (0,135))
    screen.blit(castle, (0,240))
    screen.blit(castle, (0,345))
            
    screen.blit(player, playerpos)

    
    #화면 다시그리기
    pygame.display.flip()
    
    #게임종료
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            keys[0]=True
        elif event.key == pygame.K_a:
            keys[1]=True
        elif event.key == pygame.K_s:
            keys[2]=True
        elif event.key == pygame.K_d:
            keys[3]=True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            keys[0]=False
        elif event.key == pygame.K_a:
            keys[1]=False
        elif event.key == pygame.K_s:
            keys[2]=False
        elif event.key == pygame.K_d:
            keys[3]=False

#moveplayer
if keys[0]:
    playerpos[1] = playerpos[1] - 5
elif keys[2]:
    playerpos[1] = playerpos[1] + 5
if keys[1]:
    playerpos[0] = playerpos[0] - 5
elif keys[3]:
    playerpos[0] = playerpos[0] + 5


