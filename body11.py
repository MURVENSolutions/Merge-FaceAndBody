import cv2

# Load the face and body images
face = cv2.imread("C:/Users/IT/Downloads/photo1675429675.png")
body = cv2.imread("C:/Users/IT/Downloads/photo1673603078_background_removed.png")

# Create an empty image with the same shape as the body
result = body.copy()

# Get the dimensions of the body image
body_height, body_width, _ = body.shape

# Get the dimensions of the face image
face_height, face_width, _ = face.shape

# Specify the desired position of the face in relation to the body image
offset_x = 20
offset_y = -230

# Calculate the starting coordinates of the ROI
start_x = (body_width - face_width) // 2 + offset_x
start_y = (body_height - face_height) // 2 + offset_y

print("start_x:", start_x)
print("start_y:", start_y)
print("face_width:", face_width)
print("face_height:", face_height)
print("body_width:", body_width)
print("body_height:", body_height)

# Check if the starting position is within the bounds of the body image
if start_x >= 0 and start_y >= 0 and start_x + face_width <= body_width and start_y + face_height <= body_height:
    # Define the ROI as a rectangular region at the specified position on the body image
    roi = result[start_y: start_y+face_height, start_x: start_x+face_width]

    # Use the mask to merge the face with the body
    face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(face_gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    result_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    face_fg = cv2.bitwise_and(face, face, mask=mask)
    result[start_y: start_y+face_height, start_x: start_x+face_width] = cv2.add(result_bg, face_fg)

cv2.imshow("result", result)
cv2.waitKey(0)
