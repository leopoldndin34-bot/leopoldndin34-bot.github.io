# -*- coding: utf-8 -*-
"""
Générateur du portfolio de Léopold César N'DIN.
Ce script fabrique les pages HTML du site à partir des contenus ci-dessous.
Il n'est PAS nécessaire pour publier le site : les fichiers .html déjà générés suffisent.
(Le dossier _source est ignoré par GitHub Pages.)
Utilisation (facultative) :  python3 _source/construire.py
"""
import json, os, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://leopoldndin34-bot.github.io/"
EMAIL = "leopoldndin34@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/leopold-n-din-a68049248"   # ← collez ici l'adresse de votre profil LinkedIn (ex. https://www.linkedin.com/in/...)
TELEPHONE = "+225 01 01 79 98 33"   # ← laissez vide ("") pour ne pas publier votre numéro
FORMSPREE = "https://formspree.io/f/xeaazeol"   # ← facultatif : https://formspree.io/f/xxxxxx pour recevoir les messages sans messagerie
CV_PDF = "assets/docs/CV_Leopold_Cesar_NDIN.pdf"

MANIFEST = json.load(open(Path(__file__).parent / "images.json"))

def esc(s): return html.escape(s, quote=True)

# ------------------------------------------------------------------ icônes
I = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>',
 "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 "cone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9.5 4h5L19 19H5z"/><path d="M8 11h8M6.8 15h10.4M3 19h18"/></svg>',
 "cube": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M12 12l8-4.5M12 12v9M12 12L4 7.5"/></svg>',
 "beam": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h18M3 11h18M6 11v9M18 11v9M3 20h6M15 20h6"/><path d="M8 5l4-2 4 2"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20V4M4 20h16"/><path d="M7 16c3-1 4-9 6-9s3 7 6 8"/></svg>',
 "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
}

LOGO = '''<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><rect x="1" y="1" width="38" height="38" rx="9" fill="#141a22" stroke="#344152"/><path d="M9 29V11l11 18V11" fill="none" stroke="#e8ebef" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M24 29h7" stroke="#f2a541" stroke-width="2.6" stroke-linecap="round"/><circle cx="31" cy="12" r="2.2" fill="#f2a541"/></svg>'''

def img(path, alt, cls="", sizes="(max-width: 700px) 100vw, 50vw", lazy=True, thumb=True):
    m = MANIFEST[path]
    src = f"assets/img/projets/{path}.webp"
    t = f"assets/img/projets/{path}-720.webp"
    if m["w"] <= 720: t = src  # petite image : pas de miniature séparée
    srcset = f' srcset="{{R}}{t} 720w, {{R}}{src} {m["w"]}w" sizes="{sizes}"' if thumb and m["w"] > 720 else ""
    return (f'<img src="{{R}}{t if thumb else src}"{srcset} width="{m["w"]}" height="{m["h"]}" alt="{esc(alt)}"'
            f'{" loading=\"lazy\" decoding=\"async\"" if lazy else ""}{f" class=\"{cls}\"" if cls else ""}>')

def video_html(p, R):
    src, poster, label = p["video"]
    return (f'<div class="video-wrap"><video class="cover-video" autoplay muted loop playsinline preload="metadata" poster="{R}{poster}" aria-label="{esc(label)}">'
            f'<source src="{R}{src}" type="video/mp4"></video>'
            f'<button type="button" class="vid-btn" aria-label="Mettre la vidéo en pause" data-label-play="Lire la vidéo" data-label-pause="Mettre la vidéo en pause">'
            f'<svg class="i-pause" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>'
            f'<svg class="i-play" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></button></div>')

# ------------------------------------------------------------------ projets
PROJETS = [
 {
  "slug": "metro-abidjan-plans-methodes",
  "num": "P-01",
  "cat": "methodes",
  "court": "Plans méthodes — Ligne 1 du Métro d’Abidjan",
  "titre": "Plans méthodes pour les ouvrages de la Ligne 1 du Métro d’Abidjan",
  "meta": "SICMA · Bouygues TP · Depuis oct. 2025",
  "resume": "Traduire les plans d’exécution en plans méthodes 2D/3D lisibles par le chantier — terrassement, ferraillage, coffrage, pose de dalles et de travées — puis suivre leur mise en œuvre.",
  "couverture": ("metro-abidjan-plans-methodes/travee-chantier-1", "Levage de nuit d’une travée du viaduc par grue mobile"),
  "outils": ["Revit", "AutoCAD", "Gestion BIM", "Techniques de construction"],
  "spec": [("Entreprise", "SICMA — Bouygues Travaux Publics"), ("Lieu", "Abidjan, Côte d’Ivoire"), ("Rôle", "Ingénieur méthodes"), ("Période", "30 oct. 2025 — en cours")],
  "description": "Plans méthodes 2D/3D réalisés pour la Ligne 1 du Métro d’Abidjan : terrassement, ferraillage, coffrage, pose de dalles préfabriquées et de travées du viaduc.",
 },
 {
  "slug": "pfe-aide-decision-dalle-viaduc",
  "num": "P-02",
  "cat": "decision",
  "court": "Aide à la décision — dalle du viaduc",
  "titre": "Processus d’aide à la décision pour le choix de la méthode de réalisation de la dalle du viaduc",
  "meta": "Projet de fin d’études · INPHB / SICMA · 2025",
  "resume": "Comparer la préfabrication intégrale et les prédalles collaborantes par des analyses probabilistes (PERT, Monte-Carlo) puis trancher avec une analyse multicritère Fuzzy AHP : la préfabrication intégrale est retenue (54 % contre 46 %).",
  "couverture": ("pfe-aide-decision-dalle-viaduc/monte-carlo-resultats", "Histogramme et courbe cumulative des durées simulées par Monte-Carlo"),
  "outils": ["Python", "PERT", "Monte-Carlo", "Fuzzy AHP"],
  "spec": [("Cadre", "Projet de fin d’études — INPHB / SICMA"), ("Lieu", "Abidjan, Côte d’Ivoire"), ("Rôle", "Stagiaire conducteur travaux"), ("Période", "4 mars — 4 sept. 2025")],
  "description": "Projet de fin d’études : outil d’aide à la décision (PERT, Monte-Carlo, Fuzzy AHP) pour choisir la méthode de réalisation de la dalle du viaduc de la Ligne 1 du Métro d’Abidjan.",
 },
 {
  "slug": "batiment-habitation",
  "num": "P-03",
  "cat": "conception",
  "court": "Conception & dimensionnement d’un bâtiment",
  "titre": "Conception et dimensionnement d’un bâtiment d’habitation",
  "meta": "Projet personnel · 2026",
  "resume": "De l’aide à la conception jusqu’à la note de calcul : plans et coupes, maquette 3D, rendus réalistes sous Enscape et dimensionnement des éléments porteurs sous Robot Structural Analysis.",
  "couverture": ("batiment-habitation/rendu-facade-nuit", "Rendu réaliste de nuit de la façade du bâtiment"),
  "video": ("assets/video/batiment-visite-enscape.mp4", "assets/img/projets/batiment-habitation/visite-enscape-poster.webp", "Visite virtuelle du bâtiment réalisée avec Enscape"),
  "outils": ["Revit", "Enscape", "Robot Structural Analysis", "Conception BIM"],
  "spec": [("Cadre", "Projet personnel"), ("Lieu", "Abidjan, Côte d’Ivoire"), ("Rôle", "Conception et calcul"), ("Année", "2026")],
  "description": "Projet personnel de conception et de dimensionnement d’un bâtiment d’habitation : plans 2D, maquette BIM, rendus réalistes et calcul de structure sous Robot.",
 },
]

