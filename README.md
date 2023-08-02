# New Horizon Project

Initially, this site was written to participate in the "knowledge" competition in the "new horizons" nomination as a platform for educating users in the field of learning the Russian language.

The source code of the platform is distributed under the license ..., but the texts of articles and other educational materials are not published.

## screenshots

1. Main page
![1](./misc/description_images/Screenshot%20from%202023-08-02%2004-55-22.png)


<!-- ![2](./misc/description_images/Screenshot%20from%202023-08-02%2004-55-28.png) -->

2. The page with the article
![3](./misc/description_images/Screenshot%20from%202023-08-02%2004-55-34.png)


## setup & start

makefile - control scripts for:
  * start, stop systemd service<br>
    `make setup`<br>
    `make start`<br>
    `make stop`


## django apps

django application files are stored in the app directory

### Articles

the structure of the article suggests the presence of:
  * subheadings in \<h6\> tags (this helps to automatically generate a block of content (with link navigation within the document)
  * assigned article categories
  * a block of enticing text that is displayed in the article card
  * an image that is displayed in the article card and in the text of the article itself

### Projects

the structure of the project block assumes:
  * internal links to articles (optional)
  * a block of enticing text that is displayed in the article card
  * an image that is displayed in the article card and in the text of the article itself

### popular_elements

this block contains
  * popular articles - listing of featured articles
  * popular projects - listing of selected projects

### main

this block, in addition to the basic files of the project, contains the template of the page "about"
