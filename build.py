#!/usr/bin/env python3
"""
Static site builder — shahidul-shabuz.github.io

One layout, one stylesheet, five pages. Nav and footer are defined once, here.
Run:  python3 build.py      →  writes dist/
"""

import os, re, shutil, datetime

ROOT   = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(ROOT, "static")
DIST   = os.path.join(ROOT, "dist")

# --------------------------------------------------------------------------
# Identity
# --------------------------------------------------------------------------
SITE        = "https://shahidul-shabuz.github.io"
NAME        = "Md Shahidul Islam Shabuz"
SHORT       = "Md Shahidul Islam Shabuz"   # display name — full form, as he uses it
ROLE        = "Assistant Professor, Computer Science and Engineering, RSTU"
SCHOLAR     = "https://scholar.google.com/citations?user=VDtX90sAAAAJ&hl=en"
ORCID       = "https://orcid.org/0009-0008-8271-888X"
ORCID_ID    = "0009-0008-8271-888X"
GITHUB      = "https://github.com/shahidul-shabuz"
LINKEDIN    = "https://www.linkedin.com/in/shahidul-shabuz/"
EMAIL       = "shahidul.shabuz@gmail.com"
EMAIL_UNI   = "mshahidul@rstu.edu.bd"
DOI_URL     = "https://doi.org/10.3390/a19080615"
PAPER_URL   = "https://www.mdpi.com/1999-4893/19/8/615"
PAPER_PDF   = "https://www.mdpi.com/1999-4893/19/8/615/pdf"
BUILT       = datetime.date.today().isoformat()

NAV = [
    ("index.html",        "Home"),
    ("research.html",     "Research"),
    ("publications.html", "Publications"),
    ("teaching.html",     "Teaching"),
    ("cv.html",           "CV"),
]

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=JetBrains+Mono:wght@400;500&"
         "family=Public+Sans:wght@400;500;600&"
         "family=Spectral:ital,wght@0,400;0,600;1,400&display=swap")

# --------------------------------------------------------------------------
# Layout
# --------------------------------------------------------------------------

def nav_html(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'      <a href="{href}"{cur}>{label}</a>')
    return "\n".join(out)


def header(current):
    return f"""<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="shell header-bar">
    <a class="wordmark" href="index.html"><span class="given">Md</span> Shahidul Islam Shabuz</a>

    <nav class="nav" id="nav" aria-label="Primary">
{nav_html(current)}
    </nav>

    <div class="header-tools">
      <button class="icon-btn" id="theme-btn" type="button" aria-label="Switch theme" title="Switch theme">&#9790;</button>
      <button class="icon-btn nav-btn" id="nav-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav">&#9776;</button>
    </div>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="shell footer-grid">
    <div class="footer-note">
      &copy; <span id="year">2026</span> {NAME}<br>
      Department of CSE, Rajshahi Science and Technology University<br>
      Natore, Rajshahi, Bangladesh
    </div>
    <nav aria-label="Footer">
      <a href="research.html">Research</a>
      <a href="publications.html">Publications</a>
      <a href="teaching.html">Teaching</a>
      <a href="cv.html">CV</a>
      <a href="{SCHOLAR}" rel="noopener">Google Scholar</a>
      <a href="{GITHUB}" rel="noopener">GitHub</a>
      <a href="mailto:{EMAIL}">Email</a>
    </nav>
  </div>
</footer>"""


def jsonld():
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "%s",
  "alternateName": "Shahidul Islam Shabuz",
  "jobTitle": "Assistant Professor",
  "email": "mailto:%s",
  "url": "%s/",
  "image": "%s/assets/img/social-card.jpg",
  "worksFor": {
    "@type": "CollegeOrUniversity",
    "name": "Rajshahi Science and Technology University",
    "address": { "@type": "PostalAddress", "addressLocality": "Natore", "addressRegion": "Rajshahi", "addressCountry": "BD" }
  },
  "alumniOf": { "@type": "CollegeOrUniversity", "name": "Dhaka University of Engineering & Technology" },
  "knowsAbout": [
    "Computer Vision", "Attention Mechanisms", "Explainable Artificial Intelligence",
    "Medical Image Analysis", "Deep Learning", "Intelligent Transportation Systems"
  ],
  "sameAs": ["%s", "%s", "%s", "%s"]
}
</script>""" % (NAME, EMAIL_UNI, SITE, SITE, ORCID, SCHOLAR, GITHUB, LINKEDIN)


def document(page_file, title, description, body):
    """Wrap page body in the full HTML document."""
    canonical = f"{SITE}/" if page_file == "index.html" else f"{SITE}/{page_file}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="{NAME}">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="profile">
<meta property="og:site_name" content="{SHORT}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/social-card.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}/assets/img/social-card.jpg">

<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/css/site.css">
{jsonld()}
</head>
<body>
{header(page_file)}

<main id="main">
{body}
</main>

{FOOTER}
<script src="assets/js/site.js"></script>
</body>
</html>
"""

