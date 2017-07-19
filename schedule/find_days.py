import re

def get_days(interval):
    num = re.findall(r'\d+', interval)
    if 'day' in interval and num:
        days = num[0]
    elif 'week' in interval and num:
        days = num[0] * 7
    else:
        days = 0
    return days