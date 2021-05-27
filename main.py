import cv2
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

def go_right(save, pos_x, pos_y):
    image = CvOverlayImage.overlay(bg, prt, (pos_x, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 30), (pos_x+10, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 0), (pos_x+20, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, -30), (pos_x+30, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

def go_left(save, pos_x, pos_y):
    image = CvOverlayImage.overlay(bg, rotate(prt, 180), (pos_x, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 150), (pos_x-10, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 180), (pos_x-20, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 210), (pos_x-30, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

def go_upper(save, pos_x, pos_y):
    image = CvOverlayImage.overlay(bg, rotate(prt, 90), (pos_x, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 120), (pos_x, pos_y-10))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 90), (pos_x, pos_y-20))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 60), (pos_x, pos_y-30))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

def go_below(save, pos_x, pos_y):
    image = CvOverlayImage.overlay(bg, rotate(prt, 270), (pos_x, pos_y))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 240), (pos_x, pos_y+10))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 300), (pos_x, pos_y+20))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)

    image = CvOverlayImage.overlay(bg, rotate(prt, 270), (pos_x, pos_y+30))
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
    cv2.imwrite("image.png", image)
    image = cv2.imread("image.png")
    save.write(image)


if __name__ == '__main__':
    prt = cv2.imread("./imgs/protagonist_openeyes.png", -1) # (375, 454, 4)
    prt = cv2.resize(prt, (int(prt.shape[1] / 15), int(prt.shape[0] / 15))) # (20, 30, 4)
    bg = cv2.imread("./imgs/bg.png") # (366, 603, 3)

    mp4 = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    save = cv2.VideoWriter("./video.mp4", mp4, 8.0, (bg.shape[1], bg.shape[0]))

    pos_x  = 20
    pos_y  = 168
    go_right(save, pos_x, pos_y)
    go_below(save, pos_x+40, pos_y)
    go_right(save, pos_x+40, pos_y+40)
    go_right(save, pos_x+80, pos_y+40)
    go_upper(save, pos_x+120, pos_y+40)
    go_right(save, pos_x+120, pos_y)
    go_right(save, pos_x+160, pos_y)
    go_below(save, pos_x+200, pos_y)
    go_below(save, pos_x+200, pos_y+40)
    go_right(save, pos_x+200, pos_y+80)
    go_right(save, pos_x+240, pos_y+80)
    go_below(save, pos_x+280, pos_y+80)
    go_upper(save, pos_x+280, pos_y+120)
    go_left(save, pos_x+280, pos_y+80)
    go_left(save, pos_x+240, pos_y+80)
    go_left(save, pos_x+200, pos_y+80)
    go_upper(save, pos_x+160, pos_y+80)
    go_upper(save, pos_x+160, pos_y+40)
    go_left(save, pos_x+160, pos_y+0)
    go_below(save, pos_x+120, pos_y+0)
    go_left(save, pos_x+120, pos_y+40)
    go_left(save, pos_x+80, pos_y+40)
    go_upper(save, pos_x+40, pos_y+40)
    go_upper(save, pos_x+40, pos_y+0)
    go_right(save, pos_x+40, pos_y-40)
    go_upper(save, pos_x+80, pos_y-40)
    go_upper(save, pos_x+80, pos_y-80)
    go_right(save, pos_x+80, pos_y-120)
    go_below(save, pos_x+120, pos_y-120)
    go_below(save, pos_x+120, pos_y-80)
    go_right(save, pos_x+120, pos_y-40)
    go_right(save, pos_x+160, pos_y-40)
    go_left(save, pos_x+200, pos_y-40)
    go_upper(save, pos_x+160, pos_y-40)
    go_upper(save, pos_x+160, pos_y-80)
    go_upper(save, pos_x+160, pos_y-120)
    go_right(save, pos_x+160, pos_y-160)
    go_right(save, pos_x+200, pos_y-160)
    go_right(save, pos_x+240, pos_y-160)
    go_below(save, pos_x+280, pos_y-160)
    go_right(save, pos_x+280, pos_y-120)
    go_below(save, pos_x+320, pos_y-120)
    go_below(save, pos_x+320, pos_y-80)
    go_below(save, pos_x+320, pos_y-40)
    go_below(save, pos_x+320, pos_y-0)
    go_below(save, pos_x+320, pos_y+40)
    go_right(save, pos_x+320, pos_y+80)
    go_left(save, pos_x+360, pos_y+80)
    go_upper(save, pos_x+320, pos_y+80)
    go_upper(save, pos_x+320, pos_y+40)
    go_upper(save, pos_x+320, pos_y+0)
    go_right(save, pos_x+320, pos_y-40)
    go_right(save, pos_x+360, pos_y-40)
    go_below(save, pos_x+400, pos_y-40)
    go_below(save, pos_x+400, pos_y-0)
    go_right(save, pos_x+400, pos_y+40)
    go_upper(save, pos_x+440, pos_y+40)
    go_upper(save, pos_x+440, pos_y+0)
    go_upper(save, pos_x+440, pos_y-40)
    go_upper(save, pos_x+440, pos_y-80)
    go_upper(save, pos_x+440, pos_y-120)
    go_right(save, pos_x+440, pos_y-160)
    go_below(save, pos_x+480, pos_y-160)
    go_below(save, pos_x+480, pos_y-120)
    go_below(save, pos_x+480, pos_y-80)
    go_below(save, pos_x+480, pos_y-40)
    go_right(save, pos_x+480, pos_y-0)

    cv2.destroyAllWindows()
    save.release()
