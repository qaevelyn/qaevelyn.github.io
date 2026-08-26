---
permalink: /portfolio/
title: "Lookbook — Sovereign AI Portfolio"
---

<style>
/* ===== FONTS ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@700&display=swap');

/* ===== RESET & BASE ===== */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', sans-serif;
  background: #faf9f7;
  color: #1a1a1a;
}

.lookbook-container {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

/* ===== SPREADS ===== */
.ship-spread {
  display: none;
  gap: 2rem;
  align-items: stretch;
  margin: 1rem 0;
  animation: fadeIn 0.4s ease;
}

.ship-spread.active {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.ship-spread.intro {
  display: block;
  padding: 3rem 2.5rem;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.04);
  text-align: center;
}

.ship-spread.intro.active {
  display: block;
}

.ship-spread.toc {
  display: block;
  padding: 2.5rem 2rem;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.04);
  text-align: center;
}

.ship-spread.toc.active {
  display: block;
}

/* ===== PAGES ===== */
.ship-spread .page {
  padding: 1.75rem;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  justify-content: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.ship-spread .page:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0,0,0,0.08);
}

.ship-spread .page h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: #1a1a1a;
}

.ship-spread .page .badge {
  display: inline-block;
  background: #1a1a1a;
  color: #fff;
  padding: 0.2rem 1rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 0.75rem;
  align-self: flex-start;
}

.ship-spread .page .badge.ibm {
  background: #0062ff;
}

.ship-spread .page .badge.aws {
  background: #ff9900;
  color: #1a1a1a;
}

.ship-spread .page .badge.cert {
  background: #2d3748;
}

.ship-spread .page .links a {
  display: inline-block;
  margin: 0.25rem 0.25rem 0 0;
  padding: 0.4rem 1.2rem;
  background: #1a1a1a;
  color: #fff;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 500;
  transition: background 0.2s ease;
}

.ship-spread .page .links a:hover {
  background: #007acc;
}

.ship-spread .page .placeholder {
  width: 100%;
  height: 140px;
  background: #f0edea;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #888;
  font-size: 0.9rem;
  margin: 0.5rem 0;
  border: 1px dashed #ccc;
}

.ship-spread .page .school-image {
  width: 100%;
  height: 120px;
  background: #e8e4e0;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #666;
  font-size: 0.85rem;
  margin: 0.5rem 0;
  border: 1px solid #ddd;
}

.ship-spread .page .school-link {
  font-size: 0.9rem;
  margin-top: 0.25rem;
}

.ship-spread .page .school-link a {
  color: #007acc;
  text-decoration: none;
}

.ship-spread .page .school-link a:hover {
  text-decoration: underline;
}

/* ===== INTRO PAGE ===== */
.intro h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.2rem;
  margin-bottom: 0.75rem;
}

.intro .tagline {
  font-size: 1.2rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.intro .bio {
  max-width: 700px;
  margin: 0 auto 1rem auto;
  line-height: 1.7;
  font-size: 1.05rem;
  color: #2d2d2d;
}

.intro blockquote {
  font-size: 1.1rem;
  border-left: 4px solid #007acc;
  padding-left: 1.25rem;
  max-width: 600px;
  margin: 1rem auto;
  color: #1a1a1a;
  font-style: italic;
}

.intro .certs-summary {
  background: #f8f6f4;
  padding: 1rem 1.5rem;
  border-radius: 10px;
  max-width: 700px;
  margin: 1.25rem auto 0;
  font-size: 0.95rem;
  color: #2d2d2d;
  border: 1px solid #e8e4e0;
}

/* ===== TOC ===== */
.toc h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  margin-bottom: 1rem;
}

.toc ul {
  list-style: none;
  padding: 0;
  max-width: 400px;
  margin: 0 auto;
  text-align: left;
}

.toc ul li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #eee;
  font-size: 1rem;
}

.toc ul li a {
  color: #1a1a1a;
  text-decoration: none;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
}

