let level = 1;
let sec = 0;
let min = 0;
let timeinterval = null;
let opertaors = ['+', '-', '*', '/' , '%'];
let fNumber;
let lNumber;
let selectedOperator;
let qnumber = 1;
let answeList = [];

// ------------------
const selectElement = document.getElementById('level-select');
const minElement = document.getElementById('min');
const secElement = document.getElementById('sec');
const questionElement = document.getElementById('question');
const answerElement = document.getElementById('answer');
const operatorElement = document.getElementById('op');
const fnumElement = document.getElementById('f-number');
const lnumElement = document.getElementById('l-number');




// ------------------




// ------------------

const start = () => {
    manageTime();
}

// ------------------

// const manageTime = () => {
//     min = 0;
//     sec = 0;
//     clearInterval(timeinterval);
//     timeinterval = setInterval(() => {
//         console.log(new Date().toISOString().split('T')[1].split('.')[0]);
//         console.log()
//     }, 1000);
// }

const manageTime = () => {
    let min = '00'; // Set initial minutes to 10
    let sec = '00';  // Set initial seconds to 0
    secElement.textContent = sec; // Display the seconds
    minElement.textContent = min; // Display the minutes

    generateQueston(level);

    clearInterval(timeinterval); // Clear any existing interval
    
    timeinterval = setInterval(() => {
        sec++; // Increment seconds by 1
        if (sec === 60) { // If seconds reach 60
            min++; // Increment minutes by 1
            sec = 0; // Reset seconds
        }
        sec = sec % 60; // Reset seconds
        sec = 10 > sec ? `0${sec}` : sec; // Add leading zero to seconds
        min = min % 10; // Reset minutes
        min = 10 > min ? `0${min}` : min; // Add leading zero to minutes

        secElement.textContent = sec // Display the seconds
        minElement.textContent = min; // Display the minutes
        // Display the time in MM:SS format
        console.log(`${String(min).padStart(2, '0')}:${String(sec).padStart(2, '0')}`);
        
    }, 1000); // Update the time every second
}


// ------------------

const generateQueston = (selectLevel) => { 

    let maxNumber = 10;

    if(selectLevel == 2) {
        maxNumber = 50;
    } else  if (selectLevel == 3) {
        maxNumber = 100;
    }

    fNumber = Math.floor(Math.random() * maxNumber) + 1;
    lNumber = Math.floor(Math.random() * maxNumber) + 1;
    selectedOperator = opertaors[Math.floor(Math.random() * 5)];

    operatorElement.textContent = selectedOperator;
    fnumElement.textContent = fNumber;
    lnumElement.textContent = lNumber;

}


const submitData = () => {
    let answer = 0;
    if (selectedOperator && fNumber && lNumber) {
        fNumber = parseInt(fNumber);
        lNumber = parseInt(lNumber);
        switch (selectedOperator) {
            case '+':
                answer = fNumber + lNumber;
                break;
            case '-':
                answer = fNumber - lNumber;
                break;
            case '*':
                answer = fNumber * lNumber;
                break;
            case '/':
                answer = fNumber / lNumber;
                break;
            case '%':
                answer = fNumber % lNumber;
                break;
            default:
                alert("Something went wrong");
                break;
        }
        console.log(answer);
        console.log(answerElement.value);
        if (answer == parseInt(answerElement.value)) {
            alert('Correct Answer');
            manageTime();
        } else {
            alert('Wrong Answer');
            manageTime();
        }

        let obj = {
                "q number": qnumber,
                "Time": `${min}:${sec}`,
                "Level": level,
                "Question": `${fNumber} ${selectedOperator} ${lNumber}`,
                "Answer": answer,
                "User Answer": parseInt(answerElement.value),
                "Correct": true,
            }
            console.log(obj);
            answeList.push(obj);
            console.log(answeList);
            qnumber++;
    }
}

const skipQuiz = () => {
    let obj = {
        "q number": qnumber,
        "Time": `${min}:${sec}`,
        "Level": level,
        "Question": `${fNumber} ${selectedOperator} ${lNumber}`,
        "Answer": answer,
        "User Answer": parseInt(answerElement.value),
        "Correct": false,
    }
    console.log(obj);
    answeList.push(obj);
    manageTime();
    console.log(answeList);
    qnumber++;
                                                                                                                                                                         
}