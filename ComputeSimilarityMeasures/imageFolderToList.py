import os

'''
This function lists the image_path folder and creates a nested image pair list
for the real and fake images

Inputs:
  images_path - a variable containing a string of filepath of desired images

Output:
  pair_list - a nested list of image pair of a real image file path and a fake image file path

Example:
  imagePair_list[i][0] - real image path
  imagePair_list[i][1] - fake image path
'''

class imageFolderToList:
  def __call__(self):
    # Make list of images
    images_files = sorted(os.listdir(self))

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
      image_pair = []
      image_pair.append(i)
      image_pair.append(j)
      pair_list.append(image_pair)

    # Check that prefixes are the same
    for i in pair_list:

      if i[0][:42] == i[1][:42] and i[0][43:] != i[1][43:]:
        continue
      else:
        raise Exception('Image names do not match: ', i)

    return pair_list
