# Hướng dẫn chạy
# python sliding_window.py --image images/fire.jpg
from hammiu.helpers import pyramid, sliding_window
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# định nghĩa windowSize
(winW, winH) = (128, 128)

# Duyệt qua image pyramid
for resized in pyramid(image, scale=1.5):
    # Duyệt qua các sliding windows cho mỗi layer của image pyramid
    for (x, y, window) in sliding_window(image, stepSize=32, windowSize=(winW, winH)):
        # Nếu như window không thỏa mãn kích thước mong đợi của chúng ta thì bỏ qua
        if window.shape[0] != winH or window.shape[1] != winW:
            continue    # tiếp tục vòng lặp for
            # thực chất phần này sẽ dành cho việc khác
        
        clone = resized.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        cv2.imshow("window", clone)
        cv2.waitKey(1)
        time.sleep(0.025)