# --------------------------------------------------------------------------
# Shared fragments
# --------------------------------------------------------------------------

PAPER_TITLE = ("An Attention-Enhanced CNN with Explainable AI for Driver "
               "Behavior Detection in Intelligent Transportation Systems")

PAPER_AUTHORS = ('Abdullah Al Mamun, <b>Md Shahidul Islam Shabuz</b>, Md Nahidur Rahaman, '
                 'Khawja Imran Masud, Md. Biddut Hossain')

PAPER_VENUE = '<em>Algorithms</em> (MDPI), vol. 19, no. 8, art. 615 &middot; 23 July 2026'

PAPER_STATS = """<div class="stats">
  <div><b>99.48%</b><span>Mean accuracy</span></div>
  <div><b>122</b><span>Frames per second</span></div>
  <div><b>42.92M</b><span>Parameters</span></div>
  <div><b>5-fold</b><span>Stratified CV</span></div>
</div>"""

CONTACT_BAND = f"""<section class="band band-tint">
  <div class="shell">
    <div class="band-head">
      <h2>Contact</h2>
    </div>

    <div class="contact-grid">
      <a href="mailto:{EMAIL}">
        <span>Email</span><strong>{EMAIL}</strong>
      </a>
      <a href="mailto:{EMAIL_UNI}">
        <span>University email</span><strong>{EMAIL_UNI}</strong>
      </a>
      <a href="{SCHOLAR}" rel="noopener">
        <span>Google Scholar</span><strong>Publication record</strong>
      </a>
      <a href="{ORCID}" rel="noopener">
        <span>ORCID</span><strong>{ORCID_ID}</strong>
      </a>
      <a href="{GITHUB}" rel="noopener">
        <span>GitHub</span><strong>github.com/shahidul-shabuz</strong>
      </a>
      <a href="{LINKEDIN}" rel="noopener">
        <span>LinkedIn</span><strong>in/shahidul-shabuz</strong>
      </a>
      <div>
        <span>Based in</span><strong>Natore, Rajshahi, Bangladesh</strong>
      </div>
    </div>
  </div>
</section>"""

# --------------------------------------------------------------------------
# Page: Home
# --------------------------------------------------------------------------

HOME = f"""<section class="hero">
  <div class="shell hero-grid">
    <div>
      <h1>{SHORT}</h1>
      <p class="role">
        <b>Assistant Professor</b>, Department of Computer Science and Engineering,
        Rajshahi Science and Technology University
      </p>
      <p class="role last">
        M.Sc. candidate, Dhaka University of Engineering &amp; Technology,
        supervised by Prof. Dr. Momotaz Begum
      </p>

      <p class="thesis">
        Attention-based deep learning, with an emphasis on interpretability and
        on efficiency at deployment.
      </p>


      <div class="linkrow">
        <a class="chip chip-solid" href="research.html">Read the research</a>
        <a class="chip" href="{SCHOLAR}" rel="noopener">Google Scholar &#8599;</a>
        <a class="chip" href="cv.html">Curriculum vitae</a>
      </div>
    </div>

    <figure class="frame">
      <span class="frame-img">
        <span class="brk"></span>
        <picture>
          <source srcset="assets/img/profile.webp" type="image/webp">
          <img src="assets/img/profile.jpg" width="450" height="570"
               alt="Portrait of Md Shahidul Islam Shabuz">
        </picture>
      </span>
      <figcaption>Natore, Rajshahi<br>Bangladesh</figcaption>
    </figure>
  </div>
</section>

<section class="band">
  <div class="shell">
    <div class="band-head">
      <h2>Research</h2>
    </div>

    <div class="entries">

      <article class="entry">
        <div class="entry-meta"><b>2026</b>Journal article</div>
        <div class="entry-body">
          <h3>{PAPER_TITLE}</h3>
          <p>A multi-head attention CNN for driver distraction recognition, with
          Grad-CAM attribution showing that the network attends to hands, face and
          mobile device — the same evidence a human observer would use. Published in
          <em>Algorithms</em> (MDPI).</p>
          <div class="linkrow">
            <a class="chip" href="{DOI_URL}" rel="noopener">DOI 10.3390/a19080615</a>
            <a class="chip" href="publications.html">Details &amp; abstract</a>
          </div>
        </div>
      </article>

      <article class="entry">
        <div class="entry-meta"><b>2020&ndash;2021</b>B.Sc. thesis</div>
        <div class="entry-body">
          <h3>Brain tumor segmentation from MRI with convolutional networks</h3>
          <p>An end-to-end CNN pipeline — preprocessing, training and evaluation
          against reference annotations — for automatic segmentation of tumor
          regions in brain MRI. Supervised by Prof. Dr. Mohammod Abul Kashem at DUET.</p>
          <div class="linkrow">
            <a class="chip" href="assets/files/brain-tumor-segmentation-thesis.pdf">Thesis PDF</a>
            <a class="chip" href="research.html">Research overview</a>
          </div>
        </div>
      </article>

    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <div class="band-head">
      <h2>News</h2>
    </div>

    <div class="entries">
      <article class="entry">
        <div class="entry-meta"><b>Nov 2026</b></div>
        <div class="entry-body">
          <h3>M.Sc. coursework completed</h3>
          <p>Computer Science and Engineering, Dhaka University of Engineering &amp;
          Technology. CGPA 4.00 out of 4.00.</p>
        </div>
      </article>

      <article class="entry">
        <div class="entry-meta"><b>Aug 2026</b></div>
        <div class="entry-body">
          <h3>Selected for the JST Sakura Science Exchange Program</h3>
          <p>Nominated by the Department of Computer Science and Engineering at DUET
          for the JST Sakura Science Exchange Program 2026 at Shizuoka University,
          Japan &mdash; one of six M.Sc. students selected on academic record, research
          and publication experience, and fit with the host institution&rsquo;s research
          areas. The exchange visit is planned for February 2027.</p>
        </div>
      </article>

      <article class="entry">
        <div class="entry-meta"><b>Jul 2026</b></div>
        <div class="entry-body">
          <h3>Paper published in <em>Algorithms</em></h3>
          <p><em>Algorithms</em> 19(8), article 615, 23 July 2026. Open access &mdash;
          <a href="{DOI_URL}" rel="noopener">10.3390/a19080615</a>.
          <a href="publications.html">Full record</a>.</p>
        </div>
      </article>

      <article class="entry">
        <div class="entry-meta"><b>May 2026</b></div>
        <div class="entry-body">
          <h3>Supervised undergraduate project completed</h3>
          <p>BookCycleBD, a peer-to-peer marketplace for second-hand books, was
          completed and deployed by Md. Marzan Haque under my supervision.
          <a href="teaching.html">Project details</a>.</p>
        </div>
      </article>

    </div>
  </div>
</section>

{CONTACT_BAND}"""

