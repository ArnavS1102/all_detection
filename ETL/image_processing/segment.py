import sys
import os
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import torch
import matplotlib.patches as patches

from segment_anything import sam_model_registry 
from segment_anything import SamAutomaticMaskGenerator
from segment_anything import SamPredictor

class Segment:
    def __init__(self, pth_path, model_type, device):
        self.pth_path = pth_path
        self.model_type = model_type
        self.device = device
        self.sam = sam_model_registry[model_type](checkpoint = self.pth_path)
        self.sam.to(device=device)
        self.mask_generator = SamAutomaticMaskGenerator(self.sam)

    def create_directories(self, dest_dir):
        os.mkdir(dest_dir, exist_ok=True)
        os.mkdir(f'{dest_dir}/train', exist_ok=True)
        os.mkdir(f'{dest_dir}/test', exist_ok=True)
        os.mkdir(f'{dest_dir}/validation', exist_ok=True)
        
        self.create_class_directories(f'{dest_dir}/train')
        self.create_class_directories(f'{dest_dir}/test')
        self.create_class_directories(f'{dest_dir}/validation')

    def create_class_directories(self, parent_dir):
        classes = ['absent', 'present']
        for class_name in classes:
            class_path = os.path.join(parent_dir, class_name)
            os.mkdir(class_path, exist_ok=True)

    def segment_img(self, image):
        masks = self.mask_generator.generate(image)
        mask = masks[0]

        maskiseg = mask['segmentation']
        box0 = mask['bbox']

        xc, yc, w, h = box0
        x0 = xc
        y0 = yc
        x1 = xc + w
        y1 = yc + h

        boximage = image[y0:y1, x0:x1, :]
        boxmask = maskiseg[y0:y1, x0:x1]

        negative_img = np.tile(boxmask[:, :, np.newaxis], (1, 1, 3)).astype(int)

        masked_image = cv2.multiply(negative_img, boximage, dtype=cv2.CV_8U)
        masked_image = masked_image.astype(np.uint8)

        return masked_image

    def segment_dir(self, source_dir, dest_dir):
        dirs = ['train', 'test', 'validation']
        classes = ['present', 'absent']

        self.create_directories(dest_dir)
        
        for i in dirs:
            for j in classes:
                path = os.path.join(source_dir, i, j)
                for c, k in enumerate(os.listdir(path)):
                    image_path = os.path.join(path, k)
                    img = cv2.imread(image_path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    masked_img = self.segment_img(img)

                    out_path = os.path.join(dest_dir, i, j)
                    plt.imsave(out_path, masked_img)



    
    
        









