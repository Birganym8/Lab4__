from datetime import datetime, timedelta


current_date = datetime.now()


new_date = current_date - timedelta(days=5)


print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("New Date (5 days earlier):", new_date.strftime("%Y-%m-%d"))