# ------------------------------------------------------------------ gabarit commun
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

def head(title, desc, path, R, og_img="assets/img/og-image.png", jsonld=""):
    url = SITE_URL + path
    return f'''<!doctype html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="Léopold César N’DIN">
<meta name="theme-color" content="#0b0e13">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Léopold César N’DIN — Portfolio">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{R}favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{R}apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="{R}assets/css/style.css">
{jsonld}
</head>
<body>
<a class="skip-link" href="#contenu">Aller au contenu</a>
<div class="progress" aria-hidden="true"></div>
'''

NAV = [("profil", "Profil"), ("parcours", "Parcours"), ("competences", "Compétences"), ("projets", "Projets"), ("cv", "CV"), ("contact", "Contact")]

def header(R, home=True):
    base = "" if home else f"{R}index.html"
    items = "".join(f'<li><a href="{base}#{i}">{t}</a></li>' for i, t in NAV[:-1])
    return f'''<header class="site-header">
  <nav class="container nav" aria-label="Navigation principale">
    <a class="brand" href="{R}index.html" aria-label="Accueil — Léopold César N’DIN">{LOGO}<span>César N’DIN<small>Ingénieur TP · Méthodes &amp; BIM</small></span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
    <ul class="nav-links" id="menu">
      {items}
      <li class="nav-cta"><a class="btn btn-primary btn-sm" href="{base}#contact">Me contacter</a></li>
    </ul>
  </nav>
</header>
'''

def footer(R, home=True):
    base = "" if home else f"{R}index.html"
    nav = "".join(f'<li><a href="{base}#{i}">{t}</a></li>' for i, t in NAV)
    projs = "".join(f'<li><a href="{R}projets/{p["slug"]}.html">{esc(p["court"])}</a></li>' for p in PROJETS)
    li = f'<li><a href="{LINKEDIN_URL}" rel="noopener" target="_blank">LinkedIn</a></li>' if LINKEDIN_URL else ""
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div class="foot-about">
        <a class="brand" href="{R}index.html">{LOGO}<span>César N’DIN<small>Ingénieur TP · Méthodes &amp; BIM</small></span></a>
        <p>Ingénieur Travaux Publics diplômé de l’ESTP — INPHB. Méthodes de construction, maquette BIM et calcul de structures, au service de chantiers plus sûrs et mieux préparés.</p>
      </div>
      <div><h4>Navigation</h4><ul>{nav}</ul></div>
      <div><h4>Projets</h4><ul>{projs}<li><a href="{R}{CV_PDF}" download>Télécharger le CV</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>{li}</ul></div>
    </div>
    <div class="foot-bottom"><span>© <span data-year>2026</span> Léopold César N’DIN — Tous droits réservés.</span><a class="to-top" href="#contenu">Haut de page ↑</a></div>
  </div>
</footer>
<script src="{R}assets/js/main.js" defer></script>
</body>
</html>
'''

# ------------------------------------------------------------------ dessin du hero (illustration originale)
HERO_SVG = '''<svg class="drawing" viewBox="0 0 560 400" role="img" aria-labelledby="dtitle">
  <title id="dtitle">Schéma de principe original : pose d’une dalle de viaduc à la grue entre deux piles</title>
  <g class="fade" style="--d:.1s">
    <text x="20" y="28">PLAN MÉTHODE · PHASAGE</text>
    <text x="20" y="44" class="t-accent">PHASE 03 — POSE DE LA DALLE</text>
  </g>
  <!-- axes -->
  <g class="fade" style="--d:.3s">
    <path class="ln-thin" stroke-dasharray="10 4 2 4" d="M110 70V350M280 70V350M450 70V350"/>
    <circle class="ln-thin" cx="110" cy="62" r="9"/><text x="106.5" y="65.5">A</text>
    <circle class="ln-thin" cx="280" cy="62" r="9"/><text x="276.5" y="65.5">B</text>
    <circle class="ln-thin" cx="450" cy="62" r="9"/><text x="446.5" y="65.5">C</text>
  </g>
  <!-- sol -->
  <path class="ln draw" style="--d:.2s" d="M14 330H546"/>
  <path class="ln-thin fade" style="--d:1s" d="M24 330l-8 10M44 330l-8 10M64 330l-8 10M84 330l-8 10M124 330l-8 10M144 330l-8 10M164 330l-8 10M184 330l-8 10M204 330l-8 10M224 330l-8 10M244 330l-8 10M304 330l-8 10M324 330l-8 10M344 330l-8 10M364 330l-8 10M384 330l-8 10M404 330l-8 10M424 330l-8 10M484 330l-8 10M504 330l-8 10M524 330l-8 10M544 330l-8 10"/>
  <!-- fondations -->
  <path class="ln-thin draw" style="--d:.6s" stroke-dasharray="4 3" d="M98 330v40M122 330v40M268 330v40M292 330v40M438 330v40M462 330v40"/>
  <path class="ln draw" style="--d:.5s" d="M88 330h44v-14H88zM258 330h44v-14h-44zM428 330h44v-14h-44z"/>
  <!-- piles -->
  <path class="ln draw" style="--d:.7s" d="M100 316V186h20v130M270 316V186h20v130M440 316V186h20v130"/>
  <path class="ln draw" style="--d:.9s" d="M88 186h44l-6-12H94zM258 186h44l-6-12h-38zM428 186h44l-6-12h-38z"/>
  <!-- tablier posé -->
  <path class="ln draw" style="--d:1.1s" d="M20 152H292v22H20M20 152v22"/>
  <path class="ln-thin draw" style="--d:1.3s" d="M20 160H292M60 174v-8M150 174v-8M200 174v-8M240 174v-8"/>
  <!-- grue -->
  <path class="ln draw" style="--d:1.4s" d="M478 330v-26h62v26M486 304v-14h30v14"/>
  <circle class="ln draw" style="--d:1.5s" cx="490" cy="330" r="0.1"/>
  <path class="ln-accent draw" style="--d:1.6s" d="M500 292L370 40M508 292L374 40"/>
  <path class="ln-thin draw" style="--d:1.8s" d="M503 292L372 40M372 40l-6 8"/>
  <!-- charge levée -->
  <g class="lift">
    <path class="ln-accent draw" style="--d:2s" d="M372 40V78M372 78L306 104M372 78L436 104"/>
    <rect class="draw ln-accent" style="--d:2.1s" x="300" y="104" width="142" height="20" rx="1"/>
    <path class="fade" style="--d:2.6s;fill:rgba(242,165,65,.14)" d="M300 104h142v20H300z"/>
  </g>
  <!-- cotes -->
  <g class="fade" style="--d:2.4s">
    <path class="dim" d="M110 368H280M450 368H280M110 362v12M280 362v12M450 362v12"/>
    <text x="150" y="388">TRAVÉE POSÉE</text>
    <text x="318" y="388" class="t-accent">TRAVÉE À POSER</text>
    <path class="dim" d="M292 140v-16M300 140v-16" />
    <text x="20" y="200">±0,00</text>
  </g>
