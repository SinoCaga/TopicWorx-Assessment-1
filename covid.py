import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load
with open("covid_data.txt", "r", encoding="utf-8-sig") as f:
    raw_data = json.load(f)

df = pd.DataFrame(raw_data)#putting the data into rows and colums using pandas datframe

# Clean "1 139" style strings
def clean_number(v):
    if isinstance(v, str):
        v = v.replace(" ", "")
    return pd.to_numeric(v, errors="coerce")

for col in ["Total Confirmed Cases", "Total Deaths", "Total Recovered",
            "Active Cases", "Daily Confirmed Cases", "Daily  deaths"]:
    df[col] = df[col].apply(clean_number)

df["Date"] = pd.to_datetime(df["Date"], format="%Y/%m/%d")#date format conversion to datetime object
df = df.sort_values("Date").reset_index(drop=True)#sorting the data cronologically and resetting the index

# Plot
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("COVID-19 Progression (Mar 5 – Jun 12, 2020)",
             fontsize=16, fontweight="bold")

axes[0, 0].plot(df["Date"], df["Total Confirmed Cases"], color="steelblue", lw=2)
axes[0, 0].set_title("Total Confirmed Cases")

axes[0, 1].bar(df["Date"], df["Daily Confirmed Cases"], color="orange", alpha=0.6)
axes[0, 1].plot(df["Date"],
                df["Daily Confirmed Cases"].rolling(7, min_periods=1).mean(),
                color="red", lw=2)
axes[0, 1].set_title("Daily New Cases + 7-day average")

axes[1, 0].plot(df["Date"], df["Total Deaths"], color="black", lw=2)
axes[1, 0].set_title("Total Deaths")

axes[1, 1].plot(df["Date"], df["Active Cases"], color="crimson", lw=2, label="Active")
axes[1, 1].plot(df["Date"], df["Total Recovered"], color="green", lw=2, label="Recovered")
axes[1, 1].set_title("Active vs Recovered")
axes[1, 1].legend()

for ax in axes.flat:
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("covid_dashboard.png", dpi=150)
plt.show()