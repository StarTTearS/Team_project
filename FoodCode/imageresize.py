import os
import cv2


def resize_images(input_folder, output_folder, width=640, height=480):
    # 출력 폴더가 존재하지 않는 경우 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 입력 폴더의 모든 이미지 파일에 대해 반복
    for filename in os.listdir(input_folder):
        # 이미지 파일인 경우에만 처리
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
            # 이미지 파일 경로
            input_path = os.path.join(input_folder, filename)
            # 이미지를 읽어옴
            image = cv2.imread(input_path)
            # 이미지가 None이 아닌 경우에만 처리
            if image is not None:
                # 이미지 크기를 조정
                resized_image = cv2.resize(image, (width, height))
                # 새로운 파일 경로 및 이름
                output_path = os.path.join(output_folder, filename)
                # 이미지 저장
                cv2.imwrite(output_path, resized_image)
                print(f"{filename} resized and saved.")


# 입력 폴더 및 출력 폴더 경로
input_folder = "/home/kyj/Foodimage/images"
output_folder = "/home/kyj/Foodimage/Writeimage"

# 이미지 크기 조정
resize_images(input_folder, output_folder)
