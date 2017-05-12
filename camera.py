import picamera
import time


with picamera.PiCamera() as camera:
    camera.rotation = 90
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('pic.jpg')