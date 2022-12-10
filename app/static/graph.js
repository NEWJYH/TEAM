let defaultStart = 0;

/** input 태그 디폴트 설정하는 함수 */
function defaultOption() {
    const today = new Date();
    const lastWeek = new Date();
    lastWeek.setDate(today.getDate() - 7)
    // 오늘과 지난주를 기간 인풋에 넣을 수 있는 형태로 만듦
    let day = today.getDate()
    day = day < 10 ? '0' + day : day;
    let lastWeekDay = lastWeek.getDate()
    lastWeekDay = lastWeekDay < 10 ? '0' + lastWeekDay : lastWeekDay

    let month = today.getMonth() + 1
    month = month < 10 ? '0' + month : month;
    let lastWeekMonth = lastWeek.getMonth() + 1
    lastWeekMonth = lastWeekMonth < 10 ? '0' + lastWeekMonth : lastWeekMonth

    const forDefault = today.getFullYear() + '-' + month + '-' + day;
    const forStartDefault = lastWeek.getFullYear() + '-' + lastWeekMonth + '-' + lastWeekDay;
    // 기간 인풋 기본값 설정
    document.getElementById('endDate').value = forDefault
    document.getElementById('endDate2').value = forDefault
    document.getElementById('endDate3').value = forDefault

    document.getElementById('startDate').value = forStartDefault
    document.getElementById('startDate2').value = forStartDefault
    document.getElementById('startDate3').value = forStartDefault

    // 기간 인풋의 최대 최소값 설정
    document.getElementById('endDate').setAttribute('max', forDefault)
    document.getElementById('endDate2').setAttribute('max', forDefault)
    document.getElementById('endDate3').setAttribute('max', forDefault)

    document.getElementById('startDate').setAttribute('max', forDefault)
    document.getElementById('startDate2').setAttribute('max', forDefault)
    document.getElementById('startDate3').setAttribute('max', forDefault)

    document.getElementById('endDate').setAttribute('min', document.getElementById('startDate').value)
    document.getElementById('endDate2').setAttribute('min', document.getElementById('startDate2').value)
    document.getElementById('endDate3').setAttribute('min', document.getElementById('startDate3').value)
}
defaultOption()

