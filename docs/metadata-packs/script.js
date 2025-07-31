document.addEventListener('DOMContentLoaded', () => {
    const packLinks = document.querySelectorAll('#metadata-packs a');
    const packPreview = document.getElementById('pack-preview');

    packLinks.forEach(link => {
        link.addEventListener('mouseover', async (event) => {
            event.preventDefault();
            const url = event.target.href;
            try {
                const response = await fetch(url);
                const data = await response.text(); // Get as text to handle both JSON and CSV
                packPreview.innerHTML = `<h3>Preview: ${event.target.textContent}</h3><pre>${data.substring(0, 200)}...</pre>`;
                packPreview.style.display = 'block';
            } catch (error) {
                packPreview.innerHTML = `<h3>Error loading preview.</h3><p>${error.message}</p>`;
                packPreview.style.display = 'block';
            }
        });

        link.addEventListener('mouseout', () => {
            packPreview.style.display = 'none';
            packPreview.innerHTML = '';
        });
    });
});