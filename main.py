import json
import re


class Validator:
    """
    Класс Валидатор
    """
    def __init__(self, records):
        self.records = records
        self.dict_errors = {"email": 0, "height": 0, "snils": 0, "passport": 0, "university": 0, "work_experience": 0, "political_views": 0, "worldview": 0, "address": 0}
        self.valid_count = 0
        self.invalid_count = 0

    def validate(self):
        pass

    def validate_email(self,email : str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        else:
            self.dict_errors["email"] += 1
            return False

    def validate_height(self, height: str) -> bool:
        pattern = "\d{.}\d\d"
        if re.match(pattern, height):
            return True
        else:
            self.dict_errors["height"] += 1
            return False

    def validate_snils(self, snils: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, snils):
            return True
        else:
            self.dict_errors["snils"] += 1
            return False

    def validate_passport(self, passport: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, passport):
            return True
        else:
            self.dict_errors["passport"] += 1
            return False

    def validate_university(self, university: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, university):
            return True
        else:
            self.dict_errors["university"] += 1
            return False

    def validate_work_experience(self, work_experience: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, work_experience):
            return True
        else:
            self.dict_errors["work_experience"] += 1
            return False

    def validate_political_views(self, political_views: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, political_views):
            return True
        else:
            self.dict_errors["political_views"] += 1
            return False

    def validate_worldview(self, worldview: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, worldview):
            return True
        else:
            self.dict_errors["worldview"] += 1
            return False

    def validate_address(self, address: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, address):
            return True
        else:
            self.dict_errors["address"] += 1
            return False


class Record:
    """Класс Запись"""
    def __init__(self,email,height,snils,passport,university,work_experience,political_views,worldview,address):
        self.email = email
        self.height = height
        self.snils = snils
        self.passport = passport
        self.university = university
        self.work_experience = work_experience
        self.political_views = political_views
        self.worldview = worldview
        self.address = address


path = 'path/to/file.txt'
loaded_data = json.load(open(path))
records = []
for item in loaded_data:
    records.append(Record(**item))
    # вызов validate
Validator(records)