</svg>'''

# ------------------------------------------------------------------ page d'accueil
def page_index():
    R = ""
    jsonld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Léopold César N’DIN","alternateName":"N’DIN N’DIN Léopold César","jobTitle":"Ingénieur Travaux Publics — Méthodes & BIM","url":"%s","email":"mailto:%s","alumniOf":[{"@type":"CollegeOrUniversity","name":"École Supérieure des Travaux Publics (ESTP) — INPHB Yamoussoukro"}],"worksFor":{"@type":"Organization","name":"Société Ivoirienne de Construction du Métro d’Abidjan (SICMA)"},"address":{"@type":"PostalAddress","addressLocality":"Abidjan","addressCountry":"CI"},"knowsAbout":["Méthodes de construction","BIM","Revit","Robot Structural Analysis","Planification","Python"]}</script>''' % (SITE_URL, EMAIL)
    h = head("Léopold César N’DIN — Ingénieur Travaux Publics · Méthodes & BIM",
             "Portfolio de Léopold César N’DIN, ingénieur Travaux Publics (ESTP — INPHB) : plans méthodes sur la Ligne 1 du Métro d’Abidjan, maquette BIM, calcul de structures et aide à la décision.",
             "", R, jsonld=jsonld)

    cards = []
    for i, p in enumerate(PROJETS):
        feat = " featured" if i == 0 else ""
        c_img = video_html(p, R) if p.get("video") else img(p["couverture"][0], p["couverture"][1], sizes="(max-width: 860px) 100vw, 60vw").replace("{R}", R)
        chips = "".join(f'<span class="chip">{esc(t)}</span>' for t in p["outils"])
        cards.append(f'''
      <article class="p-card{feat} reveal" data-cat="{p["cat"]}">
        <div class="p-media"><span class="p-num">{p["num"]}</span>{c_img}</div>
        <div class="p-body">
          <p class="p-meta">{esc(p["meta"])}</p>
          <h3>{esc(p["titre"])}</h3>
          <p>{esc(p["resume"])}</p>
          <div class="chips">{chips}</div>
          <a class="p-link stretch" href="projets/{p["slug"]}.html">Voir l’étude de cas {I["arrow"]}</a>
        </div>
      </article>''')

    contact_li = ""
    if LINKEDIN_URL:
        contact_li += f'<li><a href="{LINKEDIN_URL}" target="_blank" rel="noopener">{I["linkedin"]}<span><small>LinkedIn</small>Léopold N’DIN</span></a></li>'
    if TELEPHONE:
        contact_li += f'<li><a href="tel:{TELEPHONE.replace(" ", "")}">{I["phone"]}<span><small>Téléphone</small>{TELEPHONE}</span></a></li>'

    body = f'''{header(R)}
<main id="contenu">

<!-- ===================== ACCUEIL ===================== -->
<section class="hero grid-bg" id="accueil" aria-labelledby="titre-hero">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Portfolio · Abidjan, Côte d’Ivoire</p>
      <h1 id="titre-hero">Léopold César<span class="surname">N’DIN</span></h1>
      <p class="role">Ingénieur Travaux Publics <span>/ Concepteur BIM</span></p>
      <p class="pitch">Je transforme des plans d’exécution en méthodes de chantier claires et sûres. Sur la Ligne 1 du Métro d’Abidjan, je prépare le phasage des ouvrages en 2D/3D et j’utilise le calcul probabiliste et la programmation pour éclairer les choix de construction.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#projets">Voir mes projets {I["arrow"]}</a>
        <a class="btn" href="{CV_PDF}" download="CV_Leopold_Cesar_NDIN.pdf">{I["download"]} Télécharger le CV</a>
        <a class="btn btn-ghost" href="#contact">Me contacter</a>
      </div>
      <div class="hero-meta">
        <span><i class="status-dot" aria-hidden="true"></i> Ingénieur méthodes — SICMA / Bouygues TP</span>
        <span>ESTP — INPHB (CTI)</span>
      </div>
    </div>
    <figure class="hero-figure" style="margin:0">
      {HERO_SVG}
      <figcaption class="cartouche"><span>Dessin</span><span>Schéma de principe</span><span>Auteur</span><span>L. C. N’DIN</span></figcaption>
    </figure>
  </div>
</section>

<div class="container">
  <div class="stats" role="list">
    <div class="stat reveal" role="listitem"><b>37,4<em> km</em></b><span>de métro aérien — le projet sur lequel je travaille</span></div>
    <div class="stat reveal" role="listitem"><b>4</b><span>expériences terrain depuis 2023 (routes, assainissement, viaduc)</span></div>
    <div class="stat reveal" role="listitem"><b>6</b><span>plans méthodes présentés dans ce portfolio</span></div>
    <div class="stat reveal" role="listitem"><b>Bac<em>+5</em></b><span>Ingénieur Travaux Publics, diplôme accrédité CTI</span></div>
  </div>
</div>

<!-- ===================== PROFIL ===================== -->
<section class="section" id="profil" aria-labelledby="titre-profil">
  <div class="container">
    <div class="section-head reveal">
      <p class="axis"><i>01</i> Profil</p>
      <div><h2 id="titre-profil">Entre le bureau d’études et le chantier</h2></div>
    </div>
    <div class="about">
      <figure class="portrait reveal" style="margin:0">
        <span class="corner tl" aria-hidden="true"></span><span class="corner tr" aria-hidden="true"></span>
        <img src="assets/img/cesar-ndin-portrait.webp" width="358" height="512" alt="Portrait de Léopold César N’DIN en costume" loading="lazy">
        <figcaption><span>L. C. N’DIN</span><span>Ing. TP</span></figcaption>
      </figure>
      <div class="about-text reveal">
        <p class="lead">Ingénieur des Travaux Publics, je combine <em>rigueur technique</em> et <em>sens de l’innovation</em> pour améliorer la qualité et l’efficacité des projets.</p>
        <p>Formé à l’École Supérieure des Travaux Publics de l’INPHB (Yamoussoukro), j’ai construit mon parcours sur le terrain : suivi de travaux routiers et d’assainissement, puis préfabrication et pose des dalles du viaduc de la Ligne 1 du Métro d’Abidjan. J’y suis aujourd’hui ingénieur méthodes : je réalise les plans méthodes à partir des plans d’exécution, je les présente aux équipes et j’en suis la mise en place sur les chantiers.</p>
        <p>En parallèle, je développe des compétences en conception BIM, en calcul de structures et en outils numériques : mon projet de fin d’études s’appuie sur un programme Python de simulation Monte-Carlo pour éclairer un choix de méthode de construction.</p>
        <dl class="facts">
          <div><dt>Poste actuel</dt><dd>Ingénieur méthodes — SICMA</dd></div>
          <div><dt>Basé à</dt><dd>Abidjan, Côte d’Ivoire</dd></div>
          <div><dt>Langues</dt><dd>Français (natif) · Anglais (B1)</dd></div>
          <div><dt>Mobilité</dt><dd>Permis B</dd></div>
        </dl>
        <ul class="quals" aria-label="Principales qualifications">
          <li>Élaboration et suivi de plans méthodes</li>
          <li>Réalisation de maquettes BIM</li>
          <li>Étude de structures</li>
          <li>Planification, suivi et coordination de travaux d’infrastructures</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ===================== PARCOURS ===================== -->
<section class="section alt" id="parcours" aria-labelledby="titre-parcours">
  <div class="container">
    <div class="section-head reveal">
      <p class="axis"><i>02</i> Parcours</p>
      <div><h2 id="titre-parcours">Expériences et formation</h2><p>Du terrassement routier au viaduc du métro : un parcours construit sur le chantier.</p></div>
    </div>
    <div class="tl-wrap">
      <div>
        <p class="tl-title">Expérience professionnelle</p>
        <ol class="timeline">
          <li class="tl-item current reveal">
            <span class="tl-date">30 oct. 2025 — en cours</span><span class="badge">Actuel</span>
            <h3>Ingénieur Méthodes</h3>
            <p class="tl-org">SICMA — Société Ivoirienne de Construction du Métro d’Abidjan · Bouygues Travaux Publics</p>
            <ul>
              <li>Réalisation de plans méthodes à partir de plans d’exécution</li>
              <li>Présentation et suivi de la mise en place des plans sur les chantiers</li>
              <li>Visites sécurité et qualité pendant la réalisation des travaux</li>
            </ul>
          </li>
          <li class="tl-item reveal">
            <span class="tl-date">4 mars — 4 sept. 2025</span>
            <h3>Stagiaire Conducteur Travaux</h3>
            <p class="tl-org">SICMA · Bouygues Travaux Publics</p>
            <ul>
              <li>Procédures pour la préfabrication des dalles du viaduc</li>
              <li>Planning de production sous contraintes (transport, clavage, pose de dalles…)</li>
              <li>Contrôle des travaux ; commande et réception de matériels et matériaux</li>
            </ul>
          </li>
          <li class="tl-item reveal">
            <span class="tl-date">22 juin — 20 août 2024</span>
            <h3>Stagiaire Ingénieur Travaux</h3>
            <p class="tl-org">Smart Business Holding (SBH)</p>
            <ul>
              <li>Dimensionnement d’un système d’assainissement autonome et individuel</li>
              <li>Plans d’implantation du système ; suivi et contrôle des travaux</li>
              <li>Gestion des matériaux</li>
            </ul>
          </li>
          <li class="tl-item reveal">
            <span class="tl-date">30 juil. — 10 sept. 2023</span>
            <h3>Stagiaire Ingénieur Travaux</h3>
            <p class="tl-org">Smart Business Holding (SBH)</p>
            <ul>
              <li>Suivi de travaux routiers</li>
              <li>Gestion du transport de matériaux</li>
              <li>Détermination des quantités de matériaux en terrassement</li>
            </ul>
          </li>
        </ol>
      </div>
      <div>
        <p class="tl-title">Formation</p>
        <ol class="timeline">
          <li class="tl-item reveal">
            <span class="tl-date">2022 — 2025</span>
            <h3>Ingénieur Travaux Publics</h3>
            <p class="tl-org">École Supérieure des Travaux Publics (ESTP) — Institut National Polytechnique Félix Houphouët-Boigny (INPHB), Yamoussoukro · Accrédité CTI</p>
          </li>
          <li class="tl-item reveal">
            <span class="tl-date">2022</span>
            <h3>Programme d’anglais</h3>
            <p class="tl-org">Sunyani Technical University (Ghana)</p>
          </li>
          <li class="tl-item reveal">
            <span class="tl-date">2020 — 2022</span>
            <h3>Classes préparatoires MPSI / MP</h3>
            <p class="tl-org">CPGE de l’INPHB, Yamoussoukro</p>
          </li>
          <li class="tl-item reveal">
            <span class="tl-date">2020</span>
            <h3>Baccalauréat série C</h3>
            <p class="tl-org">Lycée Konan Camille d’Adiaké</p>
          </li>
        </ol>
      </div>
    </div>
  </div>
</section>

<!-- ===================== COMPÉTENCES ===================== -->
<section class="section" id="competences" aria-labelledby="titre-competences">
  <div class="container">
    <div class="section-head reveal">
      <p class="axis"><i>03</i> Compétences</p>
      <div><h2 id="titre-competences">Ce que je sais faire, et où le voir</h2><p>Pas de jauges ni de pourcentages : chaque domaine renvoie au projet qui le démontre.</p></div>
    </div>
    <div class="skills">
      <article class="skill-card reveal">
        <div class="ico">{I["cone"]}</div>
        <h3>Méthodes &amp; travaux</h3>
        <ul><li>Plans méthodes et phasage 2D/3D</li><li>Suivi de conformité, visites sécurité et qualité</li><li>Procédures de préfabrication</li><li>Quantités, commandes et réception de matériaux</li></ul>
        <a class="proof" href="projets/metro-abidjan-plans-methodes.html">Voir : plans méthodes du métro →</a>
      </article>
      <article class="skill-card reveal">
        <div class="ico">{I["cube"]}</div>
        <h3>BIM &amp; modélisation</h3>
        <ul><li>Maquettes BIM et plans 2D/3D</li><li>Rendus réalistes</li></ul>
        <div class="chips"><span class="chip steel">Revit</span><span class="chip steel">Enscape</span><span class="chip steel">NavisWorks</span><span class="chip steel">AutoCAD</span><span class="chip steel">SketchUp</span><span class="chip steel">FreeCAD</span></div>
        <a class="proof" href="projets/batiment-habitation.html">Voir : bâtiment d’habitation →</a>
      </article>
      <article class="skill-card reveal">
        <div class="ico">{I["beam"]}</div>
        <h3>Calcul de structures</h3>
        <ul><li>Dimensionnement des éléments porteurs</li><li>Rédaction de note de calcul</li><li>Dimensionnement d’assainissement autonome</li></ul>
        <div class="chips"><span class="chip steel">Robot Structural Analysis</span></div>
        <a class="proof" href="projets/batiment-habitation.html#calculs">Voir : modèle Robot →</a>
      </article>
      <article class="skill-card reveal">
        <div class="ico">{I["chart"]}</div>
        <h3>Planification &amp; décision</h3>
        <ul><li>Planning de production sous contraintes</li><li>Analyses probabilistes PERT et Monte-Carlo</li><li>Analyse multicritère Fuzzy AHP</li></ul>
        <div class="chips"><span class="chip steel">Microsoft Project</span></div>
        <a class="proof" href="projets/pfe-aide-decision-dalle-viaduc.html">Voir : projet de fin d’études →</a>
      </article>
      <article class="skill-card reveal">
        <div class="ico">{I["code"]}</div>
        <h3>Programmation &amp; données</h3>
        <ul><li>Simulation Monte-Carlo en Python</li><li>Tableaux de bord et analyse de données</li></ul>
        <div class="chips"><span class="chip steel">Python</span><span class="chip steel">C#</span><span class="chip steel">VBA</span><span class="chip steel">Power BI</span><span class="chip steel">Excel</span></div>
        <a class="proof" href="projets/pfe-aide-decision-dalle-viaduc.html#outil">Voir : programme Monte-Carlo →</a>
      </article>
      <article class="skill-card reveal">
        <div class="ico">{I["globe"]}</div>
        <h3>Langues &amp; savoir-être</h3>
        <ul><li>Français — langue maternelle</li><li>Anglais — niveau B1 (test elAo)</li></ul>
        <div class="chips"><span class="chip">Rigueur</span><span class="chip">Prise d’initiative</span><span class="chip">Esprit d’équipe</span><span class="chip">Autonomie</span><span class="chip">Leadership</span><span class="chip">Sens du détail</span><span class="chip">Adaptabilité</span><span class="chip">Ouverture d’esprit</span></div>
      </article>
    </div>
    <div class="soft reveal">
      <div><h3>Centres d’intérêt</h3><div class="chips"><span class="chip">BIM</span><span class="chip">Musique</span><span class="chip">Dessin</span></div></div>
      <div><h3>Sport</h3><div class="chips"><span class="chip">Athlétisme</span><span class="chip">Volley-ball</span><span class="chip">Natation</span></div></div>
    </div>
  </div>
</section>

<!-- ===================== PROJETS ===================== -->
<section class="section alt" id="projets" aria-labelledby="titre-projets">
  <div class="container">
    <div class="section-head reveal">
      <p class="axis"><i>04</i> Projets</p>
      <div><h2 id="titre-projets">Réalisations</h2><p>Chaque projet est présenté comme une étude de cas : contexte, démarche, outils, livrables.</p></div>
    </div>
    <div class="filters" role="group" aria-label="Filtrer les projets">
      <button class="filter" data-filter="tous" aria-pressed="true">Tous</button>
      <button class="filter" data-filter="methodes" aria-pressed="false">Méthodes chantier</button>
      <button class="filter" data-filter="decision" aria-pressed="false">Aide à la décision</button>
      <button class="filter" data-filter="conception" aria-pressed="false">Conception &amp; calcul</button>
    </div>
    <div class="projects">{"".join(cards)}
    </div>
  </div>
</section>

<!-- ===================== CV ===================== -->
<section class="section" id="cv" aria-labelledby="titre-cv">
  <div class="container">
    <div class="section-head reveal">
      <p class="axis"><i>05</i> CV</p>
      <div><h2 id="titre-cv">Mon CV en un clic</h2></div>
    </div>
    <div class="cv-block reveal">
      <a class="cv-thumb" href="{CV_PDF}" target="_blank" rel="noopener" aria-label="Ouvrir le CV au format PDF dans un nouvel onglet">
        <img src="assets/img/cv-apercu.webp" width="720" height="1018" alt="Aperçu de la première page du CV de Léopold César N’DIN" loading="lazy">
      </a>
      <div class="cv-info">
        <h3>Curriculum vitæ — Léopold César N’DIN</h3>
        <p>Formation, expériences, projets et logiciels en deux pages. Le PDF en libre téléchargement est une <strong>version de présentation</strong>, sans numéro de téléphone. Le CV complet est envoyé sur demande.</p>
        <div class="cv-actions">
          <a class="btn btn-primary" href="{CV_PDF}" download="CV_Leopold_Cesar_NDIN.pdf">{I["download"]} Version de présentation (PDF)</a>
          <a class="btn" href="#contact" data-objet="Demande de CV complet">{I["mail"]} Demander le CV complet</a>
          <a class="btn" href="{CV_PDF}" target="_blank" rel="noopener">{I["eye"]} Consulter en ligne</a>
        </div>
        <div class="qr">
          <img src="assets/img/qr-portfolio.svg" width="96" height="96" alt="QR code menant à ce portfolio">
          <p><strong>QR code du portfolio</strong>Scannez-le pour ouvrir ce site depuis un téléphone : il figure aussi sur mon CV papier.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===================== CONTACT ===================== -->
<section class="section alt" id="contact" aria-labelledby="titre-contact">
  <div class="container">
    <div class="section-head reveal">
      <p class="axis"><i>06</i> Contact</p>
      <div><h2 id="titre-contact">Travaillons ensemble</h2><p>Un poste, une mission, une collaboration ? Écrivez-moi.</p></div>
    </div>
    <div class="contact">
      <div class="reveal">
        <ul class="contact-list">
          <li><a href="mailto:{EMAIL}">{I["mail"]}<span><small>E-mail</small>{EMAIL}</span></a></li>
          {contact_li}
          <li><div>{I["pin"]}<span><small>Localisation</small>Abidjan, Côte d’Ivoire</span></div></li>
        </ul>
        <div class="avail"><p class="eyebrow" style="margin-bottom:10px">Ouvert aux opportunités</p><p>Postes en méthodes, travaux ou BIM, missions en free-lance et collaborations sur des projets d’infrastructures, en Côte d’Ivoire comme à l’international.</p><a class="btn btn-sm" href="#contact" data-objet="Demande de CV complet">{I["mail"]} Demander mon CV complet</a></div>
      </div>
      <form class="form reveal" id="contact-form" data-email="{EMAIL}" data-endpoint="{FORMSPREE}" novalidate>
        <div class="row">
          <div class="field"><label for="f-nom">Nom complet *</label><input id="f-nom" name="nom" autocomplete="name" required></div>
          <div class="field"><label for="f-mail">E-mail *</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="row">
          <div class="field"><label for="f-org">Entreprise / organisation</label><input id="f-org" name="organisation" autocomplete="organization"></div>
          <div class="field"><label for="f-obj">Objet</label>
            <select id="f-obj" name="objet"><option>Opportunité d’emploi</option><option>Demande de CV complet</option><option>Mission / free-lance</option><option>Collaboration</option><option>Autre</option></select></div>
        </div>
        <div class="field"><label for="f-msg">Message *</label><textarea id="f-msg" name="message" required></textarea></div>
        <div class="hp" aria-hidden="true"><label>Ne pas remplir <input name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
        <button class="btn btn-primary" type="submit">{I["mail"]} {"Envoyer le message" if FORMSPREE else "Préparer l’e-mail"}</button>
        <p class="form-note">{"Votre message m’est transmis directement." if FORMSPREE else "Ce bouton ouvre votre messagerie avec le message prérempli : rien n’est envoyé sans votre action."}</p>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
</main>
'''
    return h + body + footer(R)

