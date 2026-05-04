// Dark-Mode
document.addEventListener("DOMContentLoaded", () => {

    let darkmode = localStorage.getItem('darkmode');
    const themeSwitch = document.getElementById('theme-switch');

    const enableDarkmode = () => {
        document.body.classList.add('darkmode');
        localStorage.setItem('darkmode', 'active');
    }

    const disableDarkmode = () => {
        document.body.classList.remove('darkmode');
        localStorage.removeItem('darkmode');
    }

    if(darkmode === "active") enableDarkmode();

    themeSwitch.addEventListener("click", () => {
        darkmode = localStorage.getItem('darkmode');
        darkmode !== "active" ? enableDarkmode() : disableDarkmode();
    });


})


console.log("Precious")

// Image Slider
const slides = document.querySelectorAll(".slide");
let current = 0;
document.getElementById("next").addEventListener("click", () => {
    slides[current].style.display = "none";
    current = (current + 1) % slides.length;
    slides[current].style.display = "block";
});

// To-do List
document.getElementById("addTask").addEventListener("click", () => {
    const input = document.getElementById("taskInput");
    if(input.value !== ""){
        const li = document.createElement("li");
        li.innerText = input.value;
        li.addEventListener("click", () => li.remove());
        document.getElementById("taskList").appendChild(li);
        input.value = "";
    }
});

// Modal Popup
const modal = document.getElementById("modal");
document.getElementById("openModal").addEventListener("click", () => {
    modal.style.display = "block";
})
document.getElementById("closeModal").addEventListener("click", () =>{
    modal.style.display = "none"
})


// Sample....
const heading = document.getElementById("myHeading");
heading.style.color ="blue";
const boxes = document.getElementsByClassName("box");
boxes[0].style.backgroundColor = "yellow";