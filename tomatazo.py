import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tomatazos en el teatro PRO 03",
    page_icon="🍅",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #1b0f0f;
}

.block-container {
    padding-top: 0.35rem;
    padding-bottom: 0.35rem;
    max-width: 1060px;
}

@media (max-width: 760px) {
    .block-container {
        padding-left: 0.05rem;
        padding-right: 0.05rem;
        padding-top: 0.05rem;
    }

    h1 {
        font-size: 1.15rem !important;
        line-height: 1.05 !important;
        margin-bottom: 0.05rem !important;
        text-shadow: 1px 1px 0 #4a0000;
}
}

h1 {
    text-align: center;
    color: #f5e0b8;
    margin-bottom: 0.15rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🍅 Tomatazos en el teatro PRO 03")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#f0d250;
        font-size:16px;
        font-weight:bold;
        margin-bottom:10px;">
        Desarrollado por Jesús Platero
    </div>
    """,
    unsafe_allow_html=True
)

components.html("""<style>
html, body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

button {
    -webkit-tap-highlight-color: transparent;
}

#gameWrap {
    width: 100%;
    display: flex;
    justify-content: center;
}

#game {
    display: block;
    outline: none;
    border: 4px solid #4a0000;
    border-radius: 14px;
    background: #e6d2aa;
    box-shadow: 0 8px 24px rgba(80, 0, 0, 0.35);
}

.control-row {
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 8px;
    flex-wrap: wrap;
}

.main-btn {
    font-family: Arial, sans-serif;
    font-weight: bold;
    padding: 8px 16px;
    border-radius: 10px;
    border: 2px solid #780000;
    background: #f5e0b8;
    color: #780000;
    cursor: pointer;
    touch-action: manipulation;
}

.green-btn {
    background: #1eaa55;
    color: white;
}

.level-btn {
    font-family: Arial, sans-serif;
    font-weight: bold;
    padding: 8px 14px;
    border-radius: 999px;
    border: 2px solid #780000;
    background: #f5e0b8;
    color: #780000;
    cursor: pointer;
    touch-action: manipulation;
}

#touchBar {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 9px;
    margin-top: 9px;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}

.touch-btn {
    font-family: Arial, sans-serif;
    font-weight: bold;
    border-radius: 13px;
    border: 3px solid #780000;
    background: #f5e0b8;
    color: #780000;
    cursor: pointer;
    touch-action: none;
    user-select: none;
}

#btnLeft, #btnRight {
    font-size: 30px;
    width: 76px;
    height: 58px;
}

#btnShoot {
    font-size: 18px;
    min-width: 170px;
    height: 58px;
    background: #1eaa55;
    color: white;
}

#helpText {
    text-align: center;
    color: #f5e0b8;
    font-family: Arial, sans-serif;
    font-weight: bold;
    margin-top: 7px;
    margin-bottom: 0;
    font-size: 14px;
}

@media (max-width: 760px) {
    #game {
        border-width: 3px;
        border-radius: 10px;
    }

    .control-row {
        gap: 6px;
        margin-top: 5px;
    }

    .main-btn {
        padding: 7px 11px !important;
        font-size: 13px !important;
    }

    .level-btn {
        padding: 7px 10px !important;
        font-size: 13px !important;
    }

    #touchBar {
        gap: 6px !important;
        margin-top: 6px !important;
    }

    #btnLeft, #btnRight {
        width: 76px !important;
        height: 60px !important;
        font-size: 30px !important;
    }

    #btnShoot {
        min-width: 145px !important;
        height: 60px !important;
        font-size: 17px !important;
    }

    #helpText {
        display: none;
    }
}
</style>

<div id="gameWrap">
    <canvas id="game" tabindex="0"></canvas>
</div>

<div class="control-row">
    <button id="btnMenu" class="main-btn">M / Menú</button>
    <button id="btnStart" class="main-btn green-btn">ENTER / Continuar</button>
</div>

<div id="levelBar" class="control-row">
    <button id="btnNivel1" class="level-btn">Nivel 1</button>
    <button id="btnNivel2" class="level-btn">Nivel 2</button>
    <button id="btnNivel3" class="level-btn">Nivel 3</button>
