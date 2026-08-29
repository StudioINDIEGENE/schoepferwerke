/* Schöpferwerke — Interaktionen */
(() => {
  'use strict';
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Sticky nav ---- */
  const nav = document.getElementById('nav');
  const onScroll = () => nav.classList.toggle('nav--scrolled', window.scrollY > 60);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---- Mobile menu ---- */
  const burger = document.getElementById('burger');
  const menu = document.getElementById('menu');
  const toggleMenu = (force) => {
    const open = force ?? !document.body.classList.contains('menu-open');
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', String(open));
  };
  burger.addEventListener('click', () => toggleMenu());
  menu.addEventListener('click', (e) => { if (e.target.tagName === 'A') toggleMenu(false); });

  /* ---- Scroll reveal ---- */
  const reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(el => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(el => io.observe(el));
  }

  /* ---- Rotating word (Intro) ---- */
  const rot = document.getElementById('rotWord');
  if (rot && !reduce) {
    const words = ['fremdbestimmt', 'erschöpft', 'getrennt', 'im Aussen', 'unruhig'];
    let i = 0;
    setInterval(() => {
      i = (i + 1) % words.length;
      rot.style.transition = 'opacity .45s, transform .45s';
      rot.style.opacity = '0';
      rot.style.transform = 'translateY(10px)';
      setTimeout(() => {
        rot.textContent = words[i];
        rot.style.opacity = '1';
        rot.style.transform = 'none';
      }, 450);
    }, 2800);
  }

  /* ---- Count-up stats ---- */
  const counters = document.querySelectorAll('.stat__num[data-count]');
  const setVal = (el, n) => {
    const suffix = el.dataset.suffix || '';
    el.innerHTML = n + (suffix ? `<span class="plus">${suffix}</span>` : '');
  };
  const animateCount = (el) => {
    const target = +el.dataset.count, dur = 1600, start = performance.now();
    const step = (now) => {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      setVal(el, Math.round(target * eased));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if (counters.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      counters.forEach(el => setVal(el, +el.dataset.count));
    } else {
      const cio = new IntersectionObserver((entries) => {
        entries.forEach(e => { if (e.isIntersecting) { animateCount(e.target); cio.unobserve(e.target); } });
      }, { threshold: 0.6 });
      counters.forEach(el => cio.observe(el));
    }
  }

  /* ---- FAQ smooth height (native <details>) ---- */
  document.querySelectorAll('.faq').forEach(faq => {
    const summary = faq.querySelector('summary');
    summary.addEventListener('click', (e) => {
      e.preventDefault();
      if (faq.hasAttribute('open')) {
        faq.classList.remove('is-open');
        setTimeout(() => faq.removeAttribute('open'), 380);
      } else {
        faq.setAttribute('open', '');
        requestAnimationFrame(() => faq.classList.add('is-open'));
      }
    });
  });

  /* ---- Booking form: Netlify submit with graceful mailto fallback ---- */
  const encode = (data) => Object.keys(data).map(k => encodeURIComponent(k) + '=' + encodeURIComponent(data[k])).join('&');
  const booking = document.getElementById('bookingForm');
  if (booking) booking.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!booking.checkValidity()) { booking.reportValidity(); return; }
    const fd = new FormData(booking);
    const data = {}; fd.forEach((v, k) => { data[k] = v; });
    try {
      const res = await fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: encode(data) });
      if (!res.ok) throw new Error('non-ok');
      booking.classList.add('sent');
      booking.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
    } catch (err) {
      // Fallback (z.B. lokal ohne Netlify): E-Mail-Programm mit vorausgefüllter Nachricht öffnen
      const subject = 'Session-Anfrage — ' + (data.format || '');
      const body = `Name: ${data.name || ''}\nE-Mail: ${data.email || ''}\nBegleitung: ${data.format || ''}\nAufmerksam über: ${data.source || ''}\n\n${data.message || ''}`;
      window.location.href = `mailto:info@schoepferwerke.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    }
  });

  /* ---- Newsletter ---- */
  const news = document.getElementById('newsletterForm');
  if (news) news.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!news.checkValidity()) { news.reportValidity(); return; }
    const fd = new FormData(news);
    const data = {}; fd.forEach((v, k) => { data[k] = v; });
    try {
      const res = await fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: encode(data) });
      if (!res.ok) throw new Error('non-ok');
    } catch (_) { /* still confirm to the visitor */ }
    news.innerHTML = '<p style="font-family:var(--serif);font-size:1.3rem;color:var(--ink)">Danke — schön, dass du dabei bist.</p>';
  });
})();
