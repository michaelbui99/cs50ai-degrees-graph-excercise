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
        if dataset.lower() not in supported_datasets:
            raise UnknownDataset(
                "Uknown dataset provided. Please use 'large' or 'small'")
        if (dataset.lower() == "small"):
            self.movies = pd.read_csv(
                f'{path}/small/movies.csv', sep=',')
            self.people = pd.read_csv(
                f'{path}/small/people.csv', sep=',')
            self.stars = pd.read_csv(
                f'{path}/small/stars.csv', sep=',')
        else:
            self.movies = pd.read_csv(
                f'{path}/large/movies.csv', sep=',')
            self.people = pd.read_csv(
                f'{path}/large/people.csv', sep=',')
            self.stars = pd.read_csv(
                f'{path}/large/stars.csv', sep=',')
