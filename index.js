import { neonbar } from './neonheader.js';
import { neonmain } from './neonmain.js';
import { neonfooter } from './neonfooter.js';

const neonmonkeyheader = document.getElementById('neon-monkey-header');
neonmonkeyheader.appendChild(neonbar);

const neonmonkeymain = document.getElementById('neon-monkey-main');
neonmonkeymain.appendChild(neonmain);

const neonmonkeyfooter = document.getElementById('neon-monkey-footer');
neonmonkeyfooter.appendChild(neonfooter);
