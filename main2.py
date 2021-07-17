import cv2
import math
import numpy as np
from PIL import Image

class CvOverlayImage(object):
    def __init__(self):
        pass

    @classmethod
    def overlay(
            cls,
            cv_background_image,
            cv_overlay_image,
            point,
    ):
        """
        Parameters
        ----------
        cv_background_image : [OpenCV Image]
        cv_overlay_image : [OpenCV Image]
        point : [(x, y)]
        Returns : [OpenCV Image]
        """
        overlay_height, overlay_width = cv_overlay_image.shape[:2]

        # OpenCV to PIL
        # backbround image
        cv_rgb_bg_image = cv2.cvtColor(cv_background_image, cv2.COLOR_BGR2RGB)
        pil_rgb_bg_image = Image.fromarray(cv_rgb_bg_image)
        pil_rgba_bg_image = pil_rgb_bg_image.convert('RGBA')
        # overlay image
        cv_rgb_ol_image = cv2.cvtColor(cv_overlay_image, cv2.COLOR_BGRA2RGBA)
        pil_rgb_ol_image = Image.fromarray(cv_rgb_ol_image)
        pil_rgba_ol_image = pil_rgb_ol_image.convert('RGBA')

        # composite() needs to the same size images
        # prepare image
        pil_rgba_bg_temp = Image.new('RGBA', pil_rgba_bg_image.size,
                                     (255, 255, 255, 0))
        # pile images to determine composite
        pil_rgba_bg_temp.paste(pil_rgba_ol_image, point, pil_rgba_ol_image)
        result_image = \
            Image.alpha_composite(pil_rgba_bg_image, pil_rgba_bg_temp)

        # Oconvert OpenCV
        cv_bgr_result_image = cv2.cvtColor(
            np.asarray(result_image), cv2.COLOR_RGBA2BGRA)

        return cv_bgr_result_image

def rotate(img, angle):
    h = img.shape[0]
    w = img.shape[1]
    center = (int(w / 2), int(h / 2))
    scale = 1.0
    trans = cv2.getRotationMatrix2D(center, angle , scale)
    r_img = cv2.warpAffine(img, trans, (w, h))
    return r_img

def go_right(save, prt, px, py, enemy, ex, ey, bg):
    image = CvOverlayImage.overlay(bg, prt, (px, py))
    save_image(save, image, px, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 30), (px+10, py))
    save_image(save, image, px+10, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 0), (px+20, py))
    save_image(save, image, px+20, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, -30), (px+30, py))
    save_image(save, image, px+30, py, ex, ey)

def go_left(save, prt, px, py, enemy, ex, ey, bg):
    image = CvOverlayImage.overlay(bg, rotate(prt, 180), (px, py))
    save_image(save, image, px, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 150), (px-10, py))
    save_image(save, image, px-10, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 180), (px-20, py))
    save_image(save, image, px-20, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 210), (px-30, py))
    save_image(save, image, px-30, py, ex, ey)

def go_upper(save, prt, px, py, enemy, ex, ey, bg):
    image = CvOverlayImage.overlay(bg, rotate(prt, 90), (px, py))
    save_image(save, image, px, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 120), (px, py-10))
    save_image(save, image, px, py-10, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 90), (px, py-20))
    save_image(save, image, px, py-20, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 60), (px, py-30))
    save_image(save, image, px, py-30, ex, ey)

def go_below(save, prt, px, py, enemy, ex, ey, bg):
    image = CvOverlayImage.overlay(bg, rotate(prt, 270), (px, py))
    save_image(save, image, px, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 240), (px, py+10))
    save_image(save, image, px, py+10, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 300), (px, py+20))
    save_image(save, image, px, py+20, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, 270), (px, py+30))
    save_image(save, image, px, py+30, ex, ey)

def go_back(save, prt, px, py, enemy, ex, ey, direction, bg):
    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px, py))
    save_image(save, image, px, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction-30), (px-5, py))
    save_image(save, image, px, py+10, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px-10, py))
    save_image(save, image, px, py+20, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction+30), (px-15, py))
    save_image(save, image, px, py+30, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px-20, py))
    save_image(save, image, px, py, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction-30), (px-25, py))
    save_image(save, image, px, py+10, ex, ey)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px-30, py))
    save_image(save, image, px, py+20, ex, ey)

