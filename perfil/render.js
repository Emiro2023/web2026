const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage();
  await p.goto('file://' + __dirname + '/logos.html');
  const names = ['1-eam-sound-co','2-meridian-audio','3-eamtone','4-monotone'];
  for (let i = 0; i < 4; i++) await p.locator('#c' + (i+1)).screenshot({ path: `${names[i]}.png` });
  // hoja comparativa con recorte circular (como se ve en Suno)
  await p.setContent(`<body style="margin:0;background:#111;display:grid;grid-template-columns:repeat(2,420px);gap:40px;padding:40px">${names.map((n,i)=>`<div style="text-align:center;color:#ddd;font:20px Liberation Sans"><img src="file://${__dirname}/${n}.png" style="width:400px;height:400px;border-radius:50%"><div style="margin-top:10px">${i+1}. ${n.slice(2).replace(/-/g,' ')}</div></div>`).join('')}</body>`);
  await p.screenshot({ path: 'comparativa.png', fullPage: true });
  await b.close();
})();
