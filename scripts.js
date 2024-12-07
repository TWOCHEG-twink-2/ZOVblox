async function loadMarkdown(sectionId, filePath) {
    try {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`Не удалось загрузить файл ${filePath}`);
        }
        const text = await response.text();
        const markedContent = marked.parse(text); // Используется библиотека marked.js
        document.getElementById(sectionId).innerHTML = markedContent;
    } catch (error) {
        console.error(error);
        document.getElementById(sectionId).innerText = 'Ошибка загрузки содержимого: ' + error;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // Загрузка markdown содержимого
    loadMarkdown('section1', 'assets/content/section1.md');
    loadMarkdown('section2', 'assets/content/section2.md');
    loadMarkdown('section3', 'assets/content/section3.md');
    loadMarkdown('section4', 'assets/content/section4.md');
    loadMarkdown('section5', 'assets/content/section5.md');
    loadMarkdown('section6', 'assets/content/section6.md');

    // Массив с путями к изображениям
    const images = [
        'assets/img/zov_1.jpg',
        'assets/img/zov_2.jpg',
        'assets/img/zov_3.jpg',
        'assets/img/zov_4.jpg'
    ];

    // Выбираем случайное изображение
    const randomImage = images[Math.floor(Math.random() * images.length)];

    // Находим элемент header и применяем случайное изображение в качестве фона
    document.querySelector('header').style.setProperty('--background-image', `url(${randomImage})`);
});

async function loadContributors() {
    const repoUrl = "https://api.github.com/repos/TWOCHEG/ZOVblox/contributors";
    const contributorsElement = document.getElementById("contributors");

    try {
        const response = await fetch(repoUrl);
        if (!response.ok) {
            throw new Error("Не удалось загрузить авторов.");
        }

        const contributors = await response.json();
        if (!contributors || contributors.length === 0) {
            contributorsElement.innerHTML = "<p>Авторы не найдены.</p>";
            return;
        }

        // Создание карточек для каждого автора
        const contributorHTML = contributors.map(contributor => `
            <div class="contributor-card">
                <img src="${contributor.avatar_url}" alt="${contributor.login}" class="avatar">
                <div class="contributor-info">
                    <a href="${contributor.html_url}" target="_blank" class="contributor-name">${contributor.login}</a>
                    <p class="contributor-description">${contributor.contributions} коммит(ов)</p>
                </div>
            </div>
        `).join("");

        contributorsElement.innerHTML = `
            <div class="contributor-grid">
                ${contributorHTML}
            </div>
        `;
    } catch (error) {
        console.error(error);
        contributorsElement.innerHTML = "<p>Ошибка загрузки авторов.</p>";
    }
}

async function loadFooter(footerId, footerPath) {
    try {
        const response = await fetch(footerPath);
        if (!response.ok) {
            throw new Error(`Не удалось загрузить файл ${footerPath}`);
        }
        const footerContent = await response.text();
        document.getElementById(footerId).innerHTML = footerContent;

        // После загрузки футера вызываем loadContributors
        loadContributors();
    } catch (error) {
        console.error(error);
        document.getElementById(footerId).innerText = 'Ошибка загрузки футера.' + error;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    loadFooter('footer', 'footer.html');
});