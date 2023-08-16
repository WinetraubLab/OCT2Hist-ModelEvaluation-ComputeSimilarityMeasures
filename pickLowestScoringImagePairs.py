import numpy as np

'''
This function sorts lowest-scoring image pairs using argsort for each metric, adds them to an array, checking if it's not there already, and returns the array

Inputs:
  1. ssim - array of SSIM scores
  2. mse - array of MSE scores
  3. psnr - array of PSNR scores
  4. mae - array of MAE scores
  5. pcc - array of PCC scores

Outputs: 
  1. worst_scores - array of lowest-scoring image pair file paths
'''

def pickLowestScoringImagePairs(ssim, mse, psnr, mae, pcc):
    # Worst scores per metric lists
    worst_ssim = np.array(ssim).argsort()
    worst_mse = np.array(mse).argsort()[::-1]
    worst_psnr = np.array(psnr).argsort()
    worst_mae = np.array(mae).argsort()[::-1]
    worst_pcc = np.array(pcc).argsort()

    # Create an array of lowest-scoring pairs
    worst_scores = []

    # Adds a pair after checking if it's already there
    for i in range(25):
        if len(worst_scores) >= 25:
            break
        else:
            if worst_ssim[i] not in worst_scores:
                worst_scores.append(worst_ssim[i])

            if worst_mse[i] not in worst_scores:
                worst_scores.append(worst_mse[i])

            if worst_psnr[i] not in worst_scores:
                worst_scores.append(worst_psnr[i])

            if worst_mae[i] not in worst_scores:
                worst_scores.append(worst_mae[i])

            if worst_pcc[i] not in worst_scores:
                worst_scores.append(worst_pcc[i])

    return worst_scores
