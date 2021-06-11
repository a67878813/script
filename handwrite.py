from PIL import Image, ImageFont

from handright import Template, handwrite

text = "啊啊啊啊巴巴爸爸啛啛喳喳顶顶顶顶柔柔弱弱共和国刚刚\n\r 顶顶顶顶灌灌灌灌哈哈哈哈斤斤计较坎坎坷坷啦啦啦啦噢噢噢噢噗噗噗噗噗"
template = Template(
    background=Image.new(mode="1", size=(3300, 1000), color=1),
    font=ImageFont.truetype("C:\\font\\MiNiJianJiaShu-1.ttf", size=150),
    word_spacing = 2, line_spacing_sigma = 1,
    font_size_sigma = 2,
    word_spacing_sigma = 0.8,
    perturb_x_sigma = 3,
    perturb_y_sigma = 3,
    perturb_theta_sigma = 0.1
)
images = handwrite(text, template)
for im in images:
    assert isinstance(im, Image.Image)
    im.save("C:\\font\\3.png")
    #im.show()
