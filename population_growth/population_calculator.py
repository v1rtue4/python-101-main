# Population Growth Calculator
# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

# Current Population
current_population = 380123456

# Time intervals in seconds
birth_interval = 6
death_interval = 12
imigration_interval = 40

# Seconds in one non-leap year
seconds_per_year = 365 * 24 * 60 * 60

# Calculate number of events per year
births_per_year = seconds_per_year / birth_interval
deahts_per_year = seconds_per_year / death_interval
imigrants_per_year = seconds_per_year / imigration_interval

# Calculate net change per year
net_change_per_year = births_per_year - deahts_per_year + imigrants_per_year

# Calculate population after 3 years
population_after_3_years = current_population + (net_change_per_year * 3)

# Display results
print("Estimated population after 3 years:", population_after_3_years)
