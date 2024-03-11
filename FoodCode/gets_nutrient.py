def get_calorie(food_name):
    calorie_map = {
        "chicken": 2121,
        "pizza": 2903,
        "nudle": 740,
        "tang": 813,
        "boiled_egg": 77,
        "chicken_fillet": 164.9,
        "cucumber": 22,
        "tteokbokki": 650,
        "hambuger": 640,
        "kimbap": 500,
        "kimchi_soup": 128,
        "set": 2333
    }
    return calorie_map.get(food_name.lower(), 0)


def get_carbs(food_name):
    carbs_map = {
        "chicken": 122,
        "pizza": 228.64,  # 피자의 탄수화물 정보를 입력하세요
        "nudle": 133,  # 누들의 탄수화물 정보를 입력하세요
        "tang": 76.5,  # 탕의 탄수화물 정보를 입력하세요
        "boiled_egg": 0.56,  # 삶은 계란의 탄수화물 정보를 입력하세요
        "chicken_fillet": 0,  # 치킨 필레의 탄수화물 정보를 입력하세요
        "cucumber": 6,  # 오이의 탄수화물 정보를 입력하세요
        "tteokbokki": 120.84,  # 떡볶이의 탄수화물 정보를 입력하세요
        "hambuger": 52.2,  # 햄버거의 탄수화물 정보를 입력하세요
        "kimbap": 73.5,  # 김밥의 탄수화물 정보를 입력하세요
        "kimchi_soup": 6.38,  # 김치찌개의 탄수화물 정보를 입력하세요
        "set": 342.5  # 세트 메뉴의 탄수화물 정보를 입력하세요
    }
    return carbs_map.get(food_name.lower(), 0)


def get_protein(food_name):
    protein_map = {
        "chicken": 144,
        "pizza": 75.44,  # 피자의 단백질 정보를 입력하세요
        "nudle": 24.395,  # 누들의 단백질 정보를 입력하세요
        "tang": 44.5,  # 탕의 단백질 정보를 입력하세요
        "boiled_egg": 6.26,  # 삶은 계란의 단백질 정보를 입력하세요
        "chicken_fillet": 31,  # 치킨 필레의 단백질 정보를 입력하세요
        "cucumber": 1,  # 오이의 단백질 정보를 입력하세요
        "tteokbokki": 13.94,  # 떡볶이의 단백질 정보를 입력하세요
        "hambuger": 37.00,  # 햄버거의 단백질 정보를 입력하세요
        "kimbap": 12.2,  # 김밥의 단백질 정보를 입력하세요
        "kimchi_soup": 8.17,  # 김치찌개의 단백질 정보를 입력하세요
        "set": 93.29  # 세트 메뉴의 단백질 정보를 입력하세요
    }
    return protein_map.get(food_name.lower(), 0)


def get_fat(food_name):
    fat_map = {
        "chicken": 117,
        "pizza": 90.08,  # 피자의 지방 정보를 입력하세요
        "nudle": 18,  # 누들의 지방 정보를 입력하세요
        "tang": 36.8,  # 탕의 지방 정보를 입력하세요
        "boiled_egg": 5.28,  # 삶은 계란의 지방 정보를 입력하세요
        "chicken_fillet": 3.6,  # 치킨 필레의 지방 정보를 입력하세요
        "cucumber": 0,  # 오이의 지방 정보를 입력하세요
        "tteokbokki": 5.82,  # 떡볶이의 지방 정보를 입력하세요
        "hambuger": 30.48,  # 햄버거의 지방 정보를 입력하세요
        "kimbap": 15.3,  # 김밥의 지방 정보를 입력하세요
        "kimchi_soup": 8.09,  # 김치찌개의 지방 정보를 입력하세요
        "set": 72.8  # 세트 메뉴의 지방 정보를 입력하세요
    }
    return fat_map.get(food_name.lower(), 0)


def get_sugar(food_name):
    sugar_map = {
        "chicken": 58,
        "pizza": 36,  # 피자의 당류 정보를 입력하세요
        "nudle": 22.12,  # 누들의 당류 정보를 입력하세요
        "tang": 38.2,  # 탕의 당류 정보를 입력하세요
        "boiled_egg": 1.1,  # 삶은 계란의 당류 정보를 입력하세요
        "chicken_fillet": 0,  # 치킨 필레의 당류 정보를 입력하세요
        "cucumber": 0,  # 오이의 당류 정보를 입력하세요
        "tteokbokki": 19.4,  # 떡볶이의 당류 정보를 입력하세요
        "hambuger": 9.14,  # 햄버거의 당류 정보를 입력하세요
        "kimbap": 6.75,  # 김밥의 당류 정보를 입력하세요
        "kimchi_soup": 6.9,  # 김치찌개의 당류 정보를 입력하세요
        "set": 82.44  # 세트 메뉴의 당류 정보를 입력하세요
    }
    return sugar_map.get(food_name.lower(), 0)


def get_sodium(food_name):
    sodium_map = {
        "chicken": 0.664,  # 치킨의 나트륨 정보를 입력하세요
        "pizza": 6.43,  # 피자의 나트륨 정보를 입력하세요
        "nudle": 2.4,  # 누들의 나트륨 정보를 입력하세요
        "tang": 1.3,  # 탕의 나트륨 정보를 입력하세요
        "boiled_egg": 0.062,  # 삶은 계란의 나트륨 정보를 입력하세요
        "chicken_fillet": 0.074,  # 치킨 필레의 나트륨 정보를 입력하세요
        "cucumber": 0,  # 오이의 나트륨 정보를 입력하세요
        "tteokbokki": 1.21,  # 떡볶이의 나트륨 정보를 입력하세요
        "hambuger": 0.9,  # 햄버거의 나트륨 정보를 입력하세요
        "kimbap": 0.9,  # 김밥의 나트륨 정보를 입력하세요
        "kimchi_soup": 1.97,  # 김치찌개의 나트륨 정보를 입력하세요
        "set": 6.1  # 세트 메뉴의 나트륨 정보를 입력하세요
    }
    return sodium_map.get(food_name.lower(), 0)
