import csv
import matplotlib.pyplot as plt
import numpy as np




def read_data_to_file(data_file_path):
    """
    :param data_file_path: Data from 2030 (with factors)
    :return: data[time, totalGen,__ ,Solar]
    """
    return 0
    pass

def factor_add(data, solar_factor, general_factor):
    """
    :param: solar_factor: the pre-calculated solar factor
    :param: genera_general_factor: the pre-calculated general factor
    :param: data: the csv data - dictionary
    add factor to data
    """


def write_to_file(file_path, data):
    """
    :param file_path: csv path
    :param data: the calculated data
    After the greedy model this function write the calculated data to a csv file.
    """
    pass


def plot_data(date, length):
    """
    :param date: the date of the plotted data.
    :param length: the length in time of the plotted data.
    this function plot graph in certian length and time.
    """

def one_hour_calculation(data, day, time, ramp_up):
    """
    :param data: data from last calculations
    :param ramp_up: The slope of the turbines
    :param day: the day in year(int) the data is calculated on.
    :param time: the hour in day(int) the data is calculated on.
    this function calculate one hour with the greedy model.
    """

def greedy_model_calculation(data, year_number = 1, ramp_up = 0):
    """
    :param data: data of 2050
    :param year_number: number of repeats
    :param ramp_up: ramp up of the gas turbines
    calculate the gas use, the battery use and ...
    """

if __name__ == '__main__':
    solar_factor = 1
    general_factor = 1
    data = read_data_to_file('data.csv') # data is a dictionary
    greedy_model_calculation(data)
    write_to_file('results.csv', data)

