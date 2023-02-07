from app.logging import Logs
from constants import JSON_CHUNKS_SIZE, PATH_DIR
import json
import datetime

log = Logs()


def process_files_chunks(path, filenames: list) -> list:
    all_data = []
    for filename in filenames:
        log.info(filename)
        print(f"Loading file: {filename}")
        with open(path + filename, "r") as f:
            data = [filename]
            counter = 0
            while True:
                line = f.readline()
                if not line:
                    log.error(f"Not able to load a line from: {filename}")
                    break
                data.append(json.loads(line))
                counter += 1
                if counter >= JSON_CHUNKS_SIZE:
                    all_data.append(data)
                    data = []
                    counter = 0
            all_data.append(data)
    return all_data


def read_json(files: list) -> list:
    # the data are related to the same day, so we need to order by clock time
    sorted_files = sorted(files, key=lambda x: int(x.split("-")[-2]))
    files_chunks = process_files_chunks(PATH_DIR, sorted_files)
    return files_chunks
