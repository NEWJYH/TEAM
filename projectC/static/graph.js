/** input 태그 디폴트 설정하는 함수 */
function defaultOption() {
    const today = new Date();
    const lastWeek = new Date();
    lastWeek.setDate(today.getDate() - 7)

    // 오늘과 지난주를 기간 인풋에 넣을 수 있는 형태로 만듦
    const forDefault = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
    const forStartDefault = lastWeek.getFullYear() + '-' + (lastWeek.getMonth() + 1) + '-' + lastWeek.getDate()
    // 기간 인풋 기본값 설정
    document.getElementById('endDate').value = forDefault
    document.getElementById('endDate2').value = forDefault
    document.getElementById('startDate').value = forStartDefault
    document.getElementById('startDate2').value = forStartDefault
    // 기간 인풋의 최대 최소값 설정
    document.getElementById('endDate').setAttribute('max', forDefault)
    document.getElementById('endDate2').setAttribute('max', forDefault)
    document.getElementById('startDate').setAttribute('max', forDefault)
    document.getElementById('startDate2').setAttribute('max', forDefault)
    document.getElementById('endDate').setAttribute('min', document.getElementById('startDate').value)
    document.getElementById('endDate2').setAttribute('min', document.getElementById('startDate2').value)
}
defaultOption()

/**
input name='unit' or 'unit2' 변경시               
시간 선택 메뉴 시각화 여부를 변경하고                    
input id='startDate' or 'startDate2'의 기본값 변경하는 함수
*/
function changeUnitOfTime(i) {
    const today = new Date();
    const forCheckTime = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate()

    let checkUnitOfTime = document.querySelector('input[name="unit"]:checked').value;
    let startTimeArea = document.getElementById('selectStartTime');
    let endTimeArea = document.getElementById('selectEndTime');
    let startDateInput = document.getElementById('startDate');
    let endDateInput = document.getElementById('endDate');
    let endTimeForToday = document.getElementById(today.getHours());
    let twentyThree = document.getElementById(23);

    if (i == 1) { } else if (i == 2) {
        checkUnitOfTime = document.querySelector('input[name="unit2"]:checked').value;
        startTimeArea = document.getElementById('selectStartTime2');
        endTimeArea = document.getElementById('selectEndTime2');
        startDateInput = document.getElementById('startDate2');
        endDateInput = document.getElementById('endDate2');
        endTimeForToday = document.getElementById(today.getHours() + '_2');
        twentyThree = document.getElementById('23_2');
    }



    if (checkUnitOfTime === 'hour') {
        startTimeArea.style.display = 'inline';
        endTimeArea.style.display = 'inline';
        startDateInput.value = endDateInput.value
    } else {
        startTimeArea.style.display = 'none';
        endTimeArea.style.display = 'none';
        const endInputDate = endDateInput.value
        const timeToDayInput = new Date();
        timeToDayInput.setFullYear(endInputDate.substr(0, 4))
        timeToDayInput.setMonth(endInputDate.substr(5, 2) - 1)
        timeToDayInput.setDate(endInputDate.substr(8, 2))
        timeToDayInput.setDate(timeToDayInput.getDate() - 7)
        startDateInput.value = timeToDayInput.getFullYear() + '-' + (timeToDayInput.getMonth() + 1) + '-' + timeToDayInput.getDate()
    }

    if (endDateInput.value == forCheckTime) {
        endTimeForToday.setAttribute('selected', 'selected')
    } else {
        twentyThree.setAttribute('selected', 'selected')
    }
    endDateInput.setAttribute('min', startDateInput.value)
}

/** input id='endDate' or 'endDate2' 변경 시 시작 기간 제한하는 함수 */
function limitStartDate(i) {
    if (i == 1) {
        document.getElementById('startDate').setAttribute('max', document.getElementById('endDate').value)
    } else if (i == 2) {
        document.getElementById('startDate2').setAttribute('max', document.getElementById('endDate2').value)
    }
}

/** 
 * input id='startDate' or 'startDate2' 변경 시        
 * 끝 기간 제한하는 함수 
*/
function limitEndDate(i) {
    if (i == 1) {
        document.getElementById('endDate').setAttribute('min', document.getElementById('startDate').value)
    } else if (i == 2) {
        document.getElementById('endDate2').setAttribute('min', document.getElementById('startDate2').value)
    }
}

/**
일 단위 선택일 경우 기간만 가져오고        
시간 단위 선택일 경우 기간에 시간을 붙여서 가져와           
시작 기간과 끝 기간을 어레이로 반환하는 함수
*/
function addTimeToDate(i) {
    const today = new Date();

    let checkUnitOfTime = document.querySelector('input[name="unit"]:checked').value;
    let startHourValue = document.getElementById('startTime').value;
    let endHourValue = document.getElementById('endTime').value;
    let startDateInput = document.getElementById('startDate');
    let endDateInput = document.getElementById('endDate');

    if (i == 1) { } else if (i == 2) {
        checkUnitOfTime = document.querySelector('input[name="unit2"]:checked').value;
        startHourValue = document.getElementById('startTime2').value;
        endHourValue = document.getElementById('endTime2').value;
        startDateInput = document.getElementById('startDate2');
        endDateInput = document.getElementById('endDate2');
    }

    let startDateTime = '';
    let endDateTime = '';
    if (checkUnitOfTime === 'hour') {
        if (parseInt(startHourValue) < 10) {
            startDateTime = startDateInput.value + ' 0' + startHourValue + ':00';
        } else {
            startDateTime = startDateInput.value + ' ' + startHourValue + ':00';
        }
        if (parseInt(endHourValue) < 10) {
            endDateTime = endDateInput.value + ' 0' + endHourValue + ':00';
        } else {
            endDateTime = endDateInput.value + ' ' + endHourValue + ':00';
        }
    } else {
        startDateTime = startDateInput.value;
        endDateTime = endDateInput.value
    }
    const timeArray = [startDateTime, endDateTime]
    return timeArray
}

