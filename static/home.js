document.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const href = this.getAttribute('href');
    const overlay = document.getElementById('page-transition');
    overlay.classList.add('active');
    setTimeout(() => window.location.href = href, 500);
  });
});
const clickSound = new Audio('click.mp3');
document.querySelectorAll('button').forEach(btn => {
  btn.addEventListener('click', () => clickSound.play());
});
document.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const href = this.getAttribute('href');
    const overlay = document.getElementById('page-transition');
    overlay.classList.add('active');
    setTimeout(() => window.location.href = href, 500);
  });
});