.toc ul li a:hover {
  color: #007acc;
}

.toc ul li a .page-num {
  color: #888;
  font-weight: 400;
}

/* ===== NAVIGATION ===== */
.nav-controls {
  margin-top: 2.5rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.nav-controls button {
  padding: 0.6rem 1.8rem;
  font-size: 1rem;
  font-weight: 500;
  background: #1a1a1a;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.1s ease;
}

.nav-controls button:hover {
  background: #007acc;
}

.nav-controls button:active {
  transform: scale(0.96);
}

.nav-controls button:disabled {
  opacity: 0.3;
  cursor: not-allowed;
  transform: none;
}

.page-indicator {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #777;
  text-align: center;
}

/* ===== KEYBOARD HINT ===== */
.keyboard-hint {
  text-align: center;
  font-size: 0.8rem;
  color: #aaa;
  margin-top: 0.5rem;
}

/* ===== ANIMATIONS ===== */
@keyframes fadeIn {
  0% { opacity: 0; transform: translateY(8px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* ===== RESPONSIVE ===== */
@media (max-width: 700px) {
  .ship-spread.active {
    grid-template-columns: 1fr;
  }
  .intro h2 {
    font-size: 1.6rem;
  }
  .ship-spread .page h3 {
    font-size: 1.3rem;
  }
  .ship-spread.intro {
    padding: 2rem 1.25rem;
  }
  .toc ul li {
    font-size: 0.9rem;
  }
}
</style>

<div class="lookbook-container">

  <!-- ============================================================
  SPREAD 1 — TABLE OF CONTENTS (Page 1, stands alone)
  ============================================================ -->
  <div id="toc" class="ship-spread toc active">
    <h2>Lookbook</h2>
    <p style="margin-bottom: 1.5rem; color: #555;">Sovereign AI Portfolio — Evelyn Caro</p>
    <ul>
      <li><a href="#" onclick="goToSpread(1); return false;">Intro / Story <span class="page-num">Pages 2–3</span></a></li>
      <li><a href="#" onclick="goToSpread(2); return false;">Ship 1 — AWS SageMaker RAG <span class="page-num">Pages 4–5</span></a></li>
      <li><a href="#" onclick="goToSpread(3); return false;">Ship 2 — AWS SageMaker Agentic RAG <span class="page-num">Pages 6–7</span></a></li>
      <li><a href="#" onclick="goToSpread(4); return false;">Ship 3 — IBM Granite RAG <span class="page-num">Pages 8–9</span></a></li>
      <li><a href="#" onclick="goToSpread(5); return false;">Ship 4 — IBM Granite Agentic RAG <span class="page-num">Pages 10–11</span></a></li>
      <li><a href="#" onclick="goToSpread(6); return false;">Certifications <span class="page-num">Pages 12–13+</span></a></li>
    </ul>
  </div>

  <!-- ============================================================
  SPREAD 2 — INTRO / STORY (Pages 2–3)
  ============================================================ -->
  <div id="intro" class="ship-spread intro">
    <div style="grid-column: 1 / -1;">
      <h2>Intro / Story</h2>
      <div class="tagline">Sovereign AI Engineer · RAG Pipeline Architect · Lead Strategic Consultant</div>
      <div class="bio">
        <p>I engineer sovereign AI systems that run locally, on my terms. Built 4 RAG pipelines. Tested them adversarially. Now in conversation with a national historical organization partnered with a major university — proof of concept pending.</p>
        <p style="margin-top: 0.75rem;">This portfolio is a lookbook of my work — Ships first, then the credentials that built the foundation.</p>
      </div>
      <blockquote>Sovereign systems, local first. No cloud dependency.</blockquote>
      <div class="certs-summary">
        <strong>Credentials, not calendar:</strong> I hold certifications in AI, LangChain, and Agentic RAG from Google and IBM. I am currently adding AWS enterprise cloud certification through the Per Scholas re/Start program.
      </div>
    </div>
  </div>

  <!-- ============================================================
  SPREAD 3 — SHIP 1 (Pages 4–5)
  ============================================================ -->
  <div id="ship-1" class="ship-spread">
    <div class="page">
      <h3>Ship 1</h3>
      <div class="placeholder">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>AWS SageMaker · Standard RAG</em></p>
    </div>
    <div class="page">
      <h3>Ship 1 — AWS SageMaker RAG</h3>
      <div class="badge aws">Standard RAG</div>
      <p style="font-size:0.95rem; line-height:1.6;">Retrieval-Augmented Generation on AWS SageMaker using vector databases and large language models. Built and deployed locally on an M1 MacBook Air.</p>
      <div class="links">
        <a href="https://github.com/qaevelyn/ship1-aws-rag">GitHub</a>
        <a href="https://qaevelyn.github.io/ship1-aws-rag/">Live Demo</a>
      </div>
      <p style="font-size:0.85rem; color:#888; margin-top:0.5rem;">🎥 Video demo pending</p>
    </div>
  </div>

  <!-- ============================================================
  SPREAD 4 — SHIP 2 (Pages 6–7)
  ============================================================ -->
  <div id="ship-2" class="ship-spread">
    <div class="page">
      <h3>Ship 2</h3>
      <div class="placeholder">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>AWS SageMaker · Agentic RAG</em></p>
    </div>
    <div class="page">
      <h3>Ship 2 — AWS SageMaker Agentic RAG</h3>
      <div class="badge aws">Agentic RAG</div>
      <p style="font-size:0.95rem; line-height:1.6;">Agentic RAG pipeline on AWS SageMaker — retrieval + action (API calls, decision-making). Demonstrates autonomous reasoning and tool use.</p>
      <div class="links">
        <a href="https://github.com/qaevelyn/ship2-aws-agentic-rag">GitHub</a>
        <a href="https://qaevelyn.github.io/ship2-aws-agentic-rag/">Live Demo</a>
      </div>
      <p style="font-size:0.85rem; color:#888; margin-top:0.5rem;">🎥 Video demo pending</p>
    </div>
  </div>

  <!-- ============================================================
  SPREAD 5 — SHIP 3 (Pages 8–9)
  ============================================================ -->
  <div id="ship-3" class="ship-spread">
    <div class="page">
      <h3>Ship 3</h3>
      <div class="placeholder">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>IBM Granite · Standard RAG</em></p>
    </div>
    <div class="page">
      <h3>Ship 3 — IBM Granite RAG</h3>
      <div class="badge ibm">Standard RAG</div>
      <p style="font-size:0.95rem; line-height:1.6;">RAG pipeline on IBM Granite, demonstrating cross-platform AI/cloud capabilities. Built to show interoperability and model flexibility.</p>
      <div class="links">
        <a href="https://github.com/qaevelyn/ship3-ibm-granite-rag">GitHub</a>
        <a href="https://qaevelyn.github.io/ship3-ibm-granite-rag/">Live Demo</a>
      </div>
      <p style="font-size:0.85rem; color:#888; margin-top:0.5rem;">🎥 Video demo pending</p>
    </div>
  </div>

  <!-- ============================================================
  SPREAD 6 — SHIP 4 (Pages 10–11)
  ============================================================ -->
  <div id="ship-4" class="ship-spread">
    <div class="page">
      <h3>Ship 4</h3>
      <div class="placeholder">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>IBM Granite · Agentic RAG</em></p>
    </div>
    <div class="page">
      <h3>Ship 4 — IBM Granite Agentic RAG</h3>
      <div class="badge ibm">Agentic RAG</div>
      <p style="font-size:0.95rem; line-height:1.6;">Agentic RAG pipeline on IBM Granite — retrieval + action. Cross-platform agentic architecture with autonomous reasoning and decision-making.</p>
      <div class="links">
        <a href="https://github.com/qaevelyn/ship4-ibm-granite-agentic-rag">GitHub</a>
        <a href="https://qaevelyn.github.io/ship4-ibm-granite-agentic-rag/">Live Demo</a>
      </div>
      <p style="font-size:0.85rem; color:#888; margin-top:0.5rem;">🎥 Video demo pending</p>
    </div>
  </div>

  <!-- ============================================================
  SPREAD 7 — CERTIFICATIONS (Pages 12–13)
  ============================================================ -->
  <div id="certs-1" class="ship-spread">
    <div class="page">
      <h3>Google AI Professional Certificate</h3>
      <div class="badge cert">AI · ML</div>
      <div class="school-image">🏛️ Google — Homepage</div>
      <div class="school-link"><a href="https://developers.google.com/machine-learning" target="_blank">developers.google.com/machine-learning</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">Foundational AI and machine learning skills.</p>
    </div>
    <div class="page">
      <h3>IBM SkillsBuild — LangChain</h3>
      <div class="badge cert">LangChain</div>
      <div class="school-image">🏛️ IBM — Homepage</div>
      <div class="school-link"><a href="https://www.ibm.com/skillsbuild" target="_blank">ibm.com/skillsbuild</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">LangChain for building LLM-powered applications.</p>
    </div>
  </div>

  <!-- ============================================================
  SPREAD 8 — CERTIFICATIONS (Pages 14–15)
  ============================================================ -->
  <div id="certs-2" class="ship-spread">
    <div class="page">
      <h3>IBM SkillsBuild — Agentic RAG</h3>
      <div class="badge cert">Agentic RAG</div>
      <div class="school-image">🏛️ IBM — Homepage</div>
      <div class="school-link"><a href="https://www.ibm.com/skillsbuild" target="_blank">ibm.com/skillsbuild</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">Agentic RAG patterns and implementation.</p>
    </div>
    <div class="page">
      <h3>AWS re/Start — In Progress</h3>
      <div class="badge aws">AWS</div>
      <div class="school-image">🏛️ AWS — Homepage</div>
      <div class="school-link"><a href="https://aws.amazon.com/training/restart/" target="_blank">aws.amazon.com/training/restart</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">Enterprise cloud certification — currently enrolled.</p>
    </div>
  </div>

  <!-- ============================================================
  NAVIGATION
  ============================================================ -->
  <div class="nav-controls">
    <button id="prev-spread" disabled>← Previous</button>
    <button id="next-spread">Next →</button>
  </div>
  <div class="page-indicator" id="spread-counter">1 / 8</div>
  <div class="keyboard-hint">← → arrow keys to navigate</div>
</div>

<script>
(function() {
  const spreads = document.querySelectorAll('.ship-spread');
  const prevBtn = document.getElementById('prev-spread');
  const nextBtn = document.getElementById('next-spread');
  const counter = document.getElementById('spread-counter');
  let current = 0;

  function showSpread(index) {
    spreads.forEach((s, i) => {
      s.classList.toggle('active', i === index);
    });
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === spreads.length - 1;
    counter.textContent = (index + 1) + ' / ' + spreads.length;
    current = index;
    // Scroll to top of container
    document.querySelector('.lookbook-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function goToSpread(index) {
    if (index >= 0 && index < spreads.length) {
      showSpread(index);
    }
  }

  // Expose to global for TOC links
  window.goToSpread = goToSpread;

  prevBtn.addEventListener('click', () => {
    if (current > 0) showSpread(current - 1);
  });

  nextBtn.addEventListener('click', () => {
    if (current < spreads.length - 1) showSpread(current + 1);
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft' && current > 0) {
      e.preventDefault();
      showSpread(current - 1);
    } else if (e.key === 'ArrowRight' && current < spreads.length - 1) {
      e.preventDefault();
      showSpread(current + 1);
    }
  });

  showSpread(0);
})();
</script>
