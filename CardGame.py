import pygame, random
from resize import Resize
import time
pygame.init()


class Card:
    def __init__(self, screen, resize, W, H, number):
        self.resize = resize
        self.screen = screen
        self.number = number
        self.W = W
        self.H = H
        listedNum = list(str(number))
        if len(listedNum) == 2:
            self.row = 2
            if number >= 10:
                self.column = int(listedNum[1])+1
        else:
            self.row = 1
            if int(listedNum[0]) == 0:
                self.column = 1
            else:
                self.column = int(listedNum[0])

        self.PATH = "IMG/card.png"
        self.img = pygame.image.load(self.PATH)
        self.imgSize = self.img.get_size()
        self.ratioW = self.W/10.09009009009009
        self.ratioH = self.H/2
        self.imgRect = self.img.get_rect(center=((self.ratioW*self.column,
                                                  self.ratioH*self.row - self.imgSize[1])))
        self.font = pygame.font.Font("04B_19.ttf", 32)
        self.color = None
        self.isClicked = False

    def selectColor(self, colorList):
        self.color = random.choice(colorList)
        colorList.remove(self.color)
        return colorList

    def click(self, pos):
        x = pos[0]
        y = pos[1]
        if self.imgRect.left <= x <= self.imgRect.right and self.imgRect.top < y < self.imgRect.bottom:
            return self.color

    def resizeCard(self, W, H):
        self.W, self.H = W, H
        self.ratioW = self.W/10.09009009009009
        self.ratioH = self.H/2
        self.img = self.resize.resizeIMG(self.PATH, self.imgSize)
        self.imgRect = self.img.get_rect(center=((self.ratioW*self.column,
                                                  self.ratioH*self.row - self.imgSize[1])))
        self.font = self.resize.resizeFont(32, "04B_19.ttf")

        self.imgSize = self.img.get_size()

    def draw(self):
        self.screen.blit(self.img, self.imgRect)
        text = self.font.render(f"{self.number}", False, (14, 14, 155))
        textSize = text.get_size()
        self.screen.blit(text, (self.imgRect.centerx-textSize[0]/2, self.imgRect.centery-textSize[1]/2))
        if self.isClicked is True:
            rect = pygame.Rect(self.imgRect.topleft, self.imgSize)
            pygame.draw.rect(self.screen, self.color, rect)


class Bg:
    def __init__(self, screen, resize, W, H):
        self.screen = screen
        self.resize = resize
        self.W = W
        self.H = H
        self.PATH = "IMG/CardGame.png"
        self.img = pygame.image.load(self.PATH)
        self.size = self.img.get_size()
        self.rect = self.img.get_rect(topleft=(0, 0))

    def resizeBg(self, W, H):
        self.W, self.H = W, H
        self.img = self.resize.resizeIMG(self.PATH, self.size)
        self.rect = self.img.get_rect(topleft=(0, 0))
        self.size = self.img.get_size()

    def draw(self):
        self.screen.blit(self.img, self.rect)



