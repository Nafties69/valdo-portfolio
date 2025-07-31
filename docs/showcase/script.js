const images = [
  {
    "src": "https://via.placeholder.com/250?text=Enriched+Image+1",
    "title": "A Rhino on a Field",
    "description": "An AI-enriched image of a rhino.",
    "keywords": ["rhino", "field", "ai", "nature"]
  },
  {
    "src": "https://via.placeholder.com/250?text=Enriched+Image+2",
    "title": "Fairy Houses",
    "description": "An AI-enriched image of fairy houses.",
    "keywords": ["fairy", "house", "fantasy", "ai"]
  },
  {
    "src": "https://via.placeholder.com/250?text=Enriched+Image+3",
    "title": "Placeholder",
    "description": "A placeholder image.",
    "keywords": ["placeholder", "demo"]
  }
];

const imageGrid = document.querySelector('.image-grid');
const searchInput = document.getElementById('search');
const keywordFilter = document.getElementById('keyword-filter');

function populateKeywords() {
  const allKeywords = new Set();
  images.forEach(image => {
    image.keywords.forEach(keyword => {
      allKeywords.add(keyword);
    });
  });

  allKeywords.forEach(keyword => {
    const option = document.createElement('option');
    option.value = keyword;
    option.textContent = keyword.charAt(0).toUpperCase() + keyword.slice(1);
    keywordFilter.appendChild(option);
  });
}

function filterImages() {
  const searchTerm = searchInput.value.toLowerCase();
  const selectedKeyword = keywordFilter.value;

  imageGrid.innerHTML = '';

  images
    .filter(image => {
      const titleMatch = image.title.toLowerCase().includes(searchTerm);
      const descriptionMatch = image.description.toLowerCase().includes(searchTerm);
      const keywordMatch = selectedKeyword ? image.keywords.includes(selectedKeyword) : true;
      return (titleMatch || descriptionMatch) && keywordMatch;
    })
    .forEach(image => {
      const imageContainer = document.createElement('div');
      imageContainer.classList.add('image-container');

      const img = document.createElement('img');
      img.src = image.src;
      img.alt = image.title;

      const overlay = document.createElement('div');
      overlay.classList.add('overlay');

      const title = document.createElement('h3');
      title.textContent = image.title;

      const description = document.createElement('p');
      description.textContent = image.description;

      const keywords = document.createElement('p');
      keywords.textContent = `Keywords: ${image.keywords.join(', ')}`;

      overlay.appendChild(title);
      overlay.appendChild(description);
      overlay.appendChild(keywords);

      imageContainer.appendChild(img);
      imageContainer.appendChild(overlay);

      imageGrid.appendChild(imageContainer);
    });
}

populateKeywords();
filterImages();

searchInput.addEventListener('input', filterImages);
keywordFilter.addEventListener('change', filterImages);

const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const captionText = document.getElementById('caption');
const closeBtn = document.querySelector('.close');

imageGrid.addEventListener('click', (e) => {
    if (e.target.tagName === 'IMG') {
        lightbox.style.display = 'block';
        lightboxImg.src = e.target.src;
        captionText.innerHTML = e.target.alt;
    }
});

closeBtn.addEventListener('click', () => {
    lightbox.style.display = 'none';
});