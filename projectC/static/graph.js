/*
중간 기간 계산 함수 
시작 날짜와 종료 날짜를 입력으로 받아
시작 날짜와 종료 날짜를 포함한 중간 날짜 어레이를 반환
*/
function getDateRangeData(param1, param2) {  //param1은 시작일, param2는 종료일이다.
    let res_day = [];
    let ss_day = new Date(param1);
    let ee_day = new Date(param2);
    while (ss_day.getTime() <= ee_day.getTime()) {
        let _mon_ = (ss_day.getMonth() + 1);
        _mon_ = _mon_ < 10 ? '0' + _mon_ : _mon_;
        let _day_ = ss_day.getDate();
        _day_ = _day_ < 10 ? '0' + _day_ : _day_;
        res_day.push(ss_day.getFullYear() + '-' + _mon_ + '-' + _day_);
        ss_day.setDate(ss_day.getDate() + 1);
    }
    return res_day;
}

/* 
보낼 데이터를 입력으로 받고
해당 데이터를 보내서 받아온 데이터를 히든 태그의 value에 저장 
*/
function sendAndReceiveData(postData) {
    // XHR 객체 생성
    const xhr = new XMLHttpRequest();
    // 열기 메소드
    xhr.open('GET', 'http://127.0.0.1:5500/testdata.json', false);
    xhr.onload = function () {
        // console.log('READYSTATE', xhr.readyState);
        document.getElementById('hidden').value = xhr.responseText;
    }
    xhr.send();
}

/*
히든 태그의 밸류값을 JSON형태로 가져와
소 마리수를 for문을 통해 가져온 뒤
해당 수만큼 차트에 넣을 데이터를 차트용 데이터셋에 푸쉬
*/
function createDataForChartUse() {
    let postDataValue = JSON.parse(document.getElementById('hidden').value)
    // key값이 'data'인 데이터의 value를 변수에 담는다
    let dataByDate = postDataValue.data
    // key값 추출
    let keys = Object.keys(dataByDate);

    // 소 마리 수 추출
    let endCount = 0;
    keys.forEach((key) => {
        let count = 0;
        let dailyData = dataByDate[key]
        let dailyDataKeys = Object.keys(dailyData);
        dailyDataKeys.forEach((key) => {
            count += 1;
        });
        if (endCount < count) {
            endCount = count;
        }
    });

    // 데이터를 차트에 보내기 전에 임시로 담아놓을 데이터 어레이
    let dataBeforeSendingToChart = [];
    // 임시 데이터 어레이 안에 소 마리수 만큼의 어레이 생성 
    for (i = 0; i < endCount; i++) {
        dataBeforeSendingToChart.push([])
    }

    // 날짜별로 되어있는 데이터를 소ID별로 분류해 임시 데이터 어레이에 푸쉬
    keys.forEach((key) => {
        let count = 0;
        let dailyData = dataByDate[key]

        let dailyDataKeys = Object.keys(dailyData);
        dailyDataKeys.forEach((key) => {
            dataBeforeSendingToChart[count].push(dailyData[key]['food'])
            count += 1;
        });
    });

    // 임시 데이터 어레이의 데이터를 차트에 보낼 형식으로 만든다
    let dataToSendToChart = [];
    for (i = 0; i < endCount; i++) {
        // 랜덤 색상 생성 
        // 지금은 비슷한 색상으로 나올 때가 있기 때문에 나중에 고정 색상 어레이 만들어서 거기서 뽑아올 예정
        let RGB_1 = Math.floor(Math.random() * (255 + 1))
        let RGB_2 = Math.floor(Math.random() * (255 + 1))
        let RGB_3 = Math.floor(Math.random() * (255 + 1))
        let strRGBA = 'rgba(' + RGB_1 + ',' + RGB_2 + ',' + RGB_3 + ',0.7)'

        dataToSendToChart.push(
            {
                data: dataBeforeSendingToChart[i],
                label: i + 1,
                borderColor: strRGBA,
                fill: false
            }
        )
    }
    console.log(dataToSendToChart)
    return dataToSendToChart
}

/* 
그래프 관련 값 변경 시 실행 함수
*/
function doSubmit() {
    let startDate = document.getElementById('startDate').value;
    let endDate = document.getElementById('endDate').value;
    let postData = JSON.stringify({ 'startDate': startDate, 'endDate': endDate });
    // 중간 기간 계산 함수
    let middleDate = getDateRangeData(startDate, endDate);

    sendAndReceiveData(postData);
    let chartData = createDataForChartUse();

    // 차트 업데이트
    myChart.data.labels = middleDate
    myChart.data.datasets = chartData
    myChart.update();
    myChart.options.animation.duration = 1000 // 초기 호출 이후 차트 업데이트 시 애니메이션 적용
}
doSubmit()