# Forecast Income for the Foreseeable Future!

This tool provides an estimate of how much money you will save over a given period. It consists of two main components:

## 1. Base Projection (`base_projection.py`)

This script projects the future balance of your bank account using a simple linear equation, based on:
- **Starting Point**: The current balance in the bank (non-growing part).
- **Monthly Income**: The amount of income made each month.

The equation used is:
\[ y = mx + b \]
Where:
- \( y \) is the future balance to solve for,
- \( m \) is the number of months,
- \( x \) is the monthly income,
- \( b \) is the current balance.

## 2. Savings Projection (`savings_projection.py`)

This script projects the future balance of your savings account considering the effect of compound interest, with inputs:
- **Starting Point**: The current amount in the savings account.
- **APR**: Annual Percentage Rate (interest rate).
- **Monthly Deposits**: Additional amounts deposited each month.

The balance grows each month as interest compounds, meaning each month's interest will include the previous month's accumulated interest.

## Usage
Each aspect can be ran combined or separately. projection_config.py must be filled out to be given a valid projection.

1. python base_projection.py [num_months]

This will calculate the base projection for the given number of months from today. 36 months is default if not provided. Data will be output to income_data.txt and a line graph will be shown.

2. python savings_projection.y [num_months]

This will calculate the savings projection for the given number of months from today. 36 months is default if not provided. Data will be output to savings_data.txt and a line graph will be shown.

3. python complete_projection.py [num_months]

This will calculate and combine the base projection AND the savings projection for the given number of months from today. 36 months is default if not provided. Data will be output to merged_data.txt and a line graph will be shown.