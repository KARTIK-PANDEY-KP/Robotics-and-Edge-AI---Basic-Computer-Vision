# Importing required libraries
import cv2
# import time
import matplotlib.pyplot as plt
path = "."
xCoord = []
yCoord = []
for i in range(1,34,1):
    IMAGE_PATH = path + "/" + str(i) + ".jpg"
    print(IMAGE_PATH)
    img = cv2.imread(IMAGE_PATH) 

    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # mask
    mask = cv2.inRange(hsv, (30, 118, 149),(40, 158, 198))  ##  TUNE THIS HSV RANGE 

    # convert the grayscale image to binary image
    ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

    # find contours in the binary image
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    count = 0
    for ct in contours:
        # calculate moments for each contour
        M = cv2.moments(ct)
        # calculate x,y coordinate of center
        if(M["m00"] !=0):
            count = count + 1
            Centroid_X = int(M["m10"] / M["m00"])
            Centroid_Y = int(M["m01"] / M["m00"])
            print(Centroid_X, Centroid_Y)
            
            # Storing the coordinates to visualize them later
            xCoord.append(Centroid_X)
            yCoord.append(Centroid_Y)
            cv2.circle(img, (Centroid_X, Centroid_Y), 5, (255, 255, 255), -1)
            cv2.putText(img, "centroid", (Centroid_X - 25, Centroid_Y - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            # For saving the images with centroid marked on the images
            cv2.imwrite(f'IMAGE_{i}.png', img)
            # time.sleep(100)
plt.scatter(xCoord, yCoord)
# For making iot visually appealing easy to observe
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
# For visualizing the movement of the ball
plt.show()

# Finally we can deduce that the motion of the ball is projectile on nature