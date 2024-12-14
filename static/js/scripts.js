document.addEventListener('DOMContentLoaded', function () {
    const swiperSlider = document.querySelector('.swiper');

    if (swiperSlider) {
        const swiper = new Swiper(swiperSlider, {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
         navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
             },
         autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
       });
    }
});