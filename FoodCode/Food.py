from Speech_recognition import recognize_speech  # 음성인식 모듈
from TextOutput import Output_text_and_image   # 텍스트 입력 모드(단일 추천) 및 출력 모듈
from TextOutput2 import Output_text_and_image2   # 텍스트 입력 모드(삼시세끼 추천) 및 출력 모듈
from VoiceOutput import Output_voice_and_image  # 음싱 인식 모드 및 출력 모듈
from bookmark import bookmark_recommendation  # 북마크 추천 모드 모듈
from Category import display_random_image_in_category  # 카테고리 선택 기능 모듈
import time  # 딜레이를 위한 모듈
import os  # demo.py를 실행하기 위한 모듈


def main():
    global gender  # 성별 선택을 위한 글로별 변수

    folder_path = "/home/kyj/Final_Project/Team_project/Food"  # 음식 사진 데이터 경로
    bookmark_folder = "/home/kyj/Final_Project/Team_project/Bookmark"  # 추천된 음식이 저장되는 경로
    while True:  # 다양한 기능 및 모드 선택
        mode_input = input(
            "\nMode를 선택하시오. t = 텍스트 입력 모드, v = 음성 인식 모드, s = Camera 캡쳐 모드, b = 북마크 추천 기능, c = 카테고리 선택 기능, e = 종료 :")
        if mode_input == 't':  # 텍스트 입력 모드
            gender = input("Gender M/F Selection : ").upper()  # 성별 선택
            text_mode_input = input("1 = 단일 음식 추천, 2 = 삼시세끼 음식 추천 : ")
            if text_mode_input == '1':
                # TextOutput 모듈의 Output_text_and_image 함수
                Output_text_and_image(folder_path, bookmark_folder, gender)
            else:  # TextOutput2 모듈의 Output_text_and_image2 함수
                Output_text_and_image2(folder_path, bookmark_folder, gender)
        elif mode_input == 'v':  # 음성 인식 모드
            print("성별을 입력하세요(남자, 여자):")
            time.sleep(2)
            gender = recognize_speech()  # Speech_recognition 모듈의 recognize_speech() 사용. 음성 인식
            print(f"speech : {gender}")
            # VoiceOutput 모듈의 Output_voice_and_image 함수
            Output_voice_and_image(folder_path, bookmark_folder, gender)
        elif mode_input == 'b':  # 북마크 기능
            # bookmark 모듈의 bookmark_recommendation 함수
            bookmark_recommendation(folder_path, bookmark_folder)
        elif mode_input == 'c':  # 카테고리 선택 기능
            print("출력할 카테고리를 입력하세요")
            category_name = input(
                "KoreanFood, ChineseFood, HealthFood, FastFood : ")
            display_random_image_in_category(
                folder_path, category_name, bookmark_folder)  # Category 모듈의 display_random_image_in_category 함수
        elif mode_input == 's':  # 카메라 인식 모드
            os.system(
                "python3 ./openvino/python/demo.py -i 0")  # 카메라 인식 모드 실행 명령어

        elif mode_input == 'e':  # 종료
            break
        else:
            print("잘못된 모드 입력입니다.")


if __name__ == "__main__":
    main()
