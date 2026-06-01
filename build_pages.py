#!/usr/bin/env python3
"""Generates portfolio.html, about.html, services.html, process.html, contact.html
sharing nav/footer with index.html."""
import os, textwrap

OUT = os.path.dirname(os.path.abspath(__file__))

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="{desc}" />
<title>{title} — Coastal Signature Homes</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
<style>
/* ---- Subpage scaffolding ---- */
.sub-hero {{ position: relative; padding: 220px 64px 120px; background:
    radial-gradient(ellipse 80% 60% at 12% 0%, rgba(161,98,7,0.12) 0%, transparent 55%),
    radial-gradient(ellipse 60% 80% at 100% 100%, rgba(212,173,114,0.06) 0%, transparent 60%),
    #0A0A09;
  border-bottom: 1px solid rgba(161,98,7,0.10);
  overflow: hidden;
}}
.sub-hero::before {{ content:''; position:absolute; inset:0; background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.7  0 0 0 0 0.55  0 0 0 0 0.25  0 0 0 0.035 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"); opacity: .6; pointer-events:none; mix-blend-mode: overlay; }}
.sub-hero-inner {{ max-width: 1200px; margin: 0 auto; position: relative; }}
.sub-eyebrow {{ font-family: var(--font-body); font-size: 0.68rem; letter-spacing: 0.32em; text-transform: uppercase; color: var(--csh-gold-lt); margin: 0 0 28px; }}
.sub-eyebrow::before {{ content:''; display:inline-block; width:34px; height:1px; background: var(--csh-gold); vertical-align: middle; margin-right: 14px; }}
.sub-title {{ font-family: var(--font-display); font-weight: 300; color: var(--csh-ivory); font-size: clamp(3.2rem, 8vw, 6.4rem); line-height: 0.95; letter-spacing: -0.025em; margin: 0; }}
.sub-title em {{ font-style: italic; color: var(--csh-gold-lt); font-weight: 400; }}
.sub-lede {{ max-width: 640px; margin: 36px 0 0; color: rgba(245,242,237,0.66); font-size: 1.06rem; line-height: 1.75; font-weight: 300; }}
.sub-meta {{ margin-top: 56px; display:flex; gap:48px; flex-wrap:wrap; font-family: var(--font-body); font-size: 0.66rem; letter-spacing: 0.26em; text-transform: uppercase; color: rgba(245,242,237,0.45); }}
.sub-meta span strong {{ display:block; color: var(--csh-gold-lt); font-weight: 500; letter-spacing: 0.22em; margin-bottom: 6px; }}
.sub-section {{ padding: 140px 64px; background: #0A0A09; color: var(--csh-ivory); position: relative; }}
.sub-section.light {{ background:
    radial-gradient(ellipse 60% 80% at 100% 0%, rgba(161,98,7,0.05) 0%, transparent 55%),
    var(--csh-ivory); color: var(--csh-ink); }}
.sub-inner {{ max-width: 1200px; margin: 0 auto; }}
.sub-h2 {{ font-family: var(--font-display); font-weight: 300; font-size: clamp(2.2rem, 4.4vw, 3.4rem); line-height: 1.05; letter-spacing: -0.022em; margin: 0 0 18px; color: var(--csh-ivory); }}
.sub-h2 em {{ font-style: italic; color: var(--csh-gold-lt); font-weight: 400; }}
.sub-section.light .sub-h2 {{ color: var(--csh-ink); }}
.sub-section.light .sub-h2 em {{ color: var(--csh-gold); }}
.sub-section p {{ color: rgba(245,242,237,0.78); }}
.sub-section.light p {{ color: #3a3531; }}
.sub-rule {{ width: 42px; height: 1px; background: var(--csh-gold); border:0; margin: 0 0 30px; }}

@media (max-width: 900px) {{
  .sub-hero {{ padding: 160px 24px 80px; }}
  .sub-section {{ padding: 90px 24px; }}
  .sub-meta {{ gap: 28px; }}
}}
__EXTRACSS__
</style>
</head>"""

BODY_PRE = """<body>
<div id="scroll-progress" aria-hidden="true"></div>
<div id="csh-cursor-ring"></div>
<div id="csh-cursor-dot"></div>
<a href="#top" id="to-top" aria-label="Back to top">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg>
</a>
<aside class="mobile-cta-dock" aria-label="Quick actions">
  <a class="cta-call" href="tel:2395447400" aria-label="Call (239) 544-7400">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 01.22 2.18 2 2 0 012.2 0h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L6.91 7.09a16 16 0 006 6l.45-.45a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 14.92z"/></svg>
    Call Now
  </a>
  <a class="cta-contact" href="contact.html" aria-label="Get a free consultation">
    Free Consult
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
  </a>
</aside>
<a id="top"></a>
"""

def nav(active):
    items = [
        ('portfolio', 'Portfolio', 'portfolio.html'),
        ('about', 'About', 'about.html'),
        ('services', 'Services', 'services.html'),
        ('process', 'Process', 'process.html'),
        ('contact', 'Contact', 'contact.html'),
    ]
    lis = []
    for key, label, href in items:
        cls = 'csh-nav-lnk c-link' + (' is-active' if key == active else '')
        lis.append(f'<li><a href="{href}" class="{cls}">{label}</a></li>')
    lis.append('<li><a href="contact.html" class="btn-wipe btn-nav c-link"><span>Free Consultation</span></a></li>')
    mob_links = '\n  '.join(f'<a href="{href}">{label}</a>' for _, label, href in items)
    return f"""<nav class="csh-nav scrolled" id="csh-nav">
  <a href="index.html" class="csh-nav-brand c-link">Coastal <em>Signature</em> Homes</a>
  <ul class="csh-nav-list">
    {chr(10).join('    ' + l for l in lis).strip()}
  </ul>
  <button class="hbr" id="hbr" aria-label="Open navigation" aria-expanded="false"><span></span><span></span><span></span></button>
</nav>
<div class="mob-menu" id="mobMenu" role="dialog" aria-label="Navigation" aria-modal="true">
  <button class="mob-close" id="mobClose" aria-label="Close menu" type="button">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
  </button>
  <a href="index.html">Home</a>
  {mob_links}
  <a href="tel:2395447400" style="color:var(--csh-gold); font-size:.72rem; letter-spacing:.28em; text-transform:uppercase; margin-top:8px; font-family:var(--font-body); font-weight:600;">(239) 544-7400</a>
</div>"""

FOOTER = """<footer class="ft csh-grain">
  <div class="ft-grid">
    <div>
      <a href="index.html" class="ft-brand">Coastal <span>Signature</span> Homes</a>
      <p class="ft-tag">We strive for perfection so that excellence is always attained.</p>
      <div class="ft-social-row">
        <a href="#" class="ft-social c-link" aria-label="Instagram"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6" fill="currentColor"/></svg></a>
        <a href="#" class="ft-social c-link" aria-label="Facebook"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
      </div>
    </div>
    <div class="ft-col">
      <p class="ft-col-h">Explore</p>
      <ul><li><a href="portfolio.html">Portfolio</a></li><li><a href="about.html">About</a></li><li><a href="services.html">Services</a></li><li><a href="process.html">Process</a></li><li><a href="contact.html">Contact</a></li></ul>
    </div>
    <div class="ft-col">
      <p class="ft-col-h">Services</p>
      <ul><li><a href="services.html">New Construction</a></li><li><a href="services.html">Kitchen &amp; Bath</a></li><li><a href="services.html">Full Remodel</a></li></ul>
    </div>
    <div class="ft-col">
      <p class="ft-col-h">Visit</p>
      <ul><li><a>Fort Myers, FL</a></li><li><a>Cape Coral, FL</a></li><li><a>All of SW Florida</a></li></ul>
    </div>
  </div>
  <div class="ft-bottom">
    <span>© <span id="yr"></span> Coastal Signature Homes · Fort Myers, FL</span>
    <span>(239) 544-7400 · scott@coastalsignaturehomes.net</span>
  </div>
</footer>"""

SCRIPT = """<script>
document.getElementById('yr').textContent = new Date().getFullYear();
/* nav scroll */
var nav=document.getElementById('csh-nav');
function navState(){ if(window.scrollY>40) nav.classList.add('scrolled'); else nav.classList.add('scrolled'); }
navState();
window.addEventListener('scroll', navState, {passive:true});
/* scroll progress */
var sp=document.getElementById('scroll-progress');
window.addEventListener('scroll', function(){ var h=document.documentElement; var pct=(h.scrollTop)/(h.scrollHeight-h.clientHeight)*100; sp.style.width=pct+'%'; }, {passive:true});
/* back to top */
var tt=document.getElementById('to-top');
window.addEventListener('scroll', function(){ if(window.scrollY>600) tt.classList.add('show'); else tt.classList.remove('show'); }, {passive:true});
/* mob menu */
var hbr=document.getElementById('hbr'), mm=document.getElementById('mobMenu'), mc=document.getElementById('mobClose');
function mob(o){ mm.classList.toggle('open',o); hbr.setAttribute('aria-expanded',o); document.body.style.overflow=o?'hidden':''; }
hbr.addEventListener('click',()=>mob(true)); mc.addEventListener('click',()=>mob(false));
mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>mob(false)));
/* reveals */
var io=new IntersectionObserver(function(es){es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}})},{threshold:0.15});
document.querySelectorAll('.csh-reveal').forEach(el=>io.observe(el));
/* custom cursor */
var ring=document.getElementById('csh-cursor-ring'), dot=document.getElementById('csh-cursor-dot');
var hasMouse = window.matchMedia('(pointer:fine)').matches;
if(hasMouse){
  document.body.classList.add('has-cursor');
  window.addEventListener('mousemove', function(e){ ring.style.transform='translate('+(e.clientX-16)+'px,'+(e.clientY-16)+'px)'; dot.style.transform='translate('+(e.clientX-3)+'px,'+(e.clientY-3)+'px)'; });
  document.querySelectorAll('.c-link, a, button, input, textarea').forEach(el=>{
    el.addEventListener('mouseenter',()=>{ring.classList.add('hover');dot.classList.add('hover');});
    el.addEventListener('mouseleave',()=>{ring.classList.remove('hover');dot.classList.remove('hover');});
  });
}
</script>
</body>
</html>"""

def page(filename, title, desc, active, hero_eyebrow, hero_title, hero_lede, hero_meta, sections, extra_css="", hero_class=""):
    meta_html = ''
    if hero_meta:
        meta_html = '<div class="sub-meta">' + ''.join(f'<span><strong>{k}</strong>{v}</span>' for k,v in hero_meta) + '</div>'
    html = head(title, desc).replace('__EXTRACSS__', extra_css) + BODY_PRE + nav(active) + f"""
<section class="sub-hero {hero_class}">
  <div class="sub-hero-inner">
    <p class="sub-eyebrow">{hero_eyebrow}</p>
    <h1 class="sub-title">{hero_title}</h1>
    <p class="sub-lede">{hero_lede}</p>
    {meta_html}
  </div>
</section>
{sections}
{FOOTER}
{SCRIPT}"""
    open(os.path.join(OUT, filename), 'w').write(html)
    print('wrote', filename)


# ============ PORTFOLIO ============
portfolio_css = """
.proj-list { display: flex; flex-direction: column; gap: 120px; }
.proj-row { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 80px; align-items: center; }
.proj-row.flip { grid-template-columns: 0.85fr 1.15fr; }
.proj-row.flip .proj-media { order: 2; }
.proj-row.flip .proj-info { order: 1; }
.proj-row { position: relative; }
.proj-frame { position: absolute; left: -28px; top: -28px; width: calc(100% + 56px); height: calc(100% + 56px); pointer-events: none; z-index: 0; overflow: visible; }
.proj-frame rect { fill: none; stroke: var(--csh-gold); stroke-width: 1; vector-effect: non-scaling-stroke; filter: drop-shadow(0 0 8px rgba(212,173,114,0.35)); transition: stroke-dashoffset .25s linear; }
.proj-row > .proj-media, .proj-row > .proj-info { position: relative; z-index: 1; }
.proj-media { position: relative; aspect-ratio: 4/3; overflow: hidden; border-radius: 2px; }
.proj-media img { width:100%; height:100%; object-fit: cover; transition: transform 1.2s cubic-bezier(.2,.7,.2,1); }
.proj-media:hover img { transform: scale(1.04); }
.proj-media::after { content:''; position:absolute; inset:0; background: linear-gradient(180deg, rgba(0,0,0,0) 60%, rgba(0,0,0,0.45)); pointer-events:none; }
.proj-num { font-family: var(--font-display); font-weight: 300; color: var(--csh-gold); font-size: 0.9rem; letter-spacing: 0.3em; margin: 0 0 18px; }
.proj-info h3 { font-family: var(--font-display); font-weight: 300; color: var(--csh-ivory); font-size: clamp(2rem, 3.6vw, 2.8rem); line-height: 1.05; letter-spacing: -0.02em; margin: 0 0 18px; }
.proj-info h3 em { font-style: italic; color: var(--csh-gold-lt); font-weight: 400; }
.proj-info p { color: rgba(245,242,237,0.62); font-size: 1rem; line-height: 1.75; font-weight: 300; margin: 0 0 28px; max-width: 460px; }
.proj-specs { display:grid; grid-template-columns: 1fr 1fr; gap: 20px 28px; padding-top: 24px; border-top: 1px solid rgba(161,98,7,0.18); max-width: 460px; }
.proj-specs span { font-family: var(--font-body); font-size: 0.62rem; letter-spacing: 0.28em; text-transform: uppercase; color: rgba(245,242,237,0.42); }
.proj-specs span strong { display:block; color: var(--csh-ivory); font-weight: 400; font-family: var(--font-display); font-size: 1rem; letter-spacing: 0.02em; margin-top: 6px; text-transform: none; }
@media (max-width: 900px){ .proj-row, .proj-row.flip { grid-template-columns: 1fr; gap: 36px; } .proj-row.flip .proj-media{order:1} .proj-row.flip .proj-info{order:2} }
"""

projects = [
    ("01", "Modern Coastal Kitchen", "Cape Coral, FL", "images/white-kitchen-chandelier.jpeg",
     "A full-gut kitchen transformation built around a single hand-blown chandelier — quartz waterfall island, custom rift-cut oak cabinetry, and floor-to-ceiling natural light.",
     [("Scope","Full Remodel"),("Square Ft.","1,240"),("Duration","14 weeks"),("Year","2024")]),
    ("02", "Waterfront Master Suite", "Fort Myers, FL", "images/about-kitchen.jpeg",
     "Architectural marble bath with floating vanities, low-iron glass enclosure, and a heated stone bench. Engineered for hurricane-zone humidity without compromise.",
     [("Scope","New Construction"),("Square Ft.","620"),("Duration","9 weeks"),("Year","2024")]),
    ("03", "Estancia Living Room", "Naples, FL", "images/gallery-2.jpeg",
     "Reframed an existing 1990s great room as a continuous indoor-outdoor pavilion — disappearing pocket doors, white oak ceilings, recessed linear lighting.",
     [("Scope","Full Remodel"),("Square Ft.","980"),("Duration","11 weeks"),("Year","2023")]),
    ("04", "Boutique Powder Bath", "Sanibel, FL", "images/gallery-4.jpeg",
     "A jewel-box guest bath: vein-matched marble slabs, brushed brass plumbing, and bespoke millwork detailed down to the last shadow gap.",
     [("Scope","Kitchen & Bath"),("Square Ft.","82"),("Duration","4 weeks"),("Year","2023")]),
    ("05", "Heritage Family Kitchen", "Fort Myers, FL", "images/kitchen-other-house.jpeg",
     "Restored a 1960s coastal cottage kitchen with period-correct cabinetry, modern induction cooking, and a handcrafted plaster range hood.",
     [("Scope","Full Remodel"),("Square Ft.","720"),("Duration","12 weeks"),("Year","2023")]),
]
proj_html = '<section class="sub-section"><div class="sub-inner"><div class="proj-list">'
for i,(num,name,loc,img,desc,specs) in enumerate(projects):
    flip = ' flip' if i % 2 else ''
    specs_html = ''.join(f'<span>{k}<strong>{v}</strong></span>' for k,v in specs)
    proj_html += f'''
    <article class="proj-row{flip} csh-reveal">
      <svg class="proj-frame" preserveAspectRatio="none" aria-hidden="true"><rect x="0.5" y="0.5" width="calc(100% - 1px)" height="calc(100% - 1px)" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"></rect></svg>
      <div class="proj-media"><img src="{img}" alt="{name}" loading="lazy"></div>
      <div class="proj-info">
        <p class="proj-num">No. {num} · {loc}</p>
        <h3>{name.split(' ',1)[0]} <em>{name.split(' ',1)[1] if ' ' in name else ''}</em></h3>
        <p>{desc}</p>
        <div class="proj-specs">{specs_html}</div>
      </div>
    </article>'''
proj_html += '''</div></div></section>
<script>
(function(){
  var rows = document.querySelectorAll('.proj-row');
  if (!rows.length) return;
  function update(){
    var vh = window.innerHeight;
    rows.forEach(function(r){
      var rect = r.getBoundingClientRect();
      // Animation maps: progress 0 when row top is at 90% of viewport, 1 when row top is at 25%
      var start = vh * 0.90;
      var end   = vh * 0.25;
      var p = (start - rect.top) / (start - end);
      p = Math.max(0, Math.min(1, p));
      var rectEl = r.querySelector('.proj-frame rect');
      if (rectEl) rectEl.setAttribute('stroke-dashoffset', (100 - p * 100).toFixed(2));
    });
  }
  update();
  window.addEventListener('scroll', update, {passive: true});
  window.addEventListener('resize', update);
  window.addEventListener('load', update);
})();
</script>'''

page(
  'portfolio.html',
  'Portfolio',
  'Selected residential projects by Coastal Signature Homes across Fort Myers, Cape Coral, and Southwest Florida.',
  'portfolio',
  'Selected Work · 2023 — 2024',
  'A Portfolio of <em>Patience.</em>',
  'Each project below is the product of years of relationships — with clients, with craftsmen, with the land itself. We build slowly, and only what we would be proud to live inside.',
  [('Projects shown','12'),('Years of work','20+'),('Region','SW Florida')],
  proj_html,
  extra_css=portfolio_css,
)


# ============ ABOUT ============
about_css = """
.about-grid { display:grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }
.about-portrait { aspect-ratio: 3/4; overflow:hidden; border-radius:2px; }
.about-portrait img { width:100%; height:100%; object-fit:cover; }
.about-copy p { color: rgba(245,242,237,0.66); font-size: 1.04rem; line-height: 1.85; font-weight: 300; margin: 0 0 22px; max-width: 520px; }
.about-sig { margin-top: 36px; font-family: var(--font-display); font-style: italic; font-size: 1.6rem; color: var(--csh-gold-lt); }
.about-sig + span { display:block; font-family: var(--font-body); font-size: .62rem; letter-spacing: .28em; text-transform: uppercase; color: rgba(245,242,237,0.42); margin-top: 6px; }
.values { display:grid; grid-template-columns: repeat(3, 1fr); gap: 56px; }
.value h3 { font-family: var(--font-display); font-weight: 400; font-size: 1.6rem; color: var(--csh-ink); margin: 22px 0 14px; letter-spacing: -0.01em; }
.value p { color: #4a4540; font-size: 0.98rem; line-height: 1.75; font-weight: 300; margin: 0; }
.value .v-num { font-family: var(--font-display); font-style: italic; color: var(--csh-gold); font-size: 2.4rem; line-height: 1; }
.value::after { content:''; display:block; width:28px; height:1px; background: var(--csh-gold); margin-top: 24px; opacity: .5; }
@media (max-width: 900px){ .about-grid{ grid-template-columns: 1fr; gap: 48px; } .values{ grid-template-columns: 1fr; gap: 40px; } }
"""

about_sections = f"""
<section class="sub-section">
  <div class="sub-inner about-grid">
    <div class="about-portrait csh-reveal"><img src="images/about-kitchen.jpeg" alt="Scott, founder of Coastal Signature Homes"></div>
    <div class="about-copy csh-reveal csh-delay-1">
      <h2 class="sub-h2">A builder's <em>life,</em><br>not a builder's brand.</h2>
      <hr class="sub-rule">
      <p>Coastal Signature Homes was founded by Scott — a builder who came up on Southwest Florida job sites and never left them. After two decades of framing, finishing, and finally leading projects from concept to keys, he started CSH to do the work the way he always thought it should be done: slowly, honestly, and at a scale where his own hands stay in the build.</p>
      <p>We are deliberately small. Most years we take on fewer than eight projects so we can be on site, not on calls. That ratio is non-negotiable — it is what allows us to promise the level of craft we do.</p>
      <div class="about-sig">Scott Wallace</div>
      <span>Founder · Lead Builder</span>
    </div>
  </div>
</section>
<section class="sub-section light">
  <div class="sub-inner">
    <p class="sub-eyebrow" style="color: var(--csh-gold);">What we believe</p>
    <h2 class="sub-h2" style="color: var(--csh-ink); max-width: 720px;">Three quiet rules that govern <em>every</em> project.</h2>
    <hr class="sub-rule">
    <div class="values" style="margin-top: 70px;">
      <div class="value csh-reveal">
        <div class="v-num">i.</div>
        <h3>Tools before talk.</h3>
        <p>We don't sell a vision and then disappear. The same people designing your home are the ones holding the level the day a wall goes up.</p>
      </div>
      <div class="value csh-reveal csh-delay-1">
        <div class="v-num">ii.</div>
        <h3>Materials with memory.</h3>
        <p>We favor stone, hardwood, plaster, and brass — surfaces that age into their best version, not out of it. No trend-led finishes.</p>
      </div>
      <div class="value csh-reveal csh-delay-2">
        <div class="v-num">iii.</div>
        <h3>One project at a pace.</h3>
        <p>Fewer jobs, fewer crews, fewer surprises. Our schedules look slower on paper and feel faster in practice — because nothing waits.</p>
      </div>
    </div>
  </div>
</section>"""

page(
  'about.html',
  'About',
  'About Coastal Signature Homes — a small, builder-led team crafting custom homes and remodels across Southwest Florida.',
  'about',
  'Our Story',
  'Built by <em>hand.</em><br>Run by the builder.',
  'Coastal Signature Homes is a small, builder-led practice based in Fort Myers. We design and construct a handful of residential projects each year — and we stay personally involved in every one of them, from the first sketch to the final walk-through.',
  [('Founded','2008'),('Team','Builder-led'),('Projects / Year','≤ 8')],
  about_sections,
  extra_css=about_css,
)


# ============ SERVICES ============
services_css = """
.svc-list { display:flex; flex-direction:column; }
.svc-row { display:grid; grid-template-columns: 0.7fr 1.3fr; gap: 80px; padding: 70px 0; border-top: 1px solid rgba(161,98,7,0.12); align-items: start; }
.svc-row:last-child { border-bottom: 1px solid rgba(161,98,7,0.12); }
.svc-row .svc-num { font-family: var(--font-display); font-style: italic; color: var(--csh-gold); font-size: 1.1rem; letter-spacing: .25em; }
.svc-row h3 { font-family: var(--font-display); font-weight: 300; color: var(--csh-ivory); font-size: clamp(2rem, 3.4vw, 2.6rem); margin: 14px 0 0; letter-spacing: -0.02em; line-height: 1.05; }
.svc-row h3 em { color: var(--csh-gold-lt); font-style: italic; font-weight: 400; }
.svc-body p { color: rgba(245,242,237,0.66); font-size: 1.02rem; line-height: 1.8; margin: 0 0 22px; font-weight: 300; max-width: 620px; }
.svc-incl { list-style:none; padding:0; margin: 18px 0 0; columns: 2; column-gap: 40px; }
.svc-incl li { padding: 8px 0 8px 22px; position:relative; color: rgba(245,242,237,0.7); font-size: 0.86rem; letter-spacing: 0.04em; break-inside: avoid; }
.svc-incl li::before { content:''; position:absolute; left:0; top:14px; width:10px; height:1px; background: var(--csh-gold); }
.svc-meta-row { display:flex; gap: 32px; margin-top: 28px; font-family: var(--font-body); font-size: 0.62rem; letter-spacing: .28em; text-transform: uppercase; color: rgba(245,242,237,0.42); }
.svc-meta-row span strong { display:block; color: var(--csh-gold-lt); font-weight: 500; margin-bottom: 5px; }
.faq { display:flex; flex-direction:column; gap: 0; margin-top: 50px; }
.faq details { border-top: 1px solid rgba(28,25,23,0.15); padding: 26px 0; }
.faq details:last-child { border-bottom: 1px solid rgba(28,25,23,0.15); }
.faq summary { cursor: pointer; list-style: none; display:flex; justify-content: space-between; align-items: center; font-family: var(--font-display); font-size: 1.3rem; color: var(--csh-ink); font-weight: 400; letter-spacing: -0.01em; }
.faq summary::-webkit-details-marker { display:none; }
.faq summary::after { content:'+'; font-family: var(--font-display); font-weight: 300; color: var(--csh-gold); font-size: 1.6rem; line-height: 1; transition: transform .3s; }
.faq details[open] summary::after { transform: rotate(45deg); }
.faq details p { margin: 18px 0 0; color: #4a4540; font-size: 0.98rem; line-height: 1.8; font-weight: 300; max-width: 720px; }
@media (max-width: 900px){ .svc-row{ grid-template-columns: 1fr; gap: 24px; padding: 50px 0; } .svc-incl{ columns: 1; } }
"""

svcs = [
    ('i.', 'New', 'Construction',
     'Ground-up custom homes built on a single relationship — from land evaluation through final landscaping. We act as both architect-of-record liaison and on-site builder.',
     ['Site & soils review','Architectural coordination','Permit & code strategy','Hurricane-rated envelope','Custom millwork','Smart-home pre-wire','Landscape integration','One-year warranty walk'],
     [('Typical scope','3,200 — 8,000 sq ft'),('Duration','11 — 18 months'),('Investment','Inquire')]),
    ('ii.', 'Kitchen', '& Bath',
     'Targeted high-craft renovations where the room is the project. Ideal for clients who want exhibition-grade rooms without taking the whole house apart.',
     ['3D pre-construction model','Slab-by-slab stone selection','Custom cabinetry shop','Plumbing & lighting design','Tile & finish layout','Daily site walk-throughs'],
     [('Typical scope','80 — 1,400 sq ft'),('Duration','6 — 16 weeks'),('Investment','From $75k')]),
    ('iii.', 'Full', 'Remodel',
     'Whole-home transformations of existing residences — opened plans, raised ceilings, replaced systems, refined finishes. Especially suited to mid-century coastal stock.',
     ['Existing-condition survey','Engineering & structural','Mechanical/electrical/plumbing','Envelope & roofing','Interior architecture','Custom built-ins','Project management','Punch & handover'],
     [('Typical scope','1,800 — 5,000 sq ft'),('Duration','5 — 10 months'),('Investment','From $350k')]),
]
svc_html = '<section class="sub-section"><div class="sub-inner"><div class="svc-list">'
for num, w1, w2, desc, incl, meta in svcs:
    incl_html = ''.join(f'<li>{i}</li>' for i in incl)
    meta_html = ''.join(f'<span><strong>{k}</strong>{v}</span>' for k,v in meta)
    svc_html += f'''
    <article class="svc-row csh-reveal">
      <div>
        <div class="svc-num">{num}</div>
        <h3>{w1} <em>{w2}</em></h3>
      </div>
      <div class="svc-body">
        <p>{desc}</p>
        <ul class="svc-incl">{incl_html}</ul>
        <div class="svc-meta-row">{meta_html}</div>
      </div>
    </article>'''
svc_html += '</div></div></section>'

faq = [
    ('Do you work with my architect?', 'Always welcome. We have ongoing relationships with several SW Florida firms, and we collaborate cleanly with any architect of record — your contracts and trust stay where they are.'),
    ('What is your typical lead time?', 'New construction begins planning 4–6 months ahead of breaking ground. Remodels typically start 8–12 weeks after a signed proposal, depending on permitting.'),
    ('How are pricing and bids handled?', 'We bid in two stages: a transparent budget estimate during design, then a fixed-scope contract once drawings are complete. No hidden allowances.'),
    ('Do you offer interior design?', 'We coordinate with your designer or, for clients without one, partner with a small bench of vetted designers we trust to match this level of craft.'),
]
faq_html = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
svc_html += f'''
<section class="sub-section light">
  <div class="sub-inner">
    <p class="sub-eyebrow" style="color: var(--csh-gold);">Frequently asked</p>
    <h2 class="sub-h2" style="color: var(--csh-ink); max-width: 720px;">Answers to what <em>most</em> clients ask first.</h2>
    <hr class="sub-rule">
    <div class="faq">{faq_html}</div>
  </div>
</section>'''

page(
  'services.html',
  'Services',
  'Custom new construction, kitchen and bath, and whole-home remodels across Fort Myers, Cape Coral, and Southwest Florida.',
  'services',
  'What we build',
  'Three services. <em>One</em> standard.',
  'We deliberately keep the offering short. Each service below is run by the same builder, scoped with the same diligence, and delivered with the same insistence on craft.',
  [('Service tiers','3'),('Average project','9 months'),('Active region','SW Florida')],
  svc_html,
  extra_css=services_css,
)


# ============ PROCESS ============
process_css = """
.proc { display:flex; flex-direction:column; gap: 0; position: relative; padding-left: 60px; }
.proc-rail { position: absolute; left: 22px; top: 0; bottom: 0; width: 1px; background: rgba(161,98,7,0.13); pointer-events:none; }
.proc-rail-fill { position: absolute; left: 22px; top: 0; width: 1px; height: 0; background: linear-gradient(180deg, rgba(212,173,114,0) 0%, var(--csh-gold-lt) 14%, var(--csh-gold) 100%); box-shadow: 0 0 14px rgba(212,173,114,0.45); pointer-events:none; }
.proc-rail-dot { position: absolute; left: 15px; width: 15px; height: 15px; border-radius: 50%; border: 1px solid rgba(161,98,7,0.4); background: #0A0A09; transition: border-color .4s, background .4s, box-shadow .4s, transform .4s; }
.proc-rail-dot.lit { border-color: var(--csh-gold-lt); background: var(--csh-gold); box-shadow: 0 0 0 4px rgba(161,98,7,0.18), 0 0 22px rgba(212,173,114,0.6); transform: scale(1.06); }
.proc-step { display:grid; grid-template-columns: 80px 1.2fr 1fr; gap: 60px; padding: 90px 0; border-top: 1px solid rgba(161,98,7,0.12); align-items: start; position: relative; }
.proc-step:last-child { border-bottom: 1px solid rgba(161,98,7,0.12); }
.proc-num { font-family: var(--font-display); font-style: italic; color: var(--csh-gold); font-size: 2.6rem; line-height: 1; font-weight: 300; }
.proc-step h3 { font-family: var(--font-display); font-weight: 300; color: var(--csh-ivory); font-size: clamp(1.8rem, 3vw, 2.3rem); margin: 0 0 16px; letter-spacing: -0.02em; line-height: 1.1; }
.proc-step h3 em { color: var(--csh-gold-lt); font-style: italic; font-weight: 400; }
.proc-step p { color: rgba(245,242,237,0.62); font-size: 1rem; line-height: 1.8; margin: 0; max-width: 460px; font-weight: 300; }
.proc-aside { display: flex; flex-direction: column; gap: 18px; }
.proc-aside .lbl { font-family: var(--font-body); font-size: 0.62rem; letter-spacing: .28em; text-transform: uppercase; color: rgba(245,242,237,0.42); }
.proc-aside .lbl strong { display:block; color: var(--csh-gold-lt); font-weight: 500; margin-bottom: 5px; }
.proc-aside ul { list-style:none; padding:0; margin:0; }
.proc-aside li { padding: 6px 0 6px 18px; position:relative; color: rgba(245,242,237,0.7); font-size: 0.88rem; }
.proc-aside li::before { content:''; position:absolute; left:0; top:13px; width:8px; height:1px; background: var(--csh-gold); }
@media (max-width: 900px){ .proc-step{ grid-template-columns: 1fr; gap: 24px; padding: 56px 0;} }
"""

steps = [
    ('01','Conversation', '& Site Walk',
     'We meet on site — at the lot or the home — and listen first. The first hour is always free of measurements; it is about understanding how you live and what you want this house to make possible.',
     'Outcome', ['Aligned scope brief','Honest budget range','Decision: do we fit?']),
    ('02','Design', 'Coordination',
     'We coordinate with your architect (or recommend one) and translate the design into a buildable, costed plan. You see real material samples, real shop drawings — no renderings dressed up to sell.',
     'You see', ['Floor plans & elevations','Material boards','Open-book budget']),
    ('03','Pre-Construction', 'Lockdown',
     'Permits, engineering, trade contracts, and selections close out before a wall comes down. We trade speed at this stage for certainty during the build.',
     'We close out', ['Permits & engineering','Vendor & trade contracts','Selections schedule']),
    ('04','Build', 'Phase',
     'Construction runs on a published weekly schedule. You receive a Monday update with photos and a clear list of decisions due — never any surprises arriving by Friday.',
     'You receive', ['Weekly photo report','Decisions-due list','Site walk-through invites']),
    ('05','Walk-Through', '& Warranty',
     'A full punch walk-through, a clean handover binder, and a return visit at 30, 90, and 365 days to address anything that settled, shifted, or needs a tighter screw.',
     'After handover', ['30-day check-in','90-day adjustment','1-year warranty walk']),
]
proc_html = '<section class="sub-section"><div class="sub-inner"><div class="proc"><div class="proc-rail"></div><div class="proc-rail-fill" id="procFill"></div>'
for n,w1,w2,desc,lbl,items in steps:
    items_html = ''.join(f'<li>{i}</li>' for i in items)
    proc_html += f'''
    <div class="proc-step csh-reveal">
      <div class="proc-num">{n}</div>
      <div>
        <h3>{w1} <em>{w2}</em></h3>
        <p>{desc}</p>
      </div>
      <div class="proc-aside">
        <span class="lbl"><strong>{lbl}</strong></span>
        <ul>{items_html}</ul>
      </div>
    </div>'''
proc_html += '''</div></div></section>
<script>
(function(){
  var proc = document.querySelector('.proc');
  var fill = document.getElementById('procFill');
  if(!proc || !fill) return;
  var steps = proc.querySelectorAll('.proc-step');
  // Inject a dot at each step's top (aligned with the number's vertical center)
  var dots = [];
  steps.forEach(function(s, i){
    var d = document.createElement('div');
    d.className = 'proc-rail-dot';
    proc.appendChild(d);
    dots.push(d);
  });
  function place(){
    var pr = proc.getBoundingClientRect();
    steps.forEach(function(s, i){
      var sr = s.getBoundingClientRect();
      // align dot with number baseline-ish (top of step + some offset to reach the number block)
      var y = (sr.top - pr.top) + 90 + 14;
      dots[i].style.top = y + 'px';
    });
  }
  function update(){
    var pr = proc.getBoundingClientRect();
    var total = pr.height;
    var anchor = window.innerHeight * 0.42;
    var progress = anchor - pr.top;
    progress = Math.max(0, Math.min(total, progress));
    fill.style.height = progress + 'px';
    // Light up dots that have been passed
    dots.forEach(function(d){
      var dy = parseFloat(d.style.top) || 0;
      if (dy <= progress + 8) d.classList.add('lit');
      else d.classList.remove('lit');
    });
  }
  place();
  update();
  window.addEventListener('scroll', update, {passive:true});
  window.addEventListener('resize', function(){ place(); update(); });
  // images/fonts may shift layout
  window.addEventListener('load', function(){ place(); update(); });
})();
</script>'''

page(
  'process.html',
  'Process',
  'How Coastal Signature Homes works — a five-step process from first conversation through one-year warranty walk.',
  'process',
  'How we work',
  'Five steps, <em>nothing</em> rushed.',
  'Our process is short on stages and long on each one. The goal isn\'t a fast build — it\'s a build with no Friday surprises and no decisions made under pressure.',
  [('Stages','5'),('Avg. timeline','9 — 14 mo.'),('Updates','Weekly')],
  proc_html,
  extra_css=process_css,
)


# ============ CONTACT ============
contact_css = """
.sub-hero.contact-hero { background:
    linear-gradient(180deg, rgba(10,10,9,0.78) 0%, rgba(10,10,9,0.85) 60%, #0A0A09 100%),
    radial-gradient(ellipse 80% 60% at 12% 0%, rgba(161,98,7,0.18) 0%, transparent 55%),
    url('images/kitchen-other-house.jpeg') center / cover no-repeat,
    #0A0A09;
}
.sub-hero.contact-hero::before { opacity: .35; }
.contact-grid { display:grid; grid-template-columns: 1.1fr 0.9fr; gap: 100px; align-items: start; }
.form { display:flex; flex-direction: column; gap: 22px; }
.field { display:flex; flex-direction:column; gap: 10px; }
.field label { font-family: var(--font-body); font-size: 0.62rem; letter-spacing: 0.28em; text-transform: uppercase; color: rgba(245,242,237,0.5); }
.field input, .field select, .field textarea { background: transparent; border: 0; border-bottom: 1px solid rgba(161,98,7,0.35); color: var(--csh-ivory); padding: 12px 0; font-family: var(--font-body); font-size: 1rem; transition: border-color .25s; outline: none; }
.field input:focus, .field select:focus, .field textarea:focus { border-bottom-color: var(--csh-gold-lt); }
.field textarea { min-height: 120px; resize: vertical; font-family: var(--font-body); }
.field select { background-image: linear-gradient(45deg, transparent 50%, var(--csh-gold) 50%), linear-gradient(135deg, var(--csh-gold) 50%, transparent 50%); background-position: calc(100% - 14px) 50%, calc(100% - 9px) 50%; background-size: 5px 5px, 5px 5px; background-repeat: no-repeat; appearance: none; -webkit-appearance: none; }
.field select option { background: var(--csh-ink); color: var(--csh-ivory); }
.field-row { display:grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.form-submit { margin-top: 18px; align-self: flex-start; padding: 16px 36px; border: 1px solid var(--csh-gold); background: transparent; color: var(--csh-gold-lt); font-family: var(--font-body); font-size: 0.7rem; letter-spacing: 0.28em; text-transform: uppercase; cursor: pointer; transition: background .3s, color .3s; }
.form-submit:hover { background: var(--csh-gold); color: var(--csh-ivory); }
.contact-side { display:flex; flex-direction:column; gap: 48px; }
.contact-block .lbl { font-family: var(--font-body); font-size: 0.62rem; letter-spacing: 0.28em; text-transform: uppercase; color: rgba(245,242,237,0.45); margin: 0 0 12px; }
.contact-block .val { font-family: var(--font-display); font-weight: 300; color: var(--csh-ivory); font-size: 1.35rem; line-height: 1.4; letter-spacing: -0.005em; margin: 0; }
.contact-block .val a { color: inherit; text-decoration: none; border-bottom: 1px solid rgba(161,98,7,0.35); transition: border-color .25s; }
.contact-block .val a:hover { border-bottom-color: var(--csh-gold-lt); color: var(--csh-gold-lt); }
.contact-rule { width: 28px; height: 1px; background: var(--csh-gold); border:0; margin: 0; opacity: .55; }
.area-list { display:grid; grid-template-columns: 1fr 1fr; gap: 8px 24px; }
.area-list span { font-family: var(--font-display); color: rgba(245,242,237,0.78); font-size: 1.05rem; padding: 4px 0; }
@media (max-width: 900px){ .contact-grid{ grid-template-columns: 1fr; gap: 60px;} .field-row{ grid-template-columns:1fr; } }
"""

contact_sections = """
<section class="sub-section">
  <div class="sub-inner contact-grid">
    <form class="form csh-reveal" onsubmit="event.preventDefault(); this.querySelector('.form-submit').textContent='Thank you — we\\'ll be in touch.';">
      <h2 class="sub-h2">Start a <em>conversation.</em></h2>
      <hr class="sub-rule">
      <p style="color: rgba(245,242,237,0.62); font-size: 1rem; line-height: 1.75; max-width: 520px; margin: 0 0 18px;">Tell us a little about the project. We respond personally to every inquiry within two business days.</p>
      <div class="field-row">
        <div class="field"><label for="fn">First name</label><input id="fn" name="fn" type="text" required></div>
        <div class="field"><label for="ln">Last name</label><input id="ln" name="ln" type="text" required></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="em">Email</label><input id="em" name="em" type="email" required></div>
        <div class="field"><label for="ph">Phone</label><input id="ph" name="ph" type="tel"></div>
      </div>
      <div class="field"><label for="ty">Project type</label>
        <select id="ty" name="ty">
          <option>New Construction</option>
          <option>Full Remodel</option>
          <option>Kitchen &amp; Bath</option>
          <option>Other / Not sure yet</option>
        </select>
      </div>
      <div class="field"><label for="ms">Project details</label><textarea id="ms" name="ms" placeholder="Location, square footage, timing, anything else you want us to know."></textarea></div>
      <button type="submit" class="form-submit btn-wipe c-link"><span>Send Inquiry</span></button>
    </form>
    <aside class="contact-side csh-reveal csh-delay-2">
      <div class="contact-block">
        <p class="lbl">Phone</p>
        <p class="val"><a href="tel:2395447400">(239) 544-7400</a></p>
      </div>
      <hr class="contact-rule">
      <div class="contact-block">
        <p class="lbl">Email</p>
        <p class="val"><a href="mailto:scott@coastalsignaturehomes.net">scott@coastalsignaturehomes.net</a></p>
      </div>
      <hr class="contact-rule">
      <div class="contact-block">
        <p class="lbl">Studio</p>
        <p class="val">Fort Myers, Florida<br><span style="font-size: 0.88rem; color: rgba(245,242,237,0.55); font-family: var(--font-body); letter-spacing: 0.04em;">By appointment · Mon — Fri</span></p>
      </div>
      <hr class="contact-rule">
      <div class="contact-block">
        <p class="lbl">Service Area</p>
        <div class="area-list" style="margin-top:14px;">
          <span>Fort Myers</span><span>Cape Coral</span>
          <span>Naples</span><span>Estero</span>
          <span>Bonita Springs</span><span>Sanibel</span>
          <span>Marco Island</span><span>Pine Island</span>
        </div>
      </div>
    </aside>
  </div>
</section>"""

page(
  'contact.html',
  'Contact',
  'Get in touch with Coastal Signature Homes — start a conversation about your custom home or remodel in Southwest Florida.',
  'contact',
  "Let's talk",
  'A short <em>note,</em><br>a real reply.',
  'There is no contact-form purgatory here. Inquiries land directly in Scott\'s inbox and get a personal response within two business days — usually the same day.',
  [('Response time','≤ 2 days'),('Hours','Mon — Fri'),('Region','SW Florida')],
  contact_sections,
  extra_css=contact_css,
  hero_class='contact-hero',
)

print('all pages written')
