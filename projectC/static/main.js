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

/* 기간 제출시 실행 함수
기간 입력으로부터 값을 받아와서 중간 기간 계산 함수를 통해
중간 기간 어레이를 생성한 후
차트의 라벨값을 해당 어레이로 변경 후 차트 업데이트
*/
function doSubmit() {
    let startDate = document.getElementById('startDate').value; // 시작 날짜
    let endDate = document.getElementById('endDate').value; // 마지막 날짜
    let middleDate = getDateRangeData(startDate, endDate) // 이건 날짜 범위를 구하기 위한 함수 
    myChart.data.labels = middleDate // 그래프 라벨을 그려주기 위함
    myChart.update(); // 그래프 업데이트
    myChart.options.animation.duration = 1000 // 초기 호출 이후 차트 업데이트 시 애니메이션 적용
}
doSubmit()



// var colorNames = Object.keys(window.chartColors);
// // chartColor는 아래 차트 옵션에 정의되어 있음
// // 데이터셋 추가 버튼 
// document.getElementById('addDataset').addEventListener('click', function () {
// 	var colorNames = Object.keys(window.chartColors);
// 	// 새로운 데이터셋 세팅 
// 	var newData = {
// 		// 라벨 
// 		label: 'Dataset',
// 		// 꼭지점
// 		backgroundColor: '',
// 		// 라인색 
// 		borderColor: '',
// 		data: [],
// 	};

// 	var fill = [
// 		'end',
// 		'start', 
// 		'origin', 
// 		false 
// 	];

// 	for (let index = 0; index < 4; index++) {
// 		// 데이터 세팅 
// 		var settingData = JSON.parse(JSON.stringify(newData));
// 		// 배경
// 		settingData.backgroundColor = chartColors[colorNames[index + 1]];
// 		// 선색
// 		settingData.borderColor = chartColors[colorNames[index + 2]];
// 		// 라벨
// 		settingData.label = 'new Data line' + (index + 1) + '/ Fill=' + fill[index];
// 		// 채우기 옵션
// 		settingData.fill = fill[index];
// 		// 데이터 채우기 
// 		for(var i = 0; i < Chart.instances[0].config.data.datasets[0].data.length; i++){
// 			settingData.data.push(randomScalingFactor());
// 		}
// 		// 데이터 반영 
// 		Chart.instances[index].data.datasets.push(settingData);
// 		// 라인 차트 업데이트 
// 		Chart.instances[index].update();
// 	}
// });

//