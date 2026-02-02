let currentIndex = 0;
const slides = [
    'slide1.png',
    'slide2.jpg',
    'slide3.jpeg'
];

function updateCarousel() {
    const slideElements = document.querySelectorAll('.carousel-slide');
    const indicators = document.querySelectorAll('.indicator-dot');
    
    // インデックスの計算
    const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
    const nextIndex = (currentIndex + 1) % slides.length;
    
    // 各スライドの画像を更新
    slideElements[0].querySelector('img').src = `/static/images/${slides[prevIndex]}`;
    slideElements[1].querySelector('img').src = `/static/images/${slides[currentIndex]}`;
    slideElements[2].querySelector('img').src = `/static/images/${slides[nextIndex]}`;
    
    indicators.forEach((dot, index) => {
        if (index === currentIndex) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateCarousel();
}

function goToSlide(index) {
    currentIndex = index;
    updateCarousel();
}

// 初期化
document.addEventListener('DOMContentLoaded', function() {
    updateCarousel();
});