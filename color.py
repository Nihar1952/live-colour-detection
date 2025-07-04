import cv2
import pandas as pd
import numpy as np
from scipy.spatial import KDTree


csv_file = 'colors.csv'
colors_df = pd.read_csv(csv_file, header=None)

# based on the csv present
IDX_NAME = 1
IDX_R = 3
IDX_G = 4
IDX_B = 5

# building a KDTree 
rgb_array = colors_df[[IDX_R, IDX_G, IDX_B]].to_numpy()
color_tree = KDTree(rgb_array)


def nearest_color_name(r_val, g_val, b_val):
    _, idx = color_tree.query([r_val, g_val, b_val])
    name = colors_df.loc[idx, IDX_NAME]
    return name


clicked = False
red = green = blue = x_pos = y_pos = 0
chosen_color_name = ""

# double-click handler
def on_mouse_event(event, x, y, flags, param):
    global red, green, blue, x_pos, y_pos, clicked, chosen_color_name

    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos, y_pos = x, y

       
        b_pixel, g_pixel, r_pixel = frame[y, x]
        red, green, blue = int(r_pixel), int(g_pixel), int(b_pixel)

        
        chosen_color_name = nearest_color_name(red, green, blue)


camera = cv2.VideoCapture(0)
cv2.namedWindow("Live Color Detection")
cv2.setMouseCallback("Live Color Detection", on_mouse_event)

while True:
    success, frame = camera.read()
    if not success:
        print("Couldn't read from camera – is it in use?")
        break

   
    frame = cv2.flip(frame, 1)

    if clicked:
        #showing colour info box near click
        rect_w, rect_h = 250, 60
        x_offset = min(x_pos, frame.shape[1] - rect_w)
        y_offset = min(y_pos, frame.shape[0] - rect_h)

        
        cv2.rectangle(frame, (x_offset, y_offset), (x_offset + rect_w, y_offset + rect_h),
                      (blue, green, red), -1)

      
        brightness = red + green + blue
        font_color = (0, 0, 0) if brightness >= 400 else (255, 255, 255)

        label = f"{chosen_color_name} | R={red} G={green} B={blue}"
        cv2.putText(frame, label, (x_offset + 10, y_offset + 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, font_color, 2, cv2.LINE_AA)

    
    cv2.imshow("Live Color Detection", frame)

    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII code for esc key
        break

# cleanup
camera.release()
cv2.destroyAllWindows()
