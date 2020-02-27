# imageGradientBlending
CIS 581 course project

## Implementation of blending images in the gradient domain as described in the paper Poisson Image Editing by Patrick Perez, Michel Gangnet and Andrew Blake.

## To run

First, to generate a mask for the source image: type—— python3 createMask.py --path '1_source.jpg’——  in terminal and manually draw a rough boundary for it. Then, run my “scrip.py ” it will take the source image, mask, target image as inputs and  result in the final blended image.

I have imported library “cv2” only to split image channels and merge them back.
And the “scipy.sparse.linalg.spsolve” function is used to solve the linear functions I build.


