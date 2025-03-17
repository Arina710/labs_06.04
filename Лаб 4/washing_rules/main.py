import json


def load_rules(filename="washing_rules.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def select_wash_mode(rules, clothing_type, color, dirt_level, stains, preference):
    for rule in rules:
        if (rule["type"] in [clothing_type, "любая"] and
                rule["color"] in [color, "любой", "любая"] and
                rule["dirt_level"] in [dirt_level, "любая"] and
                rule["stains"] in [stains, "любая"] and
                rule["preference"] in [preference, "нет", "любая"]):
            return rule["mode"], rule["temperature"]

    return "Обычная стирка", 40


rules = load_rules()

clothing_types = {1: "деликатная", 2: "хлопок", 3: "шерсть", 4: "синтетика"}
colors = {1: "белый", 2: "темный", 3: "любой"}
dirt_levels = {1: "слабая", 2: "сильная", 3: "любая"}
stains_options = {1: "да", 2: "нет"}
preferences = {1: "экономия воды", 2: "быстрая стирка", 3: "нет"}


def get_choice(options, prompt):
    options_str = "  ".join([f"{key}. {value}" for key, value in options.items()])
    print(f"{prompt} ({options_str})")
    choice = int(input("Введите номер: "))
    return options.get(choice, list(options.values())[-1])


clothing_type = get_choice(clothing_types, "Выберите тип одежды")
color = get_choice(colors, "Выберите цвет одежды")
dirt_level = get_choice(dirt_levels, "Выберите степень загрязнения")
stains = get_choice(stains_options, "Есть ли пятна?")
preference = get_choice(preferences, "Выберите предпочтение")

mode, temp = select_wash_mode(rules, clothing_type, color, dirt_level, stains, preference)

print(f"\nРежим стирки: {mode}\nТемпература: {temp}°C")
