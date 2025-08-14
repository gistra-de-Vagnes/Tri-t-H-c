// 🔝 BEAUTIFUL NAVBAR JAVASCRIPT 🔝

document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add scroll effect to navbar
    function handleScroll() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
    
    // Add active class to current page nav link
    function setActiveNavLink() {
        const currentPath = window.location.pathname;
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            
            // Check if link href matches current path
            const linkPath = new URL(link.href).pathname;
            if (linkPath === currentPath) {
                link.classList.add('active');
            }
        });
    }
    
    // Smooth scroll for anchor links
    function addSmoothScroll() {
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
    }
    
    // Add hover sound effect (optional)
    function addHoverEffects() {
        const hoverElements = document.querySelectorAll('.nav-link, .navbar-brand');
        
        hoverElements.forEach(element => {
            element.addEventListener('mouseenter', function() {
                // Add subtle scale effect
                this.style.transform = this.style.transform || '';
            });
        });
    }
    
    // Initialize all functions
    window.addEventListener('scroll', handleScroll);
    setActiveNavLink();
    addSmoothScroll();
    addHoverEffects();
    
    // Handle navbar collapse on mobile after clicking a link
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navbarToggler = document.querySelector('.navbar-toggler');
    
    if (navbarCollapse && navbarToggler) {
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }
    
    console.log('🔝 Beautiful navbar initialized!');
});