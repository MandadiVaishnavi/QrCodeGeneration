import qrcode
import qrcode.constants
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=20,
                 border=2)
data="https://github.com/MandadiVaishnavi"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save("qrcode.png")
print("QR code is generated")