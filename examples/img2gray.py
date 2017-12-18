import numpy as np
import scipy.misc
import sys
from PIL import Image

img=scipy.misc.imread(sys.argv[1], mode='L').astype(np.float)
if len(img.shape)==2:
	img=np.dstack((img,img,img))
img=np.clip(img, 0, 255).astype(np.uint8)
Image.fromarray(img).save(sys.argv[1].split('.jpg')[0]+'.grayscale.jpg', quality=95)
