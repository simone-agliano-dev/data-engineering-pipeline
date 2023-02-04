import time
import random
import re


def retrieve_files_by_date(file_list: list, date: str) -> list:
    filtered_files_list = [x for x in file_list if re.search(date, x)]
    return filtered_files_list


def split_into_batches(data: list, batch_size: int) -> list:
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]
