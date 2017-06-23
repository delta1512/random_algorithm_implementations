import PIL
from PIL import Image
from sys import argv,exit
from scipy.spatial import distance

try:
    image = argv[1]
except:
    print('No image specified\nExiting...')
    exit(0)

global hist
try:
    image = Image.open(image)
except:
    print('Image ' + image + ' could not be opened\nExiting...')
    exit(0)
size = image.size
#if the picture is too big, make it smaller
if size[0]*size[1] > 160000:
    image = image.resize((400, 400), PIL.Image.ANTIALIAS)
    size = image.size
pixdata = image.load()
thresh = 50
hist = {}

#converts a tuple with integers into an array with hex values
def tuptohex(tup):
    new = []
    for x in tup:
        tmp = hex(x)[2:]
        if len(tmp) < 2:
            tmp = '0' + tmp
        new.append(tmp)
    return new

#collect a dictionary of unique pixels
for x in range(size[0]):
    for y in range(size[1]):
        pixel = pixdata[x, y]
        if pixel in hist:
            hist[pixel] += 1
        else:
            hist[pixel] = 1

results = []
for x in range(5):
    record = []
    for i, pix in enumerate(hist):
        if i == 0: #get a pixel to compare with
            comparison = pix
            record.append(pix)
        else: #for every other pixel
            if distance.euclidean(comparison, pix) < thresh: #if it's within the threshold
                record.append(pix) #note it down for later
    Sum = 0
    sumPix = [0, 0, 0]
    for key in record: #go through the collected pixels
        Sum += hist[key] #sum the frequencies
        for i, pixval in enumerate(sumPix): #sum each pixel value
            sumPix[i] = pixval + key[i]
        hist.pop(key) #get rid of the pixels we used just then from the main dictionary
    av = round(Sum / len(record)) #average the frequency
    avPix = []
    for pixval in sumPix: #average each pixel value
        avPix.append(round(pixval / len(record)))
    results.append({tuple(avPix): av})

for x in results:
    print(''.join(tuptohex([i for i in x][0])), x[[i for i in x][0]])
