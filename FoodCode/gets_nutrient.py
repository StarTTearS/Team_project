def get_calorie(food_name):
    calorie_map = {
        "bulgogi": 489,
        "curry": 483,
        "fish": 218,
        "kalguksu": 493,
        "pork_belly": 775.5,
        "trotter": 582,
        "apple": 156,
        "banana": 105.6,
        "grape": 92.4,
        "salad": 16,
        "strawberry": 32,
        "sushi": 456,
        "sweet_potato": 217.6,
        "hotdog": 586,
        "chicken": 2358.5,
        "pizza": 2764.16,
        "egg": 77.5,
        "chicken_fillet": 164,
        "tteokbokki": 535,
        "hambuger": 859.2,
        "kimbap": 485,
        "kimchi_soup": 198,
        "jajangmyeon": 797,
        "jjambbong": 688,
        "sweet_and_sour_pork": 406.6
    }
    return calorie_map.get(food_name.lower(), 0)


def get_carbs(food_name):
    carbs_map = {
        "bulgogi": 15.0,
        "curry": 91.9,
        "fish": 0.56,
        "kalguksu": 95.8,
        "pork_belly": 1.05,
        "trotter": 5.7,
        "apple": 42,
        "banana": 27.6,
        "grape": 23.8,
        "salad": 3.22,
        "strawberry": 8,
        "sushi": 72,
        "sweet_potato": 51.61,
        "hotdog": 72,
        "chicken": 94.785,
        "pizza": 369.6,
        "egg": 0.55,
        "chicken_fillet": 0,
        "tteokbokki": 105,
        "hambuger": 117.3,
        "kimbap": 73.5,
        "kimchi_soup": 12,
        "jajangmyeon": 133,
        "jjambbong": 100,
        "sweet_and_sour_pork": 38.27
    }
    return carbs_map.get(food_name.lower(), 0)


def get_protein(food_name):
    protein_map = {
        "bulgogi": 56.52,
        "curry": 11.6,
        "fish": 45.2,
        "kalguksu": 20.6,
        "pork_belly": 33.83,
        "trotter": 65.1,
        "apple": 0.9,
        "banana": 1.32,
        "grape": 0.84,
        "salad": 1.25,
        "strawberry": 0.7,
        "sushi": 25.2,
        "sweet_potato": 2.9,
        "hotdog": 21.4,
        "chicken": 157.98,
        "pizza": 123.2,
        "egg": 6.5,
        "chicken_fillet": 31,
        "tteokbokki": 13,
        "hambuger": 40.23,
        "kimbap": 12.2,
        "kimchi_soup": 14,
        "jajangmyeon": 20,
        "jjambbong": 30,
        "sweet_and_sour_pork": 22.27
    }
    return protein_map.get(food_name.lower(), 0)


def get_fat(food_name):
    fat_map = {
        "bulgogi": 20.49,
        "curry": 7.8,
        "fish": 2.36,
        "kalguksu": 3.2,
        "pork_belly": 62.55,
        "trotter": 34.8,
        "apple": 0.6,
        "banana": 0.36,
        "grape": 0.56,
        "salad": 0.07,
        "strawberry": 0.3,
        "sushi": 6,
        "sweet_potato": 0.255,
        "hotdog": 24,
        "chicken": 149.965,
        "pizza": 112,
        "egg": 5.5,
        "chicken_fillet": 3.6,
        "tteokbokki": 7,
        "hambuger": 46.93,
        "kimbap": 15.3,
        "kimchi_soup": 11,
        "jajangmyeon": 20,
        "jjambbong": 19,
        "sweet_and_sour_pork": 18.4
    }
    return fat_map.get(food_name.lower(), 0)


def get_sugar(food_name):
    sugar_map = {
        "bulgogi": 7.25,
        "curry": 0.65,
        "fish": 0.16,
        "kalguksu": 1.054,
        "pork_belly": 0.084,
        "trotter": 0.45,
        "apple": 30,
        "banana": 14.4,
        "grape": 22.4,
        "salad": 0.88,
        "strawberry": 4.9,
        "sushi": 15.1,
        "sweet_potato": 12,
        "hotdog": 18.66,
        "chicken": 13.35,
        "pizza": 37.12,
        "egg": 0.55,
        "chicken_fillet": 0,
        "tteokbokki": 14,
        "hambuger": 14.08,
        "kimbap": 6.56,
        "kimchi_soup": 4,
        "jajangmyeon": 39.46,
        "jjambbong": 10.17,
        "sweet_and_sour_pork": 19.08
    }
    return sugar_map.get(food_name.lower(), 0)


def get_sodium(food_name):
    sodium_map = {
        "bulgogi": 582,
        "curry": 855.60,
        "fish": 694,
        "kalguksu": 1630.22,
        "pork_belly": 1210.43,
        "trotter": 515,
        "apple": 3,
        "banana": 1.2,
        "grape": 2.8,
        "salad": 7.2,
        "strawberry": 1,
        "sushi": 969,
        "sweet_potato": 52.7,
        "hotdog": 773.34,
        "chicken": 1721.3,
        "pizza": 6697.6,
        "egg": 62,
        "chicken_fillet": 74,
        "tteokbokki": 1207,
        "hambuger": 1387.89,
        "kimbap": 1250.16,
        "kimchi_soup": 1020,
        "jajangmyeon": 2400,
        "jjambbong": 4000,
        "sweet_and_sour_pork": 628.33
    }
    return sodium_map.get(food_name.lower(), 0)
