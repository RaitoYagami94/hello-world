import os.path
import glob
import cv2
def convertjpg(jpgfile,outdir,width=128,height=128):
    
    src = cv2.imread(jpgfile, cv2.IMREAD_ANYCOLOR)
    cv2.imshow('image',src)
    cv2.waitKey(0)
    try:
        dst = cv2.resize(src, (width,height), interpolation=cv2.INTER_CUBIC) 
        cv2.imwrite(os.path.join(outdir,os.path.basename(jpgfile)), dst)
    except Exception as e:
        print(e)
        
for jpgfile in glob.glob(r'C:\Users\hongq\OneDrive\Pictures\flower.jpg'):
    convertjpg(jpgfile,r'C:\Users\hongq\OneDrive\Pictures\flower.jpg')

