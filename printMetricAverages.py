'''
This function calculates average metric score per metric and prints them to screen

Inputs:
  1. ssim - array of SSIM scores
  2. mse - array of MSE scores
  3. psnr - array of PSNR scores
  4. mae - array of MAE scores
  5. pcc - array of PCC scores

Output: Prints score averages onto screen, rounded to three significant figures
'''


def printMetricAverages(ssim, mse, psnr, mae, pcc):
    # Averages the scores for a given list
    def average(score_list):
        return sum(score_list) / len(score_list)

    # Print metric averages
    print("Average scores:")
    print("Average SSIM: ", round(average(ssim), 3))
    print("Average MSE: ", round(average(mse), 3))
    print("Average PSNR: ", round(average(psnr), 3))
    print("Average MAE: ", round(average(mae), 3))
    print("Average PCC: ", round(average(pcc), 3))
    print("\n")
