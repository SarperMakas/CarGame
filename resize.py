import ctypes, pygame


class Resize:
    def __init__(self, W, H):
        self.w = W
        self.h = H
        self.Log = [(self.w, self.h), (self.w, self.h)]
        self.user = ctypes.windll.user32
        self.relW = self.user.GetSystemMetrics(0)
        self.relH = int(self.user.GetSystemMetrics(1) - self.user.GetSystemMetrics(1) // 20.5 + (self.user.GetSystemMetrics(1)*1.017518248175182 - self.user.GetSystemMetrics(1)))
        self.wh_Ratio = self.relW / self.relH
        self.hw_Ratio = self.relH / self.relW
        self.screenW = W
        self.screenH = H

    def resizeScreen(self):
        newScreen = pygame.display.set_mode((self.screenW, self.screenH), pygame.RESIZABLE)
        return newScreen

    def resizeWidthHeight(self, eventW, eventH):
        if self.screenW != eventW:
            self.screenW = int(eventW)
            self.screenH = int(self.screenW // self.wh_Ratio)
        else:
            self.screenH = int(eventH)
            self.screenW = int(self.screenH // self.hw_Ratio)

        self.Log.append((self.screenW, self.screenH))
        return self.screenW, self.screenH


    def resizeIMG(self, IMGPath, imgSize):

        ratioW = self.Log[-2][0] / imgSize[0]
        ratioH = self.Log[-2][1] / imgSize[1]

        W = self.screenW / ratioW
        H = self.screenH / ratioH

        if type(IMGPath) == str:
            newIMG = pygame.transform.scale(pygame.image.load(IMGPath).convert_alpha(), (int(W), int(H)))
        else:
            newIMG = pygame.transform.scale(IMGPath.convert_alpha(), (int(W), int(H)))

        return newIMG


    def resizeFont(self, normalPNT, ttf):
        font = pygame.font.Font(f'{ttf}', int(normalPNT * self.screenH / self.h))
        return font
