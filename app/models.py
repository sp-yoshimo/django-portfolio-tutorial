from django.db import models

# Create your models here.


class Profile(models.Model):
    title = models.CharField("タイトル", max_length=100, null=True, blank=True)
    subtitle = models.CharField("サブタイトル", max_length=100, null=True, blank=True)
    name = models.CharField("名前", max_length=100)
    job = models.TextField("仕事")
    introduction = models.TextField("自己紹介")
    github = models.CharField("guthub", max_length=100, null=True, blank=True)
    twitter = models.CharField("twitter", max_length=100, null=True, blank=True)
    linkedin = models.CharField("linkedin", max_length=100, null=True, blank=True)
    facebook = models.CharField("facebook", max_length=100, null=True, blank=True)
    instagram = models.CharField("instagram", max_length=100, null=True, blank=True)
    topImage = models.ImageField(upload_to="images", verbose_name="トップ画像")
    subImage = models.ImageField(upload_to="images", verbose_name="サブ画像")

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField("タイトル", max_length=100)
    image = models.ImageField(upload_to="images", verbose_name="イメージ画像")
    thumbnail = models.ImageField(
        upload_to="images", verbose_name="サムネイル画像", null=True, blank=True
    )
    skill = models.CharField("スキル", max_length=100)
    url = models.CharField("URL", max_length=100, null=True, blank=True)
    created = models.DateField("作成日")
    description = models.TextField("説明")

    def __str__(self):
        return self.title


class Experience(models.Model):
    occupation = models.CharField("職種", max_length=100)
    company = models.CharField("会社", max_length=100)
    description = models.TextField("説明")
    place=models.CharField("場所",max_length=100)
    period=models.CharField("期間",max_length=100)

    def __str__(self):
        return self.occupation
    

class Education(models.Model):
    course=models.CharField("コース",max_length=100)
    school=models.CharField("学校",max_length=100)
    place=models.CharField("場所",max_length=100)
    period=models.CharField("期間",max_length=100)

    def __str__(self):
        return self.course