# ------------------------------------------------------------------ pages projet
def gallery(items, R, plan=False, wide=False):
    out = []
    for path, alt in items:
        m = MANIFEST[path]
        thumb = img(path, alt, sizes="(max-width: 700px) 50vw, 300px").replace("{R}", R)
        out.append(f'<button type="button" class="{"plan" if plan else ""}" data-full="{R}assets/img/projets/{path}.webp" data-caption="{esc(alt)}" aria-label="Agrandir : {esc(alt)}"><figure style="margin:0;height:100%">{thumb}<figcaption>{esc(alt)}</figcaption></figure></button>')
    return f'<div class="gallery{" wide" if wide else ""}">{"".join(out)}</div>'

def plate(no, title, text, plans, photos, R):
    p = f'<div class="plate reveal"><div class="plate-head"><span class="no">PLANCHE {no:02d}</span><h3>{esc(title)}</h3>{f"<p>{text}</p>" if text else ""}</div>'
    if plans: p += '<p class="gal-label">Plan méthode</p>' + gallery(plans, R, plan=True, wide=True)
    if photos: p += '<p class="gal-label">Sur le chantier</p>' + gallery(photos, R)
    return p + '</div>'

def case_page(p, sections, R="../"):
    idx = PROJETS.index(p)
    prev = PROJETS[idx - 1]; nxt = PROJETS[(idx + 1) % len(PROJETS)]
    jsonld = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"CreativeWork","name":"%s","description":"%s","author":{"@type":"Person","name":"Léopold César N’DIN","url":"%s"},"url":"%sprojets/%s.html"}</script>' % (p["titre"], p["description"], SITE_URL, SITE_URL, p["slug"])
    h = head(f'{p["court"]} — Léopold César N’DIN', p["description"], f'projets/{p["slug"]}.html', R, jsonld=jsonld)
    spec = "".join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in p["spec"])
    toc = "".join(f'<li><a href="#{sid}">{esc(t)}</a></li>' for sid, t, _ in sections)
    secs = "".join(f'<section class="case-section" id="{sid}" aria-labelledby="h-{sid}"><h2 id="h-{sid}"><small>{i+1:02d}</small>{esc(t)}</h2>{c}</section>' for i, (sid, t, c) in enumerate(sections))
    cover = video_html(p, R) if p.get("video") else img(p["couverture"][0], p["couverture"][1], lazy=False, sizes="100vw", thumb=False).replace("{R}", R)
    chips = "".join(f'<span class="chip steel">{esc(t)}</span>' for t in p["outils"])
    body = f'''{header(R, home=False)}
<main id="contenu">
  <section class="case-hero grid-bg">
    <div class="container">
      <p class="crumbs"><a href="{R}index.html">Accueil</a> / <a href="{R}index.html#projets">Projets</a> / {p["num"]}</p>
      <p class="eyebrow">{esc(p["meta"])}</p>
      <h1>{esc(p["titre"])}</h1>
      <p class="summary">{esc(p["resume"])}</p>
      <div class="chips" style="margin-top:20px">{chips}</div>
      <dl class="spec">{spec}</dl>
      <figure class="case-cover" style="margin-left:0;margin-right:0">{cover}</figure>
    </div>
  </section>
  <div class="container case-layout">
    <nav class="toc" aria-label="Sommaire du projet"><p>Sommaire</p><ol>{toc}</ol></nav>
    <div>{secs}</div>
  </div>
  <div class="container">
    <nav class="case-nav" aria-label="Autres projets">
      <a href="{prev["slug"]}.html"><small>← Projet précédent</small><strong>{esc(prev["court"])}</strong></a>
      <a class="next" href="{nxt["slug"]}.html"><small>Projet suivant →</small><strong>{esc(nxt["court"])}</strong></a>
    </nav>
  </div>
</main>
'''
    return h + body + footer(R, home=False)

