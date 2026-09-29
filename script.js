const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const themeToggle = document.querySelector(".theme-toggle");
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");

const setTheme = (isDark) => {
  document.documentElement.classList.toggle("dark-mode", isDark);
  themeToggle?.setAttribute("aria-pressed", String(isDark));
  themeToggle?.setAttribute("aria-label", isDark ? "Aktifkan light mode" : "Aktifkan dark mode");
  const label = themeToggle?.querySelector(".theme-label");
  if (label) label.textContent = isDark ? "Light mode" : "Dark mode";
};

const savedTheme = localStorage.getItem("theme");
setTheme(savedTheme ? savedTheme === "dark" : prefersDark.matches);

themeToggle?.addEventListener("click", () => {
  const isDark = !document.documentElement.classList.contains("dark-mode");
  setTheme(isDark);
  localStorage.setItem("theme", isDark ? "dark" : "light");
});

menuToggle?.addEventListener("click", () => {
  const isOpen = navLinks.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
});

navLinks?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("open");
    menuToggle?.setAttribute("aria-expanded", "false");
  });
});
