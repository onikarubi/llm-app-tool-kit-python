import pytest
import openai
import os
from src.fine_tuning.fine_tuning import get_train_csv_file
from src.fine_tuning.data_format_generator import TrainingJsonFormatter


def test_get_train_csv_file():
    csv_file = get_train_csv_file("yukkuri-marisa.csv")
    assert os.path.exists(csv_file)


# def test_create_dataset(tmpdir):
#     csv_file = get_train_csv_file("yukkuri-marisa.csv")
#     formatter = TrainingJsonFormatter(
#         csv_file, "src/fine_tuning/train_json"
#     )
#     formatter.saved_train_file()


# def test_upload_training_file():
#     openai.File.create(
#         file=open("src/fine_tuning/train_json/yukkuri-marisa.jsonl"),
#         purpose="fine-tune",
#     )


def test_fine_tuning_execute():
    response = openai.FineTuningJob.create(
        model="gpt-3.5-turbo",
        training_file="file-3TUIZJ4ZrHE36AdaVvD4Xtny",
        hyperparameters={
            "n_epochs": 6,
        },
    )
    print(response)