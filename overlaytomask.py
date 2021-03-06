import cv2
import numpy as np

def gen_rgb_mask():
    # Load a colored image and a filter
    org = cv2.imread('input/test.png', cv2.IMREAD_UNCHANGED)  #original image input
    bld = cv2.imread('demo/result.png', cv2.IMREAD_UNCHANGED) #blended image output = mask overlay + original image
    org = cv2.resize(org, (bld.shape[1], bld.shape[0]), interpolation = cv2.INTER_AREA)
    if org.shape[2]==4:
      org = org[:,:,:3]
      cv2.imwrite('input/test.png', org)
    
    # Extract filter overlay on the original image (same formula to remove filter, except exchange 'org' & 'fil')
    fil = cv2.addWeighted(bld,2,org,-1, 0) #segment mask filter
    
    # Save output mask
    cv2.imwrite('demo/rgb_mask.png', fil)