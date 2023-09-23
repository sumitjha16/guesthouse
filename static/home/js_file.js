var i = 0;
var txt = 'Welcome to Heart of Chennai!';
var speed = 80;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("typing-effect").textContent += txt[i];
    i++;
    setTimeout(typeWriter, speed);
  }
}
window.onload = function() {
  typeWriter();
};


