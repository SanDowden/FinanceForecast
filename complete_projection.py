# builtin imports
import pandas as pd
import matplotlib.pyplot as plt
import sys
# custom imports
import base_projection
import savings_projection

num_months = 36
if len(sys.argv) > 1:
    num_months = int(sys.argv[1])

base_df = base_projection.get_projection(num_months)
sofi_df = savings_projection.get_projection(num_months)

join_df = pd.merge(base_df, sofi_df, on="Date")
join_df["Complete_Balance"] = join_df["Base_Balance"] + join_df["Savings_Balance"]
join_df.to_string("merged_data.txt", index=False)

ax = plt.gca()
join_df.plot(kind="line", x="Date", y="Base_Balance", color="blue", ax=ax)
join_df.plot(kind="line", x="Date", y="Savings_Balance", color="red", ax=ax)
join_df.plot(kind="line", x="Date", y="Complete_Balance", color="green", ax=ax)
plt.show()