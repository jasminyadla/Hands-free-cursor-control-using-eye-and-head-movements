# import numpy as np


# # Returns EAR given eye landmarks
# def eye_aspect_ratio(eye):
#     # Compute the euclidean distances between the two sets of
#     # vertical eye landmarks (x, y)-coordinates
#     A = np.linalg.norm(eye[1] - eye[5])
#     B = np.linalg.norm(eye[2] - eye[4])

#     # Compute the euclidean distance between the horizontal
#     # eye landmark (x, y)-coordinates
#     C = np.linalg.norm(eye[0] - eye[3])

#     # Compute the eye aspect ratio
#     ear = (A + B) / (2.0 * C)

#     # Return the eye aspect ratio
#     return ear


# # Returns MAR given eye landmarks
# def mouth_aspect_ratio(mouth):
#     # Compute the euclidean distances between the three sets
#     # of vertical mouth landmarks (x, y)-coordinates
#     A = np.linalg.norm(mouth[13] - mouth[19])
#     B = np.linalg.norm(mouth[14] - mouth[18])
#     C = np.linalg.norm(mouth[15] - mouth[17])

#     # Compute the euclidean distance between the horizontal
#     # mouth landmarks (x, y)-coordinates
#     D = np.linalg.norm(mouth[12] - mouth[16])

#     # Compute the mouth aspect ratio
#     mar = (A + B + C) / (2 * D)

#     # Return the mouth aspect ratio
#     return mar


# # Return direction given the nose and anchor points.
# def direction(nose_point, anchor_point, w, h, multiple=1):
#     nx, ny = nose_point
#     x, y = anchor_point

#     if nx > x + multiple * w:
#         return 'right'
#     elif nx < x - multiple * w:
#         return 'left'

#     if ny > y + multiple * h:
#         return 'down'
#     elif ny < y - multiple * h:
#         return 'up'

#     return 'none'






import numpy as np

# Returns EAR given eye landmarks
def eye_aspect_ratio(eye):
    # Compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # Compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = np.linalg.norm(eye[0] - eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # Return the eye aspect ratio
    return ear

# Returns MAR given mouth landmarks
def mouth_aspect_ratio(mouth):
    # Compute the euclidean distances between the three sets
    # of vertical mouth landmarks (x, y)-coordinates
    A = np.linalg.norm(mouth[13] - mouth[19])
    B = np.linalg.norm(mouth[14] - mouth[18])
    C = np.linalg.norm(mouth[15] - mouth[17])

    # Compute the euclidean distance between the horizontal
    # mouth landmarks (x, y)-coordinates
    D = np.linalg.norm(mouth[12] - mouth[16])

    # Compute the mouth aspect ratio
    mar = (A + B + C) / (2 * D)

    # Return the mouth aspect ratio
    return mar

# Return direction given the nose and anchor points.
def direction(nose_point, anchor_point, w, h, multiple=1):
    nx, ny = nose_point
    x, y = anchor_point

    if nx > x + multiple * w:
        return 'right'
    elif nx < x - multiple * w:
        return 'left'

    if ny > y + multiple * h:
        return 'down'
    elif ny < y - multiple * h:
        return 'up'

    return 'none'





# import numpy as np
# import cv2

# # Returns EAR given eye landmarks
# def eye_aspect_ratio(eye):
#     # Compute the euclidean distances between the two sets of
#     # vertical eye landmarks (x, y)-coordinates
#     A = np.linalg.norm(eye[1] - eye[5])
#     B = np.linalg.norm(eye[2] - eye[4])

#     # Compute the euclidean distance between the horizontal
#     # eye landmark (x, y)-coordinates
#     C = np.linalg.norm(eye[0] - eye[3])

#     # Compute the eye aspect ratio
#     ear = (A + B) / (2.0 * C)

#     # Return the eye aspect ratio
#     return ear

# # Returns MAR given eye landmarks
# def mouth_aspect_ratio(mouth):
#     # Compute the euclidean distances between the three sets
#     # of vertical mouth landmarks (x, y)-coordinates
#     A = np.linalg.norm(mouth[13] - mouth[19])
#     B = np.linalg.norm(mouth[14] - mouth[18])
#     C = np.linalg.norm(mouth[15] - mouth[17])

#     # Compute the euclidean distance between the horizontal
#     # mouth landmarks (x, y)-coordinates
#     D = np.linalg.norm(mouth[12] - mouth[16])

#     # Compute the mouth aspect ratio
#     mar = (A + B + C) / (2 * D)

#     # Return the mouth aspect ratio
#     return mar

# # Returns the center of the eye
# def eye_center(eye):
#     M = cv2.moments(eye)
#     if M["m00"] != 0:
#         center_x = int(M["m10"] / M["m00"])
#         center_y = int(M["m01"] / M["m00"])
#     else:
#         center_x, center_y = 0, 0
#     return (center_x, center_y)
