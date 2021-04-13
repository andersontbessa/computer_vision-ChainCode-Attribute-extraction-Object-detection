
def normalizeImage(v): #função para normalizar a imagem entre zeros e uns.
    v = (v-v.min())/(v.max()-v.min())
    result= (v*255).astype(np.uint8)
    return result

def writeElementInDataset(filename,data):
    newElement = " ".join(str(x) for x in data)
    newElement = newElement.replace(" ", ",") + '\n'
    filename.write(newElement)
