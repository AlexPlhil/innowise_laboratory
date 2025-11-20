#функция определения возрастной категории
def generate_profile(age: int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

# Для ввода имени
user_name = input("Enter your full name: ")

# Для ввода года рождения
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

# Определение текущего возраста
current_age = 2025 - birth_year

# Определение возрастной категории
life_stage = generate_profile(current_age)

# Определение, какие хобби у человека
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()

    if hobby.lower() == "stop":
        break

    if hobby:
        hobbies.append(hobby)

# Словарь, который хранит информацию о персоне

user_profile = {
    "name": user_name,
    "age": current_age,
    "birth_year": birth_year,
    "life_stage": life_stage,
    "hobbies": hobbies
}

# Вывод информации

print("\n----- USER PROFILE -----")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")

# Информация по хобби

if not hobbies:
    print("\nYou didn't mention any hobbies.")
else:
    print(f"\nFavorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")