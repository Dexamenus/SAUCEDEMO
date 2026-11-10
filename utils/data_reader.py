import json
from pathlib import Path


TEST_DATA_DIR = Path(__file__).resolve().parents[1] / "test_data"


def read_json(filename):
    with (TEST_DATA_DIR / filename).open(encoding="utf-8") as data_file:
        return json.load(data_file)
