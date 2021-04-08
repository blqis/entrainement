import PIL
from PIL import Image



def noircissement(image) :
    (xmax,ymax) = image.size
    for x in range(xmax):
        for y in range(ymax):
            px = image.getpixel((x,y));
            (r,g,b)=px;
            px2 = (r//2, g//2, b//2);
            image.putpixel((x,y), px2)

def test(image) :
    for x in range(250):
        for y in range(250):
            px = image.getpixel((x,y));
            (r,g,b)=px;
            px2 = (r, 0, 0);
            image.putpixel((x,y), px2)


def blanchissement(image) :
    (xmax,ymax) = image.size
    for x in range(xmax):
        for y in range(ymax):
            px = image.getpixel((x,y));
            (r,g,b)=px;
            px2 = (r+(255-r)//2 , g+(255-g)//2, b+(255-b)//2);
            image.putpixel((x,y), px2)



def negatif(image) :
    (xmax,ymax) = image.size
    for x in range(xmax):
        for y in range(ymax):
            px = image.getpixel((x,y));
            (r,g,b)=px;
            px2 = (255-r , 255-g, 255-b);
            image.putpixel((x,y), px2)


def FlipHorizontale(image) :
    (xmax,ymax) = image.size
    for x in range(xmax):
        for y in range(ymax//2):
            px = image.getpixel((x,y))
            px2 = image.getpixel((x,ymax-y-1))
            image.putpixel((x,y), px2)
            image.putpixel((x,ymax-y-1),px)


def Rotation(image):
    i=complex(0,1)
    (xmax,ymax)=image.size
    rot=Image.new("RGB",(xmax,ymax))
    for y in range(ymax):
        for x in range(xmax):
            px=image.getpixel((x,y))
            rot.putpixel((ymax-y-1,x),px)
    return rot


##image = Image.open("peppers.jpg")
##blanchissement(image)
##image.show()
##image.save("peppersBlanchit.jpg")



##image = Image.open("peppers.jpg")
##negatif(image)
##image.show()
##image.save("peppersNegatif.jpg")


##image = Image.open("peppers.jpg")
##FlipHorizontale(image)
##image.show()
##image.save("peppersFlipHoriz.jpg")


##image=Image.open("peppers.jpg")
##rot=Rotation(image)
##rot.show()
##image.save("peppersRotation.jpg")


def binaire(n):
    b = bin(n)
    a = b[2:]
    while len(a) < 8:
        a = "0" + a
    return a


#print(binaire(8))



def dissimulation (imageforte, imagefaible):
    image = Image.new("RGB", (xmax,ymax))
    for x in range(xmax):
        for y in range(ymax):
            pxF = imageforte.getpixel((x,y))
            (rF, gF, bF) = pxF
            pxf = imagefaible.getpixel((x,y))
            (rf, gf, bf) = pxf
            a = []

            for k in range(0,3):

                F = binaire(pxF[k])
                f = binaire(pxf[k])
                newb = F[0:4] + f[0:4]
                new = int(newb, 2)
                a.append(new)
            image.putpixel((x,y), tuple(a))

    return image



def recuperation(imageforte):
    (xmax, ymax) = imageforte.size
    imageR = Image.new("RGB", (xmax,ymax))
    for x in range(xmax):
        for y in range(ymax):
            pxF = imageforte.getpixel((x,y))
            (rF, gF, bF) = pxF

            b = []
            for k in range(0,3):
                F = binaire(pxF[k])
                newb = F[4:] + "1000"
                new = int(newb, 2)
                b.append(new)
            imageR.putpixel((x,y), tuple(b))
    return imageR


#image5 = Image.open("oeuf.jpg")
image = Image.open("image.jpg")
imageR = recuperation(image)
imageR.save("imageR.jpg")

