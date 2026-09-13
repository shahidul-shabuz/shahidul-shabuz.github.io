# shahidul-shabuz.github.io

Personal academic website of Md Shahidul Islam Shabuz — Assistant Professor,
Department of Computer Science and Engineering, Rajshahi Science and Technology
University.

Live at <https://shahidul-shabuz.github.io/>

## Structure

```
index.html            Home — identity, research thesis, selected work, news, contact
research.html         Research statement and project detail
publications.html     Peer-reviewed record with DOI, full text and BibTeX
teaching.html         Courses, student supervision, academic service
cv.html               Full CV (mirrors the PDF; print stylesheet generates it)
404.html
assets/css/site.css   The entire stylesheet
assets/js/site.js     Theme toggle, mobile nav, footer year — enhancement only
assets/img/           Portrait, social card, service evidence (WebP)
assets/files/         CV, thesis and project report PDFs
build.py              Generates the five pages from one shared layout
```

No build step is required to view the site: open `index.html` in a browser.

## Editing

`build.py` holds the navigation, header and footer once, so they cannot drift
between pages. Edit the page content inside it and run `python3 build.py`, which
writes `dist/`. If you edit the HTML directly instead, apply any header, nav or
footer change to all five pages by hand.

Common edits:

- **Add a publication** — copy an `<article class="pub">` block in the
  `PUBLICATIONS` section of `build.py`.
- **Add news** — copy an `<article class="entry">` block in the `HOME` News section.
- **Replace the CV** — swap `assets/files/shahidul-islam-shabuz-cv.pdf`, keeping the
  filename, and mirror the change in the `CV` section so the page and PDF agree.
- **Change colours** — the `:root` token block at the top of `assets/css/site.css`
  (`--accent`, `--signal`); dark-theme values are redefined twice below it.

## Licence

Source MIT. Text, images and documents © Md Shahidul Islam Shabuz.
