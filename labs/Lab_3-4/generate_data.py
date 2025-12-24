import json
import random
import os


def generate_vacancies(n=100):
    professions = [
        'Программист Python', 'Программист Java', 'Программист C#',
        'Программист JavaScript', 'Программист C++', 'Программист PHP',
        'Программист Go', 'Программист Ruby'
    ]

    cities = ['Москва', 'СПб', 'Екатеринбург', 'Казань']
    companies = ['Яндекс', 'Сбер', 'Тинькофф', 'VK']

    data = []
    for i in range(n):
        profession = random.choice(professions) if random.random() > 0.1 else None
        vacancy = {
            'id': i + 1,
            'profession': profession,
            'town': random.choice(cities),
            'company': random.choice(companies)
        }
        data.append(vacancy)
    return data


if __name__ == '__main__':
    vacancies = generate_vacancies(100)

    with open('data_light.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies, f, ensure_ascii=False, indent=2)

    print("✅ Lab_3-4/data_light.json создан!")
    print(f"📊 Вакансий: {len(vacancies)}")
    print("\n🚀 Запуск: python test_all.py")
