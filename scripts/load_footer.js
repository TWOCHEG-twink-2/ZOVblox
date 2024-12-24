async function loadContributors() {
    const repoUrl = "https://api.github.com/repos/TWOCHEG-twink-2/ZOVblox/contributors";
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

        // тут короче пришлось в ручную карту сделать потому что его нету на гит хабе
        contributorsElement.innerHTML = `
            <div class="contributor-grid">
                ${contributorHTML}
                <div class="contributor-card">
                    <img src="https://cs6.pikabu.ru/post_img/big/2015/08/03/6/1438593490_2019547442.png" alt="егор" class="avatar">
                    <div class="contributor-info">
                        <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="contributor-name">егор (нету на гит хабе)</a>
                        <p class="contributor-description">1488 коммит(ов)</p>
                    </div>
                </div>
            </div>
        `;
    } catch (error) {
        console.error(error);
        contributorsElement.innerHTML = "<p>ошибка загрузки авторов</p>";
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
    loadFooter('footer', 'templates/footer.html');
});