from PIL import Image
img = Image.open('chrome2014.png')
pix = img.load()
msg = ""
for i in range(32):
    for j in range(32):
        msg = msg + bin(pix[j,i][0])[-1] + bin(pix[j,i][1])[-1] + bin(pix[j,i][2])[-1]
print(str(msg))
