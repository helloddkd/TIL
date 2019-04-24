/* 1. <input> 태그 안의 값을 잡는다. */
const inputArea= document.querySelector('#js-userinput');
const button = document.querySelector('#js-go');
const resultArea = document.querySelector('#result-area');


const init = () => {
    inputArea.addEventListener('keydown', e => {
        if (e.code === 'Enter') {
            searchAndPush(inputArea.value);
        }
    });
    button.addEventListener('click', e => {
        searchAndPush(inputArea.value);
    });
};
init()
/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */

//AJAX 요청을 보낸다
/*
기존의 요청
1. 링크누른다
2. href로 요청간다
3. 새로고침 후 응답을 render한다.
 */
/*
AJAX 요청 => Single Page Application SPA
1. 어떤 event가 발생한다.
2. 요청을 전송하고, 응답이 도착할 때까지 기다린다. 화면전환은 없다!
3. 응답이 오면 지금문서에서 응답내용을 추가로 render한다.
 */


/* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */



const searchAndPush = keyword => {
    const KEY = 'VACXg5oPq5dSZGzY3OxDKPlmkxL6vrqk';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;

    const AJAXCall = new XMLHttpRequest(); //AJAX 요청을 보내줄 친구
    AJAXCall.open('GET', URL); //요청발사준비끝
    AJAXCall.send();
    AJAXCall.addEventListener('load', e=>{
        const parsedData = JSON.parse(e.target.response);
        pushToDOM(parsedData);
    })
    const pushToDOM = dataset => {
        resultArea.innerHTML = null;
        const dataArray = dataset.data;
        for (const imgData of dataArray) {
            imgURL = imgData.images.fixed_height.url;
            element = document.createElement('img');
            element.src = imgURL;
            element.classList.add('container-image');
            element.alt = imgData.title;
            resultArea.appendChild(element);
        };
    }
}