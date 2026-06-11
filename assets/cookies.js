(function () {
  var STORAGE_KEY = 'csh_cookie_consent';

  // Already decided — do nothing
  if (localStorage.getItem(STORAGE_KEY)) return;

  /* ── Styles ── */
  var style = document.createElement('style');
  style.textContent = [
    '#csh-cookie{',
      'position:fixed;bottom:0;left:0;right:0;z-index:99999;',
      'background:#1C1917;',
      'border-top:1px solid rgba(161,98,7,0.25);',
      'padding:24px 40px;',
      'display:flex;align-items:center;justify-content:space-between;gap:32px;flex-wrap:wrap;',
      'transform:translateY(100%);',
      'transition:transform .5s cubic-bezier(.4,0,.2,1);',
      'box-shadow:0 -8px 40px rgba(0,0,0,0.45);',
    '}',
    '#csh-cookie.csh-cookie-visible{transform:translateY(0);}',
    '#csh-cookie p{',
      'margin:0;font-family:"Montserrat",sans-serif;font-size:0.78rem;',
      'line-height:1.65;font-weight:300;color:rgba(245,242,237,0.66);',
      'max-width:680px;',
    '}',
    '#csh-cookie p a{color:rgba(212,173,114,0.85);text-decoration:underline;}',
    '#csh-cookie p strong{',
      'display:block;font-family:"Cormorant Garamond",serif;font-weight:400;',
      'font-size:1.05rem;color:#FAFAF9;letter-spacing:-0.01em;margin-bottom:6px;',
    '}',
    '.csh-cookie-btns{display:flex;gap:12px;flex-shrink:0;}',
    '.csh-cookie-btn{',
      'font-family:"Montserrat",sans-serif;font-size:0.6rem;letter-spacing:0.26em;',
      'text-transform:uppercase;padding:11px 26px;border:1px solid;cursor:pointer;',
      'transition:background .25s,color .25s,border-color .25s;white-space:nowrap;',
      'background:transparent;',
    '}',
    '.csh-cookie-btn-decline{',
      'border-color:rgba(161,98,7,0.35);color:rgba(245,242,237,0.45);',
    '}',
    '.csh-cookie-btn-decline:hover{',
      'border-color:rgba(161,98,7,0.7);color:rgba(245,242,237,0.75);',
    '}',
    '.csh-cookie-btn-accept{',
      'border-color:#A16207;color:#d4ad72;',
    '}',
    '.csh-cookie-btn-accept:hover{',
      'background:#A16207;color:#FAFAF9;',
    '}',
    '@media(max-width:640px){',
      '#csh-cookie{padding:20px 20px 28px;flex-direction:column;align-items:flex-start;}',
      '.csh-cookie-btns{width:100%;}',
      '.csh-cookie-btn{flex:1;text-align:center;}',
    '}',
  ].join('');
  document.head.appendChild(style);

  /* ── Banner HTML ── */
  var banner = document.createElement('div');
  banner.id = 'csh-cookie';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', 'Cookie consent');
  banner.innerHTML = [
    '<p>',
      '<strong>This site uses cookies.</strong>',
      'We use cookies to understand how visitors interact with our site and to improve your experience. ',
      'You can choose to accept or decline. Declining will not affect your ability to browse the site. ',
      '<a href="/privacy.html">Privacy Policy</a>',
    '</p>',
    '<div class="csh-cookie-btns">',
      '<button class="csh-cookie-btn csh-cookie-btn-decline" id="csh-cookie-decline">Decline</button>',
      '<button class="csh-cookie-btn csh-cookie-btn-accept" id="csh-cookie-accept">Accept Cookies</button>',
    '</div>',
  ].join('');
  document.body.appendChild(banner);

  // Slide in after a short delay
  setTimeout(function () {
    banner.classList.add('csh-cookie-visible');
  }, 800);

  function dismiss(choice) {
    localStorage.setItem(STORAGE_KEY, choice);
    banner.style.transition = 'transform .4s cubic-bezier(.4,0,.2,1)';
    banner.classList.remove('csh-cookie-visible');
    setTimeout(function () { banner.remove(); }, 450);
  }

  document.getElementById('csh-cookie-accept').addEventListener('click', function () {
    dismiss('accepted');
  });

  document.getElementById('csh-cookie-decline').addEventListener('click', function () {
    dismiss('declined');
  });
})();