</div>

<div id="touchBar">
    <div style="display:flex; gap:7px;">
        <button id="btnLeft" class="touch-btn">←</button>
        <button id="btnRight" class="touch-btn">→</button>
    </div>
    <button id="btnShoot" class="touch-btn">🍅 DISPARAR</button>
</div>

<p id="helpText">PC: clic dentro del juego. 1, 2 o 3 eligen nivel. ENTER empieza/continúa. ESPACIO dispara. Móvil: ← → y DISPARAR.</p>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const BASE_W = 900;
const BASE_H = 650;

canvas.width = BASE_W;
canvas.height = BASE_H;

const esMovil = window.matchMedia("(max-width: 760px)").matches || ("ontouchstart" in window);

function ajustarCanvas() {
    const margenW = esMovil ? 0.99 : 0.94;
    const anchoMax = esMovil ? window.innerWidth * margenW : Math.min(window.innerWidth * margenW, 1040);
    const altoMax = esMovil ? window.innerHeight * 0.80 : Math.min(window.innerHeight * 0.74, 670);
    const altoPorAncho = anchoMax * (BASE_H / BASE_W);
    const altoFinal = Math.min(altoPorAncho, altoMax);
    const anchoFinal = altoFinal * (BASE_W / BASE_H);
    canvas.style.width = `${Math.floor(anchoFinal)}px`;
    canvas.style.height = `${Math.floor(altoFinal)}px`;
}

window.addEventListener("resize", ajustarCanvas);
window.addEventListener("orientationchange", () => setTimeout(ajustarCanvas, 150));
ajustarCanvas();
canvas.style.border = "4px solid #4a0000";
canvas.style.borderRadius = "12px";
canvas.style.background = "#e6d2aa";
canvas.style.boxShadow = "0 8px 24px rgba(80, 0, 0, 0.35)";
canvas.style.display = "block";
canvas.style.outline = "none";

function enfocarCanvas() {
    try { canvas.focus({preventScroll:true}); } catch (err) { canvas.focus(); }
}

enfocarCanvas();
canvas.addEventListener("click", enfocarCanvas);
canvas.addEventListener("mouseenter", enfocarCanvas);
window.addEventListener("load", enfocarCanvas);
setInterval(() => {
    if (estado === "fin" || estado === "victoria" || estado === "cambio_nivel") enfocarCanvas();
}, 350);

const W = BASE_W;
const H = BASE_H;

let estado = "menu";
let puntos = 0;
let puntosNivel = 0;
let vidas = 5;
let nivel = 1;
let nivelElegido = 1;
let doble = false;
let dobleHasta = 0;
let mensajeNivel = "";
let esNuevoRecord = false;
let record = Number(localStorage.getItem("tomatazos_record") || 0);
let particulas = [];
let teclas = {};

let jugador = {
    x: 420,
    y: 560,
    w: 55,
    h: 55,
    vel: 7
};

let tomates = [];
let huevos = [];
let actores = [];
let bonus = [];
let penalizaciones = [];
let impactos = [];

function teclaNormalizada(e) {
    return (e.key || "").toLowerCase();
}

function manejarTecla(e) {
    const k = teclaNormalizada(e);
    teclas[e.key] = true;
    teclas[k] = true;

    if (e.code === "Space" || e.key === "ArrowLeft" || e.key === "ArrowRight" || k === "m" || e.code === "Enter" || e.key === "Escape") {
        e.preventDefault();
    }

    if (estado === "menu") {
        if (e.key === "1") elegirNivel(1);
        if (e.key === "2") elegirNivel(2);
        if (e.key === "3") elegirNivel(3);
        if (e.code === "Enter") nuevaPartida(nivelElegido);
        return;
    }

    if (estado === "jugando" && e.code === "Space") {
        lanzarTomate();
        return;
    }

    if (estado === "cambio_nivel") {
        if (e.code === "Enter") pasarAlSiguienteNivel();
        if (k === "m" || e.code === "KeyM" || e.key === "Escape") volverAlMenu();
        return;
    }

    if (estado === "fin" || estado === "victoria") {
        if (k === "m" || e.code === "KeyM" || e.key === "Escape" || e.code === "Enter") volverAlMenu();
    }
}

