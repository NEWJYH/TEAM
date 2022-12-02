let cctvChoice = ''; // cctv 선택값
let cctvImg = ''; // 보여지는 cctv img 태그
let mapImg = ''; // 보여지는 map img 태그
let cctvUrl = ''; // cctv src 경로
let imgUrl = ''; // map src 경로

function changeCCTVNum() {
    cctvChoice = document.getElementById("CCTVNum").value
    mapImg = document.getElementById('mapImg')
    cctvImg = document.getElementById('cctvImg')

    cctvUrl = '/cv_live/stream_video';
    imgUrl = '/static/img/' + cctvChoice + '.png';

    cctvImg.setAttribute('src', cctvUrl)
    mapImg.setAttribute('src', imgUrl);
};