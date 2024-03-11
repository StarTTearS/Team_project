import cv2
import os


def find_food(image):
    # Food 폴더 경로 설정
    folder_path = "/home/kyj/Final_Project/Team_project/Food"

    # Food 폴더 안의 서브폴더 목록 가져오기
    food_folders = [f for f in os.listdir(
        folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # ORB 특징점 검출기 생성
    orb = cv2.ORB_create()

    # 입력 이미지의 특징점과 디스크립터 추출
    kp1, des1 = orb.detectAndCompute(image, None)

    for food_folder in food_folders:
        # 음식 폴더 안의 이미지 파일 목록 가져오기
        food_images = [os.path.join(folder_path, food_folder, f) for f in os.listdir(
            os.path.join(folder_path, food_folder)) if f.endswith(('.jpg', '.jpeg', '.png'))]

        for food_image_path in food_images:
            # 음식 이미지 읽기
            food_img = cv2.imread(food_image_path)

            # ORB 특징점과 디스크립터 추출
            kp2, des2 = orb.detectAndCompute(food_img, None)

            # BFMatcher 생성
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)

            # 일치하는 부분 표시
            if len(matches) > 20:  # 임의의 매치 수 기준 설정
                top_left = (0, 0)
                bottom_right = (food_img.shape[1], food_img.shape[0])
                cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
                # 일치하는 음식 이미지 파일명과 음식 폴더명 반환
                return image, os.path.basename(food_image_path), food_folder

    return image, None, None


def main():
    cap = cv2.VideoCapture(0)  # 카메라 캡처
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # 입력 이미지에서 음식 찾기
        processed_frame, food_name, food_folder = find_food(frame)

        # 음식이 있는 경우 음식 이름과 음식 폴더 출력
        if food_name:
            cv2.putText(processed_frame, food_name, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(processed_frame, f"Food Category: {food_folder}", (
                50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 이미지 출력
        cv2.imshow('Food Recognition', processed_frame)

        # 'q' 키를 누를 때까지 대기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
