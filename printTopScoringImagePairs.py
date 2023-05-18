import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

'''
This function prints the highest-scoring image pairs in the format of the real and fake image side-by-side, and its metric scores under

Inputs:
  1. ssim - array of SSIM scores
  2. mse - array of MSE scores
  3. psnr - array of PSNR scores
  4. mae - array of MAE scores
  5. pcc - array of PCC scores
  6. top_list - array of highest-scoring image pair indexes
  7. pair_list - a nested list of image pairs of a real image file path and a fake image file path
  8. amount_to_print - integer of desired amount of image pairs and their scores to print

Output: Prints real and fake image to skin, along with their metric scores
'''

def printTopScoringImagePairs(ssim, mse, psnr, mae, pcc, top_list, images_path, pair_list, amount_to_print):
    # Outputs the highest scoring image pairs
    rows = 2
    columns = 2

    print("Highest scorers: \n")
    for i in range(amount_to_print):
        # Display the top scorers
        fig = plt.figure(figsize=(13, 10))

        # Adds a subplot at the 1st position
        fig.add_subplot(rows, columns, 1)

        # Showing image
        plt.imshow(cv2.imread(images_path + "/" + pair_list[top_list[i]][0]))
        plt.axis('off')
        plt.title("Real Image: " + "\n" + pair_list[top_list[i]][0])

        # Add subplot at 2nd position
        fig.add_subplot(rows, columns, 2)

        # Showing image
        plt.imshow(cv2.imread(images_path + "/" + pair_list[top_list[i]][1]))
        plt.axis('off')
        plt.title("Fake Image: " + "\n" + pair_list[top_list[i]][1])
        plt.show()

        print("\n")
        print("Scores: ")
        print("SSIM: ", ssim[top_list[i]])
        print("MSE: ", mse[top_list[i]])
        print("PSNR: ", psnr[top_list[i]])
        print("MAE: ", mae[top_list[i]])
        print("PCC: ", pcc[top_list[i]])
        print("\n")
        print("\n")
