export const neonmonkeyheader = document.getElementById('neon-monkey-header');
export const neonmonkeymain = document.getElementById('neon-monkey-main');
export const neonmonkeyfooter = document.getElementById('neon-monkey-footer');

const ellomast = document.createElement('div');

ellomast.textContent = 'nion!!';

ellomast.style.color = '#abcdef';

ellomast.addEventListener('click', () => {
  ellomast.style.fontsize = ellomast.style.fontsize + 26;
});

neonmonkeymain.appendChild(ellomast);
