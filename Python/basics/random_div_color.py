#!/usr/bin/python
# coding:utf-8

import colorsys
import random


def get_div_colors(n):          #HLS
    div_colors = []
    i = 0
    step = 360.0 / n
    while i < 360:
        h = i
        s = 90 + random.random() * 10
        l = 50 + random.random() * 10
        for_div_co = [h/360.0, l/100.0, s/100.0]
        div_colors.append(for_div_co)
        i += step

    return div_colors


def ncolors(n):             #RGB
    rgb_colors = []
    if n < 1:
        return rgb_colors
    div_color = get_div_colors(n)
    for div in div_color:
        _r, _g, _b = colorsys.hls_to_rgb(div[0], div[1], div[2])
        r, g, b = [int(x * 255.0) for x in (_r, _g, _b)]
        rgb_colors.append([r, g, b])

    return rgb_colors

print(ncolors(18))
#print(get_div_colors(18))


def RGB_to_Hex(rgb):        #Hex
    RGB = rgb.split(',')
    color = '#'
    for i in RGB:
        n = int(i)
        # hex(), this function is used to convert decimal to hexadecimal.
        color += str(hex(n))[-2:].replace('x', '0').upper()
    print(color)
    return color


def text_save(filename, data):
  file = open(filename, 'a')
  for i in range(len(data)):
    s = str(data[i]).replace('[', '').replace(']', '')
    s = s.replace("'", '') + '\n'
    #file.write(s) #RGB
    HEX = RGB_to_Hex(s)
    #file.write(HEX + '\n')
    file.write('\"{}\", '.format(HEX))       # for R
  file.close()
  print("saved successfully")

text_save("div_colors.txt", ncolors(18))