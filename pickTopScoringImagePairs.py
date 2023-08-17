'''
This function sorts best-scoring images for each metric, adds them to a list, checking if it's not there already, and returns the list

Inputs:
  1. ssim - array of SSIM scores
  2. mse - array of MSE scores
  3. psnr - array of PSNR scores
  4. mae - array of MAE scores
  5. pcc - array of PCC scores
  6. real_image_paths - a list containing real images
  7. fake_image_paths - a list containing fake images
  8. amount_to_print - integer of desired amount of image pairs and their scores to print

Outputs: 
  1. top_scores - nested list of top-scoring images' score and index
'''


def pickTopScoringImagePairs(ssim, mse, psnr, mae, pcc, amount_to_print):
    # Best scores per metric lists
    best_ssim = []
    best_mse = []
    best_psnr = []
    best_mae = []
    best_pcc = []

    for i in range(len(ssim)):
        best_ssim.append([ssim[i], i])
        best_mse.append([mse[i], i])
        best_psnr.append([psnr[i], i])
        best_mae.append([mae[i], i])
        best_pcc.append([pcc[i], i])

    best_ssim = sorted(best_ssim, reverse=True)
    best_mse = sorted(best_mse)
    best_psnr = sorted(best_psnr, reverse=True)
    best_mae = sorted(best_mae)
    best_pcc = sorted(best_pcc, reverse=True)

    # Creates a list of images' highest scores and their indexes
    top_scores = []

    # Adds an image's score and its index after checking if it's already there
    for i in range(amount_to_print):
        if len(top_scores) >= amount_to_print * 5:
            break
        else:
            if best_ssim[i][1] not in top_scores:
                top_scores.append(best_ssim[i][1])

            if best_mse[i][1] not in top_scores:
                top_scores.append(best_mse[i][1])

            if best_psnr[i][1] not in top_scores:
                top_scores.append(best_psnr[i][1])

            if best_mae[i][1] not in top_scores:
                top_scores.append(best_mae[i][1])

            if best_pcc[i][1] not in top_scores:
                top_scores.append(best_pcc[i][1])

    return top_scores
