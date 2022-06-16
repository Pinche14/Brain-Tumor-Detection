import torch
import torchvision.transforms as transforms
import cv2
from Log_Writer.logger import App_Logger
import numpy as np

def process(image):
    try:
        logger = App_Logger()

        image_np = np.array(image)
        logger.log("Image converted to Array")
        if len(image_np.shape) < 3:
            image_np = cv2.cvtColor(image_np, cv2.COLOR_GRAY2RGB)
            logger.log("Image converted from grayscale to rgb")
            # image_np = skimage.color.gray2rgb(image_np)

        # image shape ( height , width , channels)
        # we want it to be ( samples , height , width , channels ) -- for tensorflow
        # for pytorch -- ( samples , channels , height , width )

        # Transform Test Image to tensor & resize
        # plt.imshow(image[0][1,:,:])

        image_torch = torch.from_numpy(image_np)
        logger.log("Image converted to Tensor")
        # image = image_torch[np.newaxis, :]
        image = image_torch.permute(2,0, 1)
        logger.log("Image shape changed successfully")

        # Preprocess Image
        image = transforms.Compose([transforms.Resize((256, 256)),
                                    transforms.ToPILImage(),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.5, .5, 0.5], [0.25, .25, 0.25])
                                    ])(image)
        logger.log("Image Transforms applied Successfully")

        image = image[np.newaxis, :]
        image = image.permute( 0,1, 2,3)
        return image
    except Exception as e:
        logger = App_Logger()
        logger.log("ERROR : Error occurred in preprocessing image\n")
        return print(e)