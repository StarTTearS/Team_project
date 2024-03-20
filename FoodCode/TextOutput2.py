from warn_good_image import good_image, warning_image  # 경고 이미지 및 격려 이미지 출력 모듈
from display_food_image import display_random_food_image  # 음식 이미지 랜덤 출력 및 음식 정보 출력 모듈
import time


# 삼시세끼 음식 정보 출력
def Output_text_and_image2(folder_path, bookmark_folder, gender):
    total_calorie = 0
    total_carbohydrate = 0
    total_protein = 0
    total_fat = 0
    total_sugar = 0
    total_sodium = 0

    for i in range(0, 3):
        calorie, carbohydrate, protein, fat, sugar, sodium = display_random_food_image(
            folder_path, bookmark_folder)  # 출력된 음식 정보 저장

        total_calorie += calorie
        total_carbohydrate += carbohydrate
        total_protein += protein
        total_fat += fat
        total_sugar += sugar
        total_sodium += sodium

        # 출력
        print(f"\n총 칼로리: {total_calorie:.2f}kcal")
        print(f"총 탄수화물: {total_carbohydrate:.2f}g")
        print(f"총 단백질: {total_protein:.2f}g")
        print(f"총 지방: {total_fat:.2f}g")
        print(f"총 당류: {total_sugar:.2f}g")
        print(f"총 나트륨: {total_sodium:.2f}mg")

    time.sleep(1)
    # 성별에 따른 활동대사량 설정 및 활동대사량을 초과하여 음식 섭취시 경고 문구 및 이미지 출력
    Text_BMR(total_calorie, gender)


def Text_BMR(total_calorie, gender):
    BMR = 2900 if gender == "M" else 2100
    if total_calorie > BMR:
        print("Warning : 너는 지금 뚱뚱해지고 있어. 이 돼지야!!!")
        warning_image()
    else:
        print("적절하게 먹고 있구나. 넌 잘하고 있어.")
        good_image()
