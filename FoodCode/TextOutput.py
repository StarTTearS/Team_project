from warn_good_image import good_image, warning_image
from display_food_image import display_random_food_image
import time


def Output_text_and_image(folder_path, bookmark_folder, gender):
    total_calorie = 0
    total_carbohydrate = 0
    total_protein = 0
    total_fat = 0
    total_sugar = 0
    total_sodium = 0

    number_input = int(input("1 = 오늘의 음식 추천, 2 = 아침, 점심, 저녁 메뉴 추천 :"))
    print()
    if number_input == 1:
        total_calorie, total_carbohydrate, total_protein, total_fat, total_sugar, total_sodium = display_random_food_image(
            folder_path, bookmark_folder)

        print(f"총 칼로리 : {total_calorie}kcal")
        print(f"총 탄수화물 : {total_carbohydrate}g")
        print(f"총 단백질 : {total_protein}g")
        print(f"총 지방 : {total_fat}g")
        print(f"총 당류 : {total_sugar}g")
        print(f"총 나트륨 : {total_sodium}mg")

    elif number_input == 2:
        while True:
            user_input = input("입력 = ")
            if user_input == "more":
                calorie, carbohydrate, protein, fat, sugar, sodium = display_random_food_image(
                    folder_path, bookmark_folder)

                total_calorie += calorie
                total_carbohydrate += carbohydrate
                total_protein += protein
                total_fat += fat
                total_sugar += sugar
                total_sodium += sodium

                print(f"총 칼로리: {total_calorie:.2f}kcal")
                print(f"총 탄수화물: {total_carbohydrate:.2f}g")
                print(f"총 단백질: {total_protein:.2f}g")
                print(f"총 지방: {total_fat:.2f}g")
                print(f"총 당류: {total_sugar:.2f}g")
                print(f"총 나트륨: {total_sodium:.2f}mg")
            elif user_input == "exit":
                break
            else:
                print("잘못된 입력입니다.")

    time.sleep(1)
    Text_BMR(total_calorie, gender)


def Text_BMR(total_calorie, gender):
    BMR = 2300 if gender == "M" else 1800
    if total_calorie > BMR:
        print(f"\n성별 : {gender}\n")
        print("Warning : 너는 지금 뚱뚱해지고 있어. 이 돼지야!!!")
        warning_image()
    else:
        print(f"\n성별 : {gender}\n")
        print("적절하게 먹고 있구나. 넌 잘하고 있어.")
        good_image()