def page_metro():
    p = PROJETS[0]; R = "../"; P = "metro-abidjan-plans-methodes/"
    plates = [
      plate(1, "Phasage du terrassement en zone marécageuse de la culée Cb, avec puisard",
            "Plan méthode du phasage de terrassement et de l’épuisement des eaux par puisard, puis suivi des travaux.",
            [(P+"terrassement-plan-1", "Vue en plan et coupe du terrassement de la culée Cb"), (P+"terrassement-plan-2", "Phasage du terrassement avec engins et puisard"), (P+"terrassement-puisard", "Détail des puisards définitif et temporaire")],
            [(P+"terrassement-chantier-1", "Fouille blindée de la culée Cb et têtes de pieux"), (P+"terrassement-chantier-2", "Vue d’ensemble de la fouille étayée"), (P+"terrassement-chantier-3", "Fond de fouille et têtes de pieux")], R),
      plate(2, "Phasage du ferraillage de la culée Cb",
            "Décomposition du ferraillage en phases successives — lit par lit de la nappe inférieure — avec vue 3D, vue en plan et coupe pour chaque phase.",
            [(P+"ferraillage-phase-1", "Phase 1 — 1er lit de la nappe inférieure"), (P+"ferraillage-phase-3", "Phase 3 — 2e lit de la nappe inférieure"), (P+"ferraillage-phase-5", "Phase 5 — 3e lit de la nappe inférieure")],
            [(P+"ferraillage-chantier-1", "Mise en place des armatures en fond de fouille"), (P+"ferraillage-chantier-2", "Équipes sur la nappe d’armatures"), (P+"ferraillage-chantier-3", "Vue de la culée en cours de ferraillage")], R),
      plate(3, "Pose des dalles préfabriquées du viaduc à l’aide d’un SPMT",
            "Phasage de l’approche, du levage, de la rotation et de la pose des dalles préfabriquées acheminées par SPMT (transporteur modulaire automoteur).",
            [(P+"spmt-phasage-1", "Phases 1 à 3 : approche, levage et rotation de la dalle"), (P+"spmt-phasage-2", "Phases 4 et 5 : avancement de la grue et pose de la dalle")],
            [(P+"spmt-chantier-1", "Dalles préfabriquées posées sur le tablier"), (P+"spmt-chantier-2", "Levage d’une dalle préfabriquée sur le viaduc")], R),
      plate(4, "Pose de la dernière travée P0 – Cb du viaduc",
            "Plan méthode du levage de la travée : implantation de la grue, rayons de travail et élévation de la manœuvre.",
            [(P+"travee-levage-plan-1", "Vue en plan du levage de la travée"), (P+"travee-levage-plan-2", "Vue en plan — position finale de la grue"), (P+"travee-levage-elevation", "Vue en élévation du levage de la travée")],
            [(P+"travee-chantier-1", "Levage de nuit de la travée"), (P+"travee-chantier-2", "Travée suspendue avant pose"), (P+"travee-chantier-3", "Grue mobile en position de levage")], R),
      plate(5, "Coffrage du voile de la culée du PRA9",
            "Implantation des tours d’étaiement, des poutres primaires et secondaires et du coffrage du voile.",
            [(P+"pra9-voile-poutres", "Vue en plan — poutres primaires et secondaires"), (P+"pra9-voile-tours", "Coupe et élévation — implantation des tours et poutres"), (P+"pra9-voile-coffrage-plan", "Vue en plan — coffrage du voile"), (P+"pra9-voile-coffrage-coupe", "Coupe — coffrage et étaiement du voile")],
            [], R),
      plate(6, "Coffrage du piédroit et du tablier du PRA9 existant",
            "Séquence de mise en place du coffrage et de l’étaiement du tablier et du piédroit.",
            [(P+"pra9-tablier-sequence", "Vue en plan — séquence de levage"), (P+"pra9-tablier-etaiement", "Principe d’étaiement du tablier"), (P+"pra9-piedroit-coupe", "Coupe longitudinale — coffrage du piédroit")],
            [(P+"pra9-chantier-1", "Mise en place du coffrage du tablier"), (P+"pra9-chantier-2", "Coffrage et étaiement du piédroit")], R),
    ]
    sections = [
      ("contexte", "Contexte", "<p>La Ligne 1 du Métro d’Abidjan est un projet de conception, construction et exploitation de <strong>37,4 km de métro aérien</strong> reliant l’aéroport Félix Houphouët-Boigny, au sud, à Anyama, au nord. Sa vocation est multimodale : des correspondances avec les bus, les taxis, les voitures et les modes doux doivent faciliter le transport urbain dans une ville marquée par des engorgements constants.</p>"),
      ("role", "Mon rôle", "<p>Au sein de la SICMA (Bouygues Travaux Publics), j’occupe le poste d’<strong>ingénieur méthodes</strong> :</p><ul><li><strong>Réalisation de plans méthodes 2D/3D</strong> à partir des plans d’exécution, pour faciliter la réalisation des ouvrages ;</li><li><strong>Présentation et suivi de la conformité</strong> des travaux réalisés par rapport aux plans méthodes ;</li><li><strong>Visites sécurité</strong> sur les différents chantiers.</li></ul>"),
      ("demarche", "Démarche", '<ol class="steps"><li><strong>Lire</strong>Analyse des plans d’exécution et des contraintes du site.</li><li><strong>Phaser</strong>Découpage de l’ouvrage en phases, choix des moyens (grues, SPMT, étaiements, puisards).</li><li><strong>Dessiner</strong>Plans méthodes 2D/3D : vues en plan, coupes, élévations, notes de sécurité.</li><li><strong>Accompagner</strong>Présentation aux équipes et suivi de la mise en place sur le chantier.</li></ol>'),
      ("realisations", "Réalisations — du plan au chantier", '<p>Six plans méthodes, chacun mis en regard de photos de leur mise en œuvre. Cliquez sur une image pour l’agrandir.</p>' + "".join(plates)),
      ("outils", "Outils et compétences mobilisés", '<div class="chips"><span class="chip steel">Revit</span><span class="chip steel">AutoCAD</span><span class="chip steel">Gestion BIM</span><span class="chip">Phasage de travaux</span><span class="chip">Levage et manutention</span><span class="chip">Coffrage et étaiement</span><span class="chip">Sécurité chantier</span></div>'),
    ]
    return case_page(p, sections)

