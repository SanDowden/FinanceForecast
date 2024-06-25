# builtin imports
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import sys
# custom imports
import format_helper as format_helper
import projection_config

def get_projection(months_to_calc) -> pd.DataFrame:
    # SETUP
    # annual interest as the advertised percentage
    annual_interest = projection_config.annual_interest
    # annual interest as the actual rate per year
    annual_interest_rate = round(annual_interest / 100, 6)
    # monthly interest multiplier
    monthly_interest_rate = round(annual_interest_rate / 12, 6)
    # current balance of savings account
    savings_balance = projection_config.savings_balance
    # direct deposit contribution
    monthly_contribution = projection_config.monthly_contribution

    # current month / year
    today = date.today()
    cur_month = today.month
    cur_year = today.year

    # BEGIN PROCESSING
    print(f"[SAVINGS] Annual Interest Rate: {annual_interest}% ({annual_interest_rate})")
    print(f"[SAVINGS] Monthly Interest Multiplier (Annual Rate divided by 12): {monthly_interest_rate}")
    print(f"[SAVINGS] Forecasting {months_to_calc} months from today...")

    data = [{"Date" : format_helper.getMonthYearLabel(cur_month, cur_year), "Savings_Balance" : savings_balance, "Interest" : 0, "Total_Increase" : 0}]

    for i in range(1, months_to_calc + 1):
        # first we increase by the money we direct deposit
        savings_balance += monthly_contribution
        # then we increase by interest added
        interest = round(savings_balance * monthly_interest_rate, 2)
        savings_balance += interest
        increase = monthly_contribution + interest

        cur_month += 1
        if cur_month == 13:
            # move into next year
            cur_month = 1
            cur_year += 1

        data.append({"Date" : format_helper.getMonthYearLabel(cur_month, cur_year), "Savings_Balance" : savings_balance, "Interest" : interest, "Total_Increase" : increase})

    return pd.DataFrame(data)

if __name__ == "__main__":
    num_months = 36
    if len(sys.argv) > 1:
        num_months = int(sys.argv[1])

    df = get_projection(num_months)
    df.to_string("savings_data.txt", index=False)
    df.plot(kind="line", x="Date", y="Savings_Balance")
    plt.show()