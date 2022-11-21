from datetime import date, timedelta
import random

# 그래프 테스트 코드
def get_test():
    today = date.today()
    defaultStart = today - timedelta(29)
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1)]
    context = {'today':today, 'defaultStart':defaultStart, 'randomlist':randomlist}
    return context