def look_around(prt, px, py, direction, enemy, ex, ey, dir_e, friend, fx, fy, bg):
    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction + 45), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction + 90), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction - 45), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction - 90), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

    image = CvOverlayImage.overlay(bg, rotate(prt, direction), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)

def stop(px, py, direction, time, ex, ey, bg):
    for i in range(time):
        image = CvOverlayImage.overlay(bg, rotate(prt1, direction), (px, py))
        save_image(save, image, px, py, ex, ey)

def surprise(px, py, direction, ex, ey, bg):
    image = CvOverlayImage.overlay(bg, rotate(prt1, direction), (px, py))
    save_image(save, image, px, py, ex, ey)
    image = CvOverlayImage.overlay(bg, rotate(prt2, direction), (px-10, py-10))
    save_image(save, image, px-10, py-10, ex, ey)

def gaze(edx, edy, ingx, ingy):
    diff_x = edx - ingx + 1
    diff_y = edy - ingy
    if diff_y < 0 and diff_x >= 0:
        direction = - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y < 0 and diff_x < 0:
        direction = 180 - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y > 0 and diff_x < 0:
        direction = 180 - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y > 0 and diff_x >= 0:
        direction = - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y == 0 and edx > ingx:
        direction = 0
    elif diff_y == 0 and edx < ingx:
        direction = 180
    elif diff_x == 0 and edy > ingy:
        direction = 90
    elif diff_x == 0 and edy < ingy:
        direction = -90
    return direction

def save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy):
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    diff_x = px - fx + 1
    diff_y = py - fy
    if diff_y < 0 and diff_x >= 0:
        direction = - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y < 0 and diff_x < 0:
        direction = 180 - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y > 0 and diff_x < 0:
        direction = 180 - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y > 0 and diff_x >= 0:
        direction = - math.degrees(math.atan(diff_y / diff_x))
    elif diff_y == 0 and px > fx:
        direction = 0
    elif diff_y == 0 and px < fx:
        direction = 180
    elif diff_x == 0 and py > fy:
        direction = 90
    elif diff_x == 0 and py < fy:
        direction = -90
    
    image = CvOverlayImage.overlay(image, rotate(friend, direction), (fx, fy))
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

def ahead(save, prt, px, py, dir_p, enemy, ex, ey, dir_e, friend, fx, fy, dir_f, bg):
    image = CvOverlayImage.overlay(bg, rotate(prt, dir_p), (px, py))
    image = CvOverlayImage.overlay(image, rotate(enemy, dir_e), (ex, ey))
    save_image(save, image, prt, px, py, enemy, ex, ey, friend, fx, fy)


