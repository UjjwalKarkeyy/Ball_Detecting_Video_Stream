import cv2

# Using index 0 for capturing video stream
cap = cv2.VideoCapture(0)

# Forcing cv2 to use MJPG format as that's the default of WSL
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# If cam is not available
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read() # Returns true/false and frame
    
    # If not ret (false) = true, cam is not receiving frame
    if not ret:
        print("Cannot receive frame")
        break

    # Converting frame to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Showing frame in a pop up window
    cv2.imshow('frame', gray)

    # Wait for zero milli seconds which basically means cv2 is checking if there was any input 'q' to stop the window
    # Also, ord means 'Ordinal' basically converting 'q' to its unicode equivalent 
    if cv2.waitKey(0) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()