import qrcode as qr
img = qr.make("https://github.com/Chandan1307?tab=repositories")
# link to generate QR code from

img.save("Github Link QR_CODE.png")