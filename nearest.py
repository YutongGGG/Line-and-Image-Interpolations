import numpy as np


class nearest:

    def function1(img,times):
        height, width, channels = img.shape
        emptyImage = np.zeros((height * times, width * times, channels), np.uint8)
        sh = height * times / height
        sw = width * times / width
        for i in range(height * times):
            for j in range(width * times):
                x = int(i / sh)
                y = int(j / sw)
                emptyImage[i, j] = img[x, y]
        return emptyImage

