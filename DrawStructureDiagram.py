from PIL import Image
import PIL.ImageDraw
import os
import csv


def StitchImages(Stitching, currentimage):
    cimg = Image.open(currentimage)
    dst = Image.new(
        'RGB', (Stitching.width, Stitching.height + cimg.height))
    dst.paste(Stitching, (0, 0))
    dst.paste(cimg, (0, Stitching.height))
    return dst


def DrawSpacer():
    spacerwidth = 3000
    spacerheight = 50
    spacer = (spacerwidth, spacerheight)
    img = Image.new('RGB', spacer, color='white')
    img.save('spacer.png')


def AddSpacer(Spacing):
    addspacerimg = Image.open("Spacer.png")
    spt = Image.new(
        'RGB', (Spacing.width, Spacing.height + addspacerimg.height))
    spt.paste(Spacing, (0, 0))
    spt.paste(addspacerimg, (0, Spacing.height))
    return spt


def DrawScaleBar():
    # Define initial diagram characteristics
    canvaswidth = 3000
    canvasheight = 50
    canvas = (canvaswidth, canvasheight)
    # Initialize white canvas
    img = Image.new('RGB', canvas, color='white')
    img.save("scale" + '.png')
    im = Image.open("scale" + '.png')
    d = PIL.ImageDraw.Draw(im)
    # Draw black line through the middle of the rectangle that starts at the left and goes a number of pixels right equal to the length of the protein
    d.line([(0, canvasheight), (3000, canvasheight)],
           fill=(0, 0, 0), width=7, joint=None)
    im.save("scale" + '.png')
    d.line([(0, 0), (0, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    d.line([(250, canvasheight/2), (250, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(500, canvasheight/2), (500, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(750, canvasheight/2), (750, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(1000, canvasheight), (1000, 0)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(1250, canvasheight/2), (1250, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(1500, canvasheight/2), (1500, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(1750, canvasheight/2), (1750, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(2000, 0), (2000, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(2250, canvasheight/2), (2250, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(2500, canvasheight/2), (2500, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(2750, canvasheight/2), (2750, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')
    d.line([(3000, 0), (3000, canvasheight)],
           fill=(0, 0, 0), width=5, joint=None)
    im.save("scale" + '.png')


def DrawGeneStructure(geneID, length, SignalPeptide, LRRStart, LRREnd, MalectinStart, MalectinEnd, TMDomainStart, TMDomainEnd):
    # This method can be modified to fit specific needs

    # Define initial diagram characteristics
    canvaswidth = 3000
    canvasheight = 50
    canvas = (canvaswidth, canvasheight)

    # Initialize white canvas
    img = Image.new('RGB', canvas, color='white')
    img.save(geneID + '.png')
    im = Image.open(geneID + '.png')
    d = PIL.ImageDraw.Draw(im)

    # Draw black line through the middle of the rectangle that starts at the left and goes a number of pixels right equal to the length of the protein
    d.line([(0, canvasheight/2), (length, canvasheight/2)],
           fill=(0, 0, 0), width=7, joint=None)
    im.save(geneID + '.png')

    # Draw a red filled rectangle that describes the signal peptide
    if SignalPeptide > 0:
        d.rectangle([(0, 0), (SignalPeptide, canvasheight)],
                    fill=(255, 0, 0), outline=(0, 0, 0), width=3)
        im.save(geneID + '.png')

    # Draw a blue filled rectangle that describes the LRR domain start and end
    d.rectangle([(LRRStart, 0), (LRREnd, canvasheight)],
                fill=(100, 100, 255), outline=(0, 0, 0), width=3)
    im.save(geneID + '.png')

    # Draw a green filled rectangle that describes the Malectin domain start and end
    if MalectinStart > 0:
        d.rectangle([(MalectinStart, 0), (MalectinEnd, canvasheight)],
                    fill=(100, 255, 100), outline=(0, 0, 0), width=3)
        im.save(geneID + '.png')

    # Draw a purple filled rectangle that describes the TM domain start and end
    d.rectangle([(TMDomainStart, 0), (TMDomainEnd, canvasheight)],
                fill=(200, 50, 200), outline=(0, 0, 0), width=3)
    im.save(geneID + '.png')


# Here we are creating empty lists which we will populate with values from the CSV file containing the data for the domain start/end positions
# This can be edited to match your dataset
lengths = []
TMStarts = []
TMEnds = []
MalectinStarts = []
MalectinEnds = []
GeneIDs = []
SignalPeptides = []
LRRStarts = []
LRREnds = []

# Here we populate the empty lists we made before with the data from our csv file that contains the domain start/end annotations
# You can edit this to fit your data, but for mine, I used Gene ID,Length,Signal Peptide End,eLRR Start,eLRR End,Malectin Domain Start,Malectin Domain End,TM Domain Start,TM Domain End
with open('annotations2.csv', newline='') as annotationscsv:
    genereader = csv.reader(annotationscsv, delimiter=',')
    for row in genereader:
        GeneIDs.append(row[0])
        lengths.append(int(row[1]))
        SignalPeptides.append(int(row[2]))
        LRRStarts.append(int(row[3]))
        LRREnds.append(int(row[4]))
        MalectinStarts.append(int(row[5]))
        MalectinEnds.append(int(row[6]))
        TMStarts.append(int(row[7]))
        TMEnds.append(int(row[8]))


# Here we go through each gene and make a png that describes its structure.
counter = 0
while counter < len(GeneIDs):
    DrawGeneStructure(GeneIDs[counter], lengths[counter], SignalPeptides[counter], LRRStarts[counter],
                      LRREnds[counter], MalectinStarts[counter], MalectinEnds[counter], TMStarts[counter], TMEnds[counter])
    print("Drawing " + GeneIDs[counter])
    counter = counter + 1

# Now we draw a png that is just white space that we can stitch in between each of these pngs.
DrawSpacer()

# Here we create the image that we will begin to stitch
StitchedImage = Image.new('RGB', (3000, 20), (255, 255, 255))

for geneimg in GeneIDs:
    StitchedImage = StitchImages(StitchedImage, geneimg + ".png")
    StitchedImage = AddSpacer(StitchedImage)
    print("Stitching " + geneimg)

StitchedImage.save("Stitched.png")
