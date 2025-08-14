// 🎬 SMOOTH ANIMATIONS JAVASCRIPT 🎬

document.addEventListener('DOMContentLoaded', function() {
    
    // 1. SCROLL REVEAL ANIMATION
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
            }
        });
    }, observerOptions);

    // Apply scroll reveal to elements
    document.querySelectorAll('.scroll-reveal').forEach(el => {
        observer.observe(el);
    });

    // 2. STAGGER ANIMATIONS FOR CARDS
    function staggerAnimation(selector, animationClass, delay = 100) {
        const elements = document.querySelectorAll(selector);
        elements.forEach((el, index) => {
            setTimeout(() => {
                el.classList.add(animationClass);
            }, index * delay);
        });
    }

    // Apply stagger animations
    staggerAnimation('.vintage-card', 'animate-fade-in-up', 150);
    staggerAnimation('.school-tag', 'animate-fade-in-scale', 50);
    staggerAnimation('.philosopher-image', 'bounce-in', 200);

    // 3. PARALLAX SCROLLING
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.parallax');
        
        parallaxElements.forEach(element => {
            const speed = element.dataset.speed || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });

    // 4. SMOOTH HOVER EFFECTS
    function addHoverEffects() {
        // Add hover lift to cards
        document.querySelectorAll('.vintage-card, .philosopher-card').forEach(card => {
            card.classList.add('hover-lift');
        });

        // Add hover glow to buttons
        document.querySelectorAll('.vintage-button, .btn').forEach(btn => {
            btn.classList.add('btn-animated');
        });

        // Add ripple effect to clickable elements
        document.querySelectorAll('.vintage-button, .btn, .school-tag').forEach(el => {
            el.classList.add('ripple');
        });
    }

    addHoverEffects();

    // 5. TYPEWRITER EFFECT
    function typeWriter(element, text, speed = 50) {
        let i = 0;
        element.innerHTML = '';
        
        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        type();
    }

    // Apply typewriter to headers
    const headers = document.querySelectorAll('.typewriter');
    headers.forEach(header => {
        const text = header.textContent;
        typeWriter(header, text, 100);
    });

    // 6. FLOATING ANIMATION FOR SPECIAL ELEMENTS
    function addFloatingAnimation() {
        document.querySelectorAll('.philosopher-image-placeholder').forEach((el, index) => {
            if (index % 2 === 0) {
                el.classList.add('float-animation');
            } else {
                el.classList.add('float-reverse');
            }
        });
    }

    addFloatingAnimation();

    // 7. PULSE ANIMATION FOR IMPORTANT ELEMENTS
    function addPulseToImportant() {
        document.querySelectorAll('.btn-primary, .vintage-button-primary').forEach(btn => {
            btn.classList.add('pulse-glow');
        });
    }

    addPulseToImportant();

    // 8. ELASTIC ANIMATION ON CLICK
    document.addEventListener('click', function(e) {
        if (e.target.matches('.vintage-button, .btn, .school-tag')) {
            e.target.classList.add('elastic-animation');
            setTimeout(() => {
                e.target.classList.remove('elastic-animation');
            }, 600);
        }
    });

    // 9. SMOOTH SCROLL FOR ANCHOR LINKS
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 10. LOADING ANIMATION
    function showLoadingAnimation() {
        const loadingElements = document.querySelectorAll('.loading-dots');
        loadingElements.forEach(el => {
            el.classList.add('loading-dots');
        });
    }

    // 11. MORPHING BACKGROUND FOR HERO SECTIONS
    function addMorphingBackground() {
        const heroSections = document.querySelectorAll('.hero-section, .main-content');
        heroSections.forEach(section => {
            section.style.position = 'relative';
            section.style.overflow = 'hidden';
            
            const morphDiv = document.createElement('div');
            morphDiv.style.position = 'absolute';
            morphDiv.style.top = '-50%';
            morphDiv.style.left = '-50%';
            morphDiv.style.width = '200%';
            morphDiv.style.height = '200%';
            morphDiv.style.background = 'linear-gradient(45deg, rgba(139, 69, 19, 0.05), rgba(210, 105, 30, 0.1))';
            morphDiv.style.zIndex = '-1';
            morphDiv.classList.add('morph-animation');
            
            section.appendChild(morphDiv);
        });
    }

    addMorphingBackground();

    // 12. PARTICLE SYSTEM
    function createParticles() {
        const particleContainer = document.createElement('div');
        particleContainer.style.position = 'fixed';
        particleContainer.style.top = '0';
        particleContainer.style.left = '0';
        particleContainer.style.width = '100%';
        particleContainer.style.height = '100%';
        particleContainer.style.pointerEvents = 'none';
        particleContainer.style.zIndex = '-1';
        
        for (let i = 0; i < 5; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 10 + 's';
            particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
            particleContainer.appendChild(particle);
        }
        
        document.body.appendChild(particleContainer);
    }

    createParticles();

    // 13. GRADIENT ANIMATION FOR SPECIAL ELEMENTS
    function addGradientAnimation() {
        document.querySelectorAll('.vintage-header').forEach(header => {
            header.classList.add('gradient-animation');
            header.style.backgroundClip = 'text';
            header.style.webkitBackgroundClip = 'text';
            header.style.color = 'transparent';
        });
    }

    // Uncomment to enable gradient text animation
    // addGradientAnimation();

    // 14. MOUSE FOLLOW EFFECT
    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;

    document.addEventListener('mousemove', function(e) {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    function animateCursor() {
        cursorX += (mouseX - cursorX) * 0.1;
        cursorY += (mouseY - cursorY) * 0.1;
        
        // Apply subtle parallax to cards based on mouse position
        document.querySelectorAll('.vintage-card').forEach(card => {
            const rect = card.getBoundingClientRect();
            const cardCenterX = rect.left + rect.width / 2;
            const cardCenterY = rect.top + rect.height / 2;
            
            const deltaX = (mouseX - cardCenterX) * 0.01;
            const deltaY = (mouseY - cardCenterY) * 0.01;
            
            card.style.transform = `translateX(${deltaX}px) translateY(${deltaY}px)`;
        });
        
        requestAnimationFrame(animateCursor);
    }

    animateCursor();

    // 15. PERFORMANCE OPTIMIZATION
    function optimizeAnimations() {
        // Add GPU acceleration to animated elements
        document.querySelectorAll('.vintage-card, .vintage-button, .school-tag, .philosopher-image').forEach(el => {
            el.classList.add('gpu-accelerated');
        });
    }

    optimizeAnimations();

    // 16. INTERSECTION OBSERVER FOR PERFORMANCE
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Start animations when element is visible
                entry.target.style.animationPlayState = 'running';
            } else {
                // Pause animations when element is not visible
                entry.target.style.animationPlayState = 'paused';
            }
        });
    });

    // Observe animated elements
    document.querySelectorAll('[class*="animation"], [class*="animate-"]').forEach(el => {
        animationObserver.observe(el);
    });

    // 17. RESIZE HANDLER FOR RESPONSIVE ANIMATIONS
    window.addEventListener('resize', function() {
        // Recalculate animations on resize
        const isMobile = window.innerWidth < 768;
        
        document.querySelectorAll('.vintage-card').forEach(card => {
            if (isMobile) {
                // Reduce animations on mobile
                card.style.transition = 'all 0.2s ease';
            } else {
                // Full animations on desktop
                card.style.transition = 'all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            }
        });
    });

    console.log('🎬 Smooth animations initialized!');
});

// 18. UTILITY FUNCTIONS
window.SmoothAnimations = {
    // Add animation to element
    addAnimation: function(element, animationClass, duration = 600) {
        element.classList.add(animationClass);
        setTimeout(() => {
            element.classList.remove(animationClass);
        }, duration);
    },

    // Stagger animation for multiple elements
    stagger: function(selector, animationClass, delay = 100) {
        const elements = document.querySelectorAll(selector);
        elements.forEach((el, index) => {
            setTimeout(() => {
                el.classList.add(animationClass);
            }, index * delay);
        });
    },

    // Reveal element with animation
    reveal: function(element) {
        element.classList.add('scroll-reveal', 'revealed');
    }
};