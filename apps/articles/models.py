import re
import collections

from django.db import models
from django_mysql.models import ListTextField

from urllib.parse import unquote

from apps.quiz.models import QuizPick4


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def get_absolute_url(self):
        return unquote(f"/articles/{self.name}")


class Article(models.Model):
    title = models.CharField(max_length=100)

    attractive_text = models.TextField(default="Завлекающий текст")
    categories = models.ManyToManyField("Category", related_name="articles")
    quizzes = models.ManyToManyField(
        QuizPick4, related_name="quizzes", default="", blank=True
    )
    image_base = models.ImageField(upload_to="img", default="img/placeholder.png")
    main_text = models.TextField(default="Основной текст")

    main_text_headers_list_keys = models.CharField(max_length=200, default=" ")

    main_text_headers_list = ListTextField(
        base_field=models.CharField(max_length=40, default=""),
        size=100,  # Maximum of 100 ids in list
        default=None,
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        # forming the key_word_headers
        def get_main_text_headers_list_keys(arr_of_headers):
            word_length_min = 4
            word_count_min = 2

            arr_of_words = []
            for phrase in arr_of_headers:
                for subphrase in phrase.split():
                    if len(subphrase) > word_length_min:
                        arr_of_words.append(subphrase)

            c = collections.Counter([el.lower() for el in arr_of_words])

            wordlist = []
            for word, count in c.most_common():
                wordlist.append(word)

            if len(wordlist) > 3:
                print(wordlist)
                return ",".join(wordlist[:8])
            else:
                print(wordlist)
                return "филология,язык,русский"

        # forming the inner subtitles
        def make_inner_titles():

            text_inner_titles = []
            count_of_h6 = self.main_text.count("<h6")

            for i, locator_group in enumerate(
                list(re.finditer(r"(<h6[^<>]*>)([^<>]*)</h6>", self.main_text))[::-1]
            ):
                locator_open_tag = locator_group.start(1), locator_group.end(1)
                self.main_text = (
                    ""
                    + self.main_text[: locator_open_tag[0]]
                    + '<h6 id="queried_header'
                    + f"{count_of_h6 - i}"
                    + '"  class="queried_header">'
                    + self.main_text[locator_open_tag[1] :]
                )

                locator_inner_content = locator_group.group(2).replace(".", "")
                text_inner_titles.append(locator_inner_content)

            text_inner_titles = text_inner_titles[::-1]

            return text_inner_titles

        self.main_text_headers_list = make_inner_titles()

        self.main_text_headers_list_keys = get_main_text_headers_list_keys(
            self.main_text_headers_list
        )

        # reshaping the input text
        self.main_text = self.main_text.strip()
        self.main_text = self.main_text.replace("<br>", "")
        self.main_text = self.main_text.replace("<p></p>", "")
        self.main_text = self.main_text.replace("\n", "")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return f"/articles/{self.pk}"


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/articles/{self.article.pk}"
