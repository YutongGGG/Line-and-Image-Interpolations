import time
import matlab.engine


class interface:

    def __init__(self):
        self.eng = matlab.engine.start_matlab()
        self.x0 = matlab.double([7.0, 10.5, 13.0, 17.5, 34.0, 40.5, 44.5, 48.0, 56.0, 61.0, 68.5, 76.5, 80.5, 91.0,
                                 96.0, 101.0, 104.0, 106.5, 111.5, 118.0, 123.5, 136.5, 142.0, 146.0, 150.0, 157.0,
                                 158.0])
        self.x1 = matlab.double([7.0, 10.5, 13.0, 17.5, 34.0, 40.5, 44.5, 48.0, 56.0, 61.0, 68.5, 76.5, 80.5, 91.0,
                                 96.0, 101.0, 104.0, 106.5, 111.5, 118.0, 123.5, 136.5, 142.0, 146.0, 150.0, 157.0,
                                 158.0])
        self.y0 = matlab.double([44, 45, 47, 50, 50, 38, 30, 30, 34, 36, 34, 41, 45, 46, 43, 37, 33, 28, 32, 65, 55,
                                 54, 52, 50, 66, 66, 68])
        self.y1 = matlab.double([44, 59, 70, 72, 93, 100, 110, 110, 110, 117, 118, 116, 118, 118, 121, 124, 121, 121,
                                 121, 122, 116, 83, 81, 82, 86, 85, 68])
        self.x2 = matlab.double([7.0, 10.5, 13.0, 17.5, 34.0, 40.5, 44.5, 48.0, 56.0, 61.0, 68.5, 76.5, 80.5, 91.0,
                                 96.0, 101.0, 104.0, 106.5, 111.5, 118.0, 123.5, 136.5, 142.0, 146.0, 150.0, 157.0,
                                 158.0])
        self.x3 = matlab.double([7.0, 10.5, 13.0, 17.5, 34.0, 40.5, 44.5, 48.0, 56.0, 61.0, 68.5, 76.5, 80.5, 91.0,
                                 96.0, 101.0, 104.0, 106.5, 111.5, 118.0, 123.5, 136.5, 142.0, 146.0, 150.0, 157.0,
                                 158.0])

    def lagrange(self):
        y2 = self.eng.lagrange(self.x0, self.y0, self.x2, nargout=1)
        y3 = self.eng.lagrange(self.x1, self.y1, self.x3, nargout=1)
        self.eng.plot(self.x2, y2, self.x3, y3)
        self.eng.title('Lagrange Interpolation')
        time.sleep(10)

    def xianxingfenduan(self):
        y2 = self.eng.liner(self.x0, self.y0, self.x2, nargout=1)
        y3 = self.eng.liner(self.x1, self.y1, self.x3, nargout=1)
        self.eng.plot(self.x2, y2, self.x3, y3)
        self.eng.title('Piecewise Linear Interpolation')
        time.sleep(10)
        print(str(self.eng.Lagran1(self.x0, self.y0, nargout=1)))

    def baoxing(self):
        y2 = self.eng.hermite1(self.x0, self.y0, self.y0, self.x2, nargout=1)
        y3 = self.eng.hermite1(self.x1, self.y1, self.y0, self.x3, nargout=1)
        self.eng.plot(self.x2, y2, 'b', self.x3, y3, 'r')
        self.eng.title('Shape-Preserving Interpolation')
        time.sleep(10)

    def sanciyangtiao(self):
        y2 = self.eng.Spline0(self.x0, self.y0, self.x2, nargout=1)
        y3 = self.eng.Spline0(self.x1, self.y1, self.x3, nargout=1)
        self.eng.plot(self.x2, y2, 'r', self.x3, y3, 'g')
        self.eng.title('Cubic Spline Interpolation')
        time.sleep(10)


# if __name__ == '__main__':
#     A()
#     A().xianxingfenduan()
