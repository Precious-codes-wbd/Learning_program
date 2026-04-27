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

// Example: simple verification
(() => {
    'use strict'
    const forms = document.querySelectorAll('.needs-validation')
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event =>{
            if (!form.checkValidity()){
                event.preventDefault()
                event.stopPropagation()
            }
            form.classList.add('was-validated')
        }, false)
    })
})()