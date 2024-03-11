import os
import random
import cv2
import speech_recognition as sr


def recognize_speech():
    # 음성 인식 객체 생성
    recognizer = sr.Recognizer()

    # 마이크에서 음성을 수집
    with sr.Microphone() as source:
        print("음성을 입력하세요...")
        recognizer.adjust_for_ambient_noise(source)  # 주변 소음 조절
        audio = recognizer.listen(source, timeout=2)
    while True:
        try:
            # 음성을 텍스트로 변환하여 반환
            text = recognizer.recognize_google(audio, language='ko-KR')
            return text
            break
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
            return ""
        except sr.RequestError as e:
            print("Google Speech Recognition 서비스에 접근할 수 없습니다; {0}".format(e))
            return ""


def display_food_image(food_name, folder_path):
    # Food 폴더 안의 이미지 파일 목록 가져오기
    subfolders = [f for f in os.listdir(
        folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # 입력된 음식명과 일치하는 서브폴더 찾기
    matching_subfolder = [
        subfolder for subfolder in subfolders if food_name.lower() in subfolder.lower()]

    if not matching_subfolder:
        print("해당하는 음식 이미지를 찾을 수 없습니다.")
        return

    # 선택한 서브폴더 안의 이미지 파일 목록 가져오기
    subfolder_path = os.path.join(folder_path, matching_subfolder[0])
    image_files = [f for f in os.listdir(
        subfolder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print("해당하는 음식 이미지를 찾을 수 없습니다.")
        return

    # 랜덤하게 음식 이미지 선택
    random_food_image = random.choice(image_files)

    # 선택한 이미지 파일 경로
    image_path = os.path.join(subfolder_path, random_food_image)

    # 이미지 파일 읽기
    image = cv2.imread(image_path)
    image = cv2.resize(image, (640, 480))

    # 이미지 출력
    cv2.imshow("Food Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    global folder_path
    folder_path = "/home/kyj/Final_Project/Team_project/Food"  # 음식 이미지가 있는 디렉토리 경로
    user_input = recognize_speech()

    if user_input:
        print("입력된 텍스트:", user_input)
        display_food_image(user_input, folder_path)


if __name__ == "__main__":
    main()
