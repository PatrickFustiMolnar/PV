# W3Schools Offline ⚡️  Update v2022.09.06

![Repo Size](https://img.shields.io/github/repo-size/ja7adr/W3Schools) ![Docker Image Size](https://img.shields.io/docker/image-size/ja7adr/w3schools?style=flat-square)

![W3schools](https://www.w3schools.com/images/w3schoolscom_gray.gif)

W3schools tutorials are available at any time within your local computer.
This edition removes all remote dependencies. Fonts and assets are loaded from the `lib` and `images` directories, so the site works completely offline using only HTML, CSS and JavaScript.

## ⁉️ How to run docker image ?

1. First pull image to your docker images : 
  - `docker pull ja7adr/w3schools`
  - `docker pull ghcr.io/ja7ad/w3schools:latest`
2. Create container from image : 

- `docker run -d -p 80:80 --name w3schools ja7adr/w3schools`
- `docker run -d -p 127.0.0.1:80:80 --name w3schools ja7adr/w3schools`

or

- `docker run -d -p 80:80 --name w3schools ghcr.io/ja7ad/w3schools`
- `docker run -d -p 127.0.0.1:80:80 --name w3schools ghcr.io/ja7ad/w3schools`

3. Open Browser for access to w3schools from http://127.0.0.1 or http://localhost


## ⁉️ How to download zipped edition?

1. Download Latest Release : [Release](https://github.com/Ja7adR/W3Schools/releases)
2. Just run file `index.html`
# PV

## Offline cleanup
Run `python3 scripts/cleanup_all.py` to apply every cleanup step across all HTML files.
This wrapper executes `simplify_html.py` then `remove_external_resources.py` in sequence.
Because the project has over 40k pages, the process can take several minutes to complete.

## Extract text content
Run `python3 scripts/extract_text.py` to create plain-text copies of every HTML page using BeautifulSoup. Each `.txt` file will be saved alongside its HTML source.

## Prune non-lesson content
Run `python3 scripts/prune_content.py --dry-run` to preview which files and directories would be removed. Omit `--dry-run` to actually delete images and other non-lesson material. The script also reorganizes any folder with more than 100 files by moving extra items into numbered `batch_` subdirectories.
