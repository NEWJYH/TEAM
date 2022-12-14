function changeVisible() {
    let style = document.getElementById('cctvListFrame')
    // console.log(window.getComputedStyle(style).display)
    // console.log(confirmVisible)
    if (window.getComputedStyle(style).display == 'none') {
        document.getElementById('cctvListFrame').setAttribute('style', 'display: block;')
    } else {
        document.getElementById('cctvListFrame').setAttribute('style', 'display: none;')
    }
}

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

// function changeCCTV(i) {
//     cctvNum = i + 1
//     document.getElementById('defaultText').innerText = cctvNum + '번 CCTV';
//     document.getElementById('cctvListFrame').setAttribute('style', 'display: none;')
// }

let cctvChoice = ''; // cctv 선택값
let cctvImg = ''; // 보여지는 cctv img 태그
let mapImg = ''; // 보여지는 map img 태그
let cctvUrl = ''; // cctv src 경로
let imgUrl = ''; // map src 경로

// function changeCCTVNum() {
//     cctvChoice = document.getElementById("CCTVNum").value
//     mapImg = document.getElementById('mapImg')
//     cctvImg = document.getElementById('cctvImg')

//     cctvUrl = '/cv_live/stream_video';
//     imgUrl = '/static/img/' + cctvChoice + '.png';

//     cctvImg.setAttribute('src', cctvUrl)
//     mapImg.setAttribute('src', imgUrl);
// };

const colorList = [
    '#ff0000', '#f77b3f', '#7abc50', '#2b654b',
    '#34345a', '#653275', '#8f2740', '#30854c'
];

const dataScale = [1280, 720];
let canvasScale = [320, 240];

const canvas = document.getElementById('mapCanvas');
/** @type {CanvasRenderingContext2D} */
const ctx = canvas.getContext("2d");

function drawCow(x, y, key) {
    ctx.beginPath();
    ctx.fillStyle = colorList[parseInt(key) - 1];
    let x1 = x * (canvas.width / dataScale[0]);
    // console.log(x1);
    let y1 = y * canvas.height / dataScale[1];
    // console.log(y1);
    ctx.arc(x1, y1, 7, 0, Math.PI * 2);
    ctx.fill();
    ctx.closePath();
}

function drawMap(param) {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // 전체 지우기
    // console.log(param)
    let ID = Object.keys(param);
    // console.log(ID)
    ID.forEach(key => {
        // console.log(param[key])
        drawCow(param[key].x, param[key].y, key)
    })
}

// setInterval(drawMap, 1000);

const data = {
    sec: 1,

}

let eachFrame = [];

function sendAndReceiveData() {
    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            // eachFrame = [];
            let minute = JSON.parse(JSON.parse(xhr.responseText));
            // console.log(minute)
            let minuteKeys = Object.keys(minute);
            minuteKeys.forEach(key => {
                let second = minute[key]
                // console.log(second)
                let secondKeys = Object.keys(second);
                secondKeys.forEach(key => {
                    // console.log(second[key])
                    eachFrame.push(second[key])
                })
            })
            // console.log(eachFrame)
            let i = 1;
            if (i == 1) {
                startUpdate()
                i = 2
            }
            data.sec += 60;
        };
    };
    postdata = JSON.stringify(data)
    xhr.open("POST", "/live/post2");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(postdata);
};

sendAndReceiveData();
setInterval(sendAndReceiveData, 30000);

const mapFunction = {
    isPause: false,
    draw: null
}
let start = '';
function startUpdate() {
    // start = new Date()
    mapFunction.isPause = false;
    mapFunction.draw = setInterval(updateMap, 78);
}

function stopUpdate() {
    // let end = new Date()
    // console.log(end.getTime() - start.getTime())
    clearInterval(mapFunction.draw);
    mapFunction.isPause = true;
    count = 0;
}

let count = 0;
function updateMap() {
    if (!mapFunction.isPause) {
        drawMap(eachFrame[count])
        // console.log(count)
        count++;
        if (count + 1 in eachFrame) {
        } else { stopUpdate() }
    }
}