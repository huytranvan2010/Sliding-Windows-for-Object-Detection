""" 
    Ở đây mình muốn kiểm tra khi nó trượt nó có lấy phần dìa nếu còn dư không?
    Đáp án là: YES 
    Ở đây có thể tạo một list để lưu các sliding window cũng được nhưng có vẻ dùng generator tiện hơn,
    duyệt đến khi nào hết thì thôi
"""
import numpy as np

image = np.zeros((7, 7))

def slide(image, stepSize):
    for i in range(0, image.shape[1], stepSize):    # i = 0, 2, 4, 6
        for j in range(0, image.shape[0], stepSize):    # j = 0, 2, 4, 6
            yield image[j: j + 2, i: i + 2]
            
            # nhận thấy phần này có image[6: 8, i: i + 2] và image[j: j + 2, 6: 8]
            # phần 6:8 - 2 pixel nhưng chỉ còn 1 pixel do đó chỉ lấy đến 7 là 6:7 thôi.
            # kết quả bên dưới mong đợi là 16

counts = 0 

for _ in slide(image, stepSize=2):
    counts += 1

print("Expected # of sliding windows: ", counts)