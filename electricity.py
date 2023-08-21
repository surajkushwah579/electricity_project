
import csv
import numpy as np
data=[]
with open("/content/drive/MyDrive/MER_T07_02A-2020-02-03 (1).csv","r") as csvfile:
  file_reader=csv.reader(csvfile, delimiter=',')
  for row in file_reader:
      data.append(row)
data=np.array(data)

print(data)


# Task 1: Explore array attributes
print("Dimensions:", data.ndim)

print("\nShape:", data.shape)
print("\nData Type:", data.dtype)

# Task 2: Print data from the first 10 rows of the 4th column
print("\nData from the 4th column (rows 0-9):", data[:11, 3])


# Task 3: Identify header row
header_row = data[0]
print("\nHeader Row:", header_row)


# Task 4: Print data from columns 2 and 3 for rows 1-20
print("\nData from columns 2 and 3 (rows 1-20):", data[1:21, 1:3])


# Task 5: Print data from the first three and last three rows for all columns
print("\nData from the first three and last three rows of all columns:")
print(data[:3])
print(data[-3:])



# Task 6: Sort data based on net amount of electricity generated
sorted_data = data[data[:, 2].argsort()][::-1]
print("\nSorted data based on net amount of electricity generated:")
print(sorted_data)



# Task 7: Calculate total amount of electricity generated using coal and nuclear between 1949-1990
filtered_data = data[1:, :]  # Exclude the header row
valid_rows = (filtered_data[:, 1].astype(int) >= 194901) & (filtered_data[:, 1].astype(int) <= 199013)

valid_sources = (filtered_data[:, 0] == 'CLETPUS') | (filtered_data[:, 0] == 'NUETPUS')

valid_rows_sources = valid_rows & valid_sources
electricity_values = filtered_data[valid_rows_sources, 2].astype(float)
total_electricity = np.sum(electricity_values)

print("\nTotal electricity generated using coal and nuclear between 1949-1990:", total_electricity)





# Task 8: Print unique sources of energy generation
unique_sources = np.unique(data[1:, 0])
print("\nUnique sources of energy generation:")
for source in unique_sources:
    print(source)

# Task 9: Print details where energy source is Wind Energy (annual data)
mask = data[1:, 0] == 'WYETPUS'
wind_energy_data = data[1:][mask]
print("\nDetails where the energy source is Wind Energy:")
for row in wind_energy_data:
    print(row)


# Task 10: Calculate total energy generated in the USA
mask = data[1:, 4] == 'Electricity Net Generation Total (including from sources not shown), All Sectors'
usa_total_energy_data = data[1:][mask]

total_energy_generated = np.sum(usa_total_energy_data[:, 2].astype(float))

print("\nTotal energy generated in the USA till date:", total_energy_generated)



# Task 11: Calculate average and standard deviation of annual energy generated from wind
wind_energy_indices = np.where(data[:, 1] == 'Wind')
wind_energy_generation = data[wind_energy_indices, 2].astype(float)
average_wind_energy = np.mean(wind_energy_generation)
std_dev_wind_energy = np.std(wind_energy_generation)
print("\nAverage annual energy generated from wind:", average_wind_energy)
print("\nStandard deviation in energy generation from wind:", std_dev_wind_energy)



# Task 12: Find maximum annual energy generated
valid_rows = data[1:][data[1:, 2] != 'Not Available']
years = valid_rows[:, 1].astype(int) // 100
values = valid_rows[:, 2].astype(float)
max_energy_index = np.argmax(values)
max_energy_year = years[max_energy_index]
max_energy_value = values[max_energy_index]

print("\nMaximum annual energy generated:", max_energy_value, "Million Kilowatthours")
print("\nYear when the maximum annual energy was generated:", max_energy_year)



# Task 13: Check if energy production increased in the last 10 years
current_year = 2023
valid_years = data[1:, 0]  # Exclude the header row
valid_mask = np.char.isnumeric(valid_years)
valid_years_numeric = valid_years[valid_mask].astype(int)
last_10_years_data = data[1:][valid_mask][valid_years_numeric >= current_year - 10]
energy_increase = np.all(np.diff(last_10_years_data[:, 3].astype(float)) >= 0)
print("\nHas energy production increased in the last 10 years?", energy_increase)




# Task 14: Analyze trend in energy generated from wind and identify largest contributor
years = data[1:, 1].astype(int) // 100
values = data[1:, 2]

values[values == 'Not Available'] = np.nan
values = values.astype(float)

wind_energy_mask = data[1:, 0] == 'WYETPUS'
wind_years = years[wind_energy_mask]
wind_values = values[wind_energy_mask]

avg_wind_energy = np.nanmean(wind_values)

max_source_index = np.nanargmax(values)
max_source = data[max_source_index + 1, 0]

print("\nAverage wind energy production:", avg_wind_energy, "Million Kilowatthours")
print("Source with the largest annual electricity production:", max_source)




# Task 15: Compute contribution of wind, solar, and their combined contribution compared to total energy generationsources = data[1:, 0]
sources = data[1:, 0]
values = data[1:, 2].astype(float)

wind_mask = sources == 'WYETPUS'
solar_mask = sources == 'SOTEPUS'

wind_energy = np.sum(values[wind_mask])
solar_energy = np.sum(values[solar_mask])

total_energy = np.sum(values)

combined_energy = wind_energy + solar_energy

wind_contribution = (wind_energy / total_energy) * 100
solar_contribution = (solar_energy / total_energy) * 100
combined_contribution = (combined_energy / total_energy) * 100

print("Wind Energy Contribution:", wind_contribution, "%")
print("Solar Energy Contribution:", solar_contribution, "%")
print("Combined Wind and Solar Contribution:", combined_contribution, "%")

if wind_contribution > combined_contribution:
    print("The national grid is shifting toward wind energy.")
else:
    print("The national grid is not fundamentally shifting toward wind energy.")
