/* MENU JSHT */
const menuToggle = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");
const closeBtn = document.getElementById("close-btn");
menuToggle.onclick = () => {
  sidebar.classList.add("open");
  document.body.classList.add("no-scroll"); // Matikan scroll
};
closeBtn.onclick = () => {
  sidebar.classList.remove("open");
  document.body.classList.remove("no-scroll");
};

/* SLIDER JSHT */
const slider   = document.querySelector('.repos-slider');
const nextBtn  = document.querySelector('.next-btn');
const prevBtn  = document.querySelector('.prev-btn');
const GAP = 15;
function cardWidth() {
  const card = document.querySelector('.repo-card');
  return card ? card.offsetWidth + GAP : 0;
}
function slide(dir = 1) {
  slider.scrollBy({ left: dir * cardWidth(), behavior: 'smooth' });
}
nextBtn.addEventListener('click', () => slide(1));
prevBtn.addEventListener('click', () => slide(-1));
window.addEventListener('resize', () => slider.scrollLeft = 0);

/* FOOTER */
document.getElementById("year").textContent = new Date().getFullYear();