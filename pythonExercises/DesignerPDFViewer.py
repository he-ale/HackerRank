

def designerPdfViewer(h: list[int], word: str):
    word= word.strip()
    height= 0
    size= 0
    for c in word:
        i= ord(c)-ord('a')
        height= max(height, h[i])
        size+= 1

    return height*size