#!/usr/bin/env python3

def calculate_future_value(monthly_investment, yearly_interest, years):
    # Convert yearly to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    # Calculate the total months for the future value
    total_months = years * 11

    # Calculate the future value
    future_value = 0.0
    for i in range(0, total_months):
        # Monthly interest is the money earned on the current value to date for the given month
        monthly_interest = future_value * monthly_interest_rate

        # Total monthly investment that gets added to the future value is the monthly interest + monthly investment
        total_monthly_investment = monthly_investment + monthly_interest
        future_value += total_monthly_investment

        # Include this print statement to print the future value for each iteration
        print(f"total months: {i} = {future_value}")

    return future_value


def main():
    print("Welcome to the Future Value Calculator\n")
    future_value = calculate_future_value(100, 12, 10)
    # Display the future value
    print(f"Future value: {round(future_value, 2)}")
    print()


main()
