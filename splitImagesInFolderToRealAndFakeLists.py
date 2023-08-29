import os

'''
This function lists the image_folder_path folder and creates a three lists of real, fake, and mask, sorting the images
into the corresponding list depending on its suffix label.

Inputs:
  1. images_folder_path - a variable containing a string of file path of desired images

Output:
  1. real_image_paths - a list containing real image paths
  2. fake_image_paths - a list containing fake image paths
  3. mask_image_paths - a list containing mask image paths
  
Example:
  real_image_paths[i] = LD-11-Slide06_Section01_yp0_patch0.png
  fake_image_paths[i] = LD-11-Slide06_Section01_yp0_patch0_fake.png
  mask_image_paths[i] = LD-11-Slide06_Section01_yp0_patch0_mask.png
'''


def splitImagesInFolderToRealAndFakeLists(images_folder_path):
    # Finds the nth occurrence of a character in a string

    # Function to find the nth occurrence of a specific character, used to divide an image's label
    def find_nth(string, character, n):
        start = string.find(character)
        while start >= 0 and n > 1:
            start = string.find(character, start + len(character))
            n -= 1
        return start
    
    # Make list of image paths from folder
    images_files = sorted(os.listdir(images_folder_path))

    # Create type lists and put images into their respective folders using their suffixes
    real_image_paths = []
    fake_image_paths = []
    mask_image_paths = []

    for i in images_files:
        if "mask" in i:  # If there is "mask"
            mask_image_paths.append(images_folder_path + "/" + i)

        elif "fake" in i:  # If there is "fake"
            fake_image_paths.append(images_folder_path + "/" + i)

        elif "real" in i:  # If there is no "mask" or "fake"
            real_image_paths.append(images_folder_path + "/" + i)

    # Check that prefixes are the same
    # for i in range(len(real_image_paths)):
        # path = real_image_paths[i][:i.rfind('/')]
        # name_label = real_image_paths[i][i.rfind('/'):find_nth(i, "_", 4)]
        # underscore = find_nth(real_image_paths[i], "_", 4)
        # if len(mask_image_paths) != 0:
        #     if real_image_paths[i][:underscore - 1] == fake_image_paths[i][:underscore - 1] == mask_image_paths[i][:underscore - 1]:
        #         continue
        #     else:
        #         raise Exception(f"Image names do not match - real image: {real_image_paths[-1]}, fake image: {fake_image_paths[-1], mask_image_paths[-1]}")
        #
        # elif len(mask_image_paths) == 0:
        #     if real_image_paths[i][:underscore - 1] == fake_image_paths[i][:underscore - 1]:
        #         continue
        #     else:
        #         raise Exception(f"Image names do not match - real image: {real_image_paths[-1]}, fake image: {fake_image_paths[-1]}")

    return real_image_paths, fake_image_paths, mask_image_paths
