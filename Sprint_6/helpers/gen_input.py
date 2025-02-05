from faker import Faker
import random


class DataGenerator:
    def __init__(self):
        self.fake = Faker('ru_RU')

    def generate_first_name(self):
        """Генерация имени"""
        return self.fake.first_name()

    def generate_last_name(self):
        """Генерация фамилии"""
        return self.fake.last_name()

    def generate_address(self):
        """Генерация адреса в формате 'к. Обнинск, ш. Льва Толстого, д. 2 стр. 80'"""
        streets = ["Льва Толстого", "Пушкина", "Тверская", "Мира"]
        return f"к. Обнинск, ш. {random.choice(streets)}, д. {random.randint(1, 100)} стр. {random.randint(1, 100)}"

    def generate_metro_station(self):
        """Генерация случайной станции метро"""
        metro_stations = [
            "Комсомольская", "Таганская", "Пушкинская",
            "Белорусская", "Смоленская", "Киевская",
            "Арбатская", "Новокузнецкая"]
        return random.choice(metro_stations)

    def generate_phone_number(self):
        """Генерация номера телефона в формате +79157201120"""
        return f"+7915{random.randint(1000000, 9999999)}"

    @staticmethod
    def get_date_plus_days(days: int = 0):
        """Возвращает дату через указанное количество дней в формате, соответствующем проекту."""
        from datetime import datetime, timedelta
        target_date = datetime.now() + timedelta(days=days)
        return target_date.strftime('%d.%m.%Y')