# --------------------------------------------------------------------------
# Page: Research
# --------------------------------------------------------------------------

RESEARCH = f"""<section class="band">
  <div class="shell split">
    <div class="split-rail">
      <p class="eyebrow">Research statement</p>
      <h1>What I work on</h1>
      <ul class="split-index">
        <li><b>Focus</b>Interpretable, efficient deep vision for safety-critical decisions</li>
        <li><b>Domains</b>Driver monitoring &middot; medical image segmentation</li>
        <li><b>Methods</b>Attention-enhanced CNNs &middot; CNN segmentation &middot; Grad-CAM attribution</li>
      </ul>
    </div>

    <div class="measure">
      <p class="lede">My research is on attention-based deep learning for visual
      recognition, and on the methods that make such models auditable and efficient
      enough to be used outside a laboratory.</p>

      <p style="margin-top:1.6rem">Two things interest me in particular.</p>

      <h2 class="h-sub" style="margin:2rem 0 .6rem">What the model attends to</h2>
      <p>In our study of driver distraction, a multi-head attention CNN reached a mean
      accuracy of 99.48% over stratified five-fold cross-validation. I find the
      Grad-CAM attribution more informative than that figure: the maps concentrated on
      hands, face and mobile device, which are the regions a human observer would use.
      Attribution is one way to check whether a model has learned the task or the
      dataset.</p>

      <h2 class="h-sub" style="margin:2rem 0 .6rem">What that costs</h2>
      <p>The same model runs at 122 frames per second with 42.92 million parameters.
      I would like to understand that trade-off better &mdash; when attention and
      attribution can be added cheaply and when they cannot &mdash; because a method
      that needs large compute is available to fewer people.</p>

      <p style="margin-top:1.6rem">My undergraduate thesis addressed a related problem
      in medical imaging: segmenting tumor regions from brain MRI with convolutional
      networks. I would like to continue in this direction for doctoral study, on
      attention-based and hybrid CNN&ndash;Transformer architectures whose
      explanations are evaluated as carefully as their accuracy.</p>

      <p style="margin-top:1.6rem">Alongside this, my graduate coursework has covered
      sequence models &mdash; RNN, LSTM, encoder&ndash;decoder and Transformer
      architectures. The mathematical notes and implementations are
      <a href="{GITHUB}/MSc-DL-for-NLP" rel="noopener">on GitHub</a>.</p>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <div class="band-head">
      <h2>Projects</h2>
    </div>

    <article style="border-top:1px solid var(--rule); padding-top:32px">
      <p class="data muted">2026 &middot; Published in <em>Algorithms</em> (MDPI)</p>
      <h3 style="font-size:1.45rem; margin:.5rem 0 1rem">Explainable driver behavior
      detection with multi-head attention</h3>

      <div class="measure">
        <p><b>Problem.</b> Driver-monitoring systems that flag distraction need to be
        accurate and auditable at the same time: a system that cannot show why it
        raised an alert is hard to evaluate and hard to trust.</p>

        <p><b>Approach.</b> We combined a convolutional backbone with a multi-head
        attention module, so the network captures both local spatial detail and
        long-range dependencies in the driver's activities. Grad-CAM was then used to
        produce attribution maps over the input, and an ablation study with k-fold
        validation isolated what the attention mechanism actually contributed.</p>

        <p><b>Result.</b> On the State Farm Distracted Driver dataset, performance held
        up consistently across all ten distraction classes in precision, recall and F1,
        and the model stayed fast enough for real-time monitoring.</p>
      </div>

      {PAPER_STATS}

      <p class="data muted" style="margin-top:22px">{PAPER_AUTHORS}</p>

      <div class="linkrow" style="margin-top:18px">
        <a class="chip chip-solid" href="{PAPER_URL}" rel="noopener">Read the paper</a>
        <a class="chip" href="{DOI_URL}" rel="noopener">DOI 10.3390/a19080615</a>
        <a class="chip" href="{PAPER_PDF}" rel="noopener">PDF</a>
        <a class="chip" href="publications.html">Abstract &amp; BibTeX</a>
      </div>
    </article>

    <article style="border-top:1px solid var(--rule); margin-top:48px; padding-top:32px">
      <p class="data muted">2020&ndash;2021 &middot; B.Sc. thesis, DUET Gazipur</p>
      <h3 style="font-size:1.45rem; margin:.5rem 0 1rem">Brain tumor MRI segmentation
      using convolutional neural networks</h3>

      <div class="measure">
        <p><b>Problem.</b> Manual delineation of tumor regions in brain MRI is slow and
        varies between readers, which is what makes automatic segmentation worth
        pursuing.</p>

        <p><b>Approach.</b> I built the full pipeline: image preprocessing, a CNN-based
        segmentation model, training, and evaluation against reference annotations,
        supervised by Prof. Dr. Mohammod Abul Kashem.</p>

        <p><b>Continuity.</b> Segmentation in MRI and distraction recognition in a
        vehicle raise the same question: whether the reader can see what the model
        used to reach its answer. Hybrid CNN&ndash;Transformer segmentation is the
        direction I would like to take this next.</p>
      </div>

      <div class="linkrow" style="margin-top:22px">
        <a class="chip chip-solid" href="assets/files/brain-tumor-segmentation-thesis.pdf">Read the thesis</a>
      </div>
    </article>

    <div class="callout">
      <h4>Doctoral study</h4>
      <p>I am applying to PhD programs for Fall 2027. If anything above is close
      to what your group works on, I would be glad to hear from you —
      <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </div>
</section>"""

