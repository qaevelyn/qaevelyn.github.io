/* lightbox.js — clickable, zoomable visuals for the accessible book. 2026-10-23.
   Progressive enhancement: without JavaScript the images render exactly as before.
   Accessibility contract:
     - keyboard operable (Tab to an image, Enter or Space to open, Esc to close)
     - focus trapped inside the viewer while open, returned to the trigger on close
     - screen readers: images announce "opens larger view"; viewer announces its title
     - reduced-motion respected (animation only under no-preference)
     - day and night both readable (near-opaque backdrop, site palette)
   Excluded on purpose: images inside links (navigation wins), [data-no-zoom],
   icon-classed images, and naturally tiny images (decoration, not exhibits).
   The page's own ArrowLeft/ArrowRight book-flip is outrun by capture-phase
   handling while the viewer is open, and untouched while it is closed. */
(function () {
  'use strict';

  var MIN_NATURAL = 200; // px — below this an image is decoration, not an exhibit
  var openedFrom = null;

  /* ---------- build the viewer once ---------- */
  var backdrop = document.createElement('div');
  backdrop.className = 'lb-backdrop';
  backdrop.hidden = true;
  backdrop.innerHTML =
    '<div class="lb-dialog" role="dialog" aria-modal="true" aria-label="Image viewer">' +
      '<div class="lb-bar">' +
        '<p class="lb-caption" aria-live="polite"></p>' +
        '<div class="lb-tools">' +
          '<button type="button" class="lb-btn" data-act="out" aria-label="Zoom out">&minus;</button>' +
          '<button type="button" class="lb-btn" data-act="reset" aria-label="Reset zoom">100%</button>' +
          '<button type="button" class="lb-btn" data-act="in" aria-label="Zoom in">+</button>' +
          '<a class="lb-btn" data-act="newtab" href="#" target="_blank" rel="noopener">Open full size in new tab</a>' +
          '<button type="button" class="lb-btn" data-act="close" aria-label="Close viewer">Close</button>' +
        '</div>' +
      '</div>' +
      '<div class="lb-pane"><img class="lb-img" alt=""></div>' +
      '<p class="lb-hint">Esc closes &middot; + / &minus; zoom &middot; Ctrl+scroll zooms &middot; double-click toggles 2&times;</p>' +
    '</div>';
  document.body.appendChild(backdrop);

  var dialog  = backdrop.querySelector('.lb-dialog');
  var pane    = backdrop.querySelector('.lb-pane');
  var img     = backdrop.querySelector('.lb-img');
  var caption = backdrop.querySelector('.lb-caption');
  var newtab  = backdrop.querySelector('[data-act="newtab"]');
  var resetBtn = backdrop.querySelector('[data-act="reset"]');

  var scale = 1;

  function applyScale() {
    img.style.width = (scale * 100) + '%';
    resetBtn.textContent = Math.round(scale * 100) + '%';
  }

  function open(lbimg) {
    if (lbimg.naturalWidth && lbimg.naturalWidth < MIN_NATURAL && !lbimg.hasAttribute('data-zoom')) return;
    openedFrom = lbimg;
    img.removeAttribute('src');
    img.src = lbimg.currentSrc || lbimg.src;
    img.alt = lbimg.alt || '';
    var label = lbimg.alt || lbimg.getAttribute('src') || 'image';
    caption.textContent = label;
    dialog.setAttribute('aria-label', 'Image viewer: ' + label);
    newtab.href = lbimg.src;
    scale = 1;
    applyScale();
    backdrop.hidden = false;
    document.documentElement.classList.add('lb-lock');
    backdrop.querySelector('[data-act="close"]').focus();
  }

  function close() {
    backdrop.hidden = true;
    document.documentElement.classList.remove('lb-lock');
    img.removeAttribute('src');
    if (openedFrom) { openedFrom.focus(); openedFrom = null; }
  }

  function step(dir) {
    scale = Math.min(4, Math.max(0.5, scale + dir * 0.25));
    applyScale();
  }

  /* ---------- toolbar + backdrop ---------- */
  dialog.addEventListener('click', function (e) {
    var act = e.target.getAttribute && e.target.getAttribute('data-act');
    if (act === 'in')      { e.preventDefault(); step(1); }
    else if (act === 'out')  { e.preventDefault(); step(-1); }
    else if (act === 'reset'){ e.preventDefault(); scale = 1; applyScale(); }
    else if (act === 'close'){ e.preventDefault(); close(); }
    /* newtab: no handler — the link navigates on its own */
  });

  backdrop.addEventListener('click', function (e) {
    if (e.target === backdrop) close(); /* click on the dimmed area closes */
  });

  pane.addEventListener('dblclick', function () {
    scale = scale > 1 ? 1 : 2;
    applyScale();
  });

  pane.addEventListener('wheel', function (e) {
    if (!e.ctrlKey && !e.metaKey) return;
    e.preventDefault();
    step(e.deltaY < 0 ? 1 : -1);
  }, { passive: false });

  /* ---------- keyboard: capture phase outruns the book's arrow-key flipper ---------- */
  document.addEventListener('keydown', function (e) {
    if (backdrop.hidden) return;

    if (e.key === 'Escape')            { e.preventDefault(); e.stopPropagation(); close(); }
    else if (e.key === '+' || e.key === '=') { e.preventDefault(); e.stopPropagation(); step(1); }
    else if (e.key === '-' || e.key === '_') { e.preventDefault(); e.stopPropagation(); step(-1); }
    else if (e.key === '0')            { e.preventDefault(); e.stopPropagation(); scale = 1; applyScale(); }
    else if (e.key === 'ArrowLeft' || e.key === 'ArrowRight' ||
             e.key === 'ArrowUp'   || e.key === 'ArrowDown') {
      e.stopPropagation(); /* pane scrolls natively; the book behind stays still */
    }
    else if (e.key === 'Tab') {
      var focusables = dialog.querySelectorAll('button, a[href]');
      var list = [];
      for (var i = 0; i < focusables.length; i++) {
        if (focusables[i].offsetParent !== null) list.push(focusables[i]);
      }
      if (!list.length) { e.stopPropagation(); return; }
      var first = list[0], last = list[list.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      e.stopPropagation();
    }
  }, true);

  /* ---------- bind the triggers ---------- */
  function isExcluded(im) {
    if (im.closest('a[href]')) return true;      /* inside a link: navigation wins */
    if (im.closest('[data-no-zoom]')) return true;
    if (im.hasAttribute('data-no-zoom')) return true;
    if (/(^|\s)icon(\s|$)/.test(im.className || '')) return true;
    return false;
  }

  var imgs = document.images;
  for (var j = 0; j < imgs.length; j++) {
    (function (im) {
      if (isExcluded(im)) return;
      im.classList.add('lb-trigger');
      im.setAttribute('tabindex', '0');
      im.setAttribute('role', 'button');
      var label = im.alt || im.getAttribute('src') || 'image';
      im.setAttribute('aria-label', label + ' — opens larger view');
      im.addEventListener('click', function () { open(im); });
      im.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(im); }
      });
    })(imgs[j]);
  }
})();
