import cv2

# Set the indices for the two cameras
camera1_index = 0
camera2_index = 2

# Create video capture objects for each camera
cap1 = cv2.VideoCapture(camera1_index)
cap2 = cv2.VideoCapture(camera2_index)

# Check if the capture objects have been initialized correctly
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: One or both cameras cannot be opened.")
    exit()

while True:
    # Capture frame from camera 1
    ret1, frame1 = cap1.read()
    if not ret1:
        print("Error: Unable to capture frame from camera 1.")
        break

    # Capture frame from camera 2
    ret2, frame2 = cap2.read()
    if not ret2:
        print("Error: Unable to capture frame from camera 2.")
        break

    # Save the frames (you can choose any format supported by OpenCV)
    cv2.imwrite('camera1_frame.jpg', frame1)
    cv2.imwrite('camera2_frame.jpg', frame2)
    print("saved images")
    # Display the frames (optional)
    cv2.imshow('Camera 1', frame1)
    cv2.imshow('Camera 2', frame2)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture objects and close all windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()