# --------------------------------------------------------------------------
# Page: Publications
# --------------------------------------------------------------------------

BIBTEX = """@article{mamun2026attention,
  author  = {Al Mamun, Abdullah and Shabuz, Md Shahidul Islam and
             Rahaman, Md Nahidur and Masud, Khawja Imran and Hossain, Md. Biddut},
  title   = {An Attention-Enhanced {CNN} with Explainable {AI} for Driver Behavior
             Detection in Intelligent Transportation Systems},
  journal = {Algorithms},
  volume  = {19},
  number  = {8},
  pages   = {615},
  year    = {2026},
  issn    = {1999-4893},
  doi     = {10.3390/a19080615},
  url     = {https://www.mdpi.com/1999-4893/19/8/615}
}"""

PUBLICATIONS = f"""<section class="band">
  <div class="shell">
    <p class="eyebrow">Publications</p>
    <h1>Peer-reviewed work</h1>
    <p class="lede measure" style="margin-top:1.4rem">
      Each entry links to the DOI and the full text. Citation counts and any newer
      items appear on <a href="{SCHOLAR}" rel="noopener">Google&nbsp;Scholar</a> and
      <a href="{ORCID}" rel="noopener">ORCID</a>.
    </p>

    <div style="margin-top:48px">
      <h2 class="eyebrow">Journal articles</h2>

      <article class="pub">
        <div class="pub-n">[1]</div>
        <div>
          <span class="tag">Published &middot; open access</span>
          <h3>{PAPER_TITLE}</h3>
          <p class="authors">{PAPER_AUTHORS}</p>
          <p class="venue">{PAPER_VENUE}</p>

          <p class="measure" style="margin-bottom:1rem">Adds a multi-head attention
          module to a convolutional network for recognizing driver distraction, and
          uses Grad-CAM to show which parts of the image the decision rests on.
          Reported at 99.48% mean accuracy over stratified five-fold
          cross-validation, running at 122 frames per second.</p>

          <div class="linkrow">
            <a class="chip chip-solid" href="{PAPER_URL}" rel="noopener">Full text</a>
            <a class="chip" href="{DOI_URL}" rel="noopener">DOI 10.3390/a19080615</a>
            <a class="chip" href="{PAPER_PDF}" rel="noopener">PDF</a>
          </div>

          <details class="abstract">
            <summary>Abstract</summary>
            <p>Driver behavior detection is essential for improving road safety in
            Intelligent Transportation Systems (ITSs). This paper proposes an
            attention-enhanced CNN integrated with Explainable Artificial Intelligence
            (XAI) to achieve reliable and interpretable driver behavior classification.
            Furthermore, the model also uses a multi-head attention mechanism to ensure
            that it captures local spatial features as well as long-range dependencies
            in the activities of the driver. The State Farm Distracted Driver dataset is
            experimented with using stratified 5-fold cross-validation. The proposed
            MHA-CNN model has a mean accuracy of 99.48% on all folds and an overall high
            levels of precision, recall, and F1-score in all ten distraction classes.
            Grad-CAM is used to produce attribution maps to improve interpretability by
            showing semantically important parts of the image, including hands, face,
            and mobile devices, and can give a visual explanation of why models make
            decisions. In addition, an ablation investigation is performed with k-fold
            validation to assess the value of the multi-head attention mechanism. Its
            model can run at 122 frames per second with 42.92 million parameters,
            showing that the suggested method is a reasonable tradeoff between accuracy,
            efficiency, and transparency and can be applied in real-time driver
            monitoring applications.</p>
            <p class="data" style="margin-top:14px">Keywords: driver behavior detection
            &middot; deep learning &middot; attention mechanism &middot; explainable AI
            &middot; intelligent transportation systems &middot; computer vision
            &middot; safety-critical systems</p>
          </details>

          <details class="abstract">
            <summary>BibTeX</summary>
            <div style="overflow-x:auto; margin-top:14px">
<pre class="data" style="margin:0; line-height:1.6; color:var(--ink-2)">{BIBTEX}</pre>
            </div>
          </details>
        </div>
      </article>
    </div>

  </div>
</section>
"""

