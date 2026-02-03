let currentIndex = 0;
const slides = [
    { image: 'slide1.png', url: '/' },  // ニュースページへ
    { image: 'slide2.jpg', url: '/business_activities/' },  // 事業内容ページへ
    { image: 'slide3.jpeg', url: '/recruitment/' }  // 採用情報ページへ
];

function updateCarousel() {
    const slideElements = document.querySelectorAll('.carousel-slide');
    const indicators = document.querySelectorAll('.indicator-dot');
    
    // インデックスの計算
    const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
    const nextIndex = (currentIndex + 1) % slides.length;
    
    // 各スライドの画像とリンクを更新
    updateSlideElement(slideElements[0], slides[prevIndex]);
    updateSlideElement(slideElements[1], slides[currentIndex]);
    updateSlideElement(slideElements[2], slides[nextIndex]);
    
    indicators.forEach((dot, index) => {
        if (index === currentIndex) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function updateSlideElement(element, slide) {
    const img = element.querySelector('img');
    img.src = `/static/images/${slide.image}`;
    
    // クリックイベントを設定
    element.style.cursor = 'pointer';
    element.onclick = function() {
        window.location.href = slide.url;
    };
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