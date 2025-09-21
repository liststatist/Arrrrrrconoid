import pygame

pygame.init()
mw = pygame.display.set_mode((500,500))
mw.fill((200,255,255))
clock = pygame.time.Clock()
game_over = False

class Area():
    def __init__(self,x,y,height,width, color = None):
        self.rect = pygame.Rect(x,y,width,height)
        if color:
            self.fill_color = color
        else:
            self.fill_color = (200,255,255)
    
    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect) 
    
    def outline(self, out_color = (32,68,212), thickness = 5):
        pygame.draw.rect(mw,out_color,self.rect, thickness)
    def coll(self,rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self,file_name,x = 0, y = 0, width = 10, height = 10,x_f = 0,y_f = 0):
        self.x_f = x_f
        self.y_f = y_f
        Area.__init__(self,x = x, y = y, height = height, width = width, color = None)
    
        self.image = pygame.image.load(file_name)
    
    def image_draw(self):
        mw.blit(self.image,(self.rect.x + self.x_f,self.rect.y+ self.y_f))

class Label(Area):
    def set_text(self, text, fsize = 12, text_color = (0,0,0)):
        self.image = pygame.font.SysFont('verdana',fsize).render(text,True,text_color)
    
    def draw(self,shift_x = 0, shift_y = 0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))

ball = Picture('ball.png',200,300,60,60,5,5)
plat = Picture('platform.png',200,550,110,25,5,0)
most = list()
x = 5
y = 5
n = 0
for i in range(24):
    emp = Picture('enemy.png',x,y,50,50,0,0)
    x += 55
    if n == 8:
        y += 55
        x -= 55 * 8 + 25
    elif n == 16:
        y += 55
        x -= 55 * 7 +25
    n +=1
    most.append(emp)
mr = False
ml = False
sp_x = 3
sp_y = 3



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mr = True 
            elif event.key == pygame.K_LEFT:
                ml = True
            elif event.key == pygame.K_q:
                
                 sp_x *= 2
                 sp_y *= 2
            elif event.key == pygame.K_w:
                 sp_x /= 2
                 sp_y /= 2
            if event.key == pygame.K_e:
                for o in most:
                    most.remove(o)
                    o.fill()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mr = False
            elif event.key == pygame.K_LEFT:
                ml = False
    if mr:
        plat.rect.x +=9
    elif ml:
        plat.rect.x -=9
    ball.rect.x += sp_x
    ball.rect.y += sp_y
    if ball.coll(plat.rect):
        sp_y *= -1
    elif ball.rect.y < 0:
        sp_y *= -1
    elif ball.rect.x < 0 or ball.rect.x > 450 :
        sp_x *= -1
    elif plat.rect.x > 400:
        plat.rect.x -=4
    elif plat.rect.x < 0:
        plat.rect.x +=4
    if ball.rect.y > 600:
        wn = Label(100,200,0,0)
        wn.set_text('Ты проиграл!!',50,(255,0,0))
        wn.draw()
        game_over = True

    

    
    mw.fill(200,255,255)   
    if ball.rect.y > 600:
        wn = Label(100,200,0,0)
        wn.set_text('Ты проиграл!!',50,(255,0,0))
        wn.draw()
        game_over = True     
    ball.fill()
    plat.fill()
    for i in most:
        i.image_draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    most.remove(i)
                    i.fill()

        if i.rect.colliderect(ball.rect):
            most.remove(i)
            i.fill()
            sp_y *= -1
    if len(most) == 0:
        win = Label(100,200,0,0)
        win.set_text('Ты победил!!',50,(0,255,0))
        win.draw()
        game_over = True
    ball.image_draw()
    plat.image_draw()
    pygame.display.update()
    clock.tick(40)
    


    












while not game_over:
    clock.tick(40)
    pygame.display.update()
