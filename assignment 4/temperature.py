#!/usr/bin/env python3
"""
author: Kelly McBean
date: 6/22/23
desc: This module contains functions for converting
temperature between degrees Fahrenheit and degrees Celsius
"""


def to_celsius(fahrenheit):
    """
    This function converts degrees Fahrenheit to Celsius
    :param fahrenheit: This is the degrees Fahrenheit to convert
    :return: This is the converted Celsius value
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def to_fahrenheit(celsius):
    """
    This function converts degrees Celsius to Fahrenheit
    :param celsius: This is the degrees Celsius to convert
    :return: This is the converted Fahrenheit value
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


def main():
    for temp in range(0, 212, 40):
        print(f"{temp} Fahrenheit = {round(to_celsius(temp))} Celsius")
    for temp in range(0, 100, 20):
        print(f"{temp} Celsius = {round(to_fahrenheit(temp))} Fahrenheit")


if __name__ == "__main__":
    main()
