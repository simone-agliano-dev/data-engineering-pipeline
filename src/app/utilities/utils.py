import time
import random
import re


def retrieve_files_by_date(file_list: list, date: str) -> list:
    filtered_files_list = [x for x in file_list if re.search(date, x)]
    return filtered_files_list


def split_into_batches(data: list, batch_size: int) -> list:
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]


def generate_id() -> str:
    timestamp = int(time.time())
    random_value = random.randint(0, 1000000)
    return f"{timestamp}{random_value}"


def validate_fields(data: dict, fields: list):
    missing_fields = []
    for field in fields:
        if field not in data:
            missing_fields.append(field)
    assert not missing_fields, f"Fields don't exist: {missing_fields} in {data}"
    return True
