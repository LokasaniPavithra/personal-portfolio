const roles = [
    "Full Stack Developer",
    "Python Developer"
];

let roleIndex = 0;
let charIndex = 0;
let currentText = "";
let isDeleting = false;

const typingElement = document.getElementById("typing-text");

function type() {

    const fullText = roles[roleIndex];

    if (!isDeleting) {
        currentText = fullText.substring(0, charIndex + 1);
        charIndex++;
    } else {
        currentText = fullText.substring(0, charIndex - 1);
        charIndex--;
    }

    typingElement.textContent = currentText;

    let speed = 100;

    if (isDeleting) {
        speed = 50;
    }

    if (!isDeleting && charIndex === fullText.length) {
        speed = 1500;
        isDeleting = true;
    }

    if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex++;

        if (roleIndex === roles.length) {
            roleIndex = 0;
        }
    }

    setTimeout(type, speed);
}

type();