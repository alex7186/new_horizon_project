# New Horizon Project

Initially, this site was written to participate in the "knowledge" competition in the "new horizons" nomination as a platform for educating users in the field of learning the Russian language.

The source code of the platform is distributed under the license ..., but the texts of articles and other educational materials are not published.

## common directory files

makefile - control scripts for:
  * start, stop, copy systemd service<br>
    `make start_service`<br>
    `make stop_service`<br>
    `make status`<br>
    `make copy_service`
  * auto push commits to github<br>
    `make push`<br>
    `make push-force`
  * updating files on the server using rsync<br>
    `make update_hosting`<br>
    `make update_local`

## service

this directory contains the starter.sh file and the system-d file of the service that starts it


## django apps

django application files are stored in the app directory

#### Articles

the structure of the article suggests the presence of:
  * subheadings in \<h6\> tags (this helps to automatically generate a block of content (with link navigation within the document)
  * assigned article categories
  * a block of enticing text that is displayed in the article card
  * an image that is displayed in the article card and in the text of the article itself

#### Projects

the structure of the project block assumes:
  * internal links to articles (optional)
  * a block of enticing text that is displayed in the article card
  * an image that is displayed in the article card and in the text of the article itself

#### popular_elements

this block contains
  * popular articles - listing of featured articles
  * popular projects - listing of selected projects

#### main

this block, in addition to the basic files of the project, contains the template of the page "about"

