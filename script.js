// script.js

// ⏳ Timer logic for practice.html
function startTimer(duration, display) {
    let timer = duration, minutes, seconds;
    const interval = setInterval(() => {
        minutes = String(Math.floor(timer / 60)).padStart(2, '0');
        seconds = String(timer % 60).padStart(2, '0');
        display.textContent = `${minutes}:${seconds}`;

        if (--timer < 0) {
            clearInterval(interval);
            alert("Time's up!");
            // You can also auto-submit here if needed
        }
    }, 1000);
}

window.addEventListener('DOMContentLoaded', () => {
    const timerElement = document.getElementById('time');
    if (timerElement) {
        const duration = 10 * 60; // 10 minutes
        startTimer(duration, timerElement);
    }
});