function soltarTecla(e) {
    const k = teclaNormalizada(e);
    teclas[e.key] = false;
    teclas[k] = false;
}

window.onkeydown = manejarTecla;
document.onkeydown = manejarTecla;
canvas.onkeydown = manejarTecla;

window.onkeyup = soltarTecla;
document.onkeyup = soltarTecla;
canvas.onkeyup = soltarTecla;

const btnMenu = document.getElementById("btnMenu");
const btnStart = document.getElementById("btnStart");
const btnLeft = document.getElementById("btnLeft");
const btnRight = document.getElementById("btnRight");
const btnShoot = document.getElementById("btnShoot");
const btnNivel1 = document.getElementById("btnNivel1");
const btnNivel2 = document.getElementById("btnNivel2");
const btnNivel3 = document.getElementById("btnNivel3");

function bloquearToque(e) {
    if (e && e.cancelable) e.preventDefault();
}

function pulsarDireccion(tecla, activo, e) {
    bloquearToque(e);
    teclas[tecla] = activo;
    enfocarCanvas();
}

function pintarBotonesNivel() {
    [btnNivel1, btnNivel2, btnNivel3].forEach((b, i) => {
        const activo = nivelElegido === i + 1;
        b.style.background = activo ? "#1eaa55" : "#f5e0b8";
        b.style.color = activo ? "white" : "#780000";
    });
}

function elegirNivel(n) {
    nivelElegido = n;
    pintarBotonesNivel();
    enfocarCanvas();
}

btnNivel1.addEventListener("click", () => elegirNivel(1));
btnNivel2.addEventListener("click", () => elegirNivel(2));
btnNivel3.addEventListener("click", () => elegirNivel(3));
pintarBotonesNivel();

function disparoTactil(e) {
    bloquearToque(e);
    enfocarCanvas();
    if (estado === "jugando") {
        lanzarTomate();
    }
}

btnLeft.addEventListener("touchstart", (e) => pulsarDireccion("ArrowLeft", true, e), {passive:false});
btnLeft.addEventListener("touchend", (e) => pulsarDireccion("ArrowLeft", false, e), {passive:false});
btnLeft.addEventListener("touchcancel", (e) => pulsarDireccion("ArrowLeft", false, e), {passive:false});
btnLeft.addEventListener("mousedown", (e) => pulsarDireccion("ArrowLeft", true, e));
btnLeft.addEventListener("mouseup", (e) => pulsarDireccion("ArrowLeft", false, e));
btnLeft.addEventListener("mouseleave", (e) => pulsarDireccion("ArrowLeft", false, e));

btnRight.addEventListener("touchstart", (e) => pulsarDireccion("ArrowRight", true, e), {passive:false});
btnRight.addEventListener("touchend", (e) => pulsarDireccion("ArrowRight", false, e), {passive:false});
btnRight.addEventListener("touchcancel", (e) => pulsarDireccion("ArrowRight", false, e), {passive:false});
btnRight.addEventListener("mousedown", (e) => pulsarDireccion("ArrowRight", true, e));
btnRight.addEventListener("mouseup", (e) => pulsarDireccion("ArrowRight", false, e));
btnRight.addEventListener("mouseleave", (e) => pulsarDireccion("ArrowRight", false, e));

btnShoot.addEventListener("touchstart", disparoTactil, {passive:false});
btnShoot.addEventListener("mousedown", disparoTactil);

btnMenu.addEventListener("click", () => {
    volverAlMenu();
    enfocarCanvas();
});

btnStart.addEventListener("click", () => {
    if (estado === "menu") nuevaPartida(nivelElegido);
    else if (estado === "cambio_nivel") pasarAlSiguienteNivel();
    else if (estado === "fin" || estado === "victoria") volverAlMenu();
    enfocarCanvas();
});

canvas.addEventListener("mousedown", () => {
    enfocarCanvas();
    if (estado === "fin" || estado === "victoria") volverAlMenu();
});

