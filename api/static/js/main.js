// JavaScript for triggering fade-in animations on scroll
document.addEventListener("DOMContentLoaded", function() {
    const fadeInElements = document.querySelectorAll('.fade-in');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    });

    fadeInElements.forEach(element => {
        observer.observe(element);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const toggleSwitch = document.getElementById("dark-mode-toggle");
    const currentMode = localStorage.getItem("theme");

    // Check for saved mode and apply it
    if (currentMode === "dark") {
        document.body.classList.add("dark-mode");
        toggleSwitch.checked = true;
    }

    // Toggle dark mode on switch click
    toggleSwitch.addEventListener("change", () => {
        document.body.classList.toggle("dark-mode");

        // Save the preference in local storage
        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("theme", "dark");
        } else {
            localStorage.setItem("theme", "light");
        }
    });
});

console.log("JavaScript file is loaded!");


