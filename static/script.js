// script.js — scroll-triggered fade-ins + active-section nav highlight

document.addEventListener('DOMContentLoaded', () => {
  // Fade in elements as they enter the viewport
  const faders = document.querySelectorAll('.fade-in');

  if ('IntersectionObserver' in window) {
    const fadeObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    faders.forEach((el) => fadeObserver.observe(el));

    // Highlight the nav link for the section currently in view
    const navLinks = document.querySelectorAll('.nav-links a[data-section]');
    const sections = Array.from(navLinks)
      .map((link) => document.getElementById(link.dataset.section))
      .filter(Boolean);

    if (sections.length) {
      const navObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const link = document.querySelector(`.nav-links a[data-section="${entry.target.id}"]`);
          if (!link) return;
          navLinks.forEach((l) => l.classList.remove('active'));
          link.classList.add('active');
        });
      }, { rootMargin: '-40% 0px -50% 0px', threshold: 0 });

      sections.forEach((section) => navObserver.observe(section));
    }
  } else {
    faders.forEach((el) => el.classList.add('visible'));
  }
});
