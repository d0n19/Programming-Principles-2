import datetime


current_date = datetime.datetime.now()
print("Current Date & Time:", current_date)

specific_date = datetime.datetime(2023, 10, 25)
print("Specific Date:", specific_date)









formatted_date = current_date.strftime("%A, %B %d, %Y - %H:%M:%S")
print("Formatted Date:", formatted_date)






future_date = current_date + datetime.timedelta(days=10)
print("Date 10 days from now:", future_date)

difference = future_date - current_date
print(f"Time Difference: {difference.days} days")







tz = datetime.timezone(datetime.timedelta(hours=5)) 
tz_date = datetime.datetime.now(tz)
print("Timezone Aware Date (UTC+5):", tz_date)