// 🚀 PERFORMANCE OPTIMIZER (NO TOGGLE BUTTONS) 🚀

class PerformanceOptimizer {
    constructor() {
        this.isLowEndDevice = false;
        this.performanceMode = false;
        this.init();
    }

    init() {
        this.detectDeviceCapabilities();
        this.applyOptimizations();
        this.monitorPerformance();
    }

    // Detect device capabilities
    detectDeviceCapabilities() {
        const checks = {
            // Check CPU cores
            cores: navigator.hardwareConcurrency || 1,
            
            // Check memory (if available)
            memory: navigator.deviceMemory || 1,
            
            // Check connection speed
            connection: navigator.connection?.effectiveType || '4g',
            
            // Check screen resolution
            pixelRatio: window.devicePixelRatio || 1,
            
            // Check if mobile
            isMobile: /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent),
            
            // Check viewport size
            viewportWidth: window.innerWidth
        };

        // Determine if low-end device
        this.isLowEndDevice = (
            checks.cores <= 2 ||
            checks.memory <= 2 ||
            checks.connection === 'slow-2g' ||
            checks.connection === '2g' ||
            (checks.isMobile && checks.viewportWidth <= 480)
        );

        console.log('🔍 Device Analysis:', {
            isLowEndDevice: this.isLowEndDevice,
            ...checks
        });

        // Auto-enable performance mode for low-end devices
        if (this.isLowEndDevice) {
            this.enablePerformanceMode();
        }
    }

    // Enable performance mode
    enablePerformanceMode() {
        document.body.classList.add('performance-mode');
        this.performanceMode = true;
        
        // Disable heavy animations
        this.disableHeavyAnimations();
        
        console.log('🚀 Performance mode enabled automatically');
    }

    // Disable heavy animations
    disableHeavyAnimations() {
        const heavyElements = document.querySelectorAll(`
            .navbar::before,
            .navbar::after,
            .simple-footer::before,
            .simple-footer::after
        `);

        heavyElements.forEach(el => {
            if (el) {
                el.style.display = 'none';
            }
        });
    }

    // Apply optimizations based on device
    applyOptimizations() {
        // Apply mobile optimizations
        if (window.innerWidth <= 768) {
            this.applyMobileOptimizations();
        }

        // Apply low-end device optimizations
        if (this.isLowEndDevice) {
            this.applyLowEndOptimizations();
        }
    }

    // Mobile optimizations
    applyMobileOptimizations() {
        // Reduce animation complexity
        const style = document.createElement('style');
        style.textContent = `
            .navbar, .simple-footer {
                background: #8B4513 !important;
            }
            .navbar::before, .simple-footer::after {
                display: none !important;
            }
        `;
        document.head.appendChild(style);
    }

    // Low-end device optimizations
    applyLowEndOptimizations() {
        const style = document.createElement('style');
        style.textContent = `
            * {
                transition-duration: 0.2s !important;
            }
            .navbar-brand, .nav-link, .footer-links-simple a {
                backdrop-filter: none !important;
                background: rgba(255, 255, 255, 0.1) !important;
            }
        `;
        document.head.appendChild(style);
    }

    // Monitor performance
    monitorPerformance() {
        if ('PerformanceObserver' in window) {
            // Monitor long tasks
            const observer = new PerformanceObserver((list) => {
                const longTasks = list.getEntries();
                if (longTasks.length > 0) {
                    console.warn('⚠️ Long tasks detected:', longTasks.length);
                    
                    // Auto-enable performance mode if too many long tasks
                    if (longTasks.length > 5 && !this.performanceMode) {
                        console.log('🚀 Auto-enabling performance mode due to long tasks');
                        this.enablePerformanceMode();
                    }
                }
            });

            try {
                observer.observe({ entryTypes: ['longtask'] });
            } catch (e) {
                console.log('Long task monitoring not supported');
            }
        }

        // Monitor frame rate
        let lastTime = performance.now();
        let frameCount = 0;
        
        const checkFrameRate = (currentTime) => {
            frameCount++;
            
            if (currentTime - lastTime >= 1000) {
                const fps = Math.round((frameCount * 1000) / (currentTime - lastTime));
                
                if (fps < 30 && !this.performanceMode) {
                    console.warn(`⚠️ Low FPS detected: ${fps}fps`);
                    // Auto-enable performance mode for poor performance
                    this.enablePerformanceMode();
                }
                
                frameCount = 0;
                lastTime = currentTime;
            }
            
            requestAnimationFrame(checkFrameRate);
        };
        
        requestAnimationFrame(checkFrameRate);
    }

    // Preload critical resources
    preloadCriticalResources() {
        const criticalCSS = [
            '/static/css/beautiful_navbar.css',
            '/static/css/beautiful_footer.css'
        ];

        criticalCSS.forEach(href => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'style';
            link.href = href;
            document.head.appendChild(link);
        });
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.performanceOptimizer = new PerformanceOptimizer();
});

// Export for manual control
window.PerformanceOptimizer = PerformanceOptimizer;