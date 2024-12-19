export const neonmain = document.createElement('div');


neonmain.textContent = 'nion!!';

neonmain.style.color = '#abcdef';

neonmain.addEventListener('click', () => {
  neonmain.style.fontsize = neonmain.style.fontsize + 26;
});
