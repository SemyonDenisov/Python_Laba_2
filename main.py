import json
import re


class Validator:
    """
    Класс Валидатор
    """
    def __init__(self, records):
        self.records = records
        self.pattern = {"email": r'^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$', "height": r"[1-2].\d{2}",
                        "snils":  r"\d{11}", "passport_number": r"\d{6}", "university": r"[a-zA-Zа-яА-ЯёЁ]",
                        "work_experience": r"[^a-zA-Zа-яА-ЯёЁ]", "political_views": r"[a-zA-Zа-яА-ЯёЁ]",
                        "worldview": r"[a-zA-Zа-яА-ЯёЁ]", "address":  r".*?"}
        self.dict_errors = {"email": 0, "height": 0, "snils": 0, "passport_number": 0,
                            "university": 0, "work_experience": 0,
                            "political_views": 0, "worldview": 0, "address": 0}
        self.valid_count = 0
        self.invalid_count = 0

    def validate_by_key(self, record, key: str) -> bool:
        if re.match(self.pattern[key], str(record[key])):
            return True
        else:
            self.dict_errors[key] += 1
            return False

    def validate(self):
        for record in self.records:
            counter_valid_part = 0
            for key in self.pattern.keys():
                if self.validate_by_key(record, key):
                    counter_valid_part += 1
            if counter_valid_part == 9:
                self.valid_count += 1
            else:
                self.invalid_count += 1
        print(self.valid_count, self.invalid_count)
        print(self.dict_errors)


class Record:
    """Класс Запись"""
    def __init__(self, dct):
        self.data = dct


path = r'C:\Users\Senya\Downloads\107.txt'
loaded_data = json.load(open(path))
records_1 = []
for item in loaded_data:
    records_1.append(item)
Validator_1 = Validator(records_1)
Validator_1.validate()
