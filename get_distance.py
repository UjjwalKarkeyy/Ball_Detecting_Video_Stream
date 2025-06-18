import cv2
from util import get_limits

# Have to install module as Pillow but import as PIL
from PIL import Image

# Using index 0 for capturing video stream
cap = cv2.VideoCapture(0)

# Forcing cv2 to use MJPG format as that's the default of WSL
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# If cam is not available
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# BRG value for color pink
pink = [203,192,255]

while True:
    ret, frame = cap.read() # Returns true/false and frame
    
    # If not ret (false) = true, cam is not receiving frame
    if not ret:
        print("Cannot receive frame")
        break

    # Getting the lower and upper limit i.e., the range of color that I spoke about in util file
    lowerLimit, upperLimit = get_limits(pink)

    # Converting from BGR to HSV
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Its like applying a filter that is black with only highlighting the color that we need with bright white
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)

    # Contours basically means the points on the boundry of the object
    # It works by using white blob that appear in our masking and gives us the points of its boundries
    # We are using retrieve external as the mode and contour approximation simple as the method
    # Returns a list of all the contours encountered
    # Another _ returned value is basically which contour is inside which like parent child values.
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:

        # Returns the contour points for the highest measure area
        cnt = max(contours, key = cv2.contourArea)
        # Finding area using the points
        area = cv2.contourArea(cnt)
        print("Area is: ", area)

    # Run the following and show the color object in front of the cam to understand what mask does
    # cv2.imshow('mask', mask)

    # Converting to image from array
    mask_img = Image.fromarray(mask)

    # Using that image and getting the boundaries of it in the form of coordinates
    bbox = mask_img.getbbox()

    # If no boundaries then bbox (boundary box) returns None
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        # Using the coordinates returned by bbox to draw a green rectange on the frame
        # First argument if passing the frame, then the coordinates, then the color of border
        # Lastly, the thickness of the border
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),5)

    # Two arguments, first is the name of the window and second is the frame itself.
    cv2.imshow("frame",frame)

    # Wait for zero milli seconds which basically means cv2 is checking if there was any input 'q' to stop the window
    # Also, ord means 'Ordinal' basically converting 'q' to its unicode equivalent 
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()