if __name__ == '__main__':
    px  = 20
    py  = 168
    ex = 220
    ey = 128
    fx = 540
    fy = 248
    right = 0
    left = 180
    upper = 90
    below = 270

    prt1 = cv2.imread("./imgs2/drop_blue.png", -1) # (375, 454, 4)
    prt1 = cv2.resize(prt1, (int(prt1.shape[1] / 15), int(prt1.shape[0] / 15))) # (20, 30, 4)
    prt2 = cv2.imread("./imgs2/drop_blue_flower.png", -1) # (375, 454, 4)
    prt2 = cv2.resize(prt2, (int(prt2.shape[1] / 15), int(prt2.shape[0] / 15))) # (30, 45, 4)
    enemy = cv2.imread("./imgs2/enemy.png", -1)
    enemy = cv2.resize(enemy, (int(enemy.shape[1] / 15), int(enemy.shape[0] / 15))) # (20, 30, 4)
    enemy2 = cv2.resize(enemy, (int(enemy.shape[1] * 3 / 2), int(enemy.shape[0] * 3 / 2))) # (20, 30, 4)
    bg3 = cv2.imread("./imgs2/bg.png") # (366, 603, 3)
    friend1 = cv2.imread("./imgs2/drop_pink.png", -1) # (375, 454, 4)
    friend1 = cv2.resize(friend1, (int(friend1.shape[1] / 15), int(friend1.shape[0] / 15))) # (20, 30, 4)
    friend2 = cv2.imread("./imgs2/drop_pink_flower.png", -1) # (375, 454, 4)
    friend2 = cv2.resize(friend2, (int(friend2.shape[1] / 15), int(friend2.shape[0] / 15))) # (30, 45, 4)
    flower_blue = cv2.imread("./imgs2/flower_blue.png", -1)
    flower_blue = cv2.resize(flower_blue, (int(flower_blue.shape[1] / 11), int(flower_blue.shape[0] / 11)))
    flower_red = cv2.imread("./imgs2/flower_red.png", -1)
    flower_red = cv2.resize(flower_red, (int(flower_red.shape[1] / 11), int(flower_red.shape[0] / 11)))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+210, py-160))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+250, py-160))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+290, py-160))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+330, py-160))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+210, py-120))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+250, py-120))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+330, py-120))
    bg3 = CvOverlayImage.overlay(bg3, flower_blue, (px+250, py-80))
    bg2 = CvOverlayImage.overlay(bg3, flower_red, (px+290, py-120))
    bg1 = CvOverlayImage.overlay(bg2, flower_blue, (px+290, py-80))
    bg4 = CvOverlayImage.overlay(bg3, flower_blue, (px+450, py-40))
    # bg1:all flowers bg2:pick blue one bg3: pick red one bg4: put one

    mp4 = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    save = cv2.VideoWriter("./main2.mp4", mp4, 7.0, (bg1.shape[1], bg1.shape[0]))

    # start
    ahead(save, prt1, px, py, right-30, enemy, ex, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+10, py, right, enemy, ex+10, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+20, py, right+30, enemy, ex+20, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+30, py, right, enemy, ex+30, ey, right+30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+40, py, upper-30, enemy, ex+40, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-10, upper, enemy, ex+50, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-20, upper+30, enemy, ex+60, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-30, upper, enemy, ex+70, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+40, py-40, upper-30, enemy, ex+80, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-50, upper, enemy, ex+90, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-60, upper+30, enemy, ex+100, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-70, upper, enemy, ex+110, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+40, py-80, upper-30, enemy, ex+120, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-90, upper, enemy, ex+130, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-100, upper+30, enemy, ex+140, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+40, py-110, upper, enemy, ex+150, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+40, py-120, right-30, enemy, ex+160, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+50, py-120, right, enemy, ex+150, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+60, py-120, right+30, enemy, ex+140, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+70, py-120, right, enemy, ex+130, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+80, py-120, right-30, enemy, ex+120, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+90, py-120, right, enemy, ex+110, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+100, py-120, right+30, enemy, ex+100, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+110, py-120, right, enemy, ex+90, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py-120, right-30, enemy, ex+80, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+130, py-120, right, enemy, ex+70, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+140, py-120, right+30, enemy, ex+60, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+150, py-120, right, enemy, ex+50, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+160, py-110, below-30, enemy, ex+40, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+160, py-100, below, enemy, ex+30, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+160, py-90, below+30, enemy, ex+20, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+160, py-80, below, enemy, ex+10, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+160, py-80, right-30, enemy, ex, ey, gaze(px+160, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+170, py-80, right, enemy, ex, ey, gaze(px+170, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+180, py-80, right+30, enemy, ex, ey, gaze(px+180, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+190, py-80, right, enemy, ex, ey, gaze(px+190, py-80, ex, ey), friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+200, py-80, right-30, enemy, ex, ey, gaze(px+200, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+210, py-80, right, enemy, ex, ey, gaze(px+210, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+220, py-80, right+30, enemy, ex, ey, gaze(px+220, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+230, py-80, right, enemy, ex, ey, gaze(px+230, py-80, ex, ey), friend1, fx, fy, left, bg1)

    # angry enemy
    ahead(save, prt1, px+240, py-80, right, enemy, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right, enemy, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right, enemy, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right, enemy, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, right-30, enemy, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, below+30, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, below, enemy, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, below-30, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, left+30, enemy, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, left, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, left-30, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+240, py-80, left, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)

    # escape
    ahead(save, prt1, px+240, py-80, left-30, enemy2, ex, ey, gaze(px+240, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+220, py-80, left, enemy2, ex, ey, gaze(px+220, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py-80, left+30, enemy2, ex, ey, gaze(px+200, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+180, py-80, left, enemy2, ex, ey, gaze(px+180, py-80, ex, ey), friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+160, py-80, upper+30, enemy2, ex, ey, gaze(px+160, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+160, py-100, upper, enemy2, ex, ey, gaze(px+160, py-100, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+160, py-120, left-30, enemy2, ex, ey, gaze(px+160, py-120, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+140, py-120, left, enemy2, ex, ey, gaze(px+140, py-120, ex, ey), friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py-120, below-30, enemy2, ex, ey, gaze(px+120, py-120, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-100, below, enemy2, ex, ey, gaze(px+120, py-100, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-80, below+30, enemy2, ex, ey, gaze(px+120, py-80, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-60, below, enemy2, ex, ey, gaze(px+120, py-60, ex, ey), friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py-40, upper-30, enemy2, ex, ey, gaze(px+120, py-40, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-40, upper, enemy2, ex, ey, gaze(px+120, py-40, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-40, upper+30, enemy2, ex, ey, gaze(px+120, py-40, ex, ey), friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-40, upper, enemy2, ex, ey, gaze(px+120, py-40, ex, ey), friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py-40, below-30, enemy, ex, ey, upper, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-30, below, enemy, ex, ey-10, upper+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-20, below+30, enemy, ex, ey-20, upper, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py-10, below, enemy, ex, ey-30, upper-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py, below-30, enemy, ex, ey-40, below, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py+10, below, enemy, ex, ey-30, below+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py+20, below+30, enemy, ex, ey-20, below, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py+30, below, enemy, ex, ey-10, below-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py+40, right-30, enemy, ex, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+130, py+40, right, enemy, ex+10, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+140, py+40, right+30, enemy, ex+20, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+150, py+40, right, enemy, ex+30, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+160, py+40, right-30, enemy, ex+40, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+170, py+40, right, enemy, ex+50, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+180, py+40, right+30, enemy, ex+60, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+190, py+40, right, enemy, ex+70, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+200, py+40, gaze(ex+80, ey, px+200, py+40), enemy, ex+80, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, gaze(ex+90, ey, px+200, py+40), enemy, ex+90, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, gaze(ex+100, ey, px+200, py+40), enemy, ex+100, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, gaze(ex+110, ey, px+200, py+40), enemy, ex+110, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+200, py+40, gaze(ex+120, ey, px+200, py+40), enemy, ex+120, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, gaze(ex+130, ey, px+200, py+40), enemy, ex+130, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, gaze(ex+140, ey, px+200, py+40), enemy, ex+140, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, gaze(ex+150, ey, px+200, py+40), enemy, ex+150, ey, right-30, friend1, fx, fy, left, bg1)

    # blue drop go another root
    ahead(save, prt1, px+200, py+40, right-45, enemy, ex+160, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, right, enemy, ex+150, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, below+45, enemy, ex+140, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+40, below, enemy, ex+130, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+200, py+40, below-30, enemy, ex+120, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+50, below, enemy, ex+110, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+60, below+30, enemy, ex+100, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+200, py+70, below, enemy, ex+90, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+200, py+80, left-30, enemy, ex+80, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+190, py+80, left, enemy, ex+70, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+180, py+80, left+30, enemy, ex+60, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+170, py+80, left, enemy, ex+50, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+160, py+80, left-30, enemy, ex+40, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+150, py+80, left, enemy, ex+30, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+140, py+80, left+30, enemy, ex+20, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+130, py+80, left, enemy, ex+10, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py+80, below-30, enemy, ex, ey, upper, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py+90, below, enemy, ex, ey-10, upper+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py+100, below+30, enemy, ex, ey-20, upper, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+120, py+110, below, enemy, ex, ey-30, upper-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+120, py+120, right-30, enemy, ex, ey-40, below, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+130, py+120, right, enemy, ex, ey-30, below+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+140, py+120, right+30, enemy, ex, ey-20, below, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+150, py+120, right, enemy, ex, ey-10, below-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+160, py+120, right-30, enemy, ex, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+170, py+120, right, enemy, ex+10, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+180, py+120, right+30, enemy, ex+20, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+190, py+120, right, enemy, ex+30, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+200, py+120, right-30, enemy, ex+40, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+210, py+120, right, enemy, ex+50, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+220, py+120, right+30, enemy, ex+60, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+230, py+120, right, enemy, ex+70, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+240, py+120, right-30, enemy, ex+80, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+250, py+120, right, enemy, ex+90, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+260, py+120, right+30, enemy, ex+100, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+270, py+120, right, enemy, ex+110, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+280, py+120, upper-30, enemy, ex+120, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+110, upper, enemy, ex+130, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+100, upper+30, enemy, ex+140, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+90, upper, enemy, ex+150, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+280, py+80, upper-30, enemy, ex+160, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+70, upper, enemy, ex+150, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+60, upper+30, enemy, ex+140, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+50, upper, enemy, ex+130, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+280, py+40, gaze(ex+120, ey, px+280, py+40), enemy, ex+120, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+40, gaze(ex+110, ey, px+280, py+40), enemy, ex+110, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+40, gaze(ex+100, ey, px+280, py+40), enemy, ex+100, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+40, gaze(ex+90, ey, px+280, py+40), enemy, ex+90, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+280, py+40, gaze(ex+80, ey, px+280, py+40), enemy, ex+80, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+40, gaze(ex+70, ey, px+280, py+40), enemy, ex+70, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+40, gaze(ex+60, ey, px+280, py+40), enemy, ex+60, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+40, gaze(ex+50, ey, px+280, py+40), enemy, ex+50, ey, left-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+280, py+40, upper-30, enemy, ex+40, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+30, upper, enemy, ex+30, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+20, upper+30, enemy, ex+20, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py+10, upper, enemy, ex+10, ey, left-30, friend1, fx, fy, left, bg1)

    # blue drop go danger root
    ahead(save, prt1, px+280, py, upper-30, enemy, ex, ey, upper, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py-10, upper, enemy, ex, ey-10, upper+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py-20, upper+30, enemy, ex, ey-20, upper, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+280, py-30, upper, enemy, ex, ey-30, upper-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+280, py-40, right-30, enemy, ex, ey-40, below, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+300, py-40, right, enemy, ex, ey-30, below+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+320, py-40, right+30, enemy, ex, ey-20, below, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+340, py-40, right, enemy, ex, ey-10, below-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+360, py-40, upper-30, enemy, ex, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+360, py-50, upper, enemy, ex+10, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+360, py-60, upper+30, enemy, ex+20, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+360, py-70, upper, enemy, ex+30, ey, right-30, friend1, fx, fy, left, bg1)

    # blue drop look enemy and enter flowers
    ahead(save, prt1, px+360, py-80, gaze(ex+40, ey, px+360, py-80), enemy, ex+40, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+360, py-80, gaze(ex+50, ey, px+360, py-80), enemy, ex+50, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+360, py-80, gaze(ex+60, ey, px+360, py-80), enemy, ex+60, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+360, py-80, gaze(ex+70, ey, px+360, py-80), enemy, ex+70, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+360, py-80, left-30, enemy, ex+80, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+350, py-80, left, enemy, ex+90, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+340, py-80, left+30, enemy, ex+100, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+330, py-80, left, enemy, ex+110, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+320, py-80, left-30, enemy, ex+120, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+320, py-80, left, enemy, ex+130, ey, right+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+320, py-80, left+30, enemy, ex+140, ey, right, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+320, py-80, left, enemy, ex+150, ey, right-30, friend1, fx, fy, left, bg1)

    ahead(save, prt1, px+320, py-80, left-30, enemy, ex+160, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+320, py-80, left, enemy, ex+150, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+320, py-80, left+30, enemy, ex+140, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+320, py-80, left, enemy, ex+130, ey, left-30, friend1, fx, fy, left, bg1)

    # pick up blue and red flowers
    ahead(save, prt1, px+320, py-80, left-30, enemy, ex+120, ey, left, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+310, py-80, left, enemy, ex+110, ey, left+30, friend1, fx, fy, left, bg1)
    ahead(save, prt1, px+300, py-80, left+30, enemy, ex+100, ey, left, friend1, fx, fy, left, bg2)
    ahead(save, prt1, px+290, py-80, left, enemy, ex+90, ey, left-30, friend1, fx, fy, left, bg2)

    ahead(save, prt1, px+280, py-80, upper, enemy, ex+80, ey, left, friend1, fx, fy, left, bg2)
    ahead(save, prt1, px+280, py-80, upper, enemy, ex+70, ey, left+30, friend1, fx, fy, left, bg2)
    ahead(save, prt1, px+280, py-80, upper, enemy, ex+60, ey, left, friend1, fx, fy, left, bg2)
    ahead(save, prt1, px+280, py-80, upper, enemy, ex+50, ey, left-30, friend1, fx, fy, left, bg2)

    ahead(save, prt1, px+280, py-80, upper-30, enemy, ex+40, ey, left, friend1, fx, fy, left, bg2)
    ahead(save, prt1, px+280, py-90, upper, enemy, ex+30, ey, left+30, friend1, fx, fy, left, bg2)
    ahead(save, prt2, px+280, py-100, upper+30, enemy, ex+20, ey, left, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+280, py-110, upper, enemy, ex+10, ey, left-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+280, py-120, below-30, enemy, ex, ey, upper, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+280, py-110, below, enemy, ex, ey-10, upper+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+280, py-100, below+30, enemy, ex, ey-20, upper, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+280, py-90, below, enemy, ex, ey-30, upper-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+280, py-80, right-30, enemy, ex, ey-40, below, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+290, py-80, right, enemy, ex, ey-30, below+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+300, py-80, right+30, enemy, ex, ey-20, below, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+310, py-80, right, enemy, ex, ey-10, below-30, friend1, fx, fy, left, bg3)

    # try to escape
    ahead(save, prt2, px+320, py-80, right-30, enemy, ex, ey, right, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+330, py-80, right, enemy, ex+10, ey, right+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+340, py-80, right+30, enemy, ex+20, ey, right, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+350, py-80, right, enemy, ex+30, ey, right-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+360, py-80, gaze(ex+40, ey, px+360, py-80), enemy, ex+40, ey, right, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-80, gaze(ex+50, ey, px+360, py-80), enemy, ex+50, ey, right+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-80, gaze(ex+60, ey, px+360, py-80), enemy, ex+60, ey, right, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-80, gaze(ex+70, ey, px+360, py-80), enemy, ex+70, ey, right-30, friend1, fx, fy, left, bg3)

    # enemy aware
    ahead(save, prt2, px+360, py-80, below, enemy, ex+80, ey, right, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-70, below, enemy, ex+80, ey, right+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-60, below, enemy, ex+80, ey, right, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-50, below, enemy, ex+80, ey, right-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+360, py-40, below, enemy, ex+80, ey, gaze(px+360, py-40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-30, below, enemy, ex+80, ey, gaze(px+360, py-30, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-20, below, enemy, ex+80, ey, gaze(px+360, py-20, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py-10, below, enemy, ex+80, ey, gaze(px+360, py-10, ex+80, ey), friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+360, py, below, enemy2, ex+80, ey, gaze(px+360, py, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+10, below, enemy, ex+80, ey, gaze(px+360, py+10, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+20, below, enemy2, ex+80, ey, gaze(px+360, py+20, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+30, below, enemy, ex+80, ey, gaze(px+360, py+30, ex+80, ey), friend1, fx, fy, left, bg3)

    # blue drop aware
    ahead(save, prt2, px+360, py+40, below-30, enemy2, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, left+30, enemy, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, left, enemy2, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, left-30, enemy, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+360, py+40, upper+30, enemy2, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, upper+40, enemy, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, upper+40, enemy2, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, upper+30, enemy, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+360, py+40, upper, enemy2, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, upper-30, enemy, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, right+30, enemy2, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+360, py+40, right, enemy, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+360, py+40, right-30, enemy, ex+80, ey, gaze(px+360, py+40, ex+80, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+370, py+40, right, enemy, ex+90, ey, gaze(px+370, py+40, ex+90, ey)+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+380, py+40, right+30, enemy, ex+100, ey, gaze(px+380, py+40, ex+100, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+390, py+40, right, enemy, ex+110, ey, gaze(px+390, py+40, ex+110, ey)-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+400, py+40, right-30, enemy, ex+120, ey, gaze(px+400, py+40, ex+120, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+410, py+40, right, enemy, ex+130, ey, gaze(px+410, py+40, ex+130, ey)+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+420, py+40, right+30, enemy, ex+140, ey, gaze(px+420, py+40, ex+140, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+430, py+40, right, enemy, ex+150, ey, gaze(px+430, py+40, ex+150, ey)-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+440, py+40, upper-30, enemy, ex+160, ey, gaze(px+440, py+40, ex+160, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py+30, upper, enemy, ex+170, ey, gaze(px+440, py+30, ex+170, ey)+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py+20, upper+30, enemy, ex+180, ey, gaze(px+440, py+20, ex+180, ey), friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py+10, upper, enemy, ex+190, ey, gaze(px+440, py+10, ex+190, ey)-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+440, py, upper-30, enemy, ex+200, ey, below, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-10, upper, enemy, ex+200, ey+10, below+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-20, upper+30, enemy, ex+200, ey+20, below, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-30, upper, enemy, ex+200, ey+30, below-30, friend1, fx, fy, left, bg3)

    ahead(save, prt2, px+440, py-40, upper-30, enemy, ex+200, ey+40, below, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-50, upper, enemy, ex+200, ey+50, below+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-60, upper+30, enemy, ex+200, ey+60, below, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-70, upper, enemy, ex+200, ey+70, below-30, friend1, fx, fy, left, bg3)

    # put flower -> bg4
    ahead(save, prt2, px+440, py-80, below-30, enemy, ex+200, ey+80, right, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-80, below, enemy, ex+210, ey+80, right+30, friend1, fx, fy, left, bg3)
    ahead(save, prt2, px+440, py-80, below+30, enemy, ex+220, ey+80, right, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+440, py-80, below, enemy, ex+230, ey+80, right-30, friend1, fx, fy, left, bg4)

    ahead(save, prt2, px+440, py-80, upper-30, enemy, ex+240, ey+80, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+440, py-90, upper, enemy, ex+240, ey+70, upper+30, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+440, py-100, upper+30, enemy, ex+240, ey+60, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+440, py-110, upper, enemy, ex+240, ey+50, upper-30, friend1, fx, fy, left, bg4)

    # enemy cannot go
    ahead(save, prt2, px+440, py-120, right, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+440, py-120, below, enemy, ex+240, ey+30, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+440, py-120, below, enemy, ex+240, ey+20, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+440, py-120, below, enemy, ex+240, ey+30, upper, friend1, fx, fy, left, bg4)

    ahead(save, prt2, px+440, py-120, right-30, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+450, py-120, right, enemy, ex+240, ey+30, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+450, py-120, right+30, enemy, ex+240, ey+20, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+470, py-120, right, enemy, ex+240, ey+30, upper, friend1, fx, fy, left, bg4)

    # enemy gaze drop
    ahead(save, prt2, px+480, py-120, below-30, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-110, below, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-100, below+30, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-90, below, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)

    ahead(save, prt2, px+480, py-80, below-30, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-70, below, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-60, below+30, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-50, below, enemy, ex+240, ey+40, upper, friend1, fx, fy, left, bg4)

    # enemy go back
    ahead(save, prt2, px+480, py-40, below-30, enemy, ex+240, ey+40, below, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-30, below, enemy, ex+240, ey+50, below+30, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-20, below+30, enemy, ex+240, ey+60, below, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+480, py-10, below, enemy, ex+240, ey+70, below-30, friend1, fx, fy, left, bg4)

    ahead(save, prt2, px+480, py, right-30, enemy, ex+240, ey+80, left, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+490, py, right, enemy, ex+230, ey+80, left+30, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+500, py, right+30, enemy, ex+220, ey+80, left, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+510, py, right, enemy, ex+210, ey+80, left-30, friend1, fx, fy, left, bg4)

    ahead(save, prt2, px+520, py, below-30, enemy, ex+200, ey+80, left, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+520, py+10, below, enemy, ex+190, ey+80, left+30, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+520, py+20, below+30, enemy, ex+180, ey+80, left, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+520, py+30, below, enemy, ex+170, ey+80, left-30, friend1, fx, fy, left, bg4)

    # blue drop give flower to pink drop
    ahead(save, prt2, px+520, py+40, below, enemy, ex+160, ey+80, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+520, py+40, below, enemy, ex+160, ey+70, upper+30, friend1, fx, fy, left, bg4)
    ahead(save, prt2, px+520, py+50, below, enemy, ex+160, ey+60, upper, friend1, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+60, below, enemy, ex+160, ey+50, upper-30, friend2, fx, fy, left, bg4)

    ahead(save, prt1, px+520, py+50, below, enemy, ex+160, ey+40, upper, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey+30, upper+30, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey+20, upper, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey+10, upper-30, friend2, fx, fy, left, bg4)

    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey+0, upper, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-10, upper+30, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-20, upper, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-30, upper-30, friend2, fx, fy, left, bg4)

    # enemy gaze no flower place
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)

    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)

    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)
    ahead(save, prt1, px+520, py+40, below, enemy, ex+160, ey-40, left, friend2, fx, fy, left, bg4)

    # goal

    cv2.destroyAllWindows()
    save.release()
