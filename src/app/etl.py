import os

from src.app.utilities.utils import retrieve_files_by_date, split_into_batches


class ETL:
    def __int__(self, date_time: str, path: str, batch_size: int):
        self.data_batch = None
        self.json_files = [f for f in os.listdir(path)]
        self.files_sorted_by_date = retrieve_files_by_date(self.json_files, date_time)
        self.batch = batch_size

    def run(self):
        for batch in split_into_batches(self.files_sorted_by_date, self.data_batch):
            self.data_batch = read_file(
                batch
            )  # ToDO read the files that are part of the batch
            transform_and_load(
                self.data_batch
            )  # ToDO transform the data before storing them to DB
