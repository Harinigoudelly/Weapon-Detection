import numpy as np

def detect_weapon(image):
    img = np.array(image)
    h, w, _ = img.shape

    # Dummy detection box (center)
    x1 = int(w * 0.3)
    y1 = int(h * 0.3)
    x2 = int(w * 0.7)
    y2 = int(h * 0.7)

    boxes = [(x1, y1, x2, y2)]
    scores = [0.90]

    return boxes, scores