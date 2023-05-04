import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

'''
This function prints the lowest-scoring image pairs in the format of the real and fake image side-by-side, and its metric scores under

Inputs:
  1. ssim - array of SSIM scores
  2. mse - array of MSE scores
  3. psnr - array of PSNR scores
  4. mae - array of MAE scores
  5. pcc - array of PCC scores
  6. topList - array of highest-scoring image pair indexes
  7. imagePair_list - a nested list of image pairs of a real image file path and a fake image file path
  8. amountToPrint - integer of desired amount of image pairs and their scores to print

Output: Prints real and fake image to skin, along with their metric scores
'''

class printLowestScoringImagePairs:
    def printLowestScoringImagePairs(ssim, mse, psnr, mae, pcc, bottom_list, imagePair_list, amountToPrint):
        # Outputs the lowest scoring image pairs
        rows = 2
        columns = 2

        print("Highest scorers: \n")
        for i in range(amountToPrint):
            # Display the lowest scorers
            fig = plt.figure(figsize=(13, 10))

            # Adds a subplot at the 1st position
            fig.add_subplot(rows, columns, 1)

            # Showing image
            plt.imshow(cv2.imread(images_folder + "/" + imagePair_list[bottom_list[i]][0]))
            plt.axis('off')
            plt.title("Real Image: " + "\n" + imagePair_list[bottom_list[i]][0])

            # Add subplot at 2nd position
            fig.add_subplot(rows, columns, 2)

            # Showing image
            plt.imshow(cv2.imread(images_folder + "/" + imagePair_list[bottom_list[i]][1]))
            plt.axis('off')
            plt.title("Fake Image: " + "\n" + imagePair_list[bottom_list[i]][1])
            plt.show()

            print("\n")
            print("Scores: ")
            print("SSIM: ", ssim[bottom_list[i]])
            print("MSE: ", mse[bottom_list[i]])
            print("PSNR: ", psnr[bottom_list[i]])
            print("MAE: ", mae[bottom_list[i]])
            print("PCC: ", pcc[bottom_list[i]])
            print("\n")
            print("\n")