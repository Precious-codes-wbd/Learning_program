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

    console.log("JavaScript is working!!");

})
console.log("Precious")
const heading = document.getElementById("myHeading");
heading.style.color ="blue";
const boxes = document.getElementsByClassName("box");
boxes[0].style.backgroundColor = "yellow";