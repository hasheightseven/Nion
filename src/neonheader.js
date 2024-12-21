export const neonbar = document.createElement('nav');

const logodiv = document.createElement('div');
logodiv.textContent = 'logo';
logodiv.style.width = '50%';
const nonlogodiv = document.createElement('div');
nonlogodiv.textContent = 'no logo';
nonlogodiv.style.width = '50%';

neonbar.appendChild(logodiv);
neonbar.appendChild(nonlogodiv);
