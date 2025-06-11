# Texas Aggie Batch Processor

A script for generating batches for Texas Aggie.

## Installing

```shell
poetry install
```

## How to Run

1. Connect to the `cifs` drive via `Finder` > `Go` > `Connect to Server`
2. Edit `batch_folder`, `final_csv_name`, and `batch_title` in `get_data.py` to reflect current batch.
3. Make sure you are in the correct virtual environment by typing `poetry shell`
4. Type `python get_data.py`
