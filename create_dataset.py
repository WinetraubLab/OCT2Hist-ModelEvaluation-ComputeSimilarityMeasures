import torch
import torchvision
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import color

import os
import shutil

images_path = "C:/Users/pato_/Documents/Code Projects/OCT2Hist-ModelEvaluation-ComputeSimilarityMeasures/images/Aidan images/"
destination = "C:/Users/pato_/Documents/Code Projects/OCT2Hist-ModelEvaluation-ComputeSimilarityMeasures/images/Pix2Pix Dataset2/"
model_path = "C:/Users/pato_/Documents/Code Projects/OCT2Hist-ModelEvaluation-ComputeSimilarityMeasures/sam_vit_h_4b8939.pth"
model_type = "vit_h"

bright_mask = None
max_mean_mask = None
max_mean = None
tissue_mask = None

# Shows an image's mask overlaid on the original image
def show_ann(ann):
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((ann["segmentation"].shape[0], ann["segmentation"].shape[1], 4))
    img[:, :, 3] = 0

    m = ann["segmentation"]
    color_mask = np.concatenate([np.random.random(3), [0.35]])
    img[m] = color_mask

    ax.imshow(img)

# Shows a given point as a star on top of an image
def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels == 1]
    neg_points = coords[labels == 0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white',
               linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white',
               linewidth=1.25)


for i, image in enumerate(os.listdir(images_path)):
    # Opens and shows inputted image from the given path
    img = cv2.imread(images_path + image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(f"Image {i}, {image} loaded.")

    # Mask generation
    from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
    sam = sam_model_registry[model_type](checkpoint=model_path)
    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(img)

    # Makes image array and converts it to grayscale
    img_array = np.array(color.rgb2gray(img))

    # Iterates through all the image's masks and outputs the mask ID with the highest pixel brightness value
    mean_pixel_intensities = np.array([], dtype=float)
    for j in range(len(masks)):
        # Mask the image
        img_array_masked = img_array.copy()

        # Replace False values with NaN
        img_array_masked[~masks[j]["segmentation"]] = np.nan

        # Get mean from the True values
        mean_pixel_intensities = np.append(mean_pixel_intensities, np.nanmean(img_array_masked))

    # Variables for later use
    max_mean_mask = np.argmax(mean_pixel_intensities)
    max_mean = np.max(mean_pixel_intensities)

    # Get the brightest pixel in image
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img_array)

    # Label brightest pixel as an input point to show
    input_point = np.array([maxLoc])
    input_label = np.array([1])

    # Iterates through an image's masks and their True/False arrays and creates a coordinates array of the "True" values per mask
    # If the brightest pixel is in a mask, it appends a tuple of the mask ID and the mask into a list, which is then sorted and the first item is outputted
    bright_masks = []
    for j in range(len(masks)):
        arr = np.where(masks[j]["segmentation"] == True)
        coordinates = list(zip(arr[1], arr[0]))

        for pair in coordinates:
            if pair == maxLoc:
                bright_masks.append((j, masks[j]))

    if len(bright_masks) != 0:
        bright_mask = sorted(bright_masks, key=lambda x: x[1]["area"], reverse=True)[0][0]

    else:
        print(f"Image {i}, {image} mask was not created")
        print("\n")
        continue


    # Checker to make sure the mask with highest pixel brightness mean and brightest pixel are the same

    if bright_mask != max_mean_mask:
        print(f"Image {i}, {image} mask was not created")
        print("\n")

    elif bright_mask == max_mean_mask:
        tissue_mask = bright_mask

        shutil.copy(images_path + image, destination)

        plt.figure(figsize=(13.30, 6.65))
        plt.imshow(masks[tissue_mask]["segmentation"], cmap='hot')
        plt.axis('off')
        plt.savefig(destination + image[:35] + " Mask.png", format='png', bbox_inches='tight', pad_inches=0)

        print(f"Image {i}, {image} mask created")
        print("\n")
