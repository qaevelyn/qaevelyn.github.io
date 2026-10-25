/* ============================================================
   CREDENTIALS WALL — data + renderer (single file to edit)
   ------------------------------------------------------------
   TO ADD A CREDENTIAL WHEN A NEW ONE LANDS:
     1. find the right group below (or add a new group block),
     2. copy one { ... } item inside that group's items,
     3. change name / issuer / date / href — add img only if
        you have a picture saved in assets/certificates/,
     4. save, commit, push. The wall re-paginates itself:
        new pages and the footer count update automatically.
   Fields per item:
     name   (required)  certificate or badge title
     href   (required)  verify link (Credly badge or Coursera verify URL)
     date   (optional)  'YYYY-MM-DD' — shown when present
     issuer (optional)  shown under the name
     img    (optional)  path to badge/certificate image
     pdf    (optional)  path to certificate PDF (adds a PDF link)
     kind   (optional)  'cert' = framed card, 'badge' = grid tile
   Group fields: title, intro, note (all optional except title).
   Search note: Mir search reads assets/certificates/manifest.json
   (the archival copy with the 5-address records). Keep that file
   in sync when convenient; the wall itself renders from here.
   ============================================================ */
(function () {
  'use strict';

  var GROUPS = [
    {
      title: 'Google IT Support Professional Certificate',
      intro: 'Course 1 of 5 complete · more on the way',
      items: [
        { name: 'Technical Support Fundamentals',
          issuer: 'Google / Coursera',
          date: '2026-10-25',
          href: 'https://coursera.org/verify/TWQ8YQLJHR2Y',
          kind: 'cert' },
        /* when the Credly badge or the PDF is saved, fill in and uncomment:
        { name: 'Technical Support Fundamentals — badge',
          href: 'https://www.credly.com/badges/XXXX',
          img: '/assets/certificates/google-it-support-course1-badge.png',
          kind: 'badge' },
        */
      ]
    },
    {
      title: 'Google AI',
      intro: '8 courses · 20+ artifacts · Aug 7, 2026',
      items: [
        { name: 'Google AI Professional Certificate',
          issuer: 'Google / Coursera',
          date: '2026-08-07',
          href: 'https://www.credly.com/badges/1b0f3b19-6f35-486a-85cf-65c1a897676c',
          img: '/assets/certificates/google-ai-certificate-preview.png',
          pdf: '/assets/certificates/google-ai-professional-certificate.pdf',
          kind: 'cert' },
        { name: 'Google AI Professional Badge',
          href: 'https://www.credly.com/badges/1b0f3b19-6f35-486a-85cf-65c1a897676c',
          img: '/assets/certificates/google-ai-professional-badge.png',
          kind: 'badge',
          tally: false  /* second view of the Professional Certificate above, not a separate credential */ },
        { name: 'Google AI Fundamentals',
          href: 'https://www.credly.com/badges/a93bef28-d559-4572-9b98-f5b0c9a637ad',
          img: '/assets/certificates/google-ai-fundamentals.png',
          kind: 'badge' },
        { name: 'AI Essentials',
          href: 'https://www.credly.com/badges/2fc30f89-95bd-42e0-8219-e826a1b68eee',
          img: '/assets/certificates/google-ai-essentials-v1.png',
          kind: 'badge' },
        { name: 'App Building',
          href: 'https://www.credly.com/badges/8d92862f-45d2-43ad-9d3e-de9bbfea967e',
          img: '/assets/certificates/google-ai-for-app-building.png',
          kind: 'badge' },
        { name: 'Content Creation',
          href: 'https://www.credly.com/badges/f1fef12b-3618-49a1-be6e-ea3447f32fdd',
          img: '/assets/certificates/google-ai-for-content-creation.png',
          kind: 'badge' },
        { name: 'Data Analysis',
          href: 'https://www.credly.com/badges/7b038438-9ec9-429a-be0d-47a3e1982c5b',
          img: '/assets/certificates/google-ai-for-data-analysis.png',
          kind: 'badge' },
        { name: 'Writing & Communicating',
          href: 'https://www.credly.com/badges/b48d5eca-9c1f-4a75-9b68-d9326371e6ab',
          img: '/assets/certificates/google-ai-for-writing-and-communicating.png',
          kind: 'badge' },
        { name: 'Prompting Essentials',
          href: 'https://www.credly.com/badges/10455919-25fb-446d-b055-2e25d55a704d',
          img: '/assets/certificates/google-prompting-essentials.png',
          kind: 'badge' }
      ]
    },
    {
      title: 'AWS Educate',
      note: 'More AWS badges coming',
      items: [
        { name: 'Introduction to Generative AI',
          issuer: 'AWS Educate',
          href: 'https://www.credly.com/badges/3836cb8e-2f7f-475c-8b66-98aaab047ff1',
          img: '/assets/certificates/aws-educate-genai-badge.png',
          kind: 'badge' }
      ]
    },
    {
      title: 'CompTIA',
      items: [
        { name: 'CompTIA A+ Certified',
          issuer: 'CompTIA',
          href: 'https://www.credly.com/badges/470f60d6-bf36-46f4-8256-81a35364b2ee',
          img: '/assets/certificates/comptia-a-certification.png',
          kind: 'badge' }
      ]
    },
    {
      title: 'IBM SkillsBuild',
      items: [
        { name: 'Computer Hardware Basics',
          issuer: 'IBM SkillsBuild / Cisco',
          href: 'https://www.credly.com/badges/424ad3cf-4019-43a2-8924-6aa3398132b1',
          img: '/assets/certificates/ibm-computer-hardware-badge.png',
          kind: 'badge' },
        { name: 'Operating Systems Basics',
          issuer: 'IBM SkillsBuild / Cisco',
          href: 'https://www.credly.com/badges/10fda710-2935-430a-971c-6c5b513c7198',
          img: '/assets/certificates/ibm-operating-systems-badge.png',
          kind: 'badge' },
        { name: 'IBM SkillsBuild — LangChain',
          issuer: 'IBM SkillsBuild',
          href: '/assets/certificates/ibm-langchain-certificate.pdf',
          img: '/assets/certificates/ibm-langchain-certificate-preview.png',
          kind: 'cert' },
        { name: 'IBM SkillsBuild — Granite Agentic RAG',
          issuer: 'IBM SkillsBuild',
          href: '/assets/certificates/ibm-granite-agentic-rag-certificate.pdf',
          img: '/assets/certificates/ibm-granite-agentic-rag-certificate-preview.png',
          kind: 'cert' }
      ]
    }
  ];

  /* ---------- renderer: no dependencies, runs synchronously ---------- */

  var CERTS_PER_PAGE = 2;   // framed cards stack vertically
  var BADGES_PER_PAGE = 8;  // 2-column grid, 4 rows

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function fmtDate(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso || '');
    if (!m) return '';
    return MONTHS[Number(m[2]) - 1] + ' ' + Number(m[3]) + ', ' + m[1];
  }

  function el(html) {
    var d = document.createElement('div');
    d.innerHTML = html;
    return d.firstChild;
  }

  function metaLine(it) {
    var bits = [];
    if (it.issuer) bits.push(esc(it.issuer));
    var d = fmtDate(it.date);
    if (d) bits.push(d);
    var out = bits.join(' · ');
    if (it.href) {
      var label = /\.pdf(\?|#|$)/.test(it.href) ? 'Certificate' : 'Verify';
      out += (out ? ' · ' : '') +
        '<a href="' + esc(it.href) + '" target="_blank" rel="noopener">' + label + '</a>';
    }
    return out;
  }

  function certCard(it) {
    var inner = '';
    if (it.img) {
      inner += '<a href="' + esc(it.href) + '" target="_blank" rel="noopener">' +
               '<img src="' + esc(it.img) + '" alt="' + esc(it.name) + '"></a>';
      inner += '<div class="cert-cap" style="font-size:0.75rem; margin-top:0.3rem;">' +
               esc(it.name) + '</div>';
    } else {
      inner += '<div class="cred-name"><a href="' + esc(it.href) +
               '" target="_blank" rel="noopener">' + esc(it.name) + '</a></div>';
    }
    if (it.pdf) {
      inner += '<div class="cred-meta"><a href="' + esc(it.pdf) +
               '" target="_blank" rel="noopener">certificate PDF</a></div>';
    }
    inner += '<div class="cert-cap cred-meta">' + metaLine(it) + '</div>';
    return '<div class="cred-frame">' + inner + '</div>';
  }

  function badgeTile(it) {
    if (!it.img) {
      return '<div class="cred-card cred-tile">' +
             '<div class="cred-name"><a href="' + esc(it.href) + '" target="_blank" rel="noopener">' +
             esc(it.name) + '</a></div>' +
             '<div class="cert-cap cred-meta">' + metaLine(it) + '</div></div>';
    }
    return '<a href="' + esc(it.href) + '" target="_blank" rel="noopener" ' +
           'style="text-decoration:none; text-align:center;">' +
           '<img src="' + esc(it.img) + '" alt="' + esc(it.name) + '" ' +
           'style="width:100px; height:auto;">' +
           '<div class="cert-cap" style="font-size:0.7rem; margin-top:0.25rem;">' +
           esc(it.name) + '</div></a>';
  }

  function renderCredentialWall(mount) {
    if (!mount) return;

    var total = 0, newest = '';
    GROUPS.forEach(function (g) {
      (g.items || []).forEach(function (it) {
        if (it.tally === false) return;  /* alternate view of another item, not counted */
        total++;
        if (it.date && it.date > newest) newest = it.date;
      });
    });

    function newSpread(childTitle) {
      var s = el('<div class="spread" data-toc-parent="Certifications" ' +
                 'data-toc-child="' + esc(childTitle) + '"></div>');
      mount.appendChild(s);
      return s;
    }
    function newPage(spread) {
      var p = el('<div class="page"></div>');
      spread.appendChild(p);
      return p;
    }
    function valley(spread) {
      spread.appendChild(el('<div class="valley"></div>'));
    }

    GROUPS.forEach(function (g) {
      var items = (g.items || []).slice();
      var certs = items.filter(function (i) { return i.kind !== 'badge'; });
      var badges = items.filter(function (i) { return i.kind === 'badge'; });
      var spread = null, page = null;

      function ensure(cap) {
        if (!spread) { spread = newSpread(g.title); page = newPage(spread); }
        if (cap && page.__fill >= cap) closePage();
      }
      function closePage() {
        if (page && page.__fill > 0 && spread.children.length < 2) {
          valley(spread); page = newPage(spread);
        } else if (page && page.__fill > 0) {
          spread = newSpread(g.title + ' (cont.)'); page = newPage(spread);
        }
      }

      ensure();
      var h = document.createElement('h3');
      h.style.textAlign = 'center';
      h.textContent = g.title;
      page.appendChild(h);
      if (g.intro) {
        var p = document.createElement('p');
        p.style.cssText = 'font-size:0.85rem; text-align:center; color:#2c1810; margin:0.5rem 0;';
        p.textContent = g.intro;
        page.appendChild(p);
      }

      certs.forEach(function (it) {
        ensure(CERTS_PER_PAGE);
        page.insertAdjacentHTML('beforeend', certCard(it));
        page.__fill = (page.__fill || 0) + 1;
      });

      /* exhibit page then badge-collection page: a group with both gets
         its framed certificates on their own page, badges on the next */
      if (certs.length && badges.length) closePage();

      for (var i = 0; i < badges.length; i += BADGES_PER_PAGE) {
        ensure(BADGES_PER_PAGE);
        var grid = el('<div class="cred-grid"></div>');
        badges.slice(i, i + BADGES_PER_PAGE).forEach(function (b) {
          grid.insertAdjacentHTML('beforeend', badgeTile(b));
        });
        page.appendChild(grid);
        page.__fill = (page.__fill || 0) + badges.slice(i, i + BADGES_PER_PAGE).length;
      }

      if (g.note && page) {
        var n = document.createElement('p');
        n.className = 'cert-cap';
        n.style.cssText = 'font-size:0.8rem; text-align:center; margin-top:1rem;';
        n.textContent = g.note;
        page.appendChild(n);
      }
    });

    if (newest) {
      var lastSpread = mount.querySelectorAll('.spread');
      var last = lastSpread[lastSpread.length - 1];
      var pages = last.querySelectorAll('.page');
      var lp = pages[pages.length - 1];
      var foot = document.createElement('p');
      foot.className = 'cert-cap cred-note';
      foot.textContent = total + ' credentials on the wall · most recent ' +
                         fmtDate(newest) + ' · records: assets/certificates/manifest.json';
      lp.appendChild(foot);
    }
  }

  window.renderCredentialWall = renderCredentialWall;
})();
