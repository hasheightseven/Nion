import neonbar import './neonheader.js';
import neonmain import './neonmain.js';
import neonfooter import './neonfooter.js';

const neonmonkeyheader = document.getElementById('neon-monkey-header');
neonmonkeyheader.appendChild(neonbar);

const neonmonkeymain = document.getElementById('neon-monkey-main');
neonmonkeymain.appendChild(neonmain);

const neonmonkeyfooter = document.getElementById('neon-monkey-footer');
neonmonkeyfooter.appendChild(neonfooter);
