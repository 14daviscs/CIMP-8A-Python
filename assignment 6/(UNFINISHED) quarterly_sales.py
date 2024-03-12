"""

#!/usr/bin/env python3

def storage():
    quarterly_sales = []

def start_inputs():
    print("The Quarterly Sales Program")
    print()
    quarterly_sales[0] = float(input("Enter sales for Q1: "))
    quarterly_sales[1] = float(input("Enter sales for Q2: "))
    quarterly_sales[2] = float(input("Enter sales for Q3: "))
    quarterly_sales[3] = float(input("Enter sales for Q4: "))
    print()
    print(f"Total:                 {quarterly_sales[0] + quarterly_sales[1] + quarterly_sales[2] + quarterly_sales[3]}")
    print(f"Average Quarter:       {}")
    print(f"Lowest Quarter:        {}")
    print(f"Highest Quarter        {}")


def main():
    storage()
    start_inputs()


if __name__ == "__main__":
    main()

"""