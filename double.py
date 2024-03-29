import cv2
import numpy as np


class double:

    def function2(img, m, n):
        height, width, channels = img.shape
        emptyImage = np.zeros((m, n, channels), np.uint8)
        value = [0, 0, 0]
        sh = m / height
        sw = n / width
        for i in range(m):
            for j in range(n):
                x = i / sh
                y = j / sw
                p = (i + 0.0) / sh - x
                q = (j + 0.0) / sw - y
                x = int(x) - 1
                y = int(y) - 1
                for k in range(3):
                    if x + 1 < m and y + 1 < n:
                        value[k] = int(
                            img[x, y][k] * (1 - p) * (1 - q) + img[x, y + 1][k] * q * (1 - p) + img[x + 1, y][k] * (
                                    1 - q) * p + img[x + 1, y + 1][k] * p * q)
                emptyImage[i, j] = (value[0], value[1], value[2])
        return emptyImage
