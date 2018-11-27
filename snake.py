# Simple snake game, based on https://pythonspot.com/snake-with-pygame/
#
# - Hannu Henttinen
# - 2018-11-27

from pygame.locals import *
import sys, pygame, time, random

class Player:
    x = [0]
    y = [0]
    step = 10
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)

        self.x[1]=1*self.step
        self.x[2]=2*self.step

    def update(self):
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

        if self.direction == 0:
            self.x[0] = self.x[0] + self.step
        if self.direction == 1:
            self.x[0] = self.x[0] - self.step
        if self.direction == 2:
            self.y[0] = self.y[0] - self.step
        if self.direction == 3:
            self.y[0] = self.y[0] + self.step

    def moveRight(self):
        if self.direction != 1:
            self.direction = 0
    def moveLeft(self):
        if self.direction != 0:
            self.direction = 1
    def moveUp(self):
        if self.direction != 3:
            self.direction = 2
    def moveDown(self):
        if self.direction != 2:
            self.direction = 3

    def draw(self,surface,image,body):
        for i in range(0,self.length):
            if i==0:
                surface.blit(image,(self.x[i],self.y[i]))
            else:
                surface.blit(body,(self.x[i],self.y[i]))

    def getStep(self):
        return self.step

class Apple:
    x = 0
    y = 0
    step = 10

    def __init__(self,x,y):
        self.x = x*self.step
        self.y = y*self.step

    def draw(self,surface,image):
        surface.blit(image,(self.x,self.y))

    def getStep(self):
        return self.step

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2+bsize-2:
            if y1 >= y2 and y1 <= y2+bsize-2:
                return True
                print("Collision [{},{}] || [{},{}]".format(x,y,width,height))
        return False

    def outOfBounds(self,x,y,width,height,bsize):
        if x > width-bsize or x < 0 or y>height-bsize or y < 0:
            print("[{},{}]".format(x,y))
            return True
        return False

class App:

    size = width, height = 800,600
    player = 0
    apple = 0
    score = 0
    game = 0
    rngMinW, rngMaxW = 0,0
    rngMinH, rngMaxH = 0,0
    isPressed = 0

    def __init__(self):
        self.rngMinW = 1
        self.rngMinH = 1
        self.rngMaxW = self.width/10
        self.rngMaxH = self.height/10
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._body_surf = None
        self.game = Game()
        self.player = Player(3)
        self.apple = Apple(random.randrange(self.rngMinW,self.rngMaxW),random.randrange(self.rngMinH,self.rngMaxH))

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE|pygame.DOUBLEBUF)
        pygame.display.set_caption("Snake, gasp")

        self._running = True
        self._image_surf = pygame.image.load("snake_head.gif").convert()
        self._body_surf = pygame.image.load("snake_body.gif").convert()
        self._apple_surf = pygame.image.load("snake_apple.gif").convert()

    def on_event(self):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        # Eat apple
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i],self.player.y[i],self.apple.getStep()):
                self.apple.x = random.randrange(self.rngMinW,self.rngMaxW)*self.apple.getStep()
                self.apple.y = random.randrange(self.rngMinH,self.rngMaxH)*self.apple.getStep()
                #print("Apple [{},{}]".format(self.apple.x,self.apple.y))
                self.player.length += 3
                self.score += 1

        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i],self.player.y[i],self.player.getStep()):
                print("You lose! Score: {}".format(self.score))
                exit(0)

        if self.game.outOfBounds(self.player.x[0],self.player.y[0],self.width,self.height,self.player.getStep()):
            print("Out of bounds! Score: {}".format(self.score))
            exit(0)

        pass

    def on_render(self):
        self._display_surf.fill((128,128,128))
        self.player.draw(self._display_surf, self._image_surf, self._body_surf)
        self.apple.draw(self._display_surf,self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if(keys[K_RIGHT] and self.isPressed==0):
                self.player.moveRight()
                self.isPressed = 1
            if(keys[K_LEFT] and self.isPressed==0):
                self.player.moveLeft()
                self.isPressed = 1
            if(keys[K_UP] and self.isPressed==0):
                self.player.moveUp()
                self.isPressed = 1
            if(keys[K_DOWN] and self.isPressed==0):
                self.player.moveDown()
                self.isPressed = 1
            if(keys[K_ESCAPE] and self.isPressed==0):
                self._running = False
                print("Thanks for playing. Score: {}".format(self.score))

            self.on_loop()
            self.on_render()

            time.sleep(50.0/1000.0)
            self.isPressed = 0
        self.on_cleanup()

## Start game
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
