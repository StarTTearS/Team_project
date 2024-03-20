import os  # 파일 및 폴더 경로 처리를 위해 사용
import cv2
import random  # random 기능 사용


def bookmark_recommendation(folder_path, bookmark_folder):  # 북마크(즐겨찾기) 기능
    # 각 카테고리의 이미지 수를 저장할 딕셔너리
    max_images_per_category = {}

    # Bookmark 폴더의 각 카테고리에 대해 이미지 수를 확인합니다.
    # os.listdir = 주어진 폴더(디렉토리) 내에 존재하는 모든 파일 및 하위 디렉토리 목록을 리스트 형식으로 반환
    # category_folder: 북마크 폴더 내의 각 카테고리 폴더의 이름을 나타내는 변수
    for category_folder in os.listdir(bookmark_folder):

        # os.path.join = 여려 개의 경로를 결합하여 하나의 유효한 파일 또는 폴더 경로를 생성
        # category_path: 각 카테고리 폴더의 전체 경로를 나타내는 변수
        category_path = os.path.join(bookmark_folder, category_folder)

        if os.path.isdir(category_path):  # 주어진 경로가 폴더(디렉토리)인지를 확인
            max_images_per_subcategory = 0  # 초기화

            # 각 카테고리의 서브폴더에 대해 이미지 수를 확인합니다.
            # subcategory_folder: 각 카테고리 내의 서브 카테고리 폴더의 이름을 나타내는 변수
            # subcategory_path: 각 서브 카테고리 폴더의 전체 경로를 나타내는 변수
            for subcategory_folder in os.listdir(category_path):
                subcategory_path = os.path.join(
                    category_path, subcategory_folder)

                if os.path.isdir(subcategory_path):
                    # len() = 주어진 리스트나 문자열의 요소(element) 수를 반환
                    # 리스트 컴프리헨션 = 간결하게 리스트를 생성하는 방법.
                    # subcategory_path에 있는 파일 중 확장자가 아래의 3개로 끝나는 파일 목록을 생성
                    # num_images: 각 서브 카테고리 폴더 내의 이미지 수를 저장하는 변수
                    num_images = len([f for f in os.listdir(
                        subcategory_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
                    max_images_per_subcategory = max(
                        max_images_per_subcategory, num_images)

            # max_images_per_category[category_folder]
            # 각 카테고리에서 가장 많은 이미지 수를 추적하는 딕셔너리. 카테고리 폴더 이름을 키(key)로 사용
            # 해당 카테고리의 서브 카테고리에서 가장 많은 이미지 수를 값으로 사용
            # max_images_per_subcategory: 각 서브 카테고리에서 가장 많은 이미지 수를 추적하는 변수
            max_images_per_category[category_folder] = max_images_per_subcategory

    # 가장 많은 이미지를 가진 카테고리를 선택합니다.
    max_category = max(max_images_per_category,
                       key=max_images_per_category.get)
    print(f"가장 많은 이미지를 가진 카테고리: {max_category}")

    # 선택된 카테고리의 이미지를 가장 많이 가진 서브폴더를 선택합니다.
    max_category_path = os.path.join(bookmark_folder, max_category)
    subcategory_folders = [f for f in os.listdir(
        max_category_path) if os.path.isdir(os.path.join(max_category_path, f))]
    if subcategory_folders:
        max_images_folders = [folder for folder in subcategory_folders if len([f for f in os.listdir(os.path.join(
            max_category_path, folder)) if f.endswith(('.jpg', '.jpeg', '.png'))]) == max(max_images_per_category.values())]
        max_images_folder = random.choice(max_images_folders)
        max_images_path = os.path.join(max_category_path, max_images_folder)
        image_files = [f for f in os.listdir(
            max_images_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
        if image_files:
            random_image_file = random.choice(image_files)
            random_image_path = os.path.join(
                max_images_path, random_image_file)
            random_image = cv2.imread(random_image_path)
            cv2.imshow("Random Image", random_image)

            # 이미지를 (x, y) 좌표에 표시
            x = 1200
            y = 300
            cv2.moveWindow('Random Image', x, y)

            while True:
                if cv2.waitKey(1) == ord('q'):
                    break
            cv2.destroyAllWindows()
            return
    print("이미지를 찾을 수 없습니다.")
