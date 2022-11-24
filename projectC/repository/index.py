from datetime import date, timedelta
import random
import json

# 그래프 테스트 코드
def get_test():
    today = date.today()
    defaultStart = today - timedelta(29)
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1)]
    testDataset = [{
        'label': "1",
        'borderColor': "#3e95cd",
    }, {
        'label': "2",
        'borderColor': "#8e5ea2",
    }, {
        'label': "3",
        'borderColor': "#3cba9f",
    }, {
        'label': "4",
        'borderColor': "#e8c3b9",
    }
    ]
    
    testDataset = json.dumps(testDataset)
    context = {'today':today, 'defaultStart':defaultStart,'randomlist':randomlist, 'testDataset':testDataset} 

    return context