def page_pfe():
    p = PROJETS[1]; R = "../"; P = "pfe-aide-decision-dalle-viaduc/"
    sections = [
      ("contexte", "Contexte", "<p>Projet de fin d’études mené en 2025 entre l’INPHB et la SICMA, pendant mon stage de conducteur de travaux sur le viaduc de la <strong>Ligne 1 du Métro d’Abidjan</strong>. Le sujet : <em>proposer un processus d’aide à la décision dans le choix des méthodes de réalisation de la dalle d’un ouvrage d’art mixte</em>.</p>"),
      ("probleme", "Problématique", "<p>Pour réaliser la dalle d’un ouvrage d’art mixte, plusieurs méthodes reconnues existent. Le choix doit être fait sous diverses contraintes — <strong>temps, coût, sécurité…</strong> — et en tenant compte de l’incertitude des durées de chantier.</p><p>Deux méthodes ont été comparées :</p><ul><li>la <strong>préfabrication intégrale</strong> de la dalle ;</li><li>les <strong>prédalles collaborantes</strong>.</li></ul>"),
      ("demarche", "Démarche", '<ol class="steps"><li><strong>Analyse des variantes</strong>Planning de chaque méthode étudié par PERT et simulation de Monte-Carlo ; autres critères : retours d’expérience, dimensionnement…</li><li><strong>Analyse multicritère</strong>Pondération et comparaison des variantes par la méthode Fuzzy AHP.</li><li><strong>Étude complète</strong>Développement détaillé de la solution retenue.</li></ol>' + gallery([(P+"processus-decision", "Processus établi pour le choix optimal de la méthode de réalisation de la dalle")], R, plan=True, wide=True)),
      ("outil", "Outil développé : simulation Monte-Carlo en Python", "<p>J’ai écrit un programme Python qui simule le planning d’un réseau de tâches : les durées de chaque tâche suivent une loi <strong>Bêta-PERT</strong> (durées optimiste, probable et pessimiste), les tâches sont ordonnées par un <strong>tri topologique</strong> (algorithme de Kahn), puis des milliers de tirages produisent la distribution de la durée totale du projet.</p><p>Les résultats sont lus sur l’histogramme des durées simulées et sur la courbe cumulative, qui donne la probabilité de terminer avant une échéance donnée.</p>" + gallery([(P+"code-python-monte-carlo", "Extrait du programme Python de simulation Monte-Carlo (Bêta-PERT)"), (P+"monte-carlo-resultats", "Histogramme des durées simulées et courbe cumulative (CDF)")], R, plan=True, wide=True)),
      ("resultat", "Résultat : la préfabrication intégrale est retenue", '<p>À l’issue de toutes les analyses et de la méthode Fuzzy AHP, la <strong>préfabrication intégrale</strong> obtient le meilleur score final. C’est la méthode retenue pour la réalisation de la dalle.</p><div class="scores" role="img" aria-label="Score final Fuzzy AHP : préfabrication intégrale 54 %, prédalles collaborantes 46 %"><div class="score win"><span class="score-label">Préfabrication intégrale <em>retenue</em></span><span class="score-bar"><i style="width:54%"></i></span><b>54 %</b></div><div class="score"><span class="score-label">Prédalles collaborantes</span><span class="score-bar"><i style="width:46%"></i></span><b>46 %</b></div></div>'),
      ("competences", "Compétences démontrées", '<div class="chips"><span class="chip steel">Python (NumPy, Matplotlib)</span><span class="chip steel">PERT</span><span class="chip steel">Monte-Carlo</span><span class="chip steel">Fuzzy AHP</span><span class="chip">Méthodes de réalisation de dalles d’ouvrage d’art mixte</span><span class="chip">Optimisation</span></div><p style="margin-top:18px">Pendant ce même stage, j’ai aussi rédigé des procédures pour la préfabrication des dalles du viaduc et établi un planning de production sous contraintes (transport, clavage, pose de dalles…).</p>'),
    ]
    return case_page(p, sections)

