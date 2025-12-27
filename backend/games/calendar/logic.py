import datetime

MONTHS = (
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
)

def build_calendar(year, month, notes):
    today = datetime.date.today()

    start = datetime.date(year, month, 1)
    while start.weekday() != 6:
        start -= datetime.timedelta(days=1)

    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    end_of_month = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)

    last = end_of_month + datetime.timedelta(days=(5 - end_of_month.weekday()) % 7 + 1)

    weeks = []
    cur = start

    while cur <= last:
        week = []
        for _ in range(7):
            key = str(cur)
            week.append({
                "day": cur.day,
                "month": cur.month,
                "year": cur.year,
                "is_today": cur == today,
                "note": notes.get(key, "")
            })
            cur += datetime.timedelta(days=1)
        weeks.append(week)

    return {
        "month_name": MONTHS[month-1],
        "year": year,
        "weeks": weeks
    }
