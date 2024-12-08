window.addEventListener('transform', () => {
    const elements = document.querySelectorAll('.header-platform, section');
    elements.forEach(el => {
        el.style.transform = 'scale(1)'; // Временное изменение
        setTimeout(() => el.style.transform = '', 0); // Сброс
    });
});

window.addEventListener('scroll', () => {
    const elements = document.querySelectorAll('.header-platform, section');
    elements.forEach(el => {
        el.style.willChange = 'transform'; // Декларация для плавности
        setTimeout(() => el.style.willChange = '', 100); // Сброс
    });
});

