const members = [
  {
    name: "Nicolas Ezequiel Lozano",
    role: "Desarrollo Frontend",
    bio: "Me encarga de la interfaz, la accesibilidad y que todo se vea bien en cualquier dispositivo.",
    skills: ["HTML", "CSS", "JavaScript"],
  },
  {
    name: "Mauro Torres",
    role: "Desarrollo Backend",
    bio: "Diseño las APIs y la lógica de la aplicación, manteniendo el código ordenado y testeado.",
    skills: ["Node.js", "Bases de datos", "APIs REST"],
  },
  {
    name: "Felipe Aviani",
    role: "Diseño UI/UX",
    bio: "Cuido la experiencia del usuario: prototipos, paletas de color y flujos intuitivos.",
    skills: ["Figma", "Wireframes", "Tipografía"],
  },
  {
    name: "Claudio Olima",
    role: "Documentación y QA",
    bio: "Escribo la documentación, busco errores y aseguramos que cada proyecto funcione.",
    skills: ["Pruebas", "Git", "Documentación"],
  },
  {
    name: "Celeste Cabrera",
    role: "Coordinación del grupo",
    bio: "Organizo tareas, tiempos y revisiones para que el grupo avance sin bloqueos.",
    skills: ["Scrum", "Gestión", "Comunicación"],
  },
];

const initials = (name) => {
  const parts = name.trim().split(" ").filter(Boolean);
  if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
  const first = parts[0][0];
  const last = parts[parts.length - 1][0];
  return (first + last).toUpperCase();
};

let currentMember = 0;
let autoPlayTimer = null;

function renderFeatured(index) {
  const m = members[index];
  const box = document.querySelector(".featured-content");
  box.style.opacity = 0;
  setTimeout(() => {
    document.getElementById("featuredAvatar").textContent = initials(m.name);
    document.getElementById("featuredName").textContent = m.name;
    document.getElementById("featuredRole").textContent = m.role;
    document.getElementById("featuredBio").textContent = m.bio;
    const skills = document.getElementById("featuredSkills");
    skills.innerHTML = "";
    m.skills.forEach((s) => {
      const li = document.createElement("li");
      li.textContent = s;
      skills.appendChild(li);
    });
    box.style.opacity = 1;
  }, 180);

  document.querySelectorAll("#carouselDots button").forEach((dot, i) => {
    dot.classList.toggle("active", i === index);
  });
}

function nextMember() {
  currentMember = (currentMember + 1) % members.length;
  renderFeatured(currentMember);
  restartAutoPlay();
}

function prevMember() {
  currentMember = (currentMember - 1 + members.length) % members.length;
  renderFeatured(currentMember);
  restartAutoPlay();
}

function restartAutoPlay() {
  clearInterval(autoPlayTimer);
  autoPlayTimer = setInterval(nextMember, 6000);
}

function renderTeam() {
  const grid = document.getElementById("teamGrid");
  grid.innerHTML = "";
  members.forEach((m) => {
    const card = document.createElement("article");
    card.className = "member-card fade-in";
    card.innerHTML = `
      <div class="avatar small">${initials(m.name)}</div>
      <h3>${m.name}</h3>
      <p>${m.role}</p>
    `;
    card.addEventListener("click", () => {
      currentMember = members.indexOf(m);
      renderFeatured(currentMember);
      restartAutoPlay();
      document.querySelector(".featured").scrollIntoView({ behavior: "smooth" });
    });
    grid.appendChild(card);
  });
}

function renderDots() {
  const dots = document.getElementById("carouselDots");
  dots.innerHTML = "";
  members.forEach((_, i) => {
    const b = document.createElement("button");
    b.setAttribute("aria-label", `Ir al miembro ${i + 1}`);
    b.addEventListener("click", () => {
      currentMember = i;
      renderFeatured(i);
      restartAutoPlay();
    });
    dots.appendChild(b);
  });
}

function animateHero() {
  const els = document.querySelectorAll(
    "#inicio .hero-eyebrow, #inicio .hero-title, #inicio .hero-text, #inicio .btn"
  );
  els.forEach((el) => {
    el.style.transition = "opacity 0.7s ease";
    requestAnimationFrame(() => requestAnimationFrame(() => (el.style.opacity = 1)));
  });
}

function initNavSpy() {
  const links = document.querySelectorAll(".nav-options a");
  const sections = [...links]
    .map((a) => document.querySelector(a.getAttribute("href")))
    .filter(Boolean);

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          links.forEach((a) =>
            a.classList.toggle("active", a.getAttribute("href") === `#${entry.target.id}`)
          );
        }
      });
    },
    { rootMargin: "-40% 0px -55% 0px" }
  );
  sections.forEach((s) => observer.observe(s));
}

function initToast() {
  const btn = document.getElementById("btnThanks");
  const toast = document.getElementById("toast");
  let timer = null;
  btn.addEventListener("click", () => {
    toast.classList.add("show");
    clearTimeout(timer);
    timer = setTimeout(() => toast.classList.remove("show"), 2600);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderDots();
  renderFeatured(0);
  renderTeam();
  animateHero();
  initNavSpy();
  initToast();
  restartAutoPlay();

  document.getElementById("btnNext").addEventListener("click", nextMember);
  document.getElementById("btnPrev").addEventListener("click", prevMember);
});
