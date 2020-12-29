# Wordpress Archive

Archives blog posts from a wordpress site (or any site with a `URL/YYYY/MM` blog format).

First, install the requirements with

```bash
pip install -r requirements.txt
```

Then, to archive a site, run

```bash
python wordpress_archive.py <url> <start_year> <end_year> <output_dir>
```

Replacing `<url>` with the base URL of your site, `<start_year>` and `<end_year>` with the years you'd like to archive through, and `<output_dir>` with the name of the directory you'd like the files saved to.  For example, to save posts from https://statmodeling.stat.columbia.edu from 2018 through 2020, and save them in the folder `gelman_archive` (don't do this, it'll take forever because they post so much lol):

```bash
python wordpress_archive.py https://statmodeling.stat.columbia.edu 2018 2020 gelman_archive
```
