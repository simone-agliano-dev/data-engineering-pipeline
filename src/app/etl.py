import os


class ETL:
    def __int__(self, date_time: str, path: str, batch_size: int):
        self.data_batch = None
        self.json_files = [f for f in os.listdir(path)]
        self.files_sorted_by_date = None
        self.batch = batch_size
