import os
import cv2
import random


def bookmark_recommendation(folder_path, bookmark_folder):
    # 각 카테고리의 이미지 수를 저장할 딕셔너리
    max_images_per_category = {}

    # Bookmark 폴더의 각 카테고리에 대해 이미지 수를 확인합니다.
    for category_folder in os.listdir(bookmark_folder):
        category_path = os.path.join(bookmark_folder, category_folder)
        if os.path.isdir(category_path):
            max_images_per_subcategory = 0
            # 각 카테고리의 서브폴더에 대해 이미지 수를 확인합니다.
            for subcategory_folder in os.listdir(category_path):
                subcategory_path = os.path.join(
                    category_path, subcategory_folder)
                if os.path.isdir(subcategory_path):
                    num_images = len([f for f in os.listdir(
                        subcategory_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
                    max_images_per_subcategory = max(
                        max_images_per_subcategory, num_images)
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
            while True:
                if cv2.waitKey(1) == ord('q'):
                    break
            cv2.destroyAllWindows()
            return
    print("이미지를 찾을 수 없습니다.")
