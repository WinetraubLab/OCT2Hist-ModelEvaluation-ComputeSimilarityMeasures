import numpy as np

'''
This function sorts best-scoring image pairs using argsort for each metric, adds them to an array, checking if it's not there already, and returns the array

Inputs:
  1. ssim - array of SSIM scores
  2. mse - array of MSE scores
  3. psnr - array of PSNR scores
  4. mae - array of MAE scores
  5. pcc - array of PCC scores

Outputs: 
  1. top_scores - array of top-scoring image pair file paths
'''

def pickTopScoringImagePairs(ssim, mse, psnr, mae, pcc):
    # Best scores per metric lists
    best_ssim = np.array(ssim).argsort()[::-1]
    best_mse = np.array(mse).argsort()
    best_psnr = np.array(psnr).argsort()[::-1]
    best_mae = np.array(mae).argsort()
    best_pcc = np.array(pcc).argsort()[::-1]

    # Creates an array of highest-scoring pairs
    top_scores = []

    # Adds a pair after checking if it's already there
    for i in range(25):
        if len(top_scores) >= 25:
            break
        else:
            if best_ssim[i] not in top_scores:
                top_scores.append(best_ssim[i])

            if best_mse[i] not in top_scores:
                top_scores.append(best_mse[i])

            if best_psnr[i] not in top_scores:
                top_scores.append(best_psnr[i])

            if best_mae[i] not in top_scores:
                top_scores.append(best_mae[i])

            if best_pcc[i] not in top_scores:
                top_scores.append(best_pcc[i])

    return top_scores
