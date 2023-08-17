'''
This function sorts worst-scoring images for each metric, adds them to a list, checking if it's not there already, and returns the list

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
  1. worst_scores - nested list of worst-scoring images' score and index
'''

def pickLowestScoringImagePairs(ssim, mse, psnr, mae, pcc, amound_to_print):
    # Worst scores per metric lists
    worst_ssim = []
    worst_mse = []
    worst_psnr = []
    worst_mae = []
    worst_pcc = []
    
    for i in range(len(ssim)):
        worst_ssim.append([ssim[i], i])
        worst_mse.append([mse[i], i])
        worst_psnr.append([psnr[i], i])
        worst_mae.append([mae[i], i])
        worst_pcc.append([pcc[i], i])

    worst_ssim = sorted(worst_ssim)
    worst_mse = sorted(worst_mse, reverse=True)
    worst_psnr = sorted(worst_psnr)
    worst_mae = sorted(worst_mae, reverse=True)
    worst_pcc = sorted(worst_pcc)

    # Create a list of images' lowest scores and their indexes
    worst_scores = []

    # Adds an image's score and its index after checking if it's already there
    for i in range(amound_to_print):
        if len(worst_scores) >= amound_to_print * 5:
            break
        else:
            if worst_ssim[i][1] not in worst_scores:
                worst_scores.append(worst_ssim[i][1])

            if worst_mse[i][1] not in worst_scores:
                worst_scores.append(worst_mse[i][1])

            if worst_psnr[i][1] not in worst_scores:
                worst_scores.append(worst_psnr[i][1])

            if worst_mae[i][1] not in worst_scores:
                worst_scores.append(worst_mae[i][1])

            if worst_pcc[i][1] not in worst_scores:
                worst_scores.append(worst_pcc[i][1])

    return worst_scores