/**
input name='unit' or 'unit2' 변경시               
시간 선택 메뉴 시각화 여부를 변경하고                    
input id='startDate' or 'startDate2'의 기본값 변경하는 함수
*/
function changeUnitOfTime(i) {
    const today = new Date();

    let day = today.getDate()
    day = day < 10 ? '0' + day : day;
    let month = today.getMonth() + 1
    month = month < 10 ? '0' + month : month;
    const forCheckTime = today.getFullYear() + '-' + month + '-' + day;

    let checkUnitOfTime = document.querySelector('input[name="unit"]:checked').value;
    let startTimeDiv = document.getElementById('startTimeSpace');
    let endTimeDiv = document.getElementById('endTimeSpace');
    let startTimeArea = document.getElementById('selectStartTime');
    let endTimeArea = document.getElementById('selectEndTime');
    let startDateInput = document.getElementById('startDate');
    let endDateInput = document.getElementById('endDate');
    let endTimeForToday = document.getElementById(today.getHours());
    let twentyThree = document.getElementById(23);

    if (i == 1) { } else if (i == 2) {
        checkUnitOfTime = document.querySelector('input[name="unit2"]:checked').value;
        startTimeDiv = document.getElementById('startTimeSpace_2');
        endTimeDiv = document.getElementById('endTimeSpace_2');
        startTimeArea = document.getElementById('selectStartTime2');
        endTimeArea = document.getElementById('selectEndTime2');
        startDateInput = document.getElementById('startDate2');
        endDateInput = document.getElementById('endDate2');
        endTimeForToday = document.getElementById(today.getHours() + '_2');
        twentyThree = document.getElementById('23_2');
    } else if (i == 3) {
        checkUnitOfTime = document.querySelector('input[name="unit3"]:checked').value;
        startTimeDiv = document.getElementById('startTimeSpace_3');
        endTimeDiv = document.getElementById('endTimeSpace_3');
        startTimeArea = document.getElementById('selectStartTime3');
        endTimeArea = document.getElementById('selectEndTime3');
        startDateInput = document.getElementById('startDate3');
        endDateInput = document.getElementById('endDate3');
        endTimeForToday = document.getElementById(today.getHours() + '_3');
        twentyThree = document.getElementById('23_3');
    }

    if (checkUnitOfTime === 'hour') {
        startTimeDiv.style.display = 'block';
        endTimeDiv.style.display = 'block';
        endTimeDiv.style.margin = '6px 0px 0px 0px';
        startTimeArea.style.display = 'inline';
        endTimeArea.style.display = 'inline';
        startDateInput.value = endDateInput.value
    } else {
        startTimeDiv.style.display = 'inline-block';
        endTimeDiv.style.display = 'inline-block';
        endTimeDiv.style.margin = '0px 0px 0px 6px';
        startTimeArea.style.display = 'none';
        endTimeArea.style.display = 'none';
        const endInputDate = endDateInput.value
        const timeToDayInput = new Date();
        timeToDayInput.setFullYear(endInputDate.substr(0, 4))
        timeToDayInput.setMonth(endInputDate.substr(5, 2) - 1)
        timeToDayInput.setDate(endInputDate.substr(8, 2))
        timeToDayInput.setDate(timeToDayInput.getDate() - 7)

        let day = timeToDayInput.getDate()
        day = day < 10 ? '0' + day : day;
        let month = timeToDayInput.getMonth() + 1
        month = month < 10 ? '0' + month : month;

        startDateInput.value = timeToDayInput.getFullYear() + '-' + month + '-' + day
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
    } else if (i == 3) {
        document.getElementById('startDate3').setAttribute('max', document.getElementById('endDate3').value)
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
    } else if (i == 3) {
        document.getElementById('endDate3').setAttribute('min', document.getElementById('startDate3').value)
    }
}

