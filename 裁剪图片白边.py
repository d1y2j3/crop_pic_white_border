import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

input_folder = 'z:/'
output_folder = 'z:/crop/'


def MyCrop(in_image_name,out_image_name):
    # 读入图片
    image = cv2.imread(in_image_name)

    # 转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.bitwise_not(gray_image)       # 去白色边，找黑色区域
    # 进行二值化处理
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    #plt.imshow(binary_image, cmap='gray')
    #plt.show()

    # 计算水平方向和垂直方向的投影
    horizontal_projection = np.sum(binary_image, axis=1)
    #print(horizontal_projection)
    vertical_projection = np.sum(binary_image, axis=0)
    #print(vertical_projection)

    # 寻找包含黑色文字的区域
    top = np.where(horizontal_projection > 1)[0][0]
    bottom = np.where(horizontal_projection > 1)[0][-1]
    left = np.where(vertical_projection > 1)[0][0]
    right = np.where(vertical_projection > 1)[0][-1]

    # 裁剪图片
    cropped_image = image[top:bottom, left:right]
    print(out_image_name)
    # 保存裁剪后的图片
    cv2.imwrite(out_image_name, cropped_image)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):

        image_path = os.path.join(input_folder, filename)

        output_path = os.path.join(output_folder, filename)
        MyCrop(image_path,output_path)


