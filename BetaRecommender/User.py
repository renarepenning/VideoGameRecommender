import pandas as pd


class User:
    def __init__(self):  # self, name, genres, consoles, key_words):
        self.name = input("Name: ")
        self.consoles = input(
            "List your console(s) with commas and no spaces: ").split(",")
        self.genres = input(
            "List your genre(s) with commas and no spaces: ").split(",")
        self.key_words = input(
            "List your key_words(s) with commas and no spaces: ").split(",")

        self.series = pd.Series(data=[self.name, self.consoles, self.genres, self.key_words],
                                index=["user", "consoles", "genres", "key_words"])

    def printUser(self):
        print(self.name, "'s profile:\n- ", self.consoles,
              "\n- ", self.genres, "\n-", self.key_words)