/**
기간 입력과 시간 입력 값을 가져와    
어레이에 '단위', '시작 날짜', '시작 시간', '종료 날짜', '종료 시간'을 담는 함수
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
    } else if (i == 3) {
        checkUnitOfTime = document.querySelector('input[name="unit3"]:checked').value;
        startHourValue = document.getElementById('startTime3').value;
        endHourValue = document.getElementById('endTime3').value;
        startDateInput = document.getElementById('startDate3');
        endDateInput = document.getElementById('endDate3');
    }

    const startDate = startDateInput.value;
    const endDate = endDateInput.value;

    let startTime = '';
    let endTime = '';
    let unit = 0;

    if (checkUnitOfTime === 'hour') {
        if (parseInt(startHourValue) < 10) {
            startTime = '0' + startHourValue + ':00';
        } else {
            startTime = startHourValue + ':00';
        }
        if (parseInt(endHourValue) < 10) {
            endTime = '0' + endHourValue + ':00';
        } else {
            endTime = endHourValue + ':00';
        }
        unit = 1;
    } else {
        unit = 0;
    }
    const timeArray = [unit, startDate, startTime, endDate, endTime]
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
    } else if (i == 3) {
        checkUnitOfTime = document.querySelector('input[name="unit3"]:checked').value;
    }
    const resDay = [];
    const toCompare = [];
    let startDay = new Date(param1);
    let endDay = new Date(param2);
    if (checkUnitOfTime === 'hour') {
        while (startDay.getTime() <= endDay.getTime()) {
            let year = startDay.getFullYear()
            let month = (startDay.getMonth() + 1);
            month = month < 10 ? '0' + month : month;
            let day = startDay.getDate();
            day = day < 10 ? '0' + day : day;
            let hour = startDay.getHours();
            hour = hour < 10 ? '0' + hour : hour;
            resDay.push(startDay.getHours());
            toCompare.push(year + '-' + month + '-' + day + ' ' + hour);
            startDay.setHours(startDay.getHours() + 1);
        }
    } else {
        while (startDay.getTime() <= endDay.getTime()) {
            let year = startDay.getFullYear()
            let month = (startDay.getMonth() + 1);
            month = month < 10 ? '0' + month : month;
            let day = startDay.getDate();
            day = day < 10 ? '0' + day : day;
            resDay.push(month + '-' + day);
            toCompare.push(year + '-' + month + '-' + day);
            startDay.setDate(startDay.getDate() + 1);
        }
    }
    return [resDay, toCompare];
}

/**
히든 태그의 밸류값을 JSON형태로 가져와
소 마리수를 for문을 통해 가져온 뒤
해당 수만큼 차트에 넣을 데이터를 차트용 데이터셋에 푸쉬
*/
function createDataForChartUse(i, param2, toCompare) {
    let dataType = '';
    if (i == 1) {
        dataType = 'meal';
    } else if (i == 2) {
        dataType = 'distance';
    } else if (i == 3) {
        dataType = 'water';
    }

    let postDataValue = JSON.parse(param2)
    // console.log(postDataValue)
    // key값이 'data'인 데이터의 value를 변수에 담는다
    let dataByDate = postDataValue.data
    // console.log(dataByDate)
    // key값 추출
    let keys = Object.keys(dataByDate);
    // console.log(keys)
    // 소 마리 수 추출
    let endCount = 0;
    keys.forEach((key) => {
        let count = 0;
        let dailyData = dataByDate[key]
        // console.log(dailyData)
        let dailyDataKeys = Object.keys(dailyData);
        dailyDataKeys.forEach((key) => {
            count++;
            // console.log(unitdata[key])
            if (endCount < count) {
                endCount = count;
            }
        });
    });
    // console.log(endCount)

    // 데이터를 차트에 보내기 전에 임시로 담아놓을 데이터 어레이
    let dataBeforeSendingToChart = [];
    // 임시 데이터 어레이 안에 소 마리수 만큼의 어레이 생성 
    for (i = 0; i < endCount; i++) {
        dataBeforeSendingToChart.push([])
    }

    let IDArray = [];

    toCompare.forEach(element => {
        if (element in dataByDate) {
            let dailyData = dataByDate[element]
            for (i = 0; i < endCount; i++) {
                if (i + 1 in dailyData) {
                    if (!i + 1 in IDArray) {
                        IDArray.push(i + 1)
                    }
                    dataBeforeSendingToChart[i].push(dailyData[i + 1][dataType])
                } else {
                    dataBeforeSendingToChart[i].push(null)
                }
            }
        } else {
            for (i = 0; i < endCount; i++) {
                dataBeforeSendingToChart[i].push(null)
            }
        }
    });

    // 날짜별로 되어있는 데이터를 소ID별로 분류해 임시 데이터 어레이에 푸쉬
    keys.forEach((key) => {
        let count = 0;
        let dailyData = dataByDate[key]
        let dailyDataKeys = Object.keys(dailyData);
        dailyDataKeys.forEach((key) => {
            // console.log(dailyData[key])
            // if (!key in IDArray) {
            //     IDArray.push(key)
            // }
            IDArray.push(key)
            dataBeforeSendingToChart[parseInt(key) - 1].push(dailyData[key][dataType])
            count++;
        });
    });
    // console.log(dataBeforeSendingToChart[0])

    // 선 색상
    const lineColor = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    // 임시 데이터 어레이의 데이터를 차트에 보낼 형식으로 만든다
    let dataToSendToChart = [];
    for (i = 0; i < endCount; i++) {
        dataToSendToChart.push(
            {
                data: dataBeforeSendingToChart[i],
                label: IDArray[i] + '번 소',
                borderColor: lineColor[i],
                borderWidth: 2,
                pointRadius: 0,
                tension: 0,
                fill: false
            }
        )
    }
    // console.log(dataToSendToChart);
    return dataToSendToChart
}