# --------------------------------------------------------------------------
# Page: Teaching
# --------------------------------------------------------------------------

COURSES = [
    "Machine Learning",
    "Artificial Intelligence",
    "Digital Image Processing",
    "Data Structures",
    "Algorithms",
    "Object-Oriented Programming",
    "Database Management Systems",
    "Operating Systems",
]

def courses_html():
    return "\n".join(
        f"""      <div class="course">
        <h3>{title}</h3>
      </div>""" for title in COURSES)


CERTS = [
    ("elc-svp-certificate", "Certificate of appreciation — Senior Vice President, English Language Club, DUET"),
    ("elc-svp-plaque", "Recognition plaque — English Language Club, DUET"),
    ("duetcs-finance-director", "Finance Director, DUET Computer Society"),
    ("duet-cse-fest-volunteer", "Volunteer certificate — DUET CSE Fest 2019"),
]

def certs_html():
    out = []
    for slug, caption in CERTS:
        out.append(f"""      <figure>
        <img src="assets/img/leadership/{slug}.webp" alt="" loading="lazy" width="1100" height="780">
        <figcaption>{caption}</figcaption>
      </figure>""")
    return "\n".join(out)


TEACHING = f"""<section class="band">
  <div class="shell">
    <p class="eyebrow">Teaching</p>
    <h1>Courses, supervision and service</h1>
    <p class="lede measure" style="margin-top:1.4rem">
      I joined RSTU as a Lecturer in October 2021 and was promoted to Assistant
      Professor in May 2024. I teach undergraduate computer science courses and their
      laboratory sessions in English, develop the course material for them, and
      advise students on undergraduate thesis and project work.
    </p>
  </div>
</section>

<section class="band band-tint">
  <div class="shell">
    <div class="band-head">
      <p class="eyebrow">Courses</p>
      <h2>Undergraduate courses taught at RSTU</h2>
      <p class="measure">Lectures and laboratory sessions, 2021 to the present.</p>
    </div>

    <div class="courses">
{courses_html()}
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <div class="band-head">
      <p class="eyebrow">Supervision</p>
      <h2>Undergraduate thesis and project supervision</h2>
    </div>

    <div class="entries">
      <article class="entry">
        <div class="entry-meta"><b>May 2026</b>Completed<br>Md. Marzan Haque</div>
        <div class="entry-body">
          <h3>BookCycleBD — an online second-hand book marketplace</h3>
          <p>A peer-to-peer marketplace built to make second-hand books more affordable
          and accessible in Bangladesh. Users publish structured listings with images,
          search and filter on book-specific criteria, and contact sellers directly;
          an administrative panel handles users, listings, categories and reports.
          Built with Next.js, React, TypeScript, Supabase PostgreSQL, NextAuth.js,
          Cloudinary and Tailwind CSS, deployed on Vercel.</p>
          <div class="linkrow">
            <a class="chip chip-solid" href="https://book-cycle-taupe.vercel.app" rel="noopener">Live platform &#8599;</a>
            <a class="chip" href="assets/files/bookcyclebd-project-report.pdf">Project report PDF</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="band band-tint">
  <div class="shell">
    <div class="band-head">
      <p class="eyebrow">Service</p>
      <h2>Academic service and student engagement</h2>
    </div>

    <div class="entries">
      <article class="entry">
        <div class="entry-meta"><b>RSTU</b>Faculty role</div>
        <div class="entry-body">
          <h3>Moderator, RSTU Computer Club</h3>
          <p>Faculty moderator for the departmental student club.</p>
        </div>
      </article>
      <article class="entry">
        <div class="entry-meta"><b>2020&ndash;present</b>Public group<br>~30,000 members</div>
        <div class="entry-body">
          <h3>Founder and moderator, The Daily English Newspapers Vocabulary</h3>
          <p>A public group I started in 2020 to help students build English vocabulary
          from the daily newspapers, aimed at readers preparing for competitive
          examinations and English proficiency tests. It has grown to roughly 30,000
          members, and I still moderate it.</p>
          <div class="linkrow">
            <a class="chip" href="https://www.facebook.com/groups/dailyenglishvocab" rel="noopener">Visit the group &#8599;</a>
          </div>
        </div>
      </article>

      <article class="entry">
        <div class="entry-meta"><b>DUET</b>As a student</div>
        <div class="entry-body">
          <h3>Student societies at DUET</h3>
          <p>Senior Vice President, English Language Club &middot; Finance Director,
          DUET Computer Society &middot; Volunteer, DUET CSE Fest 2019.</p>
        </div>
      </article>

    </div>

    <div style="margin-top:44px">
      <p class="eyebrow">Certificates</p>
      <div class="gallery">
{certs_html()}
      </div>
    </div>
  </div>
</section>"""

