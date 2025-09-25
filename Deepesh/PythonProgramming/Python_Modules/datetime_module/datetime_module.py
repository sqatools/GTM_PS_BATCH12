from datetime import datetime, timedelta

datetime_val = datetime.now()
print("current date with time :", datetime_val)  # 2025-09-23 20:07:29.701308
print("Today's date:", datetime_val.date())  # 2025-09-23
print("Today's day:", datetime_val.day)  # 23
print("Current month:", datetime_val.month)  # 9
print("Current Year:", datetime_val.year)  # 2025

result = datetime_val - timedelta(days=2)
print("2 days back date :", result.date())  # 2 days back date : 2025-09-21

result2 = datetime_val + timedelta(days=2)
print("2 days future date :", result2.date())  # 2 days future date : 2025-09-25

# 2 month back date
result3 = datetime_val - timedelta(days=60)
print("2 months back date :", result3.date())  #2025-07-25

#################################
# generate unique variable
unique_variable = datetime_val.strftime("%d_%m_%Y_%H_%M_%S")
print(unique_variable) # 23_09_2025_20_15_41