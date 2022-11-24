const today = new Date();

const lastWeek = new Date();
lastWeek.setDate(today.getDate() - 7)

// 오늘과 지난주를 기간 인풋에 넣을 수 있는 형태로 만듦
const forDefault = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
const forStartDefault = lastWeek.getFullYear() + '-' + (lastWeek.getMonth() + 1) + '-' + lastWeek.getDate()
// 기간 인풋 기본값 설정
document.getElementById('endDate').value = forDefault
document.getElementById('startDate').value = forStartDefault
// 기간 인풋의 최대 최소값 설정
document.getElementById('endDate').setAttribute('max', forDefault)
document.getElementById('startDate').setAttribute('max', forDefault)
document.getElementById('endDate').setAttribute('min', document.getElementById('startDate').value)

/*
시간 단위 선택 변경시 실행 함수
시간 선택 메뉴 시각화 여부 결정을 결정하고
시작 날짜의 기본값을 오늘로 설정
*/
function changeUnitOfTime() {
    const today = new Date();
    const forStartDate = new Date();
    const forCheckTime = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate()

    const checkUnitOfTime = document.querySelector('input[name="unit"]:checked').value;
    const startTimeArea = document.getElementById('selectStartTime');
    const endTimeArea = document.getElementById('selectEndTime');
    if (checkUnitOfTime === 'hour') {
        startTimeArea.style.display = 'inline';
        endTimeArea.style.display = 'inline';
        let dateInput = document.getElementById('startDate')
        dateInput.value = document.getElementById('endDate').value
    } else {
        startTimeArea.style.display = 'none';
        endTimeArea.style.display = 'none';
        const endInputDate = document.getElementById("endDate").value
        const timeToDayInput = new Date();
        timeToDayInput.setFullYear(endInputDate.substr(0, 4))
        timeToDayInput.setMonth(endInputDate.substr(5, 2) - 1)
        timeToDayInput.setDate(endInputDate.substr(8, 2))
        timeToDayInput.setDate(timeToDayInput.getDate() - 7)
        document.getElementById('startDate').value = timeToDayInput.getFullYear() + '-' + (timeToDayInput.getMonth() + 1) + '-' + timeToDayInput.getDate()
    }

    if (document.getElementById("endDate").value == forCheckTime) {
        const now = new Date();
        const nowtime = document.getElementById(now.getHours())
        nowtime.setAttribute('selected', 'selected')
    } else {
        const twentyThree = document.getElementById(23)
        twentyThree.setAttribute('selected', 'selected')
    }
    document.getElementById('endDate').setAttribute('min', document.getElementById('startDate').value)
}

// 끝 기간 밸류 변경 시 시작 기간 제한
function limitStartDate() {
    document.getElementById('startDate').setAttribute('max', document.getElementById('endDate').value)
}

// 시작 기간 밸류 변경 시 끝 기간 제한
function limitEndDate() {
    document.getElementById('endDate').setAttribute('min', document.getElementById('startDate').value)
}

/*
시간 단위 시간 선택 시 보낼 기간 값에 시간 붙이기 
*/
function addTimeToDate() {
    const checkUnitOfTime = document.querySelector('input[name="unit"]:checked').value;
    let startHour = '';
    let endHour = '';
    let startDateTime = '';
    let endDateTime = '';
    if (checkUnitOfTime === 'hour') {
        startHour = document.getElementById('startTime').value;
        endHour = document.getElementById('endTime').value;
        if (parseInt(startHour) < 10) {
            startDateTime = document.getElementById('startDate').value + ' 0' + startHour + ':00';
        } else {
            startDateTime = document.getElementById('startDate').value + ' ' + startHour + ':00';
        }
        if (parseInt(endHour) < 10) {
            endDateTime = document.getElementById('endDate').value + ' 0' + endHour + ':00';
        } else {
            endDateTime = document.getElementById('endDate').value + ' ' + endHour + ':00';
        }
    } else {
        startDateTime = document.getElementById('startDate').value;
        endDateTime = document.getElementById('endDate').value
    }
    const timeArray = [startDateTime, endDateTime]
    return timeArray
}

/*
중간 기간 계산 함수 
시작 날짜와 종료 날짜를 입력으로 받아
시작 날짜와 종료 날짜를 포함한 중간 날짜 어레이를 반환
*/
function getDateRangeData(param1, param2) {  //param1은 시작일, param2는 종료일이다.
    const resDay = [];
    const resDayIncludeYear = [];
    let startDay = new Date(param1);
    let endDay = new Date(param2);
    const checkUnitOfTime = document.querySelector('input[name="unit"]:checked').value;
    if (checkUnitOfTime === 'hour') {
        while (startDay.getTime() <= endDay.getTime()) {
            let month = (startDay.getMonth() + 1);
            month = month < 10 ? '0' + month : month;

            let day = startDay.getDate();
            day = day < 10 ? '0' + day : day;

            let hour = startDay.getHours();
            hour = hour < 10 ? '0' + hour : hour;

            resDay.push(startDay.getHours() + '시');
            startDay.setHours(startDay.getHours() + 1);
        }
    } else {
        while (startDay.getTime() <= endDay.getTime()) {
            let month = (startDay.getMonth() + 1);
            month = month < 10 ? '0' + month : month;
            let day = startDay.getDate();
            day = day < 10 ? '0' + day : day;
            resDayIncludeYear.push(startDay.getFullYear() + '-' + month + '-' + day);
            resDay.push(month + '-' + day);
            startDay.setDate(startDay.getDate() + 1);
        }
    }
    return resDay;
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
        let strRGBA = 'rgba(' + RGB_1 + ',' + RGB_2 + ',' + RGB_3 + ',0.5)'

        dataToSendToChart.push(
            {
                data: dataBeforeSendingToChart[i],
                label: i + 1,
                borderColor: strRGBA,
                fill: false
            }
        )
    }
    return dataToSendToChart
}

/* 
그래프 관련 값 변경 시 실행 함수
*/
function doSubmit() {
    const dateArray = addTimeToDate()
    const startDateTime = dateArray[0]
    const endDateTime = dateArray[1]

    // 방 번호
    const roomNum = document.getElementById('roomNum').value;
    // JSON 형태의 보낼 데이터에 시작 날짜, 종료 날짜, 방 번호를 담는다
    const postData = JSON.stringify({ 'startDate': startDateTime, 'endDate': endDateTime, 'roomNum': roomNum });
    // 중간 기간 계산 함수
    const middleDate = getDateRangeData(startDateTime, endDateTime);

    // 데이터 전송
    sendAndReceiveData(postData);
    // 차트에 넣을 데이터
    const chartData = createDataForChartUse();

    // 차트 업데이트
    // x축 라벨
    myChart.data.labels = middleDate
    // 데이터 셋
    myChart.data.datasets = chartData
    myChart.update();
    myChart.options.animation.duration = 1000 // 초기 호출 이후 차트 업데이트 시 애니메이션 적용


}
doSubmit()