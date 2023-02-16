import cv2 

source = cv2.VideoCapture(0)
Preview = 0 
canny = 1
image_filter = Preview
viewer = 'Filter Demo'
cv2.namedWindow(viewer, cv2.WINDOW_NORMAL)

while True:
    is_frame, frame = source.read()
    if not is_frame:
        break
    frame = cv2.flip(frame, 1)
    if image_filter == Preview:
        result = frame
    elif image_filter == canny:
        result = cv2.Canny(frame, 80, 150)
    cv2.imshow(viewer, result)

    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        break 
    elif key == ord('C') or key == ord('c'):
        image_filter = canny
    elif key == ord('P') or key == ord('p'):
        image_filter = Preview
