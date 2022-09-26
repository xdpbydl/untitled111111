import cv2 as cv


def get_distance(bg_img_path, slider_img_path):
    """获取滑块移动距离"""
    # 测试可行

    # 背景图片处理
    bg_img = cv.imread(bg_img_path, 0)  # 读入灰度图片
    bg_img = cv.GaussianBlur(bg_img, (3, 3), 0)  # 高斯模糊去噪
    bg_img = cv.Canny(bg_img, 50, 150)  # Canny算法进行边缘检测
    # 滑块做同样处理
    slider_img = cv.imread(slider_img_path, 0)
    slider_img = cv.GaussianBlur(slider_img, (3, 3), 0)
    slider_img = cv.Canny(slider_img, 50, 150)
    # 寻找最佳匹配
    res = cv.matchTemplate(bg_img, slider_img, cv.TM_CCOEFF_NORMED)
    # 最小值，最大值，并得到最小值, 最大值的索引
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # 例如：(-0.05772797390818596, 0.30968162417411804, (0, 0), (196, 1))
    top_left = max_loc[0]  # 横坐标
    # 展示圈出来的区域
    # w, h = image.shape[::-1]  # 宽高,例如(320, 160)
    # cv.rectangle(template, (x, y), (x + w, y + h), (7, 249, 151), 2)
    # cv.imshow('Show', bg_img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    print(top_left)
    return top_left


get_distance('max.png', 'xiaotu.png')