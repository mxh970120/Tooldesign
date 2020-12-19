from PIL import Image, ImageDraw

imgpath = 'test.png'  # 图片路径

# 读取图片RGB信息到array列表
im = Image.open(imgpath)  # 打开图片到im对象
w, h = im.size  # 读取图片宽、高
# print(w,h)
im = im.convert('RGB')  # 将im对象转换为RBG对象

array = []
for x in range(w):  # 输出图片对象每个像素点的RBG值到array
    for y in range(h):
        r, g, b = im.getpixel((x, y))  # 获取当前像素点RGB值
        rgb = (r, g, b)
        array.append(rgb)
print(array)

# 创建新图片对象
image = Image.new('RGB', (w, h), (255, 255, 255))

# 创建Draw对象用于绘制新图:
draw = ImageDraw.Draw(image)

i = 0
# 填充每个像素并对对应像素填上RGB值:
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=array[i])
        i = i + 1
image.save('new_im.jpg', 'jpeg')
