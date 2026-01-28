from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=10, verbose_name="ジャンル名")
    
    def __str__(self):
        return self.genre
    
class News(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name="ジャンル")
    title = models.CharField(verbose_name="ニュースタイトル")
    image = models.ImageField(null=True, default=None, upload_to='news_images/', verbose_name='画像')
    content = models.TextField(verbose_name='ニュース本文')
    created_at = models.DateField(auto_now_add=True, verbose_name='作成日時')
    delete_flag = models.BooleanField(default=False, verbose_name='削除フラグ')

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name="ジャンル")
    last_name = models.CharField(verbose_name='姓')
    first_name = models.CharField(verbose_name='名')
    postal_code = models.CharField(verbose_name='郵便番号')
    address = models.CharField(verbose_name='住所')
    phone_number = models.CharField(verbose_name='電話番号')
    image = models.ImageField(null=True, default=None, upload_to='contact_images/', verbose_name='画像')
    mail = models.EmailField(verbose_name='メールアドレス')
    content = models.TextField(verbose_name='お問い合わせ内容')
    created_at = models.DateField(auto_now_add=True, verbose_name='作成日時')
    delete_flag = models.BooleanField(default=False, verbose_name='削除フラグ')

    def __str__(self):
        return f'{self.last_name}{self.first_name}'