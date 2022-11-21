from datetime import date, timedelta
import random


def get_test():
    today = date.today()
    defaultStart = today - timedelta(29)
    dayLabel = list(range(1, (today - defaultStart).days + 1))
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1)]
    context = {'today':today, 'defaultStart':defaultStart, 'dayLabel':dayLabel, 'randomlist':randomlist}
    return context





