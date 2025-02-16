from datetime import datetime

date_string1 = "2025-02-16 14:30:00"
date_string2 = "2025-02-17 16:45:00"

date1 = datetime.strptime(date_string1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_string2, "%Y-%m-%d %H:%M:%S")


time_difference = (date2 - date1).total_seconds()


print(f"Time difference in seconds: {time_difference} seconds")
