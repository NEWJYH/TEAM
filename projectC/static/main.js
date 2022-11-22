/*
중간 기간 계산 함수 
시작 날짜와 종료 날짜를 입력으로 받아
시작 날짜와 종료 날짜를 포함한 중간 날짜 어레이를 반환
*/
function getDateRangeData(param1, param2) {  //param1은 시작일, param2는 종료일이다.
    var res_day = [];
    var ss_day = new Date(param1);
    var ee_day = new Date(param2);
    while (ss_day.getTime() <= ee_day.getTime()) {
        var _mon_ = (ss_day.getMonth() + 1);
        _mon_ = _mon_ < 10 ? '0' + _mon_ : _mon_;
        var _day_ = ss_day.getDate();
        _day_ = _day_ < 10 ? '0' + _day_ : _day_;
        res_day.push(ss_day.getFullYear() + '-' + _mon_ + '-' + _day_);
        ss_day.setDate(ss_day.getDate() + 1);
    }
    return res_day;
}

function loadData(postdata) {
    // XHR 객체 생성
    const xhr = new XMLHttpRequest();
    // 열기 메소드
    xhr.open('POST', '/post', true);
    xhr.onload = function () {
        //console.log('READYSTATE', xhr.readyState);
        console.log(this.responseText);
    }
    xhr.send(postdata);

    // const jsondata = JSON.parse(xhr.responseText);
    // return jsondata
}

const randomlist = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]

const testDataset = [{
    data: randomlist[0],
    label: "1번 방",
    borderColor: "#3e95cd",
    fill: false
}, {
    data: randomlist[1],
    label: "2번 방",
    borderColor: "#8e5ea2",
    fill: false
}, {
    data: randomlist[2],
    label: "3번 방",
    borderColor: "#3cba9f",
    fill: false
}, {
    data: randomlist[3],
    label: "4번 방",
    borderColor: "#e8c3b9",
    fill: false
}, {
    data: randomlist[4],
    label: "5번 방",
    borderColor: "#c45850",
    fill: false
}
]

/* 기간 제출시 실행 함수
기간 입력으로부터 값을 받아와서 중간 기간 계산 함수를 통해
중간 기간 어레이를 생성한 후
차트의 라벨값을 해당 어레이로 변경 후 차트 업데이트
*/
function doSubmit() {
    let startDate = document.getElementById('startDate').value;
    let endDate = document.getElementById('endDate').value;
    let middleDate = getDateRangeData(startDate, endDate)
    myChart.data.labels = middleDate
    myChart.data.datasets = testDataset
    
    loadData(startDate);
    myChart.update();
    myChart.options.animation.duration = 1000 // 초기 호출 이후 차트 업데이트 시 애니메이션 적용
}
doSubmit()