function guardarRecord() {
    const recordAnterior = Number(localStorage.getItem("tomatazos_record") || 0);
    if (puntos > recordAnterior) {
        localStorage.setItem("tomatazos_record", String(puntos));
        record = puntos;
        esNuevoRecord = true;
    } else {
        record = recordAnterior;
        esNuevoRecord = false;
    }
}

function efectoCambioNivel() {
    particulas = [];
    const colores = ["#f0d250", "#1eaa55", "#d21e1e", "#326edc", "#ffffff"];

    for (let i = 0; i < 90; i++) {
        particulas.push({
            x: W / 2,
            y: 230,
            vx: (Math.random() - 0.5) * 9,
            vy: -Math.random() * 7 - 2,
            g: 0.18 + Math.random() * 0.08,
            vida: 70 + Math.random() * 35,
            color: colores[Math.floor(Math.random() * colores.length)],
            tam: 3 + Math.random() * 5
        });
    }

    sonidoCambioNivel();
}

function actualizarParticulas() {
    particulas.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += p.g;
        p.vida--;
    });
    particulas = particulas.filter(p => p.vida > 0);
}

function dibujarParticulas() {
    particulas.forEach(p => {
        ctx.fillStyle = p.color;
        ctx.fillRect(p.x, p.y, p.tam, p.tam);
    });
}

function sonidoCambioNivel() {
    try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;

        const audio = new AudioCtx();
        const notas = [523.25, 659.25, 783.99];

        notas.forEach((freq, i) => {
            const osc = audio.createOscillator();
            const gain = audio.createGain();
            osc.type = "triangle";
            osc.frequency.value = freq;
            osc.connect(gain);
            gain.connect(audio.destination);
            gain.gain.setValueAtTime(0.001, audio.currentTime + i * 0.09);
            gain.gain.exponentialRampToValueAtTime(0.08, audio.currentTime + i * 0.09 + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, audio.currentTime + i * 0.09 + 0.16);
            osc.start(audio.currentTime + i * 0.09);
            osc.stop(audio.currentTime + i * 0.09 + 0.18);
        });
    } catch (err) {}
}

function sonidoLanzar() {
    try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;

        const audio = new AudioCtx();
        const osc = audio.createOscillator();
        const gain = audio.createGain();

        osc.frequency.value = 720;
        osc.type = "sine";
        osc.connect(gain);
        gain.connect(audio.destination);

        gain.gain.setValueAtTime(0.001, audio.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.08, audio.currentTime + 0.01);
        gain.gain.exponentialRampToValueAtTime(0.001, audio.currentTime + 0.055);

        osc.start(audio.currentTime);
        osc.stop(audio.currentTime + 0.06);
    } catch (err) {}
}

function sonidoImpacto() {
    try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;

        const audio = new AudioCtx();
        const osc = audio.createOscillator();
        const gain = audio.createGain();

        osc.frequency.value = 180;
        osc.type = "square";
        osc.connect(gain);
        gain.connect(audio.destination);

        gain.gain.setValueAtTime(0.001, audio.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.05, audio.currentTime + 0.008);
        gain.gain.exponentialRampToValueAtTime(0.001, audio.currentTime + 0.08);

        osc.start(audio.currentTime);
        osc.stop(audio.currentTime + 0.09);
    } catch (err) {}
}

function efectoImpacto(x, y) {
    impactos.push({x: x, y: y, vida: 42, max: 42, r: 5});
    sonidoImpacto();
}

function objetivoNivel() {
    // Aumentado significativamente para dar más duración
    if (nivel === 1) return 20;   // antes 10
    if (nivel === 2) return 30;   // antes 15
    return 40;                     // antes 20
}

function nuevaPartida(nivelInicial=1) {
    estado = "jugando";
    enfocarCanvas();
    puntos = 0;
    puntosNivel = 0;
    vidas = 5;
    nivel = nivelInicial;
    doble = false;
    dobleHasta = 0;
    esNuevoRecord = false;
    particulas = [];
    impactos = [];
    jugador.x = 420;
    jugador.y = 560;
    reiniciarNivel();
}

