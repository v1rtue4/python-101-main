# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

# 10 miles = 30 minutes and 30 seconds

miles = 10
minutes = 30
seconds = 30
conversion_factor = 1.6 # 1 mile to 1 kilometer

# Convert miles to kilometers
kilometers = miles * conversion_factor

# Convert time to hours
total_minutes = minutes + (seconds / 60)
hours = total_minutes / 60

# Calculate average speed
average_speed = kilometers / hours

# Display results
print(average_speed)
