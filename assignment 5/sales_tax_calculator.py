#!/usr/bin/env python3

TAX = 0.06


def sales_tax_calculator(total):
    sales_tax = total * TAX
    return sales_tax


def main():
    print("Sales Tax Calculator\n")
    total = float(input("Total amount: "))
    total_after_tax = round(total + sales_tax_calculator(total), 2)
    print(f"Total after tax: {total_after_tax}")


if __name__ == "__main__":
    main()
