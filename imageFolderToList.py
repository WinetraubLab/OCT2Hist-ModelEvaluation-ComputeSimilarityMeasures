import os

'''
This function lists the image_path folder and creates a nested image file path pair list
for the real and fake images

Inputs:
  images_path - a variable containing a string of file path of desired images

Output:
  pair_list - a nested list of image file path pairs, one a real image and the other a fake image

Example:
  pair_list[i][0] - real image path
  pair_list[i][1] - fake image path
'''


def imageFolderToList(images_path):
    # Make list of images
    images_files = sorted(os.listdir(images_path))

    # Throws exception if length of images array is not even
    if len(images_files) % 2 != 0:
        raise Exception("Uneven amount of images.", len(images_files))

    # Sort images into their respective folders using their suffixes
    real_files = []
    fake_files = []

    for i in images_files:
        if i.endswith("real_B.png"):
            real_files.append(i)
        elif i.endswith("fake_B.png"):
            fake_files.append(i)

    # Places pairs into main image pair list
    pair_list = []

    for i, j in zip(real_files, fake_files):
        # Append image pair to pair list
        image_pair = [i, j]
        pair_list.append(image_pair)

    # Check that prefixes are the same
    for i in pair_list:

        if i[0][:42] == i[1][:42] and i[0][43:] != i[1][43:]:
            continue
        else:
            raise Exception('Image names do not match: ', i)

    return pair_list