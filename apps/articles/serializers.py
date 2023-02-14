from rest_framework import serializers
from apps.articles.models import Article, Category


class ArticlePreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "title",
            "pk",
            # "attractive_text",
            "categories",
            # "image_base",
            # "main_text",
            # "created_on",
            "last_modified",
            # "main_text_headers_list",
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "title",
            "pk",
            "attractive_text",
            "categories",
            "image_base",
            "main_text",
            "created_on",
            "last_modified",
            "main_text_headers_list",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "pk")
