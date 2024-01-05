
const timeDisplay = document.getElementById('time');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');
const listBox = document.getElementById('listbox');

let isRunning = false;
let stopwatch;
let startTime;
let elapsedTime = 0;
let laps = [];

let milliseconds;
let seconds;
let formattedSeconds;
let formattedMilliseconds;
// 스톱워치 업데이트
function updateStopwatch() {
    const currentTime = Date.now();
    elapsedTime = currentTime - startTime;
    displayTime(elapsedTime);
}

// 시간을 mm:ss 형식으로 표시
function displayTime(time) {
    milliseconds = Math.floor((time % 1000) / 10);
    seconds = Math.floor((time / 1000) % 60);

    formattedSeconds = seconds.toString().padStart(2, '0');
    formattedMilliseconds = milliseconds.toString().padStart(2, '0');
    const formattedTime = formattedSeconds + " : " + formattedMilliseconds;
    timeDisplay.textContent = formattedTime;
}
// 스톱워치 시작
function startStopwatch() {
    if (!isRunning) {
        isRunning = true;
        startTime = Date.now() - elapsedTime;

        stopwatch = setInterval(updateStopwatch, 10);
    }
}

// 스톱워치 일시 정지
function stopStopwatch() {
    if (isRunning) {
        isRunning = false;
        clearInterval(stopwatch);
    }
    makeRecord();
}

// 스톱워치 초기화
function resetStopwatch() {
    if (isRunning) {
        isRunning = false;
        clearInterval(stopwatch);
    }
    elapsedTime = 0;
    laps = [];
    displayTime(0);
}

function makeRecord() {
    const li = document.createElement('li');
    const div = document.createElement('div');
    div.classList.add("checkbox");
    const inputBox = document.createElement("input");
    inputBox.setAttribute("type", "checkbox");
    inputBox.setAttribute("id", "listCheck");
    const label = document.createElement('label');
    label.setAttribute('for', 'listCheck');
    div.appendChild(inputBox);
    div.appendChild(label);
    li.appendChild(div);
    const span = document.createElement('span');
    span.innerText = formattedSeconds + " : " + formattedMilliseconds;
    li.appendChild(span);
    listBox.appendChild(li);

    console.log(listBox);
}

// 이벤트 리스너 추가
startButton.addEventListener('click', startStopwatch);
stopButton.addEventListener('click', stopStopwatch);
resetButton.addEventListener('click', resetStopwatch);

function deleteCheckedItems() {
    const checkboxes = document.querySelectorAll('#listbox input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            const listItem = checkbox.parentElement.parentElement;
            listItem.remove();
        }
    });
}

const listCheckAll = document.getElementById('listCheckAll');

// listCheckAll 체크박스 변경 이벤트 핸들러
listCheckAll.addEventListener('change', function() {
    // listCheckAll의 상태에 따라 모든 li 안의 체크박스 상태 변경
    var listItems = document.querySelectorAll('#listbox li input[type="checkbox"]');
    listItems.forEach(function(item) {
        item.checked = listCheckAll.checked;
    });
});


const trashcanIcon = document.getElementById('trashcan');
trashcanIcon.addEventListener('click', deleteCheckedItems);