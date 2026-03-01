document.addEventListener('DOMContentLoaded', () => {
    // 1. Create modal HTML elements
    const modal = document.createElement('div');
    modal.className = 'image-modal';

    const modalImg = document.createElement('img');

    const closeBtn = document.createElement('span');
    closeBtn.className = 'modal-close';
    closeBtn.innerHTML = '&times;';

    modal.appendChild(closeBtn);
    modal.appendChild(modalImg);
    document.body.appendChild(modal);

    // 2. Select all images inside the case studies
    const imageSelectors = [
        '.cs-hero-img img',
        '.cs-image-full',
        '.cs-image-box img',
        '.cs-section img',
        '.cs-bg-dark img',
        '.app-marquee-track img'
    ];

    const images = document.querySelectorAll(imageSelectors.join(', '));

    images.forEach(img => {
        // Exclude logos or small icons, verify it's an actual image tag
        if (img.tagName.toLowerCase() === 'img') {
            img.classList.add('zoomable-image');
            img.style.cursor = 'zoom-in';

            img.addEventListener('click', () => {
                // Check if the image is actually visible (not a placeholder missing src)
                if (getComputedStyle(img).display !== 'none') {
                    modal.classList.add('active');
                    modalImg.src = img.src;
                    document.body.style.overflow = 'hidden'; // Prevent background scrolling
                }
            });
        }
    });

    // 3. Modal close logic
    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';

        // Wait for CSS fade transition to finish before clearing src
        setTimeout(() => {
            if (!modal.classList.contains('active')) {
                modalImg.src = '';
            }
        }, 300);
    };

    closeBtn.addEventListener('click', closeModal);

    // Close when clicking the dark background
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close on Escape key press
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
});
