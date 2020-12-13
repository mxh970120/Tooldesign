# -*- coding=utf-8 -*-

from PIL import Image

# 用来作画的字符
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':

    im = Image.open('luxun.jpg')
    # 列多一点，不然效果一般
    im = im.resize((700, 269), Image.NEAREST)

    txt = ""

    for i in range(269):
        for j in range(700):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    with open("output.txt", 'w') as f:
        f.write(txt)