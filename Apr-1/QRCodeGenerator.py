import pyqrcode
from pyqrcode import QRCode 
  
# String which represent the QR code 
# s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

s="1234567890"
  
# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("mynumcode.svg", scale = 8) #Here mynumcode.svg file gets created when you run the code