class Main:
    def __init__(self):
        pygame.init()
        self.W = 1120
        self.H = 609
        self.gameMode = "Wait"
        self.color = [None, None]
        self.num = [None, None]
        self.wait = False
        self.count = 0
        self.click = 0
        self.clock = pygame.time.Clock()
        self.resize = Resize(self.W, self.H)
        self.screen = pygame.display.set_mode((self.W, self.H), pygame.RESIZABLE)
        self.bg = Bg(self.screen, self.resize, self.W, self.H)
        self.colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (125, 125, 125), (200, 200, 200), (200, 100, 100), (100, 200, 100)
                       , (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (125, 125, 125), (200, 200, 200), (200, 100, 100), (100, 200, 100)]

        self.Card1, self.Card11 = Card(self.screen, self.resize, self.W, self.H, 1), Card(self.screen, self.resize, self.W, self.H, 11)
        self.Card2, self.Card12 = Card(self.screen, self.resize, self.W, self.H, 2), Card(self.screen, self.resize, self.W, self.H, 12)
        self.Card3, self.Card13 = Card(self.screen, self.resize, self.W, self.H, 3), Card(self.screen, self.resize, self.W, self.H, 13)
        self.Card4, self.Card14 = Card(self.screen, self.resize, self.W, self.H, 4), Card(self.screen, self.resize, self.W, self.H, 14)
        self.Card5, self.Card15 = Card(self.screen, self.resize, self.W, self.H, 5), Card(self.screen, self.resize, self.W, self.H, 15)
        self.Card6, self.Card16 = Card(self.screen, self.resize, self.W, self.H, 6), Card(self.screen, self.resize, self.W, self.H, 16)
        self.Card7, self.Card17 = Card(self.screen, self.resize, self.W, self.H, 7), Card(self.screen, self.resize, self.W, self.H, 17)
        self.Card8, self.Card18 = Card(self.screen, self.resize, self.W, self.H, 8), Card(self.screen, self.resize, self.W, self.H, 18)
        self.Card9 = Card(self.screen, self.resize, self.W, self.H, 9)
        self.Card10 = Card(self.screen, self.resize, self.W, self.H, 10)


        self.CardList = [self.Card1, self.Card2, self.Card3, self.Card4, self.Card5, self.Card6, self.Card7, self.Card8, self.Card9, self.Card10,
                         self.Card11, self.Card12, self.Card13, self.Card14, self.Card15, self.Card16, self.Card17, self.Card18]
        self.CardDict = {1: self.Card1, 2: self.Card2, 3: self.Card3, 4: self.Card4, 5: self.Card5, 6: self.Card6, 7: self.Card7, 8: self.Card8
                         , 9: self.Card9, 10: self.Card1, 11: self.Card11, 12: self.Card12, 13: self.Card13, 14: self.Card14, 15: self.Card15, 16: self.Card16, 17: self.Card17, 18: self.Card18}
        self.choseColor()

    def mainResize(self):
        self.W, self.H = self.resize.resizeWidthHeight(self.W, self.H)
        self.resize.resizeScreen()
        self.bg.resizeBg(self.W, self.H)
        for card in self.CardList:
            card.resizeCard(self.W, self.H)

    def choseColor(self):
        for card in self.CardList:
            self.colors = card.selectColor(self.colors)

    def draw(self):
        self.bg.draw()
        if self.gameMode == "GameStart":
            for card in self.CardList:
                card.draw()

    def checkClick(self):
        pos = pygame.mouse.get_pos()
        for card in self.CardList:
            if card.click(pos) and card.isClicked is False:
                self.color[self.click] = card.click(pos)
                self.num[self.click] = card.number
                card.isClicked = True
                self.click += 1
                break
        if self.color[0] is not None and self.color[1] is not None:
            if self.color[0] == self.color[1]:
                self.color = [None, None]
            else:
                self.wait = True
                self.color = [None, None]
        self.checkWin()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                self.W, self.H = event.w, event.h
                self.mainResize()
            if event.type == pygame.KEYDOWN:
                if self.gameMode == "Wait" and event.key == pygame.K_SPACE:
                    self.gameMode = "GameStart"
                    self.bg.PATH = "IMG/CardGameBg.png"
                    self.bg.img = pygame.transform.scale(pygame.image.load(self.bg.PATH), self.bg.size)
                    self.bg.rect = self.bg.img.get_rect(topleft=(0, 0))
            if event.type == pygame.MOUSEBUTTONDOWN and self.wait is False:
                if self.click == 2:
                    self.click = 0
                self.checkClick()

    def checkWin(self):
        count = 0
        for card in self.CardList:
            if card.isClicked is True:
                count += 1
            if count == 18:
                time.sleep(1)
                print("\a")
                pygame.init()
                pygame.quit()
                Main().mainGame()

    def mainGame(self):
        pygame.init()
        while True:
            self.eventLoop()
            self.draw()
            if self.wait is True:
                self.count += 1
                if self.count == 25:
                    self.wait = False
                    self.CardDict[self.num[0]].isClicked = False
                    self.CardDict[self.num[1]].isClicked = False
                    self.count = 0



            pygame.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    Main().mainGame()
