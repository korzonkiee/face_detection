"""Maciej Korzeniewski"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
from PIL import Image


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh

    return (x, y, w, h)


i = open("./faces.csv", 'r')
for line in i:
    filename, ymin, xmax, ymax, xmin = line.split(',')
    name, file_extension = os.path.splitext("images/" + filename)
    im = Image.open("images/" + filename)
    w = int(im.size[0])
    h = int(im.size[1])
    b = (float(xmin), float(xmax), float(ymin), float(ymax))
    bb = convert((w, h), b)
    # print(bb)

    o = open(name + ".txt", "a")
    o.write(str(0) + " " +
            " ".join([str(a) for a in bb]) + '\n')
    o.close()
