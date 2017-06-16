#This file is what will build my movie data

#importing libraries to use with this file
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Data():

    # def __init__(self):
    #     self.__data = pd.read_csv('trends/arrival.csv')

    def get_mean(self):
        #Creating the two lists which will hold my data
        score_list = [] #To hold the mean scores from google
        earnings_list = [] #To hold the amount of money each movie made
        #a count variable
        count = 0
        #This list will hold all of the movies being examined I will loop
        #through this list to pull data.
        movies = ['zootopia','lalaland','arrival', 'manchesterbythesea', 'captainamerica', 'rogueone','deadpool', 'doctorstrange', 'findingdory', 'junglebook', 'suicidesquad','batman', 'Secretlifeofpets', 'hacksawridge', 'fantasticbeast', 'startrek', 'moana' ]
        #Starting a loop
        for movie in movies:
            #Pulling each specific CSV file to get google trends data
            data_trends = pd.read_csv('trends/'+movie+'.csv')
            #setting up the variable to hold the csv file containing info on
            #how much each movie made.
            data_money = pd.read_csv('movie.csv')
            #capitalize the first letter of the movie name.
            movie = movie.capitalize()
            #I then use that movie name to pull the mean from a specific column
            mean = data_trends[movie].mean()
            #I append that information to the scores list
            score_list.append(mean)
            #I now look at the money csv file and pull each data point out.
            earnings = data_money.iloc[count][1]
            #I append the amount of money each movie made to the earnings_list
            earnings_list.append(earnings)
            #I increase the count by one.
            count += 1
        # print(score_list)
        # print(earnings_list)
        plt.title("Google data compared to Earnings", fontsize=16)
        plt.xlabel("Google Trends Mean Data", fontsize=14)
        plt.ylabel("Earnings", fontsize=14)
        plt.axis([4, 22, 50000000, 600000000])
        plt.scatter(score_list, earnings_list)
        plt.show()
        # print(int(earnings_list[0]) + int(earnings_list[1]))




data = Data()
data.get_mean()
