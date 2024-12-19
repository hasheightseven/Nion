import neonmonkeymain from './index.js';

const ellomast = document.createElement('div');

ellomast.textContent = 'nion!!';

ellomast.style.color = '#abcdef';

ellomast.addEventListener('click', () => {
  ellomast.style.fontsize = ellomast.style.fontsize + 26;
});

neonmonkeymain.appendChild(ellomast);
