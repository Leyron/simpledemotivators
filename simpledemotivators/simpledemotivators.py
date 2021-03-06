from PIL import Image, ImageDraw, ImageFont, ImageOps
from simpledemotivators import settings
import textwrap

str1 = ''
str2 = ''


class demcreate:
        def __init__(self, text1: str, text2: str) -> str:
                self._text1 = text1
                self._text2 = text2

        def makeImage(self, file, RESULT_FILENAME=None):
                self._file = file
                size2 = 80
                size3 = 60
                img = Image.new('RGB', (1280, 1024), color=('#000000'))
                img_border = Image.new('RGB', (1060, 720), color=('#000000'))
                border = ImageOps.expand(img_border, border=2, fill='#ffffff')
                user_img = Image.open(file).convert("RGBA").resize((1050, 710))
                (width, height) = user_img.size
                img.paste(border, (111, 96))
                img.paste(user_img, (118, 103))
                drawer = ImageDraw.Draw(img)
                font_1 = ImageFont.truetype(font='times.ttf', size=size2, encoding='UTF-8')
                textWidth = font_1.getsize(self._text1)[0]
                while textWidth >= (width+250) - 20:
                        font_1 = ImageFont.truetype(font='times.ttf', size=size2, encoding='UTF-8')
                        textWidth = font_1.getsize(self._text1)[0]
                        size2 -= 1
                font_2 = ImageFont.truetype(font='times.ttf', size=size3, encoding='UTF-8')
                textWidth = font_2.getsize(self._text2)[0]
                while textWidth >= (width+250) - 20:
                        font_2 = ImageFont.truetype(font='times.ttf', size=size3, encoding='UTF-8')
                        textWidth = font_2.getsize(self._text2)[0]
                        size3 -= 1
                size_1 = drawer.textsize(self._text1, font=font_1)
                drawer.text(((1280 - size_1[0]) / 2, 820), self._text1, fill=(240, 230, 210), font=font_1)
                size_2 = drawer.textsize(self._text2, font=font_2)
                drawer.text(((1280 - size_2[0]) / 2, 920), self._text2, fill=(240, 230, 210), font=font_2)
                if RESULT_FILENAME == None:
                        img.save(settings.RESULT_FILENAME)
                else:
                        img.save(RESULT_FILENAME)

        def setline(self, text):
                if len(text) > 12:
                        photo1 = Image.open(self._file)
                        (width, height) = photo1.size
                        idraw = ImageDraw.Draw(photo1)
                        idraw.line((780,815, 1020, 815), fill=0, width=4)
                        font_2 = ImageFont.truetype(font='times.ttf', size=25, encoding='UTF-8')
                        size_2 = idraw.textsize(text, font=font_2)
                        idraw.text((((width+520) - size_2[0]) / 2, ((height-195) - size_2[1])), text, font=font_2)
                        photo1.save(settings.RESULT_FILENAME)
                else:
                        photo1 = Image.open(settings.RESULT_FILENAME)
                        (width, height) = photo1.size
                        idraw = ImageDraw.Draw(photo1)
                        idraw.line((940,817, 1065, 817), fill=0, width=4)
                        font_2 = ImageFont.truetype(font='times.ttf', size=20, encoding='UTF-8')
                        size_2 = idraw.textsize(text, font=font_2)
                        idraw.text((((width+729) - size_2[0]) / 2, ((height-192) - size_2[1])), text, font=font_2)
                        photo1.save(settings.RESULT_FILENAME)

