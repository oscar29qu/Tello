import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

image_path = os.path.join(os.getcwd(), 'runner.jpg')
np_image = cv2.imread(image_path)
np_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
np_image = cv2.resize(np_image, dsize=(1000,1000))

def sliding_window(image, step, ws):
    for y in range(0, image.shape[0]-ws[1]+1, step):
        for x in range(0, image.shape[1]-ws[0]+1, step):
            yield (x, y, image[y:y + ws[1], x:x + ws[0]])

windows = sliding_window(np_image, 200, (200, 200))

os.makedirs('sliding_window', exist_ok=True)

for x, window in enumerate(windows):
    f, axarr = plt.subplots(1, 2, figsize=(12, 12))
    axarr[0].imshow(np_image)
    rect = patches.Rectangle((window[0], window[1]), 200, 200, linewidth=2, edgecolor='g', facecolor='none')
    axarr[0].add_patch(rect)
    axarr[1].imshow(window[2])
    plt.savefig('sliding_window/'+str(x)+'.png', dpi=f.dpi)
    plt.pause(0.5)
    plt.close()