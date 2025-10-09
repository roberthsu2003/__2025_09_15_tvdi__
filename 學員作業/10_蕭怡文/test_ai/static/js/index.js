document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', function () {
            menuToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // 點擊選單項目時關閉選單
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', function () {
                menuToggle.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });

        // 點擊選單外部時關閉選單
        document.addEventListener('click', function (event) {
            if (!event.target.closest('nav')) {
                menuToggle.classList.remove('active');
                navLinks.classList.remove('active');
            }
        });
    }
});