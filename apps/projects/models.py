import re

from django_mysql.models import ListTextField
from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=100)

    attractive_text = models.TextField(default="Завлекающий текст")
    image_base = models.ImageField(upload_to="img", default="img/placeholder.png")
    main_text = models.TextField(default="Основной текст")

    article_inner_links = ListTextField(
        base_field=models.CharField(max_length=40, default="aaa"),
        size=100,  # Maximum of 100 ids in list
        default="",
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        article_inner_links = []
        # replace_attr_text_locators = []

        for locator_group in list(
            re.finditer(r"(<a[^<>]*>)([^<>]*)</a>", self.main_text)
        )[::-1]:

            project_a_class = "button_pr btn btn-primary button_center project_a"

            locator_open_tag = locator_group.start(1), locator_group.end(1)
            a_tag_attrs = self.main_text[locator_open_tag[0] : locator_open_tag[1]]

            for tag_locator_group in list(
                re.finditer(r'([\S]*)="([^"]*[\S^">])"', a_tag_attrs)
            ):

                attr_name = tag_locator_group.group(1)
                # attr_text = tag_locator_group.group(2)

                # перебор ссылок на статьи
                if attr_name == "href":
                    attr_text_locator = (
                        locator_open_tag[0] + tag_locator_group.start(2),
                        locator_open_tag[0] + tag_locator_group.end(2),
                    )

                    article_inner_links.append(
                        self.main_text[attr_text_locator[0] : attr_text_locator[1]]
                    )

                # # создание меток на замену классов html
                # elif attr_name == 'class':

                #     attr_text_locator = (
                #         locator_open_tag[0] + tag_locator_group.start(1),
                #         locator_open_tag[0] + tag_locator_group.end(1)
                #     )

                #     replace_attr_text_locators.append(attr_text_locator)

        # for attr_text_locator in replace_attr_text_locators:
        #     self.main_text = '' \
        #         + self.main_text[:attr_text_locator[0]] \
        #         + 'class="' \
        #         + project_a_class \
        #         + '"' \
        #         + self.main_text[attr_text_locator[1]:] \

        article_inner_links = article_inner_links[::-1]
        self.article_inner_links = article_inner_links

        self.main_text = self.main_text.strip()
        self.main_text = self.main_text.replace("<br>", "")
        self.main_text = self.main_text.replace("<p></p>", "")
        self.main_text = self.main_text.replace("\n", "")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return f"/{self.pk}"
