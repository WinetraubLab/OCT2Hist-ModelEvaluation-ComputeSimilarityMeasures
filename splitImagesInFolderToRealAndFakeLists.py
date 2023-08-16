import os

'''
This function lists the image_folder_path folder and creates a three lists of real, fake, and mask, sorting the images
into the corresponding list depending on its suffix label.

Inputs:
  1. images_folder_path - a variable containing a string of file path of desired images

Output:
  1. real_image_paths - a list containing real images
  2. fake_image_paths - a list containing fake images
  3. mask_image_paths - a list containing mask images
  
Example:
  real_image_paths[i] = LD-11-Slide06_Section01_yp0_patch0.png
  fake_image_paths[i] = LD-11-Slide06_Section01_yp0_patch0_fake.png
  mask_image_paths[i] = LD-11-Slide06_Section01_yp0_patch0_mask.png
'''


def splitImagesInFolderToRealAndFakeLists(images_folder_path):
    # Finds the nth occurrence of a character in a string
    def find_nth(string, character, n):
        start = string.find(character)
        while start >= 0 and n > 1:
            start = string.find(character, start + len(character))
            n -= 1
        return start
    
    # Make list of image paths from folder
    images_files = sorted(os.listdir(images_folder_path))

    # Sort images into their respective folders using their suffixes
    real_image_paths = []
    fake_image_paths = []
    mask_image_paths = []

    for i in images_files:
        underscore = find_nth(i, "_", 4)
        name_label = i[:underscore - 1]
        type_label = i[underscore:]

        if "mask" in type_label:  # If there's mask
            mask_image_paths.append(i)

        elif "fake" in type_label:  # If there's more real than fake
            fake_image_paths.append(i)

        else:  # if there's more fake or same amount as real
            real_image_paths.append(i)

    # Check that prefixes are the same
    for i in range(len(real_image_paths)):
        underscore = find_nth(real_image_paths[i], "_", 4)
        if len(mask_image_paths) != 0:
            if real_image_paths[i][:underscore - 1] == fake_image_paths[i][:underscore - 1] == mask_image_paths[i][:underscore - 1]:
                continue
            else:
                raise Exception(f"Image names do not match - real image: {real_image_paths[-1]}, fake image: {fake_image_paths[-1], mask_image_paths[-1]}")

        elif len(mask_image_paths) == 0:
            if real_image_paths[i][:underscore - 1] == fake_image_paths[i][:underscore - 1]:
                continue
            else:
                raise Exception(f"Image names do not match - real image: {real_image_paths[-1]}, fake image: {fake_image_paths[-1]}")

    return real_image_paths, fake_image_paths, mask_image_paths