/**
보낼 데이터를 입력으로 받고,
해당 데이터를 보내서 받아온 데이터를 히든 태그의 value에 저장 
*/
function sendAndReceiveData(i, postData, middleDate, toCompare) {
    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            let data = JSON.parse(xhr.responseText);
            // 차트에 넣을 데이터
            let chartData = createDataForChartUse(i, data, toCompare);

            let chart = foodChart
            if (i == 1) { } else if (i == 2) {
                chart = activeChart
            } else if (i == 3) {
                chart = waterChart
            }

            if (defaultStart == 0) {
                let chartData2 = createDataForChartUse(2, data, toCompare);
                let chart2 = activeChart;
                chart2.data.labels = middleDate
                chart2.data.datasets = chartData2
                chart2.update();
                chart2.options.animation.duration = 1000
                let chartData3 = createDataForChartUse(3, data, toCompare);
                let chart3 = waterChart;
                chart3.data.labels = middleDate
                chart3.data.datasets = chartData3
                chart3.update();
                chart3.options.animation.duration = 1000
                defaultStart++;
            }

            // 차트 업데이트
            // x축 라벨
            chart.data.labels = middleDate
            // 데이터 셋
            chart.data.datasets = chartData
            chart.update();
            chart.options.animation.duration = 1000
        }
    };
    xhr.open("POST", "/graph/post");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(postData);
}

/**
선택 사항 제출 시 실행 함수
*/
function doSubmit(i) {
    const dateArray = addTimeToDate(i)

    // 방 번호
    const cctvNum = document.querySelector('input[name="cctvNum"]:checked').value;
    // console.log(cctvNum)
    // JSON 형태의 보낼 데이터에 시작 날짜, 종료 날짜, 방 번호를 담는다
    const data = { formtype: dateArray[0], startday: dateArray[1], starttime: dateArray[2], endday: dateArray[3], endtime: dateArray[4], cctvnum: parseInt(cctvNum) }
    // console.log(data)
    const postData = JSON.stringify(data);

    // 중간 기간 계산 함수
    let startDateTime = dateArray[1];
    let endDateTime = dateArray[3];
    if (dateArray[0] == 1) {
        startDateTime = dateArray[1] + ' ' + dateArray[2];
        endDateTime = dateArray[3] + ' ' + dateArray[4];
    }
    const middleDate = getDateRangeData(startDateTime, endDateTime, i);

    // 데이터 전송
    // console.log(middleDate[1]);
    sendAndReceiveData(i, postData, middleDate[0], middleDate[1]);
}
// doSubmit(1)
// doSubmit(2)
// doSubmit(3)

let forCheck = 0;
function changeVisible() {
    let style = document.getElementById('cctvListFrame')
    // console.log(window.getComputedStyle(style).display)
    // console.log(document.getElementById('checkVisible').checked)
    // if (forCheck == 0) {
    //     document.getElementById('cctvListFrame').style.display = 'block';
    //     forCheck = 1;
    // } else if (forCheck == 1) {
    //     // console.log('왜 안됨?')
    //     // changeCCTV('forCheck')
    //     forCheck = 0;
    // }
    if (document.getElementById('checkVisible').checked == true) {
        document.getElementById('cctvListFrame').setAttribute('style', 'display: block;')
    } else if (document.getElementById('checkVisible').checked == false) {
        // console.log('왜 안됨?')
        document.getElementById('cctvListFrame').setAttribute('style', 'display: none;')
    }
    // if (window.getComputedStyle(style).display == 'none') {
    // } else {
    //     document.getElementById('cctvListFrame').setAttribute('style', 'display: none;')
    //     document.getElementById('checkVisible').checked == false
    // }
}

function changeCCTV(i) {
    if (i == 'forCheck') {
    } else {
        cctvNum = i + 1
        document.getElementById('defaultText').innerText = cctvNum + '번 CCTV';
    }

    document.getElementById('cctvListFrame').style.display = 'none';
    document.getElementById('checkVisible').checked = false
    // forCheck = 0;
}

let style = document.getElementById('cctvListFrame')
document.querySelector("body").addEventListener("click", function (e) {
    // console.log(e.target.id)
    // console.log(forCheck)
    if (e.target.id == e.currentTarget.querySelector("#checkVisible").id) {
    } else {
        // console.log("wrong")
        document.getElementById('cctvListFrame').style.display = 'none';
        document.getElementById('checkVisible').checked = false
    }
})