/**
중간 기간 계산 함수 
시작 기간과 종료 기간을 입력으로 받아 
중간 기간 어레이를 반환
*/
function getDateRangeData(param1, param2, i) {  //param1은 시작일, param2는 종료일이다.
    let checkUnitOfTime = document.querySelector('input[name="unit"]:checked').value;
    if (i == 1) { } else if (i == 2) {
        checkUnitOfTime = document.querySelector('input[name="unit2"]:checked').value;
    }
    const resDay = [];
    let startDay = new Date(param1);
    let endDay = new Date(param2);
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
            resDay.push(month + '-' + day);
            startDay.setDate(startDay.getDate() + 1);
        }
    }
    return resDay;
}

/**
보낼 데이터를 입력으로 받고,
해당 데이터를 보내서 받아온 데이터를 히든 태그의 value에 저장 
*/
function sendAndReceiveData(postData) {

    // XHR 객체 생성
    const xhr = new XMLHttpRequest();
    // 열기 메소드
    xhr.open('POST', '/graph/post', false);
    xhr.onload = function () {
        // console.log('READYSTATE', xhr.readyState);
        document.getElementById('hidden').value = xhr.responseText;
    }
    xhr.send(postData);
    console.log(postData);
}

/**
히든 태그의 밸류값을 JSON형태로 가져와
소 마리수를 for문을 통해 가져온 뒤
해당 수만큼 차트에 넣을 데이터를 차트용 데이터셋에 푸쉬
*/
function createDataForChartUse(i) {
    let dataType = '';
    if (i == 1) {
        dataType = 'food';
    } else if (i == 2) {
        dataType = 'active';
    }

    // let postDataValue = JSON.parse(document.getElementById('hidden').value)
    let postDataValue = JSON.parse(document.getElementById('testDataset').value)
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

    // console.log(dataByDate)
    // 날짜별로 되어있는 데이터를 소ID별로 분류해 임시 데이터 어레이에 푸쉬
    keys.forEach((key) => {
        let count = 0;
        let dailyData = dataByDate[key]

        let dailyDataKeys = Object.keys(dailyData);
        dailyDataKeys.forEach((key) => {
            dataBeforeSendingToChart[count].push(dailyData[key][dataType])
            count += 1;
        });
    });

    // 선 색상
    const lineColor = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    // 임시 데이터 어레이의 데이터를 차트에 보낼 형식으로 만든다
    let dataToSendToChart = [];
    for (i = 0; i < endCount; i++) {
        dataToSendToChart.push(
            {
                data: dataBeforeSendingToChart[i],
                label: i + 1 + '번 소',
                borderColor: lineColor[i],
                fill: false
            }
        )
    }
    return dataToSendToChart
}

/**
선택 사항 제출 시 실행 함수
*/
function doSubmit(i) {
    const dateArray = addTimeToDate(i)
    const startDateTime = dateArray[0]
    const endDateTime = dateArray[1]

    // 방 번호
    const roomNum = document.getElementById('CCTVNum').value;
    // JSON 형태의 보낼 데이터에 시작 날짜, 종료 날짜, 방 번호를 담는다
    const postData = JSON.stringify({ 'startday': startDateTime, 'endday': endDateTime, 'cctvnum': parseInt(roomNum) });
    // 중간 기간 계산 함수
    const middleDate = getDateRangeData(startDateTime, endDateTime, i);

    // 데이터 전송
    console.log(postData);
    sendAndReceiveData(postData);
    // 차트에 넣을 데이터
    const chartData = createDataForChartUse(i);

    let chart = foodChart
    if (i == 1) { } else if (i == 2) {
        chart = activeChart
    }
    // 차트 업데이트
    // x축 라벨
    chart.data.labels = middleDate
    // 데이터 셋
    chart.data.datasets = chartData
    chart.update();
    chart.options.animation.duration = 1000 // 초기 호출 이후 차트 업데이트 시 애니메이션 적용
}
doSubmit(1)
doSubmit(2)

/** CCTV 선택 변경 시 실행 함수. 선택사항들을 기본값으로 되돌린다. */
function changeCCTVNum() {
    defaultOption()
    document.getElementById('selectStartTime').style.display = 'none';
    document.getElementById('selectEndTime').style.display = 'none';
    document.getElementById('selectStartTime2').style.display = 'none';
    document.getElementById('selectEndTime2').style.display = 'none';
    changeUnitOfTime(1)
    changeUnitOfTime(2)
    doSubmit(1)
    doSubmit(2)
}