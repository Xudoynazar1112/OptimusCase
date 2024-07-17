from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS = (
    ('general', 'GENERAL'),
    ('premium', 'PREMIUM'),
)

VACANCY_STATUS = (
    ('active', 'ACTIVE'),
    ('archived', 'ARCHIVED'),
)


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars')
    study = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=STATUS, default='general')
    about = models.TextField()
    skills = models.CharField(max_length=250)
    experience = models.TextField()
    interest = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    case = models.CharField(max_length=250)
    groups = models.CharField(max_length=250)
    chat = models.CharField(max_length=250)
    target = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos')
    about = models.TextField()
    skills = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=250, choices=STATUS, default='general')
    rating = models.IntegerField(default=0)
    case = models.CharField(max_length=100)
    vacancy = models.CharField(max_length=250)
    chat = models.CharField(max_length=250)
    target = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    POST_TYPE = (
        ('post', 'POST'),
        ('article', 'ARTICLE'),
        ('vacancy', 'VACANCY'),
        ('case', 'CASE')
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)
    type = models.CharField(max_length=250, choices=POST_TYPE, default='post')

    def __str__(self):
        return self.title


class Article(Post):
    direction = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Vacancy(Post):

    location = models.CharField(max_length=150)
    requirements = models.CharField(max_length=150)
    status = models.CharField(max_length=250, choices=VACANCY_STATUS, default='active')

    def __str__(self):
        return self.title


class Case(Post):
    location = models.CharField(max_length=150)
    condition = models.CharField(max_length=150)
    status = models.CharField(max_length=250, choices=VACANCY_STATUS, default='active')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment for {self.post.title} by {self.user.first_name}"


class CompanyComment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment for {self.company.name} by {self.user.first_name}"
