import numpy as np
from skimage import color, io
from skimage.metrics import structural_similarity
from skimage.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr
import csv

'''
This function takes list of image pairs, calculates their metric scores and puts them into a csv file and returns vectors of each metric score

Inputs:
  1. real_image_paths - a list containing real images
  2. fake_image_paths - a list containing fake images
  3. mask_image_paths - a list containing mask images
  4. images_folder_path - a variable containing a string of file path of desired images
  5. outputFilePath - the desired path for the csv file to be saved in
  6. outputFileName - the desired name for the csv file containing image pair names and their metric scores, where no name defaults to file name 'output.csv'

Outputs:
  1. scores_ssim - array of SSIM scores
  2. scores_mse - array of MSE scores
  3. scores_psnr - array of PSNR scores
  4. scores_mae - array of MAE scores
  5. scores_pcc - array of PCC scores


  Expected CSV file output example:

  |  Real Image   |   Fake Image  | SSIM | MSE | PSNR | MAE | PCC |
  —————————————————————————————————————————————————————————————————
  | LG-...-real_B | LG-...-fake_B |  A   |  B  |   C  |  D  |  E  |
  —————————————————————————————————————————————————————————————————
  | LH-...-real_B | LH-...-fake_B |  V   |  W  |   X  |  Y  |  Z  |

'''

def calculateMetricArrays(real_image_paths, fake_image_paths, mask_image_paths, images_folder_path, outputFilePath='/content/drive/output.csv'):
    # Metric score lists
    scores_ssim = []
    scores_mse = []
    scores_psnr = []
    scores_mae = []
    scores_pcc = []

    # Loop that iterates through files list, converts each image to grayscale, calculates metric score,
    # puts score into array, and prints all the pairs' file names and metric scores into a csv file
    for i in range(len(real_image_paths)):
        # Convert current A and B images to grayscale
        a_image = np.array(color.rgb2gray(io.imread(images_folder_path + "/" + real_image_paths[i])))
        b_image = np.array(color.rgb2gray(io.imread(images_folder_path + "/" + fake_image_paths[i])))
        mask_image = np.array(color.rgb2gray(io.imread(images_folder_path + "/" + mask_image_paths[i])))

        # Calculate SSIM, round it, and add to array
        scores_ssim.append(round(structural_similarity(a_image, b_image, win_size=255), 3))

        # Calculate MSE, round it, and add to array
        scores_mse.append(round(mean_squared_error(a_image, b_image), 3))

        # Calculate PSNR, round it, and add to array
        scores_psnr.append(round(peak_signal_noise_ratio(a_image, b_image), 3))

        # Calculate MAE, round it, and add to array
        scores_mae.append(round(mean_absolute_error(a_image, b_image), 3))

        # Calculate PCC, round it, and add to array
        scores_pcc.append(round(pearsonr(a_image.flatten(), b_image.flatten())[0], 3))

    # Create csv file, add category row, and value rows
    with open(outputFilePath, mode='w', newline='') as csvfile:
        metrics_csvwriter = csv.writer(csvfile)
        metrics_csvwriter.writerow(["Real Image", "Fake Image", "SSIM", "MSE", "PSNR", "MAE", "PCC"])

        for i in range(len(real_image_paths)):
            metrics_csvwriter.writerow(
                [real_image_paths[i], fake_image_paths[i], scores_ssim[i], scores_mse[i], scores_psnr[i],
                 scores_mae[i], scores_pcc[i]])

    return scores_ssim, scores_mse, scores_psnr, scores_mae, scores_pcc
