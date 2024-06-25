# builtin imports
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import sys
# custom imports
import format_helper as format_helper
import projection_config


def get_projection(months_to_calc):
    # SETUP

    # whats in the bank
    net_list = projection_config.net_list
    # income each month
    income_list = projection_config.income_list

    # combined amount(s)
    total_balance = sum(net_list)
    monthly_increase = sum(income_list)

    # current month / year
    today = date.today()
    cur_month = today.month
    cur_year = today.year

    # BEGIN PROCESSING
    print(f"[BASE] Forecasting {months_to_calc} months from today...")

    data = [{"Date" : format_helper.getMonthYearLabel(cur_month, cur_year), "Base_Balance" : total_balance, "Increase" : 0}]

    for i in range(1, months_to_calc + 1):
        # increase by income amount
        total_balance += monthly_increase

        cur_month += 1
        if cur_month == 13:
            # move into next year
            cur_month = 1
            cur_year += 1

        data.append({"Date" : format_helper.getMonthYearLabel(cur_month, cur_year), "Base_Balance" : total_balance, "Increase" : monthly_increase})

    return pd.DataFrame(data)

if __name__ == "__main__":
    num_months = 36
    if len(sys.argv) > 1:
        num_months = int(sys.argv[1])

    df = get_projection(num_months)
    df.to_string("income_data.txt", index=False)
    df.plot(kind="line", x="Date", y="Balance")
    plt.show()