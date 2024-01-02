#import pip
#pip.main(["install","pillow"])
from PIL import Image
picture=Image.open("C:\\Users\\justi\\Downloads\\drago.jpg")
#picture.show()
print(picture.size)
print(picture.format_description)
cropped=picture.crop((0,0,100,100)) #(0,0) is top left. width goes right from it, height goes down from it
#cropped.show()
x=0
y=600
w=int(3840/3)
h=1300
cropped=picture.crop((x,y,w,h))
picture.paste(im=cropped,box=(0,0),mask=cropped) #needs the mask at the end for some reason
#picture.show()
#picture.resize((20,100)).show()
#picture.rotate(90).show()
picture.putalpha(100) #partiall transpart 0-255, paste semi-transparent to merge together
#picture.show()
picture.save("two_dragons.png") #replaces if there is already something named this
purple=Image.open("two_dragons.png")
purple.show()