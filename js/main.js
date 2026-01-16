// Theme Toggle Logic
const themeToggle = document.getElementById('themeToggle');
const icon = themeToggle ? themeToggle.querySelector('i') : null;

const applyTheme = (theme) => {
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
        if (icon) icon.classList.replace('fa-moon', 'fa-sun');
    } else {
        document.body.classList.remove('dark-mode');
        if (icon) icon.classList.replace('fa-sun', 'fa-moon');
    }
};

const savedTheme = localStorage.getItem('theme');
if (savedTheme) applyTheme(savedTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const isDark = document.body.classList.toggle('dark-mode');
        const theme = isDark ? 'dark' : 'light';
        localStorage.setItem('theme', theme);
        
        if (icon) {
            if (isDark) {
                icon.classList.replace('fa-moon', 'fa-sun');
            } else {
                icon.classList.replace('fa-sun', 'fa-moon');
            }
        }
    });
}

// Initialize AOS
if (typeof AOS !== 'undefined') {
    AOS.init({
        duration: 800,
        once: true,
        offset: 100
    });
}

// GSAP Hero Animation
if (typeof gsap !== 'undefined') {
    gsap.from(".profile-img", {
        duration: 1.5,
        scale: 0.5,
        opacity: 0,
        ease: "back.out(1.7)"
    });

    gsap.from(".hero-section h1", {
        duration: 1.2,
        x: -100,
        opacity: 0,
        ease: "power4.out",
        delay: 0.2
    });
    
    gsap.from(".hero-section .lead, .hero-section p, .hero-section .btn", {
        duration: 1.2,
        y: 30,
        opacity: 0,
        ease: "power4.out",
        stagger: 0.2,
        delay: 0.5
    });
}

// Project Filtering
const filterBtns = document.querySelectorAll('.filter-btn');
const projectItems = document.querySelectorAll('.project-item');

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Update active button
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        const filter = btn.getAttribute('data-filter');
        
        projectItems.forEach(item => {
            if (filter === 'all' || item.getAttribute('data-category') === filter) {
                item.style.display = 'block';
                setTimeout(() => item.style.opacity = '1', 10);
            } else {
                item.style.opacity = '0';
                setTimeout(() => item.style.display = 'none', 300);
            }
        });
    });
});

// Skill Progress Bar Animation
const skillSection = document.getElementById('about');
const progressBars = document.querySelectorAll('.progress-bar');
const percentageCounters = document.querySelectorAll('.percentage-counter');

let skillsAnimated = false;

const animateSkills = () => {
    if (skillsAnimated) return;
    skillsAnimated = true;

    progressBars.forEach(bar => {
        const targetWidth = bar.getAttribute('aria-valuenow') + '%';
        bar.style.width = '0%'; // Start at 0 for animation
        setTimeout(() => {
            bar.style.width = targetWidth;
            bar.style.transition = 'width 2s cubic-bezier(0.1, 0, 0.2, 1)';
        }, 100);
    });

    percentageCounters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const duration = 2000; 
        const startTime = performance.now();
        counter.innerText = '0%'; // Start at 0 for animation

        const updateCount = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease out cubic
            const easedProgress = 1 - Math.pow(1 - progress, 3);
            const currentValue = Math.round(easedProgress * target);

            counter.innerText = currentValue + '%';

            if (progress < 1) {
                requestAnimationFrame(updateCount);
            } else {
                counter.innerText = target + '%';
            }
        };

        requestAnimationFrame(updateCount);
    });
};

// Intersection Observer for scroll animation
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateSkills();
            skillObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

if (skillSection) {
    skillObserver.observe(skillSection);
    // Initial check
    const rect = skillSection.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom >= 0) {
        animateSkills();
    }
}

// Scroll to Top
const scrollTopBtn = document.getElementById('scrollTop');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        scrollTopBtn.classList.remove('d-none');
        scrollTopBtn.style.opacity = '1';
    } else {
        scrollTopBtn.style.opacity = '0';
        setTimeout(() => {
            if (window.pageYOffset <= 300) scrollTopBtn.classList.add('d-none');
        }, 300);
    }
});

scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Paystack Integration
const hireMeBtn = document.getElementById('hireMeBtn');

if (hireMeBtn) {
    console.log('Hire Me button found');
    hireMeBtn.onclick = function(e) {
        e.preventDefault();
        console.log('Hire Me button clicked via onclick');
        
        if (typeof PaystackPop === 'undefined') {
            alert('Payment system is still loading. Please refresh the page.');
            return;
        }

        try {
            const handler = PaystackPop.setup({
                key: 'pk_test_12db98321e8d3f2c19fa9c54b18305743ce44ef6', // Replace with your public key
                email: 'worlumiracle0@gmail.com',
                amount: 500000,
                currency: 'NGN',
                callback: function(response) {
                    alert('Payment successful! Reference: ' + response.reference);
                },
                onClose: function() {
                    console.log('Payment window closed');
                }
            });
            handler.openIframe();
        } catch (error) {
            console.error('Paystack Error:', error);
            alert('Error initializing payment. Please ensure your Public Key is correct.');
        }
    };
}

// Contact Form Handling
const contactForm = document.getElementById('contactForm');
const formStatus = document.getElementById('formStatus');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        // We revert to standard form submission with a visual feedback indicator
        const submitBtn = this.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Sending...';
        
        // Formspree will handle the redirect and confirmation
    });
}
