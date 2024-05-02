import cv2
import numpy as np
from scipy.spatial.distance import cdist

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)

def overlay_images(background_img, overlay_img, blend_percentage):
    blended_img = cv2.addWeighted(background_img, 1 - blend_percentage, overlay_img, blend_percentage, 0)
    return blended_img

while cap.isOpened():
    vergence_metric_left_2_right = []
    vergence_metric_right_2_left = []

    succes, rimg = cap.read()
    succes1, limg = cap2.read()
    cv2.imshow('right Img',rimg)
    cv2.imshow('left Img',limg)

    img_size = rimg.shape
    img_gray_right = cv2.cvtColor(rimg, cv2.COLOR_BGR2GRAY)
    img_blur_right = cv2.GaussianBlur(img_gray_right, (3,3), 0) 
    img_gray_left = cv2.cvtColor(limg, cv2.COLOR_BGR2GRAY)
    img_blur_left = cv2.GaussianBlur(img_gray_left, (3,3), 0)
    blend_percentage = 0.5
    blended_img = overlay_images(rimg, limg, blend_percentage)
    cv2.imshow("Blended Image", blended_img)
    edges_right = cv2.Canny(image=img_blur_right, threshold1=50, threshold2=200)
    edges_left = cv2.Canny(image=img_blur_left, threshold1=50, threshold2=200)
    cv2.imshow('canny right', edges_right)
    cv2.imshow('canny left', edges_left)
    sobel_final = edges_right+edges_left
    cv2.imshow('Sobel add', sobel_final)
    key = cv2.waitKey(5)

    if key == 27:
        cap.release()
        cap2.release()
        cv2.destroyAllWindows()
        break
    elif key == ord('s'):
        center_img_sizes_array = [25,50,75,100,125,150]
        print("Original image shape = ",img_size)
        for k in center_img_sizes_array:
            slice_right = edges_right[img_size[0]//2-k:img_size[0]//2+k,img_size[1]//2-k:img_size[1]//2+k]
            slice_left = edges_left[img_size[0]//2-k:img_size[0]//2+k,img_size[1]//2-k:img_size[1]//2+k]
            #cv2.imshow('slice_right',slice_right)
            #cv2.imshow('slice_left',slice_left)
            print("Right sliced image shape = ",slice_right.shape)
            print("Left sliced image shape = ",slice_left.shape)
            indices_r = np.where(slice_right != [0])
            coordinates_r = list(zip(indices_r[0], indices_r[1]))
            indices_l = np.where(slice_left != [0])
            coordinates_l = list(zip(indices_l[0], indices_l[1]))
            len_l = len(coordinates_l)
            len_r = len(coordinates_r)
            coordinates_l = np.array(coordinates_l)
            coordinates_r = np.array(coordinates_r)
            d_left2right = cdist(coordinates_l,coordinates_r)
            min_d_left2right = np.min(d_left2right,axis=1)
            vleft = np.sum(min_d_left2right)/len_l
            vergence_metric_left_2_right.append(vleft)
            d_right2left = cdist(coordinates_r,coordinates_l)
            min_d_right2left = np.min(d_right2left,axis=1)
            vright = np.sum(min_d_right2left)/len_r
            vergence_metric_right_2_left.append(vright) 
            print("Vergence metric left to right = ",vleft)
            print("Vergence metric right to left = ",vright)

        cv2.imwrite('data/final/final_left_img.png', limg)
        cv2.imwrite('data/final/final_right_img.png', rimg)
        cv2.imwrite('data/final/final_edge_left.png', edges_left)
        cv2.imwrite('data/final/final_edge_right.png', edges_right)
        cv2.imwrite('data/final/blended_image.png',blended_img)
        cv2.imwrite('data/final/final_edge_add.png', sobel_final)
        print("Vergence left to right for image sizes ",center_img_sizes_array,"is = ",vergence_metric_left_2_right)
        print("Vergence right to left for image sizes ",center_img_sizes_array,"is = ",vergence_metric_right_2_left)
       
