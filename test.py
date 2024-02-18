import nfl_data_py as nfl

season = nfl.import_seasonal_data([2023], "REG")

print(season.head(10))
