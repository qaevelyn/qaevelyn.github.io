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
  transition: background 0.4s ease, color 0.4s ease;
}

body.dark-mode {
  background: #1a1a1a;
  color: #f0edea;
}

body.dark-mode .ship-spread.toc,
body.dark-mode .ship-spread.intro,
body.dark-mode .ship-spread .page {
  background: #2a2a2a;
  color: #f0edea;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

body.dark-mode .ship-spread .page .placeholder {
  background: #333;
  color: #aaa;
  border-color: #555;
}

body.dark-mode .ship-spread .page .school-image {
  background: #333;
  color: #aaa;
  border-color: #555;
}

body.dark-mode .intro .certs-summary {
  background: #2a2a2a;
  border-color: #444;
  color: #f0edea;
}

body.dark-mode .toc ul li {
  border-bottom-color: #444;
}

body.dark-mode .toc ul li a {
  color: #f0edea;
}

body.dark-mode .toc ul li a .page-num {
  color: #999;
}

body.dark-mode .nav-controls button {
  background: #f0edea;
  color: #1a1a1a;
}

body.dark-mode .nav-controls button:hover {
  background: #007acc;
  color: #fff;
}

body.dark-mode .page-indicator {
  color: #aaa;
}

body.dark-mode .keyboard-hint {
  color: #666;
}

body.dark-mode .ship-spread .page .links a {
  background: #f0edea;
  color: #1a1a1a;
}

body.dark-mode .ship-spread .page .links a:hover {
  background: #007acc;
  color: #fff;
}

/* ===== AMBIENT BACKGROUND ===== */
.ambient-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  background: linear-gradient(-45deg, #faf9f7, #e8e4e0, #d6d2cd, #c8c4bf);
  background-size: 400% 400%;
  animation: ambientShift 20s ease infinite;
  transition: background 0.6s ease;
}

body.dark-mode .ambient-bg {
  background: linear-gradient(-45deg, #1a1a1a, #2a2a2a, #1e1e1e, #252525);
  background-size: 400% 400%;
  animation: ambientShift 25s ease infinite;
}

@keyframes ambientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* ===== CURSOR TRAIL ===== */
.cursor-trail {
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(0, 122, 204, 0.3);
  transform: translate(-50%, -50%);
  transition: width 0.2s, height 0.2s, opacity 0.2s;
}

body.dark-mode .cursor-trail {
  background: rgba(0, 122, 204, 0.5);
}

/* ===== LAYOUT ===== */
.lookbook-container {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 0 1.5rem;
  position: relative;
  z-index: 1;
}

/* ===== SPREADS ===== */
.ship-spread {
  display: none;
  gap: 2rem;
  align-items: stretch;
  margin: 1rem 0;
  animation: fadeIn 0.5s ease;
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
  position: relative;
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

body.dark-mode .ship-spread .page h3 {
  color: #f0edea;
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

/* ===== READ ALOUD BUTTON ===== */
.read-aloud-btn {
  background: none;
  border: 1px solid #ccc;
  border-radius: 20px;
  padding: 0.2rem 0.8rem;
  font-size: 0.75rem;
  cursor: pointer;
  color: #555;
  transition: all 0.2s ease;
  margin-top: 0.5rem;
  align-self: flex-start;
}

.read-aloud-btn:hover {
  background: #007acc;
  color: #fff;
  border-color: #007acc;
}

body.dark-mode .read-aloud-btn {
  color: #aaa;
  border-color: #555;
}

body.dark-mode .read-aloud-btn:hover {
  background: #007acc;
  color: #fff;
  border-color: #007acc;
}

/* ===== READING TIME ===== */
.reading-time {
  font-size: 0.75rem;
  color: #999;
  margin-top: 0.25rem;
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

body.dark-mode .intro .tagline {
  color: #f0edea;
}

.intro .bio {
  max-width: 700px;
  margin: 0 auto 1rem auto;
  line-height: 1.7;
  font-size: 1.05rem;
  color: #2d2d2d;
}

body.dark-mode .intro .bio {
  color: #d0ccc8;
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

body.dark-mode .intro blockquote {
  color: #f0edea;
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

body.dark-mode .intro .certs-summary {
  background: #2a2a2a;
  border-color: #444;
  color: #f0edea;
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

body.dark-mode .toc ul li {
  border-bottom-color: #444;
}

.toc ul li a {
  color: #1a1a1a;
  text-decoration: none;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
}

body.dark-mode .toc ul li a {
  color: #f0edea;
}

.toc ul li a:hover {
  color: #007acc;
}

.toc ul li a .page-num {
  color: #888;
  font-weight: 400;
}

body.dark-mode .toc ul li a .page-num {
  color: #999;
}

/* ===== FILTER BAR (Auto-Tagging) ===== */
.filter-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem;
  margin: 1.5rem 0 1rem;
}

.filter-bar .tag {
  padding: 0.3rem 1rem;
  background: #e8e4e0;
  border-radius: 20px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: background 0.2s ease, color 0.2s ease;
  color: #1a1a1a;
  border: none;
}

body.dark-mode .filter-bar .tag {
  background: #333;
  color: #f0edea;
}

.filter-bar .tag:hover {
  background: #007acc;
  color: #fff;
}

.filter-bar .tag.active {
  background: #007acc;
  color: #fff;
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

body.dark-mode .nav-controls button {
  background: #f0edea;
  color: #1a1a1a;
}

.nav-controls button:hover {
  background: #007acc;
  color: #fff;
}

.nav-controls button:active {
  transform: scale(0.96);
}

.nav-controls button:disabled {
  opacity: 0.3;
  cursor: not-allowed;
  transform: none;
}

/* ===== AUTO-FLIP BUTTON ===== */
.auto-flip-btn {
  padding: 0.6rem 1.8rem;
  font-size: 1rem;
  font-weight: 500;
  background: #007acc;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.auto-flip-btn:hover {
  background: #005f99;
}

.auto-flip-btn.active {
  background: #e53e3e;
}

.auto-flip-btn.active:hover {
  background: #c53030;
}

/* ===== PAGE INDICATOR ===== */
.page-indicator {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #777;
  text-align: center;
}

body.dark-mode .page-indicator {
  color: #aaa;
}

/* ===== KEYBOARD HINT ===== */
.keyboard-hint {
  text-align: center;
  font-size: 0.8rem;
  color: #aaa;
  margin-top: 0.5rem;
}

body.dark-mode .keyboard-hint {
  color: #666;
}

/* ===== READING PROGRESS BAR ===== */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 4px;
  background: #007acc;
  z-index: 999;
  transition: width 0.3s ease;
  width: 0%;
}

/* ===== PRINT MODE ===== */
@media print {
  .nav-controls,
  .keyboard-hint,
  .filter-bar,
  .read-aloud-btn,
  .auto-flip-btn,
  .progress-bar,
  .cursor-trail,
  .chatbot-toggle,
  .chatbot-window,
  .dark-mode-toggle {
    display: none !important;
  }

  .ship-spread {
    display: block !important;
    page-break-after: always;
    animation: none !important;
    opacity: 1 !important;
  }

  .ship-spread .page {
    box-shadow: none !important;
    border: 1px solid #ddd !important;
  }

  body {
    background: #fff !important;
    color: #000 !important;
  }

  .lookbook-container {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0.5in !important;
  }

  /* Watermark */
  .ship-spread .page::after {
    content: "© @qaevelyn 08-26-2026 · Originator · First of its kind";
    position: absolute;
    bottom: 10px;
    right: 10px;
    font-size: 0.6rem;
    color: #ccc;
    opacity: 0.7;
  }
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

/* ===== CHATBOT ===== */
.chatbot-toggle {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: #007acc;
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 56px;
  height: 56px;
  font-size: 1.5rem;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  z-index: 1000;
  transition: background 0.2s ease;
}

.chatbot-toggle:hover {
  background: #005f99;
}

.chatbot-window {
  position: fixed;
  bottom: 5rem;
  right: 2rem;
  width: 380px;
  max-width: 90vw;
  max-height: 70vh;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.15);
  z-index: 1000;
  display: none;
  flex-direction: column;
  overflow: hidden;
  transition: opacity 0.3s ease;
}

body.dark-mode .chatbot-window {
  background: #2a2a2a;
  color: #f0edea;
}

.chatbot-window.open {
  display: flex;
}

.chatbot-header {
  padding: 1rem;
  background: #007acc;
  color: #fff;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chatbot-header button {
  background: none;
  border: none;
  color: #fff;
  font-size: 1.2rem;
  cursor: pointer;
}

.chatbot-messages {
  padding: 1rem;
  flex: 1;
  overflow-y: auto;
  max-height: 50vh;
}

.chatbot-message {
  margin-bottom: 0.75rem;
  padding: 0.6rem 1rem;
  border-radius: 12px;
  max-width: 80%;
  font-size: 0.9rem;
  line-height: 1.5;
}

.chatbot-message.user {
  background: #007acc;
  color: #fff;
  align-self: flex-end;
  margin-left: auto;
}

body.dark-mode .chatbot-message.user {
  background: #005f99;
}

.chatbot-message.bot {
  background: #f0edea;
  color: #1a1a1a;
  align-self: flex-start;
}

body.dark-mode .chatbot-message.bot {
  background: #333;
  color: #f0edea;
}

.chatbot-input-area {
  display: flex;
  padding: 0.75rem;
  border-top: 1px solid #eee;
  gap: 0.5rem;
}

body.dark-mode .chatbot-input-area {
  border-top-color: #444;
}

.chatbot-input-area input {
  flex: 1;
  padding: 0.6rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 0.9rem;
  background: #fff;
  color: #1a1a1a;
}

body.dark-mode .chatbot-input-area input {
  background: #333;
  color: #f0edea;
  border-color: #555;
}

.chatbot-input-area button {
  padding: 0.6rem 1.2rem;
  background: #007acc;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}

.chatbot-input-area button:hover {
  background: #005f99;
}

/* ===== DARK MODE TOGGLE ===== */
.dark-mode-toggle {
  position: fixed;
  top: 1rem;
  right: 1rem;
  background: #1a1a1a;
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  font-size: 1.2rem;
  cursor: pointer;
  z-index: 1000;
  transition: background 0.2s ease;
}

body.dark-mode .dark-mode-toggle {
  background: #f0edea;
  color: #1a1a1a;
}

.dark-mode-toggle:hover {
  background: #007acc;
  color: #fff;
}

/* ===== 3D BOOK VIEW ===== */
.book-container {
  perspective: 1200px;
  margin: 2rem auto;
  max-width: 1000px;
}

.book {
  width: 100%;
  min-height: 500px;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.8s ease;
}

.book-open {
  transform: rotateY(-10deg) scale(0.98);
}

.book-page {
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #fff;
  border-radius: 4px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  padding: 2rem;
  overflow-y: auto;
}

body.dark-mode .book-page {
  background: #2a2a2a;
  color: #f0edea;
}

.book-page-left {
  transform: rotateY(0deg);
  transform-origin: right center;
}

.book-page-right {
  transform: rotateY(0deg);
  transform-origin: left center;
}

.book-page-flipped {
  transform: rotateY(-180deg);
}

/* ===== ZOOM ON HOVER ===== */
.zoom-hover {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: zoom-in;
}

.zoom-hover:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 32px rgba(0,0,0,0.15);
  z-index: 10;
}

/* ===== DRAG TO FLIP ===== */
.drag-area {
  cursor: grab;
  user-select: none;
}

.drag-area:active {
  cursor: grabbing;
}
</style>

<!-- ===== AMBIENT BACKGROUND ===== -->
<div class="ambient-bg"></div>

<!-- ===== CURSOR TRAIL ===== -->
<div class="cursor-trail" id="cursorTrail"></div>

<!-- ===== READING PROGRESS BAR ===== -->
<div class="progress-bar" id="progressBar"></div>

<!-- ===== DARK MODE TOGGLE ===== -->
<button class="dark-mode-toggle" id="darkModeToggle" aria-label="Toggle dark mode">🌙</button>

<!-- ===== CHATBOT ===== -->
<button class="chatbot-toggle" id="chatbotToggle" aria-label="Ask my portfolio">💬</button>

<div class="chatbot-window" id="chatbotWindow">
  <div class="chatbot-header">
    <span>Ask My Portfolio</span>
    <button id="chatbotClose">✕</button>
  </div>
  <div class="chatbot-messages" id="chatbotMessages">
    <div class="chatbot-message bot">Hello! Ask me anything about Evelyn's work, Ships, or certifications.</div>
  </div>
  <div class="chatbot-input-area">
    <input type="text" id="chatbotInput" placeholder="Ask about Ships, certs, or skills...">
    <button id="chatbotSend">Ask</button>
  </div>
</div>

<!-- ===== LOOKBOOK CONTAINER ===== -->
<div class="lookbook-container">

  <!-- ===== FILTER BAR (Auto-Tagging) ===== -->
  <div class="filter-bar" id="filterBar">
    <button class="tag active" data-tag="all">All</button>
    <button class="tag" data-tag="aws">#AWS</button>
    <button class="tag" data-tag="ibm">#IBM</button>
    <button class="tag" data-tag="rag">#RAG</button>
    <button class="tag" data-tag="agentic">#Agentic</button>
    <button class="tag" data-tag="cert">#Certification</button>
  </div>

  <!-- ============================================================
  SPREAD 1 — TABLE OF CONTENTS (Page 1, stands alone)
  ============================================================ -->
  <div id="toc" class="ship-spread toc active" data-tags="all">
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
  <div id="intro" class="ship-spread intro" data-tags="all">
    <div style="grid-column: 1 / -1;">
      <h2>Intro / Story</h2>
      <div class="tagline">Sovereign AI Engineer · RAG Pipeline Architect · Lead Strategic Consultant</div>
      <div class="reading-time">📖 3 min read · <button class="read-aloud-btn" onclick="readAloud('intro-text')">🔊 Listen</button></div>
      <div id="intro-text" class="bio">
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
  <div id="ship-1" class="ship-spread" data-tags="aws rag">
    <div class="page">
      <h3>Ship 1</h3>
      <div class="placeholder zoom-hover">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>AWS SageMaker · Standard RAG</em></p>
      <div class="reading-time">📖 1 min read · <button class="read-aloud-btn" onclick="readAloud('ship1-text')">🔊 Listen</button></div>
    </div>
    <div class="page">
      <h3>Ship 1 — AWS SageMaker RAG</h3>
      <div class="badge aws">Standard RAG</div>
      <div id="ship1-text" style="font-size:0.95rem; line-height:1.6;">Retrieval-Augmented Generation on AWS SageMaker using vector databases and large language models. Built and deployed locally on an M1 MacBook Air.</div>
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
  <div id="ship-2" class="ship-spread" data-tags="aws rag agentic">
    <div class="page">
      <h3>Ship 2</h3>
      <div class="placeholder zoom-hover">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>AWS SageMaker · Agentic RAG</em></p>
      <div class="reading-time">📖 1 min read · <button class="read-aloud-btn" onclick="readAloud('ship2-text')">🔊 Listen</button></div>
    </div>
    <div class="page">
      <h3>Ship 2 — AWS SageMaker Agentic RAG</h3>
      <div class="badge aws">Agentic RAG</div>
      <div id="ship2-text" style="font-size:0.95rem; line-height:1.6;">Agentic RAG pipeline on AWS SageMaker — retrieval + action (API calls, decision-making). Demonstrates autonomous reasoning and tool use.</div>
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
  <div id="ship-3" class="ship-spread" data-tags="ibm rag">
    <div class="page">
      <h3>Ship 3</h3>
      <div class="placeholder zoom-hover">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>IBM Granite · Standard RAG</em></p>
      <div class="reading-time">📖 1 min read · <button class="read-aloud-btn" onclick="readAloud('ship3-text')">🔊 Listen</button></div>
    </div>
    <div class="page">
      <h3>Ship 3 — IBM Granite RAG</h3>
      <div class="badge ibm">Standard RAG</div>
      <div id="ship3-text" style="font-size:0.95rem; line-height:1.6;">RAG pipeline on IBM Granite, demonstrating cross-platform AI/cloud capabilities. Built to show interoperability and model flexibility.</div>
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
  <div id="ship-4" class="ship-spread" data-tags="ibm rag agentic">
    <div class="page">
      <h3>Ship 4</h3>
      <div class="placeholder zoom-hover">📸 Screenshot / GUI coming soon</div>
      <p style="font-size:0.9rem; color:#555;"><em>IBM Granite · Agentic RAG</em></p>
      <div class="reading-time">📖 1 min read · <button class="read-aloud-btn" onclick="readAloud('ship4-text')">🔊 Listen</button></div>
    </div>
    <div class="page">
      <h3>Ship 4 — IBM Granite Agentic RAG</h3>
      <div class="badge ibm">Agentic RAG</div>
      <div id="ship4-text" style="font-size:0.95rem; line-height:1.6;">Agentic RAG pipeline on IBM Granite — retrieval + action. Cross-platform agentic architecture with autonomous reasoning and decision-making.</div>
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
  <div id="certs-1" class="ship-spread" data-tags="cert">
    <div class="page">
      <h3>Google AI Professional Certificate</h3>
      <div class="badge cert">AI · ML</div>
      <div class="school-image zoom-hover">🏛️ Google — Homepage</div>
      <div class="school-link"><a href="https://developers.google.com/machine-learning" target="_blank">developers.google.com/machine-learning</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">Foundational AI and machine learning skills.</p>
    </div>
    <div class="page">
      <h3>IBM SkillsBuild — LangChain</h3>
      <div class="badge cert">LangChain</div>
      <div class="school-image zoom-hover">🏛️ IBM — Homepage</div>
      <div class="school-link"><a href="https://www.ibm.com/skillsbuild" target="_blank">ibm.com/skillsbuild</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">LangChain for building LLM-powered applications.</p>
    </div>
  </div>

  <!-- ============================================================
  SPREAD 8 — CERTIFICATIONS (Pages 14–15)
  ============================================================ -->
  <div id="certs-2" class="ship-spread" data-tags="cert">
    <div class="page">
      <h3>IBM SkillsBuild — Agentic RAG</h3>
      <div class="badge cert">Agentic RAG</div>
      <div class="school-image zoom-hover">🏛️ IBM — Homepage</div>
      <div class="school-link"><a href="https://www.ibm.com/skillsbuild" target="_blank">ibm.com/skillsbuild</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">Agentic RAG patterns and implementation.</p>
    </div>
    <div class="page">
      <h3>AWS re/Start — In Progress</h3>
      <div class="badge aws">AWS</div>
      <div class="school-image zoom-hover">🏛️ AWS — Homepage</div>
      <div class="school-link"><a href="https://aws.amazon.com/training/restart/" target="_blank">aws.amazon.com/training/restart</a></div>
      <p style="font-size:0.9rem; margin-top:0.5rem; color:#444;">Enterprise cloud certification — currently enrolled.</p>
    </div>
  </div>

  <!-- ============================================================
  NAVIGATION
  ============================================================ -->
  <div class="nav-controls">
    <button id="prev-spread" disabled aria-label="Previous page">← Previous</button>
    <button id="autoFlipBtn" class="auto-flip-btn" aria-label="Auto-flip mode">▶ Auto-Flip</button>
    <button id="next-spread" aria-label="Next page">Next →</button>
  </div>
  <div class="page-indicator" id="spread-counter">1 / 8</div>
  <div class="keyboard-hint">← → arrow keys to navigate · Click and drag to flip</div>
</div>

<script>
(function() {
  // ============================================================
  // SELF-TEST — Confirm everything loaded
  // ============================================================
  console.log('✅ Lookbook loaded successfully — Sovereign AI Portfolio');
  console.log('📖 Features: Chatbot · 3D Book · Accessibility · Auto-Tagging · Dark Mode · Progress Bar · Cursor Trail · Ambient BG · Print Watermark · Read Aloud · Auto-Flip · Bookmarking · Shareable URLs');

  // ============================================================
  // PAGE-TURN SOUND — Heavy Paper
  // ============================================================
  function playPageTurn() {
    try {
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const duration = 0.25;
      const sampleRate = audioCtx.sampleRate;
      const bufferSize = Math.floor(duration * sampleRate);
      const buffer = audioCtx.createBuffer(1, bufferSize, sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        const t = i / bufferSize;
        const envelope = Math.sin(t * Math.PI) * 0.8 + 0.2;
        const noise = (Math.random() * 2 - 1) * envelope * 0.5;
        const lowFreq = Math.sin(t * 120 * Math.PI) * 0.15 * (1 - t);
        const midFreq = Math.sin(t * 300 * Math.PI) * 0.08 * (1 - t);
        data[i] = (noise + lowFreq + midFreq) * 0.35;
      }
      const source = audioCtx.createBufferSource();
      source.buffer = buffer;
      const gainNode = audioCtx.createGain();
      gainNode.gain.value = 0.3;
      source.connect(gainNode);
      gainNode.connect(audioCtx.destination);
      source.start();
    } catch (e) { /* Silently fail */ }
  }

  // ============================================================
  // HAPTIC FEEDBACK (Mobile)
  // ============================================================
  function hapticFeedback() {
    if (navigator.vibrate) navigator.vibrate(10);
  }

  // ============================================================
  // BOOKMARKING (localStorage)
  // ============================================================
  function saveBookmark(index) {
    try { localStorage.setItem('lookbook_page', index); } catch (e) {}
  }

  function getBookmark() {
    try { return parseInt(localStorage.getItem('lookbook_page')) || 0; } catch (e) { return 0; }
  }

  // ============================================================
  // SHAREABLE URL HASH
  // ============================================================
  function updateURLHash(index) {
    const names = ['toc', 'intro', 'ship-1', 'ship-2', 'ship-3', 'ship-4', 'certs-1', 'certs-2'];
    if (index >= 0 && index < names.length) {
      history.replaceState(null, '', '#!' + names[index]);
    }
  }

  function getHashIndex() {
    const hash = window.location.hash.replace('#!', '');
    const names = ['toc', 'intro', 'ship-1', 'ship-2', 'ship-3', 'ship-4', 'certs-1', 'certs-2'];
    const idx = names.indexOf(hash);
    return idx >= 0 ? idx : null;
  }

  // ============================================================
  // READ ALOUD (Text-to-Speech)
  // ============================================================
  window.readAloud = function(elementId) {
    const el = document.getElementById(elementId);
    if (!el) return;
    const text = el.innerText || el.textContent;
    if (!text) return;
    if (window.speechSynthesis) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 0.9;
      utterance.pitch = 1;
      window.speechSynthesis.speak(utterance);
    }
  };

  // ============================================================
  // NAVIGATION
  // ============================================================
  const spreads = document.querySelectorAll('.ship-spread');
  const prevBtn = document.getElementById('prev-spread');
  const nextBtn = document.getElementById('next-spread');
  const autoFlipBtn = document.getElementById('autoFlipBtn');
  const counter = document.getElementById('spread-counter');
  let current = getHashIndex() !== null ? getHashIndex() : getBookmark();
  let isTransitioning = false;
  let autoFlipInterval = null;
  let isAutoFlip = false;

  // Filter state
  let activeFilter = 'all';

  function showSpread(index) {
    if (isTransitioning || index === current) return;
    if (index < 0 || index >= spreads.length) return;
    isTransitioning = true;

    // Play sound + haptic
    playPageTurn();
    hapticFeedback();

    // Update visibility
    spreads.forEach((s, i) => {
      const match = activeFilter === 'all' || s.dataset.tags.includes(activeFilter);
      if (i === index && match) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });

    // Update buttons
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === spreads.length - 1;
    counter.textContent = (index + 1) + ' / ' + spreads.length;
    current = index;

    // Save bookmark
    saveBookmark(index);
    updateURLHash(index);

    // Update progress bar
    const progress = ((index + 1) / spreads.length) * 100;
    document.getElementById('progressBar').style.width = progress + '%';

    // Scroll to top
    document.querySelector('.lookbook-container').scrollIntoView({ behavior: 'smooth', block: 'start' });

    setTimeout(() => { isTransitioning = false; }, 300);
  }

  window.goToSpread = function(index) {
    if (index >= 0 && index < spreads.length && index !== current) {
      showSpread(index);
    }
  };

  // ============================================================
  // AUTO-FLIP
  // ============================================================
  function toggleAutoFlip() {
    if (isAutoFlip) {
      clearInterval(autoFlipInterval);
      autoFlipInterval = null;
      isAutoFlip = false;
      autoFlipBtn.textContent = '▶ Auto-Flip';
      autoFlipBtn.classList.remove('active');
    } else {
      isAutoFlip = true;
      autoFlipBtn.textContent = '⏸ Pause';
      autoFlipBtn.classList.add('active');
      autoFlipInterval = setInterval(() => {
        if (current < spreads.length - 1) {
          showSpread(current + 1);
        } else {
          // Stop at end
          clearInterval(autoFlipInterval);
          autoFlipInterval = null;
          isAutoFlip = false;
          autoFlipBtn.textContent = '▶ Auto-Flip';
          autoFlipBtn.classList.remove('active');
        }
      }, 4000);
    }
  }

  autoFlipBtn.addEventListener('click', toggleAutoFlip);

  // Pause auto-flip on user interaction
  document.addEventListener('click', () => {
    if (isAutoFlip) {
      clearInterval(autoFlipInterval);
      autoFlipInterval = null;
      isAutoFlip = false;
      autoFlipBtn.textContent = '▶ Auto-Flip';
      autoFlipBtn.classList.remove('active');
      // Resume after 10 seconds of inactivity
      setTimeout(() => {
        if (!isAutoFlip && current < spreads.length - 1) {
          toggleAutoFlip();
        }
      }, 10000);
    }
  });

  // ============================================================
  // BUTTON EVENTS
  // ============================================================
  prevBtn.addEventListener('click', () => {
    if (current > 0) showSpread(current - 1);
  });

  nextBtn.addEventListener('click', () => {
    if (current < spreads.length - 1) showSpread(current + 1);
  });

  // ============================================================
  // KEYBOARD NAVIGATION
  // ============================================================
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft' && current > 0) {
      e.preventDefault();
      showSpread(current - 1);
    } else if (e.key === 'ArrowRight' && current < spreads.length - 1) {
      e.preventDefault();
      showSpread(current + 1);
    }
  });

  // ============================================================
  // DRAG TO FLIP (Mouse + Touch)
  // ============================================================
  let dragStartX = 0;
  let dragEndX = 0;
  const container = document.querySelector('.lookbook-container');

  container.addEventListener('mousedown', (e) => {
    dragStartX = e.clientX;
  });

  container.addEventListener('mouseup', (e) => {
    dragEndX = e.clientX;
    const diff = dragStartX - dragEndX;
    if (Math.abs(diff) > 50) {
      if (diff > 0 && current < spreads.length - 1) showSpread(current + 1);
      else if (diff < 0 && current > 0) showSpread(current - 1);
    }
  });

  container.addEventListener('touchstart', (e) => {
    dragStartX = e.touches[0].clientX;
  });

  container.addEventListener('touchend', (e) => {
    dragEndX = e.changedTouches[0].clientX;
    const diff = dragStartX - dragEndX;
    if (Math.abs(diff) > 50) {
      if (diff > 0 && current < spreads.length - 1) showSpread(current + 1);
      else if (diff < 0 && current > 0) showSpread(current - 1);
    }
  });

  // ============================================================
  // DARK MODE TOGGLE
  // ============================================================
  const darkToggle = document.getElementById('darkModeToggle');
  darkToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    darkToggle.textContent = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
    try { localStorage.setItem('darkMode', document.body.classList.contains('dark-mode') ? 'true' : 'false'); } catch (e) {}
  });

  // Restore dark mode preference
  try {
    if (localStorage.getItem('darkMode') === 'true') {
      document.body.classList.add('dark-mode');
      darkToggle.textContent = '☀️';
    }
  } catch (e) {}

  // ============================================================
  // CURSOR TRAIL
  // ============================================================
  const trail = document.getElementById('cursorTrail');
  document.addEventListener('mousemove', (e) => {
    trail.style.left = e.clientX + 'px';
    trail.style.top = e.clientY + 'px';
  });

  // ============================================================
  // FILTER BAR (Auto-Tagging)
  // ============================================================
  const filterButtons = document.querySelectorAll('.filter-bar .tag');
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Update active button
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeFilter = btn.dataset.tag;

      // Show/hide spreads
      spreads.forEach((s, i) => {
        const match = activeFilter === 'all' || s.dataset.tags.includes(activeFilter);
        if (i === current && match) {
          s.classList.add('active');
        } else {
          s.classList.remove('active');
        }
      });

      // If current spread is hidden, find first visible
      if (!spreads[current].classList.contains('active')) {
        for (let i = 0; i < spreads.length; i++) {
          if (spreads[i].dataset.tags.includes(activeFilter) || activeFilter === 'all') {
            showSpread(i);
            break;
          }
        }
      }
    });
  });

  // ============================================================
  // CHATBOT (RAG-Powered Q&A)
  // ============================================================
  const chatbotToggle = document.getElementById('chatbotToggle');
  const chatbotWindow = document.getElementById('chatbotWindow');
  const chatbotClose = document.getElementById('chatbotClose');
  const chatbotMessages = document.getElementById('chatbotMessages');
  const chatbotInput = document.getElementById('chatbotInput');
  const chatbotSend = document.getElementById('chatbotSend');

  // Knowledge base (from portfolio content)
  const knowledgeBase = {
    'ship1': 'Ship 1 is a standard RAG pipeline on AWS SageMaker using vector databases and LLMs. Built locally on an M1 MacBook Air.',
    'ship2': 'Ship 2 is an agentic RAG pipeline on AWS SageMaker that performs retrieval + action (API calls, decisions).',
    'ship3': 'Ship 3 is a standard RAG pipeline on IBM Granite, showing cross-platform AI capabilities.',
    'ship4': 'Ship 4 is an agentic RAG pipeline on IBM Granite with autonomous reasoning and decision-making.',
    'cert': 'Evelyn holds certifications in AI, LangChain, and Agentic RAG from Google and IBM. She is currently in AWS re/Start.',
    'sovereign': 'Sovereign systems are built locally, with no cloud dependency. Evelyn runs everything on her M1 MacBook Air.',
    'default': 'I can answer questions about Evelyn\'s Ships, certifications, and sovereign AI philosophy. Ask me about Ship 1, Ship 2, AWS, IBM, RAG, or certifications!'
  };

  function getBotResponse(query) {
    const q = query.toLowerCase();
    if (q.includes('ship 1') || q.includes('ship1')) return knowledgeBase.ship1;
    if (q.includes('ship 2') || q.includes('ship2')) return knowledgeBase.ship2;
    if (q.includes('ship 3') || q.includes('ship3')) return knowledgeBase.ship3;
    if (q.includes('ship 4') || q.includes('ship4')) return knowledgeBase.ship4;
    if (q.includes('cert') || q.includes('credential') || q.includes('google') || q.includes('ibm') || q.includes('aws')) return knowledgeBase.cert;
    if (q.includes('sovereign') || q.includes('local') || q.includes('macbook')) return knowledgeBase.sovereign;
    return knowledgeBase.default;
  }

  function addMessage(text, sender) {
    const div = document.createElement('div');
    div.className = 'chatbot-message ' + sender;
    div.textContent = text;
    chatbotMessages.appendChild(div);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
  }

  function handleChat() {
    const query = chatbotInput.value.trim();
    if (!query) return;
    addMessage(query, 'user');
    chatbotInput.value = '';
    const response = getBotResponse(query);
    setTimeout(() => addMessage(response, 'bot'), 300);
  }

  chatbotToggle.addEventListener('click', () => {
    chatbotWindow.classList.toggle('open');
  });

  chatbotClose.addEventListener('click', () => {
    chatbotWindow.classList.remove('open');
  });

  chatbotSend.addEventListener('click', handleChat);
  chatbotInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') handleChat();
  });

  // ============================================================
  // INITIALIZE
  // ============================================================
  showSpread(current);
})();
</script>
