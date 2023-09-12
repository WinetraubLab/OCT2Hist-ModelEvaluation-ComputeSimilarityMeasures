import numpy as np
import cv2
from skimage import color, io
from skimage.metrics import structural_similarity
from skimage.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr
import csv

import sys
np.set_printoptions(threshold=sys.maxsize)

'''
This function takes lists of images, calculates their metric scores and puts them and their results into a csv file and returns vectors of each metric score

Inputs:
  1. real_image_paths - a list containing real image paths
  2. fake_image_paths - a list containing fake image paths
  3. mask_image_paths - a list containing mask images paths
  4. outputFilePath - the desired path for the csv file to be saved in
  5. outputFileName - the desired name for the csv file containing image pair names and their metric scores, where no name defaults to file name 'output.csv'

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


def calculateMetricArrays(real_image_paths, fake_image_paths, mask_image_paths, outputFilePath='/content/drive/output.csv'):
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
        a_image = np.array(cv2.cvtColor(io.imread(real_image_paths[i]), cv2.COLOR_RGB2GRAY))
        b_image = np.array(cv2.cvtColor(io.imread(fake_image_paths[i]), cv2.COLOR_RGB2GRAY))

        if len(mask_image_paths) != 0:
            # Converts mask into binary values
            mask_image = np.array(cv2.imread(mask_image_paths[i], cv2.IMREAD_GRAYSCALE))
            mask_image = cv2.threshold(mask_image, 128, 256, cv2.THRESH_BINARY)[1]

            # Isolates the section of the images as delineated by the mask
            a_image = a_image[np.any(mask_image != 0, axis=1)]
            b_image = b_image[np.any(mask_image != 0, axis=1)]

        window_size = np.shape(a_image)[0]
        if window_size % 2 == 0:
            window_size -= 1

        # Calculate SSIM, round it, and add to array
        scores_ssim.append(round(structural_similarity(a_image, b_image, win_size=window_size), 3))

        # Calculate MSE, round it, and add to array
        scores_mse.append(round(mean_squared_error(a_image, b_image), 3))

        # Calculate PSNR, round it, and add to array
        scores_psnr.append(round(peak_signal_noise_ratio(a_image, b_image), 3))

        # Calculate MAE, round it, and add to array
        scores_mae.append(round(mean_absolute_error(a_image, b_image), 3))

        # Calculate PCC, round it, and add to array
        scores_pcc.append(round(pearsonr(a_image.flatten(), b_image.flatten())[0], 3))

    def average(score_list):
        return sum(score_list) / len(score_list)

    # Create csv file, add category row, and value rows
    with open(outputFilePath, mode='w', newline='') as csvfile:
        metrics_csvwriter = csv.writer(csvfile)
        metrics_csvwriter.writerow(["Real Image", "Fake Image", "SSIM", "MSE", "PSNR", "MAE", "PCC"])

        for i in range(len(real_image_paths)):
            metrics_csvwriter.writerow(
                [real_image_paths[i], fake_image_paths[i], scores_ssim[i], scores_mse[i], scores_psnr[i],
                 scores_mae[i], scores_pcc[i]])

        metrics_csvwriter.writerow(
            ["Averages", "", f"{round(average(scores_ssim), 3)}", f"{round(average(scores_mse), 3)}",
                             f"{round(average(scores_psnr), 3)}", f"{round(average(scores_mae), 3)}",
                             f"{round(average(scores_pcc), 3)}"])

    return scores_ssim, scores_mse, scores_psnr, scores_mae, scores_pcc
