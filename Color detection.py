import cv2
import pandas as pd

# Load image
img = cv2.imread("image.jpg")

# CSV containing color names and RGB values
colors = pd.read_csv(
    "colors.csv",
    names=["Color", "ColorName", "Hex", "R", "G", "B"],
    header=None
)

clicked = False
r = g = b = x_pos = y_pos = 0

def get_color_name(R, G, B):
    minimum = float("inf")
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + \
            abs(G - int(colors.loc[i, "G"])) + \
            abs(B - int(colors.loc[i, "B"]))
        if d < minimum:
            minimum = d
            cname = colors.loc[i, "ColorName"]
    return cname

def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]

cv2.namedWindow("Image Color Detection")
cv2.setMouseCallback("Image Color Detection", draw_function)

while True:
    display = img.copy()

    if clicked:
        cv2.rectangle(display, (20, 20), (750, 60), (int(b), int(g), int(r)), -1)

        text = f"{get_color_name(r, g, b)}  RGB=({r},{g},{b})  HEX=#{int(r):02X}{int(g):02X}{int(b):02X}"

        cv2.putText(display, text, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (255, 255, 255), 2)

    cv2.imshow("Image Color Detection", display)

    if cv2.waitKey(20) & 0xFF == 27:  # Press ESC to exit
        break

cv2.destroyAllWindows()
