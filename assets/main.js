(function() {
  // Reduced motion
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.PLUTO_REDUCED = reduced;

  // Lenis smooth scrolling
  var lenis;
  if (!reduced) {
    lenis = new Lenis({
      duration: 1.4,
      easing: function(t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 1.5
    });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function(time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
    window.lenis = lenis;
  }

  // Nav scroll state
  var nav = document.getElementById('nav');
  if (nav) {
    window.addEventListener('scroll', function() {
      nav.classList.toggle('is-scrolled', window.scrollY > 60);
    }, { passive: true });
  }

  // Mobile menu
  var mnav = document.getElementById('mnav');
  if (mnav) {
    document.getElementById('mnavOpen').addEventListener('click', function() {
      mnav.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    });
    document.getElementById('mnavClose').addEventListener('click', function() {
      mnav.classList.remove('is-open');
      document.body.style.overflow = '';
    });
    mnav.querySelectorAll('a').forEach(function(a) {
      a.addEventListener('click', function() {
        mnav.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
  }

  // Scroll progress
  var progressBar = document.getElementById('scrollProgress');
  if (progressBar) {
    window.addEventListener('scroll', function() {
      var scrollTop = window.scrollY;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = (docHeight > 0 ? (scrollTop / docHeight) * 100 : 0) + '%';
    }, { passive: true });
  }

  // Reveal on scroll (simple intersection observer)
  var reveals = document.querySelectorAll('.reveal, .reveal-scale');
  if (reveals.length) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function(el) { observer.observe(el); });
  }

  console.log('Pluto BV Ltd — main.js loaded');
})();