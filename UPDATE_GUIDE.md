# Beginner Update Guide

You can update most information directly on GitHub without installing software.

## Edit a file on GitHub

1. Open your website repository.
2. Click the file you want to edit.
3. Click the pencil icon.
4. Change the text.
5. Click **Commit changes**.

## Update your photograph

Replace:

`assets/img/profile.jpg`

Keep the same filename. A vertical professional photograph works best.

## Replace your PDF CV

Replace:

`assets/files/Md_Shahidul_Islam_Shabuz_CV.pdf`

Keep the same filename so all links continue to work.

## Update the BookCycleBD supervision project

The project details are now included in `index.html`, `leadership.html` and `cv.html`.

Replace the report at:

`assets/files/BookCycleBD_Project_Report.pdf`

Keep the same filename so the website links continue to work.

The live application link currently points to:

`https://book-cycle-taupe.vercel.app`

Search for that address in the HTML files if the deployment URL changes.

## Update leadership certificates

Leadership images are stored in:

`assets/img/leadership/`

You can replace an image while keeping its existing filename, or add a new
certificate card in `leadership.html`.


## Add a new publication

Open `index.html`, search for:

`publication-card`

Copy the complete publication article and paste another copy below it. Then change:

- Status
- Year
- Title
- Authors
- Journal or conference
- Paper/code link

Use **Under Review**, **Accepted**, **Published** or **Preprint** accurately.

## Add new news

Open `index.html` and search for:

`news-list`

Copy one `news-item` block and change the date, heading and description.

## Add Google Scholar and ORCID later

After creating the profiles, add links in:

- Hero quick links
- Contact section
- Structured data (`sameAs`) near the top of `index.html`

## Change colors

Open `assets/css/styles.css`.

At the top, change:

- `--primary`
- `--accent`

Avoid changing many colors at once.

## Update the manuscript after a decision

Search for the full manuscript title in both `index.html` and `cv.html`.

- If accepted: change `Under Review` to `Accepted`.
- If published: add volume, issue, pages/article number, DOI and paper link.
- Never keep “under review” after publication.

## Preview before publishing

Double-click `index.html` on your computer. It opens in a browser.

The website uses no build system, so it can be previewed directly.
