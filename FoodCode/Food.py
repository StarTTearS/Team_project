from Speech_recognition import recognize_speech
from TextOutput import Output_text_and_image
from VoiceOutput import Output_voice_and_image
from bookmark import bookmark_recommendation
from Category import display_random_image_in_category
import time
import os


def main():
    global gender

    folder_path = "/home/kyj/Final_Project/Team_project/Food"
    bookmark_folder = "/home/kyj/Final_Project/Team_project/Bookmark"
    while True:
        mode_input = input(
            "\nMode를 선택하시오. t = 텍스트 입력 모드, v = 음성 인식 모드, s = Camera 캡쳐 모드, b = 북마크 추천 기능, c = 카테고리 선택 기능, e = 종료 :")
        if mode_input == 't':
            gender = input("Gender M/F Selection : ").upper()
            Output_text_and_image(folder_path, bookmark_folder, gender)
        elif mode_input == 'v':
            print("성별을 입력하세요(남자, 여자):")
            time.sleep(2)
            gender = recognize_speech()
            print(f"speech : {gender}")
            Output_voice_and_image(folder_path, bookmark_folder, gender)
        elif mode_input == 'b':
            bookmark_recommendation(folder_path, bookmark_folder)
        elif mode_input == 'c':
            print("출력할 카테고리를 입력하세요")
            category_name = input(
                "KoreanFood, ChineseFood, HealthFood, FastFood : ")
            display_random_image_in_category(
                folder_path, category_name, bookmark_folder)
        elif mode_input == 's':
            os.system(
                "python3 ./openvino/python/demo.py -i 0")

        elif mode_input == 'e':
            break
        else:
            print("잘못된 모드 입력입니다.")


if __name__ == "__main__":
    main()
