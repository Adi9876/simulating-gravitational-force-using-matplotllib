import cv2
import os

image_folder = 'image1'
video_name = 'simulation1.mp4'

images = [img for img in os.listdir(image_folder)]
images = sorted(images, key=lambda x: int(x.split('.')[0]))
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

for image in images:
    img = cv2.imread(os.path.join(image_folder, image))
    if img.shape == frame.shape:
	    video.write(img)

cv2.destroyAllWindows()
video.release()