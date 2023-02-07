import os

from app.utilities.utils import retrieve_files_by_date, split_into_batches
from app.data_extraction_from_files import read_json
from app.transformation_db import transform_and_load


class ETL:
    def __init__(self, date_time: str, path: str, batch_size: int):
        self.data_batch = None
        self.json_files = [f for f in os.listdir(path)]
        self.files_sorted_by_date = retrieve_files_by_date(self.json_files, date_time)
        self.batch = batch_size

    def run(self):
        for batch in split_into_batches(self.files_sorted_by_date, self.batch):
            self.data_batch = read_json(files=batch)
            transform_and_load(self.data_batch)
