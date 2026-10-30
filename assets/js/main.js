/* Portfolio — Léopold César N'DIN — interactions (aucune dépendance externe) */
(function () {
  'use strict';
  document.documentElement.classList.remove('no-js');

  /* Menu mobile */
  var btn = document.querySelector('.menu-btn');
  var links = document.querySelector('.nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      links.classList.toggle('open', !open);
    });
    links.addEventListener('click', function (e) {
      if (e.target.closest('a')) { btn.setAttribute('aria-expanded', 'false'); links.classList.remove('open'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && links.classList.contains('open')) { btn.setAttribute('aria-expanded', 'false'); links.classList.remove('open'); btn.focus(); }
    });
  }

  /* En-tête + barre de progression */
  var header = document.querySelector('.site-header');
  var bar = document.querySelector('.progress');
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle('scrolled', y > 8);
    if (bar) {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Lien actif du menu / du sommaire */
  if ('IntersectionObserver' in window) {
    var navMap = {};
    document.querySelectorAll('.nav-links a[href*="#"], .toc a').forEach(function (a) {
      var id = a.getAttribute('href').split('#')[1];
      if (id) (navMap[id] = navMap[id] || []).push(a);
    });
    var ids = Object.keys(navMap);
    if (ids.length) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            Object.values(navMap).forEach(function (arr) { arr.forEach(function (a) { a.classList.remove('active'); }); });
            (navMap[en.target.id] || []).forEach(function (a) { a.classList.add('active'); });
          }
        });
      }, { rootMargin: '-45% 0px -50% 0px' });
      ids.forEach(function (id) { var el = document.getElementById(id); if (el) spy.observe(el); });
    }

    /* Apparition au défilement */
    var rev = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); rev.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { rev.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  /* Longueur des tracés du dessin animé */
  document.querySelectorAll('.drawing .draw').forEach(function (p) {
    try { p.style.setProperty('--len', Math.ceil(p.getTotalLength()) + 1); } catch (e) { /* ignore */ }
  });

  /* Filtres de projets */
  var filters = document.querySelectorAll('.filter');
  filters.forEach(function (f) {
    f.addEventListener('click', function () {
      var cat = f.dataset.filter;
      filters.forEach(function (x) { x.setAttribute('aria-pressed', String(x === f)); });
      document.querySelectorAll('.p-card').forEach(function (card) {
        card.hidden = !(cat === 'tous' || (card.dataset.cat || '').split(' ').indexOf(cat) > -1);
      });
    });
  });

  /* Visionneuse d'images */
  var items = Array.prototype.slice.call(document.querySelectorAll('[data-full]'));
  if (items.length) {
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Visionneuse d’images');
    lb.innerHTML =
      '<div class="lb-top"><span class="lb-cap"></span><span class="lb-count"></span>' +
      '<button class="lb-btn lb-close" aria-label="Fermer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>' +
      '<div class="lb-stage"><img alt=""></div>' +
      '<button class="lb-btn lb-prev" aria-label="Image précédente"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 6l-6 6 6 6"/></svg></button>' +
      '<button class="lb-btn lb-next" aria-label="Image suivante"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></button>';
    document.body.appendChild(lb);
    var img = lb.querySelector('img'), cap = lb.querySelector('.lb-cap'), cnt = lb.querySelector('.lb-count');
    var idx = 0, lastFocus = null;
    function show(i) {
      idx = (i + items.length) % items.length;
      var it = items[idx];
      img.src = it.dataset.full;
      img.alt = it.querySelector('img') ? it.querySelector('img').alt : '';
      cap.textContent = it.dataset.caption || img.alt;
      cnt.textContent = (idx + 1) + ' / ' + items.length;
    }
    function open(i) { lastFocus = document.activeElement; show(i); lb.classList.add('open'); document.body.style.overflow = 'hidden'; lb.querySelector('.lb-close').focus(); }
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; img.src = ''; if (lastFocus) lastFocus.focus(); }
    items.forEach(function (it, i) { it.addEventListener('click', function () { open(i); }); });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(idx - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb-stage')) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
      if (e.key === 'Tab') { /* garder le focus dans la visionneuse */
        var f = lb.querySelectorAll('button'); var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
    var sx = null;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (sx === null) return; var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1)); sx = null;
    });
  }

  /* Formulaire de contact
     - Si l'attribut data-endpoint est vide : le message est préparé dans la messagerie du visiteur (aucun envoi simulé).
     - Si data-endpoint contient une adresse Formspree (https://formspree.io/f/xxxx) : envoi direct. */
  var form = document.querySelector('#contact-form');
  if (form) {
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp input').value) return;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var d = new FormData(form);
      var endpoint = form.dataset.endpoint;
      if (endpoint) {
        status.className = 'form-status'; status.textContent = 'Envoi en cours…';
        fetch(endpoint, { method: 'POST', body: d, headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (r.ok) { status.className = 'form-status ok'; status.textContent = 'Merci ! Votre message a bien été envoyé.'; form.reset(); }
            else throw new Error();
          })
          .catch(function () { status.className = 'form-status err'; status.textContent = 'L’envoi a échoué. Écrivez-moi directement à ' + form.dataset.email + '.'; });
      } else {
        var subject = (d.get('objet') || 'Prise de contact') + ' — ' + d.get('nom');
        var body = d.get('message') + '\n\n— ' + d.get('nom') + (d.get('organisation') ? ' (' + d.get('organisation') + ')' : '') + '\n' + d.get('email');
        window.location.href = 'mailto:' + form.dataset.email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
        status.className = 'form-status ok';
        status.textContent = 'Votre messagerie s’ouvre avec le message prérempli : il ne reste qu’à cliquer sur « Envoyer ».';
      }
    });
  }

  /* Vidéos de couverture : bouton pause, pause hors écran, respect de « réduire les animations » */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.video-wrap').forEach(function (w) {
    var v = w.querySelector('video'), b = w.querySelector('.vid-btn');
    var userPaused = false;
    function sync() {
      var p = v.paused;
      b.classList.toggle('paused', p);
      b.setAttribute('aria-label', p ? b.dataset.labelPlay : b.dataset.labelPause);
    }
    v.addEventListener('play', sync); v.addEventListener('pause', sync);
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); userPaused = true; }
    b.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      if (v.paused) { userPaused = false; var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); }
      else { userPaused = true; v.pause(); }
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        en.forEach(function (x) {
          if (x.isIntersecting && !userPaused) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); }
          else if (!x.isIntersecting) v.pause();
        });
      }).observe(w);
    }
    sync();
  });

  /* Boutons « Demander le CV complet » : préremplit l'objet du formulaire */
  document.querySelectorAll('[data-objet]').forEach(function (l) {
    l.addEventListener('click', function () {
      var sel = document.querySelector('#f-obj'); if (sel) sel.value = l.dataset.objet;
      var msg = document.querySelector('#f-msg');
      if (msg && !msg.value) msg.placeholder = 'Présentez-vous en quelques mots (entreprise, poste ou mission concernée) pour recevoir le CV complet.';
      setTimeout(function () { var n = document.querySelector('#f-nom'); if (n) n.focus({ preventScroll: true }); }, 600);
    });
  });

  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