class prodemoty:
        def __init__(self, str1: str, str2: str) -> str:
                self._str1 = str1
                self._str2 = str2
                
        def setimg(self, TEMPLATE_COORDS: str, TEMPLATE_WIDTH: str, TEMPLATE_HEIGHT: str, PADDING: str):
                self._TEMPLATE_COORDS = TEMPLATE_COORDS
                self._TEMPLATE_WIDTH = TEMPLATE_WIDTH
                self._TEMPLATE_HEIGHT = TEMPLATE_HEIGHT
                self._PADDING = PADDING

        def setfont(self, UPPER_FONT: str, UPPER_SIZE: str, UPPER_FONT_Y: str, LOWER_FONT: str, LOWER_SIZE: str, LOWER_FONT_Y: str):
                self._UPPER_FONT = UPPER_FONT
                self._UPPER_SIZE = UPPER_SIZE
                self._UPPER_FONT_Y = UPPER_FONT_Y
                self._LOWER_FONT = LOWER_FONT
                self._LOWER_SIZE = LOWER_SIZE
                self._LOWER_FONT_Y = LOWER_FONT_Y
                
        def isValidExtension(filename):
            for extension in EXTENSIONS:
                if settings.filename.endswith(extension):
                    return True
            return False


        def drawXAxisCenteredText(image, text, font, size, pos_y):
            draw = ImageDraw.Draw(image)
            textFont = ImageFont.truetype(font, size)
            textWidth = textFont.getsize(text)[0]

            while textWidth >= self._TEMPLATE_WIDTH - self._PADDING * 2:
                textFont = ImageFont.truetype(font, size)
                textWidth = textFont.getsize(text)[0]
                size -= 1
            
            draw.text(((self._TEMPLATE_WIDTH - textWidth) / 2, pos_y), text, font = textFont)

        def getSizeFromArea(self, area):
            return (area[2] - area[0], area[3] - area[1])

        def makeImage(self, file):
            frame = Image.open(settings.TEMPLATE_FILENAME)
            demot = Image.open(file)
            demot = demot.resize(self.getSizeFromArea(self._TEMPLATE_COORDS), Image.ANTIALIAS)
            frame.paste(demot, self._TEMPLATE_COORDS)

            demcreate.drawXAxisCenteredText(frame, self._str1,
                                  self._UPPER_FONT, self._UPPER_SIZE,
                                  self._UPPER_FONT_Y)
            demcreate.drawXAxisCenteredText(frame, self._str2,
                                  self._LOWER_FONT, self._LOWER_SIZE,
                                  self._LOWER_FONT_Y)
            frame = frame.convert("RGB")
            frame.save(settings.RESULT_FILENAME)
            frame.show()

class arrangedem:
        def __init__(self, text1: str, text2: str) -> str:
                self._text1 = text1
                self._text2 = text2

        def makeImage(self, file):
                size2 = 80
                size3 = 60
                user_img = Image.open(file).convert("RGBA")
                (width, height) = user_img.size
                img = Image.new('RGB', (width+250, height+240), color=('#000000'))
                img_border = Image.new('RGB', (width+10, height+10), color=('#000000'))
                border = ImageOps.expand(img_border, border=2, fill='#ffffff')
                img.paste(border, (111, 96))
                img.paste(user_img, (118, 103))
                drawer = ImageDraw.Draw(img)
                font_1 = ImageFont.truetype(font='times.ttf', size=50, encoding='UTF-8')
                textWidth = font_1.getsize(self._text1)[0]
                while textWidth >= (width+250) - 20:
                        font_1 = ImageFont.truetype(font='times.ttf', size=size2, encoding='UTF-8')
                        textWidth = font_1.getsize(self._text1)[0]
                        size2 -= 1
                font_2 = ImageFont.truetype(font='times.ttf', size=30, encoding='UTF-8')
                textWidth = font_2.getsize(self._text2)[0]
                while textWidth >= (width+250) - 20:
                        font_2 = ImageFont.truetype(font='times.ttf', size=size3, encoding='UTF-8')
                        textWidth = font_2.getsize(self._text2)[0]
                        size3 -= 1
                size_1 = drawer.textsize(self._text1, font=font_1)
                drawer.text((((width+250) - size_1[0]) / 2, ((height+170) - size_1[1])), self._text1, fill=(240, 230, 210), font=font_1)
                size_2 = drawer.textsize(self._text2, font=font_2)
                drawer.text((((width+250) - size_2[0]) / 2, ((height+215) - size_2[1])), self._text2, fill=(240, 230, 210), font=font_2)
                img.save(settings.RESULT_FILENAME)
class quote:
        def __init__(self, text: str, name: str) -> str:
                self._text = text
                self._name = name

        def get(self, file, RESULT_FILENAME='qresult.jpg'):
                text = ''
                lines = textwrap.wrap('"' + self._text + '"', width=24)

                for i in lines:
                        text = text + i + '\n'
                user_img = Image.new('RGB', (1155, 600), color=('#000000'))

                drawer = ImageDraw.Draw(user_img)
                font_1 = ImageFont.truetype(font='arialbd.ttf', size=40, encoding='UTF-8')

                drawer.text((529, 90), text[:292], fill='white', font=font_1)

                drawer.text((112, 510), self._name, fill='white', font=font_1)
                img = Image.open(file).convert("RGBA").resize((400, 400))
                user_img.paste(img, (100, 100))
                    
                user_img.save(RESULT_FILENAME)
