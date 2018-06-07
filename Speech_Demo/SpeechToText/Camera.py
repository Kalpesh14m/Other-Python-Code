"""This Camera Module is for open camera"""

import cv2

def camera():
    camera = cv2.VideoCapture(0)
    while True:
        return_value,image = camera.read()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow('image',gray)
        if 0xFF == ord('q'):
            break

        else:
            if cv2.waitKey(1)& 0xFF == ord('s'):
                cv2.imwrite('ImgCap/test.jpg',image)
                break

    camera.release()
    cv2.destroyAllWindows()

# camera()