function volverAlMenu() {
    estado = "menu";
    enfocarCanvas();
    puntos = 0;
    puntosNivel = 0;
    vidas = 5;
    doble = false;
    dobleHasta = 0;
    mensajeNivel = "";
    esNuevoRecord = false;
    particulas = [];
    tomates = [];
    huevos = [];
    actores = [];
    bonus = [];
    penalizaciones = [];
    impactos = [];
    jugador.x = 420;
    jugador.y = 560;
}

function pasarAlSiguienteNivel() {
    if (nivel >= 3) {
        guardarRecord();
        efectoCambioNivel();
        estado = "victoria";
        enfocarCanvas();
        return;
    }

    nivel++;
    puntosNivel = 0;
    doble = false;
    dobleHasta = 0;
    mensajeNivel = "";
    esNuevoRecord = false;
    estado = "jugando";
    enfocarCanvas();
    jugador.x = 420;
    jugador.y = 560;
    reiniciarNivel();
}

function crearActor() {
    let vel = nivel === 1 ? 1.45 : nivel === 2 ? 2.05 : 2.65;
    const coloresActores = ["#f0d250", "#e74c3c", "#3498db", "#2ecc71", "#9650b4", "#f39c12"];

    if (Math.random() < 0.5) vel *= -1;

    actores.push({
        x: 130 + Math.random() * (W - 260),
        y: 95 + Math.random() * 110,
        w: 50,
        h: 82,
        vel: vel,
        color: coloresActores[Math.floor(Math.random() * coloresActores.length)]
    });
}

function reiniciarNivel() {
    tomates = [];
    huevos = [];
    actores = [];
    bonus = [];
    penalizaciones = [];
    impactos = [];

    let cantidad = nivel === 1 ? 5 : nivel === 2 ? 7 : 9;

    for (let i = 0; i < cantidad; i++) crearActor();
}

function lanzarTomate() {
    sonidoLanzar();
    if (doble) {
        tomates.push({x: jugador.x + 9, y: jugador.y - 12, w: 15, h: 15});
        tomates.push({x: jugador.x + 31, y: jugador.y - 12, w: 15, h: 15});
    } else {
        tomates.push({x: jugador.x + 20, y: jugador.y - 12, w: 15, h: 15});
    }
}

function colision(a, b) {
    return a.x < b.x + b.w &&
           a.x + a.w > b.x &&
           a.y < b.y + b.h &&
           a.y + a.h > b.y;
}

function texto(txt, y, color="#141414", size=26, bold=false) {
    ctx.fillStyle = color;
    ctx.font = `${bold ? "bold " : ""}${size}px Trebuchet MS, Verdana, Arial`;
    ctx.textAlign = "center";
    ctx.fillText(txt, W / 2, y);
}

function cajaTexto(x, y, w, h, color, borde=null) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);

    if (borde) {
        ctx.strokeStyle = borde;
        ctx.lineWidth = 3;
        ctx.strokeRect(x, y, w, h);
    }
}

function teatro() {
    ctx.fillStyle = "#e6d2aa";
    ctx.fillRect(0, 0, W, H);

    ctx.fillStyle = "#9b5f2d";
    ctx.fillRect(0, 385, W, 265);

    ctx.fillStyle = "#140f0f";
    ctx.fillRect(0, 375, W, 10);

    ctx.fillStyle = "#870000";
    ctx.fillRect(0, 0, 90, H);
    ctx.fillRect(W - 90, 0, 90, H);

    ctx.fillStyle = "#6f0000";
    ctx.fillRect(0, 0, W, 45);

    ctx.fillStyle = "#d51b1b";
    for (let x = -40; x < W + 80; x += 80) {
        ctx.beginPath();
        ctx.arc(x + 40, 45, 45, 0, Math.PI);
        ctx.fill();
    }

    ctx.fillStyle = "rgba(80,0,0,0.25)";
    ctx.fillRect(0, 0, 90, H);
    ctx.fillRect(W - 90, 0, 90, H);
}

