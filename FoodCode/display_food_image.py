import cv2
import random
import os
from gets_nutrient import get_calorie, get_carbs, get_fat, get_protein, get_sugar, get_sodium


def display_random_food_image(folder_path, bookmark_folder):
    # Food 폴더 안의 서브폴더 목록 가져오기
    subfolders = [f for f in os.listdir(
        folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # 서브폴더가 없을 경우 에러 출력 후 종료
    if not subfolders:
        print("Error: No subfolders found in the 'Food' folder.")
        return

    # 랜덤하게 카테고리 선택
    random_category = random.choice(subfolders)
    category_path = os.path.join(folder_path, random_category)

    # 선택한 카테고리 안의 서브폴더 목록 가져오기
    sub_subfolders = [f for f in os.listdir(
        category_path) if os.path.isdir(os.path.join(category_path, f))]

    # 서브폴더가 없을 경우 에러 출력 후 종료
    if not sub_subfolders:
        print(
            f"Error: No subfolders found in the '{random_category}' category folder.")
        return

    # 랜덤하게 서브폴더 선택
    random_subfolder = random.choice(sub_subfolders)

    # 선택한 서브폴더 안의 이미지 파일 목록 가져오기
    subfolder_path = os.path.join(category_path, random_subfolder)
    image_files = [f for f in os.listdir(
        subfolder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # 이미지 파일이 없을 경우 에러 출력 후 종료
    if not image_files:
        print(
            f"Error: No image files found in the '{random_subfolder}' folder.")
        return

    # 랜덤하게 이미지 파일 선택
    random_image = random.choice(image_files)

    # 선택한 이미지 파일 경로의 전체 경로를 만듬
    image_path = os.path.join(subfolder_path, random_image)

    # 이미지 파일 읽기
    image = cv2.imread(image_path)
    image = cv2.resize(image, (840, 740))

    # 음식 이름과 칼로리
    food_name = random_subfolder
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
    cv2.imshow("Today's Food", image)

    # 해당하는 음식 폴더에 이미지 저장
    save_folder = os.path.join(
        bookmark_folder, random_category, random_subfolder)
    os.makedirs(save_folder, exist_ok=True)
    save_path = os.path.join(save_folder, random_image)
    cv2.imwrite(save_path, image)

    while True:
        if cv2.waitKey(1) == ord('q'):
            break

    # 이미지 창 닫기
    cv2.destroyAllWindows()

    return calorie, carbs, protein, fat, sugar, sodium
