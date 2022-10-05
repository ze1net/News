from django.db import models

class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='news_image/')
    date = models.DateTimeField(auto_now_add=True)

    WorldNews = 'World News'
    UzbNews = 'Uzbekistan News'
    LatestNews = 'Latest News'

    categoryies = (
        (WorldNews, 'World News'),
        (UzbNews, 'Uzbekistan News'),
        (LatestNews, 'Latest News'),
    )

    category = models.CharField(
        max_length=50,
        choices=categoryies,
        default=LatestNews,
    )

    def Selector(self):
        return self.category in (self.WorldNews, self.UzbNews, self.LatestNews)

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'

    def __str__(self):
        return f"{self.title} {self.category} {self.date}"

