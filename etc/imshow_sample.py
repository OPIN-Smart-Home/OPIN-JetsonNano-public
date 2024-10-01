import cv2
img = cv2.imread("/ultralytics/sample.jpeg")
while True:
    cv2.imshow('frame', img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