# --------------------------------------------------------------------------
# Page: CV  (mirrors the PDF exactly — one source of truth)
# --------------------------------------------------------------------------

CV = f"""<div class="shell">
  <div class="linkrow no-print" style="margin-top:36px">
    <a class="chip chip-solid" href="assets/files/shahidul-islam-shabuz-cv.pdf" download>Download PDF</a>
    <button class="chip" type="button" onclick="window.print()">Print this page</button>
  </div>

  <article class="cv-sheet">

    <header class="cv-head">
      <h1>{NAME}</h1>
      <p class="cv-role">Assistant Professor, Department of Computer Science and
      Engineering, Rajshahi Science and Technology University</p>
      <div class="cv-contact">
        Natore, Rajshahi, Bangladesh &nbsp;|&nbsp;
        <a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;|&nbsp;
        <a href="mailto:{EMAIL_UNI}">{EMAIL_UNI}</a><br>
        shahidul-shabuz.github.io &nbsp;|&nbsp;
        <a href="{ORCID}" rel="noopener">ORCID {ORCID_ID}</a> &nbsp;|&nbsp;
        <a href="{SCHOLAR}" rel="noopener">Google Scholar</a><br>
        <a href="{LINKEDIN}" rel="noopener">linkedin.com/in/shahidul-shabuz</a> &nbsp;|&nbsp;
        <a href="{GITHUB}" rel="noopener">github.com/shahidul-shabuz</a>
      </div>
    </header>

    <section class="cv-section">
      <h2>Research Interests</h2>
      <div class="cv-item">
        <ul>
          <li><b>Computer Vision &amp; Attention Mechanisms:</b> attention-enhanced CNNs,
          Vision Transformers, real-time visual recognition.</li>
          <li><b>Medical Image Analysis:</b> tumor and lesion segmentation in MRI; CNN and
          CNN&ndash;Transformer hybrid architectures.</li>
          <li><b>Sequence Modeling &amp; Explainable AI:</b> Transformer,
          encoder&ndash;decoder and RNN/LSTM models; Grad-CAM interpretability for
          deployment under limited compute.</li>
        </ul>
      </div>
    </section>

    <section class="cv-section">
      <h2>Education</h2>
      <div class="cv-item">
        <div class="cv-line">
          <h3>M.Sc. in Computer Science and Engineering</h3>
          <span class="cv-when">Dec 2025 &ndash; Present</span>
        </div>
        <p class="cv-where">Dhaka University of Engineering &amp; Technology (DUET), Gazipur, Bangladesh</p>
        <ul><li>CGPA: 4.00 / 4.00 (coursework completed).</li></ul>
      </div>
      <div class="cv-item">
        <div class="cv-line">
          <h3>B.Sc. in Computer Science and Engineering</h3>
          <span class="cv-when">Graduated Jul 2021</span>
        </div>
        <p class="cv-where">Dhaka University of Engineering &amp; Technology (DUET), Gazipur, Bangladesh</p>
      </div>
    </section>

    <section class="cv-section">
      <h2>Publications</h2>
      <div class="cv-item">
        <p class="cv-plain">A. Al Mamun, <b>M. S. I. Shabuz</b>, M. N. Rahaman,
        K. I. Masud, and M. B. Hossain, &ldquo;{PAPER_TITLE},&rdquo; <i>Algorithms</i> (MDPI),
        vol. 19, no. 8, art. 615, 2026.
        DOI: <a href="{DOI_URL}" rel="noopener">10.3390/a19080615</a> &nbsp;|&nbsp;
        <a href="{PAPER_PDF}" rel="noopener">Full text PDF</a></p>
      </div>
    </section>

    <section class="cv-section">
      <h2>Research Projects</h2>
      <div class="cv-item">
        <div class="cv-line">
          <h3>Brain Tumor MRI Image Segmentation Using Convolutional Neural Networks</h3>
          <span class="cv-when">2020 &ndash; 2021</span>
        </div>
        <p class="cv-where">B.Sc. Thesis, DUET, Gazipur, Bangladesh</p>
        <ul>
          <li>Developed a CNN-based deep learning model for automatic segmentation of
          brain tumor regions in MRI images.</li>
          <li>Implemented the full pipeline &mdash; image preprocessing, model training, and
          evaluation against reference annotations.</li>
        </ul>
      </div>
    </section>

    <section class="cv-section">
      <h2>Professional Experience</h2>
      <div class="cv-item">
        <div class="cv-line">
          <h3>Assistant Professor, Department of Computer Science and Engineering</h3>
          <span class="cv-when">May 2024 &ndash; Present</span>
        </div>
        <p class="cv-where">Rajshahi Science and Technology University (RSTU), Natore, Bangladesh</p>
        <ul>
          <li>Teach undergraduate computer science courses and laboratory sessions in
          English; advise students on undergraduate thesis and project work.</li>
        </ul>
      </div>
      <div class="cv-item">
        <div class="cv-line">
          <h3>Lecturer, Department of Computer Science and Engineering</h3>
          <span class="cv-when">Oct 2021 &ndash; Apr 2024</span>
        </div>
        <p class="cv-where">Rajshahi Science and Technology University (RSTU), Natore, Bangladesh</p>
        <ul>
          <li>Taught core undergraduate courses and developed course materials;
          promoted to Assistant Professor in 2024.</li>
        </ul>
      </div>
      <div class="cv-item">
        <div class="cv-line">
          <h3>Python Development Intern</h3>
          <span class="cv-when">Mar &ndash; Apr 2021</span>
        </div>
        <p class="cv-where">Brain Station 23, Dhaka, Bangladesh</p>
        <ul>
          <li>Built a CLI-based task management system in Python using object-oriented
          design and Git version control.</li>
        </ul>
      </div>
    </section>

    <section class="cv-section">
      <h2>Teaching</h2>
      <div class="cv-item">
        <div class="cv-line">
          <h3>Rajshahi Science and Technology University, Natore</h3>
          <span class="cv-when">Oct 2021 &ndash; Present</span>
        </div>
        <ul>
          <li><b>Courses taught:</b> Machine Learning, Artificial Intelligence, Digital
          Image Processing, Data Structures, Algorithms, Object-Oriented Programming,
          Database Management Systems, Operating Systems.</li>
          <li>Lectures and laboratory sessions delivered in English; course material
          developed for each course.</li>
        </ul>
      </div>
    </section>

    <section class="cv-section">
      <h2>Student Supervision</h2>
      <div class="cv-item">
        <div class="cv-line">
          <h3>BookCycleBD &mdash; An Online Second-Hand Book Marketplace</h3>
          <span class="cv-when">May 2026</span>
        </div>
        <p class="cv-where">B.Sc. final-year project, RSTU. Student: Md. Marzan Haque.</p>
        <ul>
          <li>Supervised a peer-to-peer marketplace for second-hand books, built with
          Next.js, React, TypeScript and Supabase PostgreSQL and deployed publicly.</li>
        </ul>
      </div>
    </section>

    <section class="cv-section">
      <h2>Service &amp; Outreach</h2>
      <div class="cv-item">
        <div class="cv-line">
          <h3>Founder and Moderator, The Daily English Newspapers Vocabulary</h3>
          <span class="cv-when">2020 &ndash; Present</span>
        </div>
        <ul>
          <li>Public learning group of approximately 30,000 members, helping readers
          build English vocabulary from the daily newspapers for competitive
          examinations and English proficiency tests &mdash;
          <a href="https://www.facebook.com/groups/dailyenglishvocab" rel="noopener">facebook.com/groups/dailyenglishvocab</a></li>
        </ul>
      </div>
      <div class="cv-item">
        <div class="cv-line"><h3>Moderator, RSTU Computer Club</h3></div>
        <p class="cv-where">Student societies, DUET: Senior Vice President, English Language
        Club; Finance Director, DUET Computer Society; Volunteer, DUET CSE Fest 2019.</p>
      </div>
    </section>

    <section class="cv-section">
      <h2>Technical Skills</h2>
      <div class="cv-item">
        <ul>
          <li><b>Programming Languages:</b> Python, C++, C, MATLAB</li>
          <li><b>Deep Learning Frameworks:</b> PyTorch, TensorFlow, Keras</li>
          <li><b>Architectures &amp; Methods:</b> CNN, U-Net, ResNet, Swin Transformer,
          Transformers, Attention Modules, RNN, LSTM, Encoder&ndash;Decoder Models,
          Transfer Learning, Explainable AI (Grad-CAM)</li>
          <li><b>Tools &amp; Databases:</b> Git, GitHub, SQL</li>
        </ul>
      </div>
    </section>

    <section class="cv-section">
      <h2>References</h2>
      <div class="cv-item">
        <p class="cv-plain"><b>Dr. Momotaz Begum</b> &mdash; Professor and Head, Department of
        Computer Science and Engineering, DUET, Gazipur, Bangladesh<br>
        M.Sc. Supervisor &nbsp;|&nbsp; drmomotaz@duet.ac.bd</p>
      </div>
      <div class="cv-item">
        <p class="cv-plain"><b>Dr. Mohammod Abul Kashem</b> &mdash; Professor, Department of
        Computer Science and Engineering, DUET, Gazipur, Bangladesh<br>
        B.Sc. Thesis Supervisor &nbsp;|&nbsp; drkashemll@duet.ac.bd</p>
      </div>
    </section>

  </article>
</div>"""

# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

PAGES = [
    ("index.html", HOME,
     f"{SHORT} | Assistant Professor, CSE, RSTU",
     "Assistant Professor of Computer Science and Engineering at Rajshahi Science and "
     "Technology University, working on interpretable, efficient deep vision models for "
     "safety-critical decisions."),

    ("research.html", RESEARCH,
     f"Research | {SHORT}",
     "Research statement and projects: attention-enhanced CNNs, Grad-CAM "
     "interpretability, medical image segmentation, and the accuracy-efficiency "
     "trade-off in deployable vision models."),

    ("publications.html", PUBLICATIONS,
     f"Publications | {SHORT}",
     "Peer-reviewed publications with DOIs, full text and BibTeX, including an "
     "attention-enhanced CNN with explainable AI in Algorithms (MDPI), 2026."),

    ("teaching.html", TEACHING,
     f"Teaching | {SHORT}",
     "Undergraduate courses taught at RSTU since 2021, student thesis and project "
     "supervision, and academic service."),

    ("cv.html", CV,
     f"Curriculum Vitae | {SHORT}",
     f"Academic curriculum vitae of {NAME}: education, publications, research "
     "projects, professional experience, technical skills and references."),
]


def build():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    shutil.copytree(STATIC, DIST)

    for fname, body, title, desc in PAGES:
        with open(os.path.join(DIST, fname), "w", encoding="utf-8") as fh:
            fh.write(document(fname, title, desc, body))

    # 404
    body404 = """<section class="band">
  <div class="shell">
    <p class="eyebrow">404</p>
    <h1>That page isn&rsquo;t here</h1>
    <p class="lede measure" style="margin-top:1.2rem">The address may have changed, or
    the link may be from an older version of this site. Everything is reachable from
    the navigation above.</p>
    <div class="linkrow" style="margin-top:2rem">
      <a class="chip chip-solid" href="index.html">Home</a>
      <a class="chip" href="research.html">Research</a>
      <a class="chip" href="publications.html">Publications</a>
      <a class="chip" href="cv.html">CV</a>
    </div>
  </div>
</section>"""
    with open(os.path.join(DIST, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(document("404.html", f"Page not found | {SHORT}",
                          "The requested page does not exist.", body404)
                 # a 404 must not be indexed, and must not claim a canonical URL
                 .replace('<link rel="canonical" href="https://shahidul-shabuz.github.io/404.html">',
                          '<meta name="robots" content="noindex, follow">')
                 .replace('href="assets/', 'href="/assets/')
                 .replace('src="assets/', 'src="/assets/')
                 .replace('href="favicon.svg"', 'href="/favicon.svg"')
                 .replace('href="index.html"', 'href="/index.html"')
                 .replace('href="research.html"', 'href="/research.html"')
                 .replace('href="publications.html"', 'href="/publications.html"')
                 .replace('href="teaching.html"', 'href="/teaching.html"')
                 .replace('href="cv.html"', 'href="/cv.html"')
                 .replace('src="assets/js', 'src="/assets/js')
                 .replace('<script src="assets/js/site.js">', '<script src="/assets/js/site.js">'))

    # sitemap
    urls = []
    for fname, *_ in PAGES:
        loc = f"{SITE}/" if fname == "index.html" else f"{SITE}/{fname}"
        pri = "1.0" if fname == "index.html" else "0.8"
        urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{BUILT}</lastmod>\n"
                    f"    <changefreq>monthly</changefreq>\n    <priority>{pri}</priority>\n  </url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(sitemap)

    open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

    open(os.path.join(DIST, ".nojekyll"), "w").write("")

    # artifact entry: the home page body only (the Artifact host supplies the shell)
    art = (f'<title>{SHORT}</title>\n'
           f'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
           f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
           f'<link rel="stylesheet" href="{FONTS}">\n'
           f'<link rel="stylesheet" href="assets/css/site.css">\n'
           f'{jsonld()}\n'
           f'{header("index.html")}\n\n<main id="main">\n{HOME}\n</main>\n\n'
           f'{FOOTER}\n<script src="assets/js/site.js"></script>\n')
    open(os.path.join(ROOT, "artifact-home.html"), "w", encoding="utf-8").write(art)

    n = sum(len(f) for _, _, f in os.walk(DIST))
    print(f"built {len(PAGES)} pages + 404 → {DIST}")


if __name__ == "__main__":
    build()
