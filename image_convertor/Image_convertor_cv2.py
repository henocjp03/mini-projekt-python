import cv2

def convert_bw(img_to_convert):
    img = cv2.imread(img_to_convert)
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(img)