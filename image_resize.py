__author__ = 'verbalist'

from PIL import Image
import time
import unittest
from matplotlib import pyplot as plt

MEDIA_ROOT = 'images/'
im_name = 'test2.jpg'
watermark = 'watermark.png'

class Test(unittest.TestCase):

    def watermark_test(self):
        watermark = 'watermark.png'
        watermark = Image.open(MEDIA_ROOT + str(watermark))
        watermark.convert('RGBA')
        watermask = watermark.convert("L").point(lambda x: max(x, 220))
        watermark.putalpha(watermask)
        resized_image = Image.open(MEDIA_ROOT + im_name)
        resized_image = resized_image.resize((470, 346), Image.ANTIALIAS)
        resized_image.paste(watermark, (320, 210), watermask)
        resized_image.save(MEDIA_ROOT + time.strftime('%H:%M:%S', time.localtime(time.time())) + '.jpeg', "JPEG")

        plt.imshow(resized_image)
        plt.show()
        self.assertEqual(1,1)

    def byte_photo(self):
        watermark = 'watermark.png'
        r = open(MEDIA_ROOT + str(watermark), 'rb')
        import io
        stream = io.BytesIO(r.read())
        im = Image.open(stream)
        im.save(MEDIA_ROOT + time.strftime('%H:%M:%S', time.localtime(time.time())) + '_d.jpeg', "JPEG")
        plt.imshow(im)
        plt.show()


if __name__ == '__main__':
    unittest.main()

