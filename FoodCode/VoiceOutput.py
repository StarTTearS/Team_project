from warn_good_image import good_image, warning_image  # 경고 이미지 및 격려 이미지 출력 모듈
from Speech_recognition import recognize_speech     # 음성 인식 모듈
from display_food_image import display_random_food_image  # 음식 이미지 랜덤 출력 및 음식 정보 출력 모듈
import time

# 음식 정보 출력 (단일 음식 및 삼시세끼)


def Output_voice_and_image(folder_path, bookmark_folder, gender):
    total_calorie = 0
    total_carbohydrate = 0
    total_protein = 0
    total_fat = 0
    total_sugar = 0
    total_sodium = 0

    print("추천 = 오늘의 음식 추천, 일정 = 아침, 점심, 저녁 메뉴 추천 : ", end='')
    time.sleep(2)
    number_input = recognize_speech()  # 음성 인식
    print(f"speech : {number_input}")

    if number_input == '추천':  # 단일 음식 추천 및 음식 정보 출력
        total_calorie, total_carbohydrate, total_protein, total_fat, total_sugar, total_sodium = display_random_food_image(
            folder_path, bookmark_folder)

        print(f"총 칼로리 : {total_calorie:.2f}kcal")
        print(f"총 탄수화물 : {total_carbohydrate:.2f}g")
        print(f"총 단백질 : {total_protein:.2f}g")
        print(f"총 지방 : {total_fat:.2f}g")
        print(f"총 당류 : {total_sugar:.2f}g")
        print(f"총 나트륨 : {total_sodium:.2f}mg")

    elif number_input == '일정':  # 삼시세끼 음식 추천 및 음식 정보 출력
        for i in range(0, 3):
            calorie, carbohydrate, protein, fat, sugar, sodium = display_random_food_image(
                folder_path, bookmark_folder)

            total_calorie += calorie
            total_carbohydrate += carbohydrate
            total_protein += protein
            total_fat += fat
            total_sugar += sugar
            total_sodium += sodium

            print(f"총 칼로리 : {total_calorie:.2f}kcal")
            print(f"총 탄수화물 : {total_carbohydrate:.2f}g")
            print(f"총 단백질 : {total_protein:.2f}g")
            print(f"총 지방 : {total_fat:.2f}g")
            print(f"총 당류 : {total_sugar:.2f}g")
            print(f"총 나트륨 : {total_sodium:.2f}mg")

    time.sleep(1)
    Voice_BMR(total_calorie, gender)


def Voice_BMR(total_calorie, gender):
    BMR = 2900 if gender == "남자" else 2100
    if total_calorie > BMR:
        print(f"\n성별 : {gender}\n")
        print("Warning : 너는 지금 뚱뚱해지고 있어. 이 돼지야!!!")
        warning_image()
    else:
        print(f"\n성별 : {gender}\n")
        print("적절하게 먹고 있구나. 넌 잘하고 있어.")
        good_image()
