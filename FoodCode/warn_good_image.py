import cv2
from Siren import Warning_Output, Good_Output


def warning_image():
    warn_path = "/home/kyj/Final_Project/Team_project/warning.png"
    warn = cv2.imread(warn_path)
    warn = cv2.resize(warn, (800, 700))

    text1 = "Stop Eating! Fire Pig!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_thickness = 2

    text_size1 = cv2.getTextSize(text1, font, font_scale, font_thickness)[0]
    text_x1 = (warn.shape[1] - text_size1[0]) // 2
    text_y1 = text_size1[1] + 20
    text_org1 = (text_x1, text_y1)

    text_color = (255, 255, 255)

    cv2.putText(warn, text1, text_org1, font,
                font_scale, text_color, font_thickness)

    cv2.imshow("Stop Eating! Fire Pig!", warn)

    # 이미지를 (x, y) 좌표에 표시
    x = 1200
    y = 300
    cv2.moveWindow('Stop Eating! Fire Pig!', x, y)

    while True:
        if cv2.waitKey(1) == ord('q'):
            Warning_Output()
            break
    cv2.destroyAllWindows()


def good_image():
    good_path = "/home/kyj/Final_Project/Team_project/good.png"
    good = cv2.imread(good_path)
    good = cv2.resize(good, (640, 800))

    text1 = "Good Job!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_thickness = 3

    text_size1 = cv2.getTextSize(text1, font, font_scale, font_thickness)[0]
    text_x1 = (good.shape[1] - text_size1[0]) // 2
    text_y1 = text_size1[1] + 20
    text_org1 = (text_x1, text_y1)

    text_color = (60, 255, 125)

    cv2.putText(good, text1, text_org1, font,
                font_scale, text_color, font_thickness)

    cv2.imshow("You are very Good!", good)

    # 이미지를 (x, y) 좌표에 표시
    x = 1200
    y = 300
    cv2.moveWindow('You are very Good!', x, y)

    while True:
        if cv2.waitKey(1) == ord('q'):
            Good_Output()
            break
    cv2.destroyAllWindows()