def page_bat():
    p = PROJETS[2]; R = "../"; P = "batiment-habitation/"
    sections = [
      ("contexte", "Contexte", "<p>Projet personnel mené en 2026 : accompagner la conception d’un bâtiment d’habitation, puis dimensionner ses éléments porteurs et produire la note de calcul. Il me permet de pratiquer toute la chaîne, de l’esquisse au calcul.</p>"),
      ("plans", "Plans 2D et coupes", gallery([(P+"coupe-1", "Coupe du bâtiment"), (P+"coupe-2", "Coupe longitudinale"), (P+"plan-masse", "Plan de masse"), (P+"plan-electricite", "Plan d’électricité d’un niveau")], R, plan=True)),
      ("maquette", "Maquette 3D", gallery([(P+"maquette-3d-1", "Vue 3D en coupe du bâtiment"), (P+"maquette-3d-2", "Vue 3D du bâtiment dans sa rue"), (P+"maquette-revit", "Maquette numérique dans Revit")], R, plan=True)),
      ("rendus", "Rendus réalistes", "<p>Rendus et visite virtuelle (vidéo en tête de page) réalisés avec <strong>Enscape</strong>.</p>" + gallery([(P+"rendu-facade-nuit", "Rendu de nuit de la façade"), (P+"rendu-exterieur-revit", "Rendu extérieur paramétré dans Revit"), (P+"rendu-salon", "Rendu du salon"), (P+"rendu-piscine", "Rendu de la piscine intérieure"), (P+"rendu-couloir", "Rendu d’un couloir")], R)),
      ("calculs", "Calcul de structure", "<p>Modélisation de l’ossature dans <strong>Robot Structural Analysis</strong>, analyse des sollicitations (moments dans les poutres, cartographies dans les dalles et les voiles) et dimensionnement des éléments porteurs, jusqu’aux fondations.</p>" + gallery([(P+"robot-modele-3d", "Modèle 3D de l’ossature dans Robot"), (P+"robot-moments-poutres", "Diagrammes de moments dans les poutres"), (P+"robot-cartographie-dalle", "Cartographie des moments dans une dalle"), (P+"robot-cartographie-voile", "Cartographie des efforts dans un voile"), (P+"robot-semelle", "Dimensionnement d’une semelle de fondation")], R, plan=True)),
      ("competences", "Compétences démontrées", '<div class="chips"><span class="chip steel">Revit</span><span class="chip steel">Enscape</span><span class="chip steel">Robot Structural Analysis</span><span class="chip">Conception 2D/3D</span><span class="chip">Conception BIM</span><span class="chip">Rendus réalistes</span><span class="chip">Dimensionnement</span><span class="chip">Note de calcul</span></div>'),
    ]
    return case_page(p, sections)

