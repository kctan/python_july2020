# instruction
# need to install the qrcode package
# pip install qrcode

import qrcode
img = qrcode.make('http://www.google.com')
img.save("test.png")