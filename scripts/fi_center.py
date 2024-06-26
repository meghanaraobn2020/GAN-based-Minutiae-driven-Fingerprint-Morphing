import cv2

def get_center_of_image(img):

  fingerprint_image = img

  # Threshold the image to create a binary image
  _, binary_image = cv2.threshold(fingerprint_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

  # Find the contours of the fingerprint object
  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Find the contour with the largest area (assuming it's the fingerprint object)
  largest_contour = max(contours, key=cv2.contourArea)

  # Find the minimum enclosing circle of the largest contour
  center, radius = cv2.minEnclosingCircle(largest_contour)
  center_x, center_y = map(int, center)

  return center_x, center_y