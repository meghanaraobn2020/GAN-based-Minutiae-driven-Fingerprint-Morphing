import cv2
import numpy as np
import sys
import fi_orientation
import similarity
import translation
import rotation
import pandas as pd


def get_best_loop_fi_alignment_config(img2, block_size, angles_img1, rel_img1, sim_score_loop_df):
    img2_h_center, img2_w_center = img2.shape[1]/2, img2.shape[0]/2
    for value in np.arange(-5, 6, 1):
        img2_t = translation.translate_image(img2, value, value)
        for angle in np.arange(-5, 6, 1):
            img2_t_r = rotation.rotate_image(
                img2_t, angle, (img2_w_center, img2_h_center))
            _, angles_img2_t_r, rel_img2_t_r = fi_orientation.calculate_angles(
                img2_t_r, block_size, smoth=True)
            similarity_score = similarity.calculate_similarity(
                angles_img1, angles_img2_t_r, rel_img1, rel_img2_t_r)
            sim_score_loop_df = sim_score_loop_df.append(
                {'rotation_angle': angle, 'tx': value, 'ty': value, 'similarity_score': similarity_score}, ignore_index=True)

    return sim_score_loop_df

def get_loop_fi_sim_score_df(block_size, img1, img2, angles_img1, rel_img1, tx_loop, ty_loop):
    sim_score_loop_df =  pd.DataFrame()
    img2_t = translation.translate_image(img2, tx_loop, ty_loop) 
    sim_score_loop_df = get_best_loop_fi_alignment_config(img2_t, block_size, angles_img1, rel_img1, sim_score_loop_df)
    return img2_t, sim_score_loop_df
    