def page_404():
    R = "/"
    h = head("Page introuvable — Léopold César N’DIN", "Cette page n’existe pas ou a été déplacée.", "404.html", R)
    h = h.replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"')
    return h + header(R, home=False) + f'''<main id="contenu" class="grid-bg"><div class="container notfound"><div>
  <p class="code">ERREUR 404 · HORS EMPRISE</p>
  <h1>Cette page n’est pas sur le plan.</h1>
  <p>L’adresse demandée n’existe pas ou a été déplacée. Revenez à l’accueil pour retrouver mes projets.</p>
  <a class="btn btn-primary" href="{R}index.html">Retour à l’accueil {I["arrow"]}</a>
</div></div></main>''' + footer(R, home=False)

if __name__ == "__main__":
    (ROOT / "index.html").write_text(page_index(), encoding="utf-8")
    (ROOT / "projets").mkdir(exist_ok=True)
    (ROOT / "projets" / f"{PROJETS[0]['slug']}.html").write_text(page_metro(), encoding="utf-8")
    (ROOT / "projets" / f"{PROJETS[1]['slug']}.html").write_text(page_pfe(), encoding="utf-8")
    (ROOT / "projets" / f"{PROJETS[2]['slug']}.html").write_text(page_bat(), encoding="utf-8")
    (ROOT / "404.html").write_text(page_404(), encoding="utf-8")
    urls = ["", *[f"projets/{p['slug']}.html" for p in PROJETS]]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE_URL}{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    print("Site généré.")
