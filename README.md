# xiaweiliu.com

Personal academic homepage of Xiawei (William) Liu, served by GitHub Pages at <https://www.xiaweiliu.com>.

Plain HTML and CSS, no build step. To preview locally:

```
python3 -m http.server 8000
```

- `index.html`: the homepage (news, publications, education, experience)
- `styles.css`: its stylesheet
- `images/`: portrait and publication teasers (animated WebP, with a still JPG for visitors who turn off motion)
- `privacy/`: privacy policy for the Hermes Mail Reader OAuth app
- `zool/`: support page (`index.html`) and privacy policy (`privacy/`) for the Zool app (it was ArkCine), English and Chinese; no analytics or web fonts on these pages
- `arkcine/`: redirects to `zool/` (and `arkcine/privacy/` to `zool/privacy/`), so links to the old name keep working
- `projects/`: side-project list (uses `geek-theme.css`)
