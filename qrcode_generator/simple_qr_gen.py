'''
This code will generate a QR code for the text or image which you are passing. 
Requirements - qrcode (can be installed by using pip install qrcode)
'''

import qrcode

input_data = input("Enter text or URL for QR Generation : ")
filename=input("Enter the filename. Default extension is .png : ")

qr =qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename+".png")

#print("QR Code Generated. Kindly check the current folder for the file with the name {}.png".format(filename))
print("QR Code Generated. Kindly check the current folder for the file with the name \033[4m\033[1m{}.png\033[0m".format(filename))
