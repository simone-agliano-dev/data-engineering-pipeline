# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from app.etl import ETL
from constants import PATH_DIR, N_BATCH_FILES, DATE


def run_pipeline():
    """ETL class takes as input
        date: when the data are considered as input,
        input_dir : location of the input files
        batch_size : number of files to be processed each iteration
    """
    etl_job = ETL(DATE, PATH_DIR, N_BATCH_FILES)
    etl_job.run()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run_pipeline()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
