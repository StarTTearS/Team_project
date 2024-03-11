import os
import cv2
import random
from gets_nutrient import get_calorie, get_carbs, get_fat, get_protein, get_sugar, get_sodium


def display_random_image_in_category(folder_path, category_name, bookmark_folder):
    # 카테고리 폴더 경로 설정
    category_path = os.path.join(folder_path, category_name)
    # 카테고리 폴더가 존재하지 않을 경우 오류 메시지 출력 후 종료
    if not os.path.isdir(category_path):
        print(f"카테고리 '{category_name}'를 찾을 수 없습니다.")
        return

    # 카테고리 폴더 내의 서브폴더 목록 가져오기
    subfolders = [f for f in os.listdir(
        category_path) if os.path.isdir(os.path.join(category_path, f))]
    # 서브폴더가 없을 경우 오류 메시지 출력 후 종료
    if not subfolders:
        print(f"카테고리 '{category_name}'에 하위 폴더가 없습니다.")
        return

    # 랜덤하게 서브폴더 선택
    subfolder_name = random.choice(subfolders)
    # 선택된 서브폴더의 경로 설정
    subfolder_path = os.path.join(category_path, subfolder_name)
    # 서브폴더 내의 이미지 파일 목록 가져오기
    image_files = [f for f in os.listdir(
        subfolder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    # 이미지 파일이 없을 경우 오류 메시지 출력 후 종료
    if not image_files:
        print(f"하위 폴더 '{subfolder_name}'에 이미지 파일이 없습니다.")
        return

    # 랜덤하게 이미지 선택
    random_image_file = random.choice(image_files)
    # 선택된 이미지 파일의 전체 경로 설정
    image_path = os.path.join(subfolder_path, random_image_file)
    # 이미지 파일 읽기
    image = cv2.imread(image_path)
    # 이미지 크기 조정
    image = cv2.resize(image, (800, 740))

    # 음식 이름과 칼로리
    food_name = subfolder_name
    calorie = get_calorie(food_name)

    # 탄수화물, 단백질, 지방, 당류 정보
    carbs = get_carbs(food_name)
    protein = get_protein(food_name)
    fat = get_fat(food_name)
    sugar = get_sugar(food_name)
    sodium = get_sodium(food_name)

    # 텍스트를 이미지 위에 출력
    text1 = f"{food_name}, Calorie = {calorie}"
    text2 = f"Carbohydrate : {carbs}g, Protein : {protein}g"
    text3 = f"Fat : {fat}g, Sugars : {sugar}g"
    text4 = f"Natrium : {sodium}g"

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2

    text_size1 = cv2.getTextSize(text1, font, font_scale, font_thickness)[0]
    text_x1 = (image.shape[1] - text_size1[0]) // 2
    text_y1 = text_size1[1] + 20
    text_org1 = (text_x1, text_y1)

    text_size2 = cv2.getTextSize(text2, font, font_scale, font_thickness)[0]
    text_x2 = (image.shape[1] - text_size2[0]) // 2
    text_y2 = text_y1 + text_size2[1] + 20
    text_org2 = (text_x2, text_y2)

    text_size3 = cv2.getTextSize(text3, font, font_scale, font_thickness)[0]
    text_x3 = (image.shape[1] - text_size3[0]) // 2
    text_y3 = text_y2 + text_size3[1] + 20
    text_org3 = (text_x3, text_y3)

    text_size4 = cv2.getTextSize(text4, font, font_scale, font_thickness)[0]
    text_x4 = (image.shape[1] - text_size4[0]) // 2
    text_y4 = text_y3 + text_size4[1] + 20
    text_org4 = (text_x4, text_y4)

    text_color = (59, 50, 255)  # 흰색

    # 이미지에 텍스트 추가
    cv2.putText(image, text1, text_org1, font,
                font_scale, text_color, font_thickness)
    cv2.putText(image, text2, text_org2, font,
                font_scale, text_color, font_thickness)
    cv2.putText(image, text3, text_org3, font,
                font_scale, text_color, font_thickness)
    cv2.putText(image, text4, text_org4, font,
                font_scale, text_color, font_thickness)

    # 이미지 출력
    cv2.imshow("Random Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 이미지를 bookmark_folder에 저장
    save_folder = os.path.join(bookmark_folder, category_name, subfolder_name)
    os.makedirs(save_folder, exist_ok=True)
    save_path = os.path.join(save_folder, random_image_file)
    cv2.imwrite(save_path, image)
