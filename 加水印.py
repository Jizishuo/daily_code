from PIL import Image, ImageDraw, ImageFont

im = Image.open("F:/python项目/日常代码/touxiang.jpg").convert("RGBA")
txt = Image.new("RGBA", im.size, (0,0,0,0))

draw = ImageDraw.Draw(txt)
mark = u"中文xxxxxxxxx@aaa"
fnt = ImageFont.truetype("msyhbd", 15) #要加中文字体才能识别中文
point = (txt.size[0] - 155, txt.size[1]-45) #位置
draw.text(point, mark, font=fnt, fill=(255,255,255,255))

out = Image.alpha_composite(im, txt)
out.save('out.png')
out.close()

'''
#判断是否是图片文件
        if not os.path.splitext(savePath)[-1].lower() in ['.jpg', '.jpge', '.png', '.bmp']:
            return
            '''