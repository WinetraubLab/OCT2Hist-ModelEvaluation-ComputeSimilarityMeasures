import cv2
# from google.colab.patches import cv2_imshow
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
  7. real_image_paths - a list containing real image paths
  8. fake_image_paths - a list containing fake image paths
  9. amount_to_print - integer of desired amount of image pairs and their scores to print

Output: Prints real and fake image to screen, along with their metric scores
'''

def printTopScoringImagePairs(ssim, mse, psnr, mae, pcc, top_list, real_images_paths, fake_images_paths, amount_to_print):
    # Outputs the highest scoring images
    rows = 2
    columns = 2

    print("Highest scorers: \n")
    for i in range(amount_to_print):
        # Display the top scorers
        fig = plt.figure(figsize=(13, 10))

        # Adds a subplot at the 1st position
        fig.add_subplot(rows, columns, 1)

        # Showing real image
        plt.imshow(cv2.imread(real_images_paths[top_list[i]]))
        plt.axis('off')
        plt.title("Real Image: " + "\n" + real_images_paths[top_list[i]])  # Make so it prints everything between the last / and ".png"

        # Add subplot at 2nd position
        fig.add_subplot(rows, columns, 2)

        # Showing fake image
        plt.imshow(cv2.imread(fake_images_paths[top_list[i]]))
        plt.axis('off')
        plt.title("Fake Image: " + "\n" + fake_images_paths[top_list[i]])  # Make so it prints everything between the last / and ".png"
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
