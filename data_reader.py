import pandas as pd
from pathlib import Path

supported_datasets = ["small", "large"]


class UnknownDataset(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class DataReader:
    def __init__(self, dataset: str):
        path = Path("./data").absolute()
        self.movies: pd.DataFrame
        self.people: pd.DataFrame
        self.stars: pd.DataFrame
        ds = dataset.lower()
        if ds not in supported_datasets:
            raise UnknownDataset(
                "Uknown dataset provided. Please use 'large' or 'small'")

        self.movies = pd.read_csv(
            f'{path}/{ds}/movies.csv', sep=',')
        self.people = pd.read_csv(
            f'{path}/{ds}/people.csv', sep=',')
        self.stars = pd.read_csv(
            f'{path}/{ds}/stars.csv', sep=',')
