import cv2
import numpy as np

def confidence(img, template):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    conf = res.max()
    print
    return np.where(res == conf), conf

files = ["img_conf_1.png", "img_conf_2.png"]

template = cv2.imread("img_conf_template.png")
# template = cv2.resize(template, (500,500))
h, w, _ = template.shape

for name in files:
    img = cv2.imread(name)
    # img = cv2.resize(img, (500,500))
    ([y], [x]), conf = confidence(img, template)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    text = f'Confidence: {round(float(conf), 2)}'
    cv2.putText(img, text, (x, y), 1, cv2.FONT_HERSHEY_PLAIN, (0, 0, 0), 2)
    cv2.imshow(name, img)
    
    
cv2.imshow('Template', template)
cv2.waitKey(0)