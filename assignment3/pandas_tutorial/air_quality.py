import pandas as pd
import matplotlib.pyplot as plt


# air_quality = pd.read_csv(
#     "https://raw.githubusercontent.com/pandas-dev/pandas/refs/heads/main/doc/data/air_quality_no2.csv",
#     index_col=0,
#     parse_dates=True,
# )
# air_quality.to_csv("./air_quality.csv")

air_quality = pd.read_csv(
    "./air_quality.csv",
    index_col=0,
    parse_dates=True,
)

# air_quality.plot()

# air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

print(
    [
        method_name
        for method_name in dir(air_quality.plot)
        if not method_name.startswith("_")
    ]
)

# OUTPUT

# [
#     "area",
#     "bar",
# cspell:disable-next-line
#     "barh",
#     "box",
#     "density",
# cspell:disable-next-line
#     "hexbin",
#     "hist",
#     "kde",
#     "line",``
#     "pie",
#     "scatter",
# ]

# air_quality.plot.box()

# axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
# fig, axs = plt.subplots(figsize=(12, 4))
# air_quality.plot.area(ax=axs)
# axs.set_ylabel("NO$_2$ concentration")
# fig.savefig("no2_concentrations.png")

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

air_quality["ration_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed)
