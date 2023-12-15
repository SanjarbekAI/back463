from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="news")
    description = models.TextField()
    author = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.created_at}"

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"


class PopularTourModel(models.Model):
    photo = models.ImageField(upload_to="tours")
    title = models.CharField(max_length=255)
    days = models.PositiveSmallIntegerField(default=0)
    price = models.FloatField(default=0)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "tour"
        verbose_name_plural = "tours"


class DestinationModel(models.Model):
    photo = models.ImageField(upload_to="destinations")
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city} | {self.created_at}"

    class Meta:
        verbose_name = "destination"
        verbose_name_plural = "destinations"


class EmailModel(models.Model):
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} | {self.created_at}"

    class Meta:
        verbose_name = "email"
        verbose_name_plural = "emails"
