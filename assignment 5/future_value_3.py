#!/usr/bin/env python3

MONTHS_PER_YEAR = 12


def calculate_future_value(monthly_investment, yearly_interest, years):
    monthly_interest_amount = yearly_interest / MONTHS_PER_YEAR / 100
    total_months = years * MONTHS_PER_YEAR

    future_value = 0.0
    for i in range(0, total_months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_amount
        future_value += monthly_interest

        print(f"total months: {i} = {future_value}")

    return future_value


def main():
    print("Welcome to the Future Value Calculator\n")
    future_value = calculate_future_value(100, 12, 10)
    print(f"Future value: {round(future_value, 2)}")
    print()


main()
