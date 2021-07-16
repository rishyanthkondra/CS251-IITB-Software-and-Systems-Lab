import numpy as np
def reconstruct_from_noisy_patches(input_dict, shape):
    """
        input_dict:
        key: 4-tuple: (topleft_row, topleft_col, bottomright_row, bottomright_col): location of the patch in the original image. topleft_row, topleft_col are inclusive but bottomright_row, bottomright_col are exclusive. i.e. if M is the reconstructed matrix. M[topleft_row:bottomright_row, topleft_col:bottomright_col] will give the patch.
        
        value: 2d numpy array: the image patch.
        
        shape: shape of the original matrix.
        """
    # Initialization: Initialise M, black_count, mid_count, white_count, mid_total
    M = np.zeros(shape)
    black_count,mid_count,white_count,mid_total = M.copy(),M.copy(),M.copy(),M.copy()
    for topleft_row, topleft_col, bottomright_row, bottomright_col in input_dict: # no loop except this!
        tlr, tlc, brr, brc = topleft_row, topleft_col, bottomright_row, bottomright_col
        patch = input_dict[(tlr, tlc, brr, brc)].copy()
        temp = np.full(shape,-1)
        temp[tlr:brr,tlc:brc] = patch
        patch = temp.copy()
        black = (patch == 0)
        white = (patch == 255)
        mid = np.logical_and(patch>0,patch<255)
        black_count[black]=black_count[black]+1
        white_count[white]=white_count[white]+1
        mid_count[mid]=mid_count[mid]+1
        mid_total[mid]+=patch[mid]
    # change black_count, mid_count, white_count, mid_total here
    # Finally change M here
    nomid = (mid_count==0)
    blackD = np.greater(black_count,white_count)
    Whitd = np.logical_and(np.less_equal(black_count,white_count),(white_count!=0))
    M[np.logical_and(nomid,blackD)] = 0
    M[np.logical_and(nomid,Whitd)] = 255
    M[np.logical_not(nomid)] = mid_total[np.logical_not(nomid)] / mid_count[np.logical_not(nomid)]
    M  = M.astype(int)
    return M # You have to return the reconstructed matrix (M).




