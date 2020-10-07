import qrcode

# Link for website
input_data = "https://coquitos-app.herokuapp.com/"

#Creating an instance of qrcode
def create_qr_code(input_data):      
    qr = qrcode.QRCode(
            version=1, # The higher this value, bigger the dimension of the generated QR Code image.
            box_size=10, #This parameter defines the size of each box in pixels
            border=5) # The border defines the thickness of the border
    qr.add_data(input_data) # method is used to pass our input text, which is the hyperlink to the article in our case
    qr.make(fit=True) # The make function with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if our input data could fit into less number of boxes.
    img = qr.make_image(fill='black', back_color='white') #the make_image function is used where we can specify the foreground and background color. 
    img.save('qrcode001.png')

create_qr_code(input_data)