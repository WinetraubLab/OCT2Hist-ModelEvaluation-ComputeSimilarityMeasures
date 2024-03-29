from splitImagesInFolderToRealAndFakeLists import splitImagesInFolderToRealAndFakeLists
from calculateMetricArrays import calculateMetricArrays
from printMetricAverages import printMetricAverages
from pickTopScoringImagePairs import pickTopScoringImagePairs
from printTopScoringImagePairs import printTopScoringImagePairs
from pickLowestScoringImagePairs import pickLowestScoringImagePairs
from printLowestScoringImagePairs import printLowestScoringImagePairs

# Input file path of images
images_folder = 'C:/Users/pato_/Documents/Code Projects/OCT2Hist-ModelEvaluation-ComputeSimilarityMeasures/images/Paulo CycleGAN'

# Select how many paired images and their scores to present (best and worst scores)
number = 1

# Output CSV file path where the scores of each image will be saved to and name of CSV file
output_csv_file_path = 'C:/Users/pato_/Documents/Code Projects/OCT2Hist-ModelEvaluation-ComputeSimilarityMeasures/images/Paulo CycleGAN/output 2023-9-11.csv'

real_list, fake_list, mask_list = splitImagesInFolderToRealAndFakeLists(images_folder)

ssim, mse, psnr, mae, pcc = calculateMetricArrays(real_list, fake_list, mask_list, output_csv_file_path)

printMetricAverages(ssim, mse, psnr, mae, pcc)

top = pickTopScoringImagePairs(ssim, mse, psnr, mae, pcc, number)
printTopScoringImagePairs(ssim, mse, psnr, mae, pcc, top, real_list, fake_list, number)

low = pickLowestScoringImagePairs(ssim, mse, psnr, mae, pcc, number)
printLowestScoringImagePairs(ssim, mse, psnr, mae, pcc, low, real_list, fake_list, number)