function persona(x, y, ropa, escala=1) {
    const cx = x + 25 * escala;

    ctx.fillStyle = "#f0be96";
    ctx.beginPath();
    ctx.arc(cx, y + 15 * escala, 13 * escala, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = ropa;
    ctx.fillRect(x + 14 * escala, y + 30 * escala, 23 * escala, 30 * escala);

    ctx.strokeStyle = "#141414";
    ctx.lineWidth = 3 * escala;

    ctx.beginPath();
    ctx.moveTo(x + 16 * escala, y + 60 * escala);
    ctx.lineTo(x + 8 * escala, y + 78 * escala);
    ctx.moveTo(x + 34 * escala, y + 60 * escala);
    ctx.lineTo(x + 43 * escala, y + 78 * escala);
    ctx.moveTo(x + 14 * escala, y + 38 * escala);
    ctx.lineTo(x + 3 * escala, y + 51 * escala);
    ctx.moveTo(x + 37 * escala, y + 38 * escala);
    ctx.lineTo(x + 48 * escala, y + 51 * escala);
    ctx.stroke();

    ctx.fillStyle = "#141414";
    ctx.beginPath();
    ctx.arc(cx - 5 * escala, y + 13 * escala, 2 * escala, 0, Math.PI * 2);
    ctx.arc(cx + 5 * escala, y + 13 * escala, 2 * escala, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(cx, y + 20 * escala, 5 * escala, 0, Math.PI);
    ctx.stroke();
}

function publico() {
    const colores = ["#326edc", "#3cb45a", "#9650b4", "#f0d250"];

    for (let x = 30; x < W; x += 70) {
        ctx.fillStyle = "#f0be96";
        ctx.beginPath();
        ctx.arc(x, 608, 15, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = colores[Math.floor(x / 70) % colores.length];
        ctx.fillRect(x - 18, 624, 36, 26);
    }
}

function dibujarMenu() {
    teatro();
    publico();

    cajaTexto(120, 76, 660, 480, "rgba(230,210,170,0.95)", "#780000");

    texto("🍅 TOMATAZOS EN EL TEATRO 🍅", 132, "#780000", 30, true);
    texto("Elige nivel antes de empezar", 174, "#555555", 21);

    texto(`Nivel elegido: ${nivelElegido}`, 220, "#a00000", 30, true);
    texto(`🏆 Récord: ${record}`, 246, "#780000", 20, true);

    texto("1  Suave: actores lentos y sin huevos", 270, "#141414", 21);
    texto("2  Teatro hostil: actores con huevos", 306, "#141414", 21);
    texto("3  Guerra total: más actores y más ataques", 342, "#141414", 21);

    texto("Pulsa 1, 2 o 3 para seleccionar", 396, "#326edc", 23, true);
    texto("← → moverse    ESPACIO lanzar tomates    ENTER empezar/continuar", 436, "#141414", 21);
    texto("Bonus verde con 2: doble tomate durante 8 segundos", 472, "#1eaa55", 19, true);
    texto("Penalización negra o huevos: pierdes una vida", 504, "#141414", 19);

    texto("ENTER PARA COMENZAR", 606, "#1eaa55", 29, true);
}

function actualizar() {
    if (estado !== "jugando") return;

    if (teclas["ArrowLeft"] && jugador.x > 105) jugador.x -= jugador.vel;
    if (teclas["ArrowRight"] && jugador.x + jugador.w < W - 105) jugador.x += jugador.vel;

    tomates.forEach(t => t.y -= 10);
    tomates = tomates.filter(t => t.y > -25);

    impactos.forEach(i => i.vida--);
    impactos = impactos.filter(i => i.vida > 0);

    actores.forEach(a => {
        a.x += a.vel;

        if (a.x < 105 || a.x + a.w > W - 105) {
            a.vel *= -1;
            a.y += nivel === 1 ? 12 : nivel === 2 ? 14 : 16;
        }

        if (nivel >= 2) {
            let prob = nivel === 2 ? 0.0025 : 0.0045;
            if (Math.random() < prob) {
                huevos.push({x: a.x + a.w / 2 - 6, y: a.y + a.h, w: 12, h: 16});
            }
        }

        if (a.y + a.h > 545) {
            vidas--;
            a.y = 95;
            a.x = 130 + Math.random() * (W - 260);
        }
    });

    huevos.forEach(h => h.y += 4 + nivel);
    huevos = huevos.filter(h => {
        if (colision(h, jugador)) {
            vidas--;
            return false;
        }
        return h.y < H;
    });

    tomates.forEach(t => {
        actores.forEach(a => {
            if (colision(t, a)) {
                t.muerto = true;
                puntos++;
                puntosNivel++;
                efectoImpacto(t.x + 8, t.y + 8);

                a.x = 130 + Math.random() * (W - 260);
                a.y = 95 + Math.random() * 115;

                if (Math.random() < 0.11) {
                    bonus.push({x: 130 + Math.random() * (W - 260), y: 90, w: 32, h: 32});
                }

                if (Math.random() < 0.075) {
                    penalizaciones.push({x: 130 + Math.random() * (W - 260), y: 90, w: 32, h: 32});
                }
            }
        });
    });

    tomates = tomates.filter(t => !t.muerto);

    bonus.forEach(b => b.y += 2.5);
    bonus = bonus.filter(b => {
        if (colision(b, jugador)) {
            doble = true;
            dobleHasta = Date.now() + 8000;
            return false;
        }
        return b.y < H;
    });

    penalizaciones.forEach(p => p.y += 3.2);
    penalizaciones = penalizaciones.filter(p => {
        if (colision(p, jugador)) {
            vidas--;
            return false;
        }
        return p.y < H;
    });

    if (doble && Date.now() > dobleHasta) doble = false;

    if (vidas <= 0) {
        guardarRecord();
        estado = "fin";
        enfocarCanvas();
        return;
    }

    if (puntosNivel >= objetivoNivel()) {
        if (nivel >= 3) {
            guardarRecord();
            efectoCambioNivel();
            estado = "victoria";
            enfocarCanvas();
        } else {
            mensajeNivel = nivel === 1 ? "Nivel 1 superado" : "Nivel 2 superado";
            efectoCambioNivel();
            estado = "cambio_nivel";
            enfocarCanvas();
        }
    }
}

function dibujarHUD() {
    cajaTexto(105, 12, 690, 62, "rgba(230,210,170,0.88)", "#780000");

    ctx.textAlign = "left";
    ctx.font = "bold 22px Trebuchet MS, Verdana, Arial";
    ctx.fillStyle = "#141414";
    ctx.fillText(`Puntos: ${puntos}`, 130, 40);
    ctx.fillText(`Vidas: ${vidas}`, 295, 40);
    ctx.fillText(`Nivel: ${nivel}`, 425, 40);
    ctx.fillText(`Ronda: ${puntosNivel}/${objetivoNivel()}`, 540, 40);

    ctx.textAlign = "right";
    ctx.font = "bold 18px Trebuchet MS, Verdana, Arial";
    ctx.fillStyle = "#780000";
    ctx.fillText(`🏆 ${record}`, 770, 38);

    if (doble) {
        const quedan = Math.max(0, Math.ceil((dobleHasta - Date.now()) / 1000));
        ctx.fillStyle = "#1eaa55";
        ctx.fillText(`⚡ Doble: ${quedan}s`, 770, 64);
    }
}

function dibujarImpactos() {
    impactos.forEach(i => {
        const progreso = 1 - (i.vida / i.max);
        const alpha = Math.max(0, i.vida / i.max);
        const radio = i.r + progreso * 28;

        ctx.fillStyle = `rgba(210,30,30,${0.55 * alpha})`;
        ctx.beginPath();
        ctx.ellipse(i.x, i.y, 18 + progreso * 8, 10 + progreso * 5, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = `rgba(120,0,0,${0.7 * alpha})`;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(i.x, i.y, radio, 0, Math.PI * 2);
        ctx.stroke();

        ctx.strokeStyle = `rgba(255,230,210,${0.55 * alpha})`;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(i.x, i.y, radio * 0.55, 0, Math.PI * 2);
        ctx.stroke();
    });
}

function dibujarJuego() {
    teatro();
    publico();
    dibujarImpactos();
    persona(jugador.x, jugador.y, "#326edc", 1.08);

    tomates.forEach(t => {
        ctx.fillStyle = "#d21e1e";
        ctx.beginPath();
        ctx.ellipse(t.x + 7, t.y + 7, 8, 8, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = "#3cb45a";
        ctx.beginPath();
        ctx.arc(t.x + 8, t.y, 3, 0, Math.PI * 2);
        ctx.fill();
    });

    huevos.forEach(h => {
        ctx.fillStyle = "#f5f5f5";
        ctx.beginPath();
        ctx.ellipse(h.x + 6, h.y + 8, 6, 8, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = "#f0d250";
        ctx.beginPath();
        ctx.arc(h.x + 6, h.y + 8, 3.5, 0, Math.PI * 2);
        ctx.fill();
    });

    actores.forEach(a => persona(a.x, a.y, a.color || "#f0d250", 1));

    bonus.forEach(b => {
        ctx.fillStyle = "#1eaa55";
        ctx.beginPath();
        ctx.arc(b.x + 16, b.y + 16, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 20px Trebuchet MS, Verdana, Arial";
        ctx.textAlign = "center";
        ctx.fillText("2", b.x + 16, b.y + 24);
    });

    penalizaciones.forEach(p => {
        ctx.fillStyle = "#141414";
        ctx.beginPath();
        ctx.arc(p.x + 16, p.y + 16, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#d21e1e";
        ctx.font = "bold 20px Trebuchet MS, Verdana, Arial";
        ctx.textAlign = "center";
        ctx.fillText("!", p.x + 16, p.y + 24);
    });

    dibujarHUD();
}

function dibujarCambioNivel() {
    actualizarParticulas();
    teatro();
    publico();
    dibujarParticulas();

    cajaTexto(120, 165, 660, 315, "rgba(230,210,170,0.96)", "#780000");

    texto(mensajeNivel, 235, "#1eaa55", 40, true);
    texto(`Puntuación total: ${puntos}`, 292, "#141414", 26);
    texto(`Vidas restantes: ${vidas}`, 330, "#141414", 24);

    texto(`¿Quieres pasar al nivel ${nivel + 1}?`, 385, "#780000", 30, true);
    texto("ENTER: sí, continuar", 430, "#1eaa55", 24, true);
    texto("M: volver al menú y elegir otro nivel", 462, "#141414", 21);
}

function dibujarFinal() {
    actualizarParticulas();
    teatro();
    publico();
    dibujarParticulas();

    cajaTexto(140, 180, 620, 260, "rgba(230,210,170,0.94)", "#780000");

    if (estado === "fin") {
        texto("FIN DE LA FUNCIÓN", 260, "#d21e1e", 42, true);
        texto(`Puntuación final: ${puntos}`, 315, "#141414", 28);
        texto(`🏆 Récord: ${record}`, 350, "#780000", 23, true);
        if (esNuevoRecord) texto("🎉 ¡NUEVO RÉCORD! 🎉", 386, "#1eaa55", 27, true);
        texto("Pulsa M, ESC o ENTER para volver al menú", 420, "#1eaa55", 22, true);
    }

    if (estado === "victoria") {
        texto("🎭 ¡OVACIÓN FINAL! 🎭", 260, "#1eaa55", 44, true);
        texto(`Puntuación final: ${puntos}`, 315, "#141414", 28);
        texto(`🏆 Récord: ${record}`, 350, "#780000", 23, true);
        if (esNuevoRecord) texto("🎉 ¡NUEVO RÉCORD! 🎉", 386, "#1eaa55", 27, true);
        texto("Pulsa M, ESC o ENTER para volver al menú", 420, "#1eaa55", 22, true);
    }
}

function dibujar() {
    if (estado === "menu") dibujarMenu();
    else if (estado === "jugando") dibujarJuego();
    else if (estado === "cambio_nivel") dibujarCambioNivel();
    else dibujarFinal();
}

function loop() {
    actualizar();
    dibujar();
    requestAnimationFrame(loop);
}

loop();
</script>
""", height=760, scrolling=False)
