var quizAnswer = "";
var quizFailResultEl = undefined;
var quizSuccessResultEl = undefined

function renderPage() {
    
    const quizAnswerEl = document.getElementById("quiz_answer");
    quizAnswer = quizAnswerEl.innerHTML
    quizAnswerEl.remove();

    quizFailResultEl = document.getElementById("quiz_fail_result");
    quizSuccessResultEl = document.getElementById("quiz_success_result");

}


function submitQuiz() {
    user_answer = document.querySelector('input[name="answer"]:checked').value;
    
    if (quizAnswer == user_answer) {
        quizSuccessResultEl.style.display = "block";
        quizFailResultEl.style.display = "none";

    } else {
        quizSuccessResultEl.style.display = "none";
        quizFailResultEl.style.display = "block";
    }
    
}


window.onload = renderPage;