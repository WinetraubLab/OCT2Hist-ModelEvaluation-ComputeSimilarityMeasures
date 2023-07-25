import torch
import torchvision
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import color

'''
This function uses Facebook's Segment Anything algorithm to get an image's masks and displays the mask with the image's
brightest pixel and the highest mean pixel brightness

Inputs: 
  1. model_type - a string of the desired Segment Anything model's name
  2. model_path - a string file path where the desired Segment Anything model file is located
  3. image - a string containing the file path of the desired image
  
Output:
  1. masks[bright_mask]["segmentation"] - 2D image of the desired mask's
'''

def find_tissue_in_oct(model_path, model_type, image):
    bright_mask = None
    max_mean_mask = None
    max_mean = None

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


    # Opens and shows inputted image from the given path
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    tissue_mask = None

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('on')
    plt.show()


    # Mask  generation
    from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
    sam = sam_model_registry[model_type](checkpoint=model_path)
    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(image)


    # Makes image array and converts it to grayscale
    img_array = np.array(color.rgb2gray(image))

    # Iterates through all the image's masks and outputs the mask ID with the highest pixel brightness value
    mean_pixel_intensities = np.array([], dtype=float)
    for i in range(len(masks)):
        # Mask the image
        img_array_masked = img_array.copy()

        # Replace False values with NaN
        img_array_masked[~masks[i]["segmentation"]] = np.nan

        # Get mean from the True values
        mean_pixel_intensities = np.append(mean_pixel_intensities, np.nanmean(img_array_masked))

    # Variables for later use
    max_mean_mask = np.argmax(mean_pixel_intensities)
    max_mean = np.max(mean_pixel_intensities)

    print(f"Mask with highest value: {max_mean_mask}, {max_mean}")


    # Get the brightest pixel in image
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img_array)

    # Label brightest pixel as an input point to show
    input_point = np.array([maxLoc])
    input_label = np.array([1])

    # Iterates through an image's masks and their True/False arrays and creates a coordinates array of the "True" values per mask
    # Checks if the brightest pixel is located in a certain mask, and outputs the mask if it is
    bright = None
    for i in range(len(masks)):
        arr = np.where(masks[i]["segmentation"] == True)
        coordinates = list(zip(arr[1], arr[0]))

        for pair in coordinates:
            if pair == maxLoc:
                bright_mask = i
                break

        else:
            continue
        break

    print(f"Mask with brightest pixel: {bright_mask}, {pair}")


    # Checker to make sure the mask with highest pixel brightness mean and brightest pixel are the same
    not_equal_counter = 0
    equal_counter = 0
    if bright_mask != max_mean_mask:
        # raise Exception(f"Mask with brightest pixel not the same as mask with highest average. "
        #                 f"Mask with brightest pixel: {bright_mask}, Mask with highest mean: {max_mean_mask}")
        print(f"Mask with brightest pixel not the same as mask with highest average. "
              f"Mask with brightest pixel: {bright_mask}, Mask with highest mean: {max_mean_mask}")

        not_equal_counter += 1

        print("Number of unmatching mask means and brightest pixels: ", not_equal_counter)

    elif bright_mask == max_mean_mask:
        tissue_mask = bright_mask

        # Opens and shows inputted image's desired mask with its brightest pixel
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        show_points(input_point, input_label, plt.gca())
        show_ann(masks[tissue_mask])
        plt.axis('on')
        plt.show()

        equal_counter += 1
        print("Number of matching mask means and brightest pixels: ", equal_counter)

        return masks[tissue_mask]["segmentation"]