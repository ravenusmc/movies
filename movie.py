#This file is what will build my movie data

#importing libraries to use with this file
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Data():

    def __init__(self):
        self.__data = pd.read_csv('movie.csv')

    def show(self):
        print(self.__data.head())

data = Data()
data.show()
