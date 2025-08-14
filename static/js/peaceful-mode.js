// 😌 PEACEFUL MODE - Simple version without toggle button

document.addEventListener('DOMContentLoaded', function() {
    
    // Tự động bật peaceful mode
    document.body.classList.add('peaceful-mode');
    
    // Tắt tất cả animations mạnh
    function disableStrongAnimations() {
        // Tắt particle system
        const particles = document.querySelectorAll('.particle');
        particles.forEach(particle => {
            particle.style.display = 'none';
        });
        
        // Tắt morphing backgrounds
        const morphElements = document.querySelectorAll('.morph-animation');
        morphElements.forEach(el => {
            el.style.animation = 'none';
        });
        
        // Tắt rotating elements
        const rotatingElements = document.querySelectorAll('.rotate-slow');
        rotatingElements.forEach(el => {
            el.style.animation = 'none';
        });
        
        // Tắt floating animations
        const floatingElements = document.querySelectorAll('.float-animation, .float-reverse');
        floatingElements.forEach(el => {
            el.style.animation = 'none';
        });
        
        // Tắt pulse animations
        const pulseElements = document.querySelectorAll('.pulse-animation, .pulse-glow');
        pulseElements.forEach(el => {
            el.style.animation = 'none';
        });
        
        // Tắt gradient animations
        const gradientElements = document.querySelectorAll('.gradient-animation');
        gradientElements.forEach(el => {
            el.style.animation = 'none';
            el.style.background = '#8B4513';
            el.style.color = 'white';
        });
    }
    
    // Chỉ giữ lại hover effects nhẹ nhàng
    function enableGentleHovers() {
        // Cards - chỉ lift nhẹ
        document.querySelectorAll('.vintage-card, .philosopher-card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px)';
                this.style.boxShadow = '0 4px 8px rgba(0,0,0,0.1)';
                this.style.transition = 'all 0.3s ease';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = '0 2px 4px rgba(0,0,0,0.1)';
            });
        });
        
        // Buttons - chỉ lift rất nhẹ
        document.querySelectorAll('.vintage-button, .btn').forEach(btn => {
            btn.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-1px)';
                this.style.boxShadow = '0 2px 4px rgba(139, 69, 19, 0.2)';
                this.style.transition = 'all 0.2s ease';
            });
            
            btn.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = 'none';
            });
        });
        
        // School tags - chỉ scale rất nhẹ
        document.querySelectorAll('.school-tag').forEach(tag => {
            tag.addEventListener('mouseenter', function() {
                this.style.transform = 'scale(1.02)';
                this.style.transition = 'all 0.2s ease';
            });
            
            tag.addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1)';
            });
        });
        
        // Links - chỉ đổi màu
        document.querySelectorAll('.vintage-link, a').forEach(link => {
            link.addEventListener('mouseenter', function() {
                this.style.color = '#654321';
                this.style.transition = 'color 0.2s ease';
            });
            
            link.addEventListener('mouseleave', function() {
                this.style.color = '#8B4513';
            });
        });
    }
    
    // Tắt scroll animations mạnh
    function disableScrollAnimations() {
        // Chỉ giữ scroll reveal nhẹ nhàng
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transition = 'opacity 0.5s ease';
                }
            });
        });
        
        document.querySelectorAll('.scroll-reveal').forEach(el => {
            el.style.opacity = '0';
            observer.observe(el);
        });
    }
    
    // Tắt typewriter effect
    function disableTypewriter() {
        document.querySelectorAll('.typewriter').forEach(el => {
            el.style.animation = 'none';
            el.style.borderRight = 'none';
        });
    }
    
    // Chạy tất cả functions
    disableStrongAnimations();
    enableGentleHovers();
    disableScrollAnimations();
    disableTypewriter();
    
    console.log('😌 Peaceful mode activated - Clean and simple!');
});

// Utility để tắt animations cho specific elements
window.PeacefulMode = {
    disable: function(selector) {
        document.querySelectorAll(selector).forEach(el => {
            el.style.animation = 'none';
            el.style.transition = 'all 0.2s ease';
        });
    },
    
    enableGentle: function(selector) {
        document.querySelectorAll(selector).forEach(el => {
            el.addEventListener('mouseenter', function() {
                this.style.opacity = '0.8';
            });
            el.addEventListener('mouseleave', function() {
                this.style.opacity = '1';
            });
        });
    }
};