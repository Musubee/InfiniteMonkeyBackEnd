from __future__ import annotations
from datetime import datetime
def timestamp_to_date_time(timestamp: datetime) -> tuple[str, str]:
	# Turns a datetime object into a date and time string according to the database key schema
	# Date => YYYY-MM-DD
	# Time => HH:MM:SS.MS
	append_zero_if_needed = lambda time_attr: f'0{time_attr}' if time_attr < 10 else str(time_attr)
	# append 0's to all single digit time attributes
	month = append_zero_if_needed(timestamp.month)
	day = append_zero_if_needed(timestamp.day)
	hour = append_zero_if_needed(timestamp.hour)
	minute = append_zero_if_needed(timestamp.minute)
	seconds = append_zero_if_needed(timestamp.second)

	date = f'{timestamp.year}-{month}-{day}'
	time = f'{hour}-{minute}-{seconds}.{timestamp.microsecond}'
	return date, time