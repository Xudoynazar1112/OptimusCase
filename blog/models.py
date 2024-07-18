from django.contrib.auth.models import AbstractUser
from django.db import models

from notification.models import Notification


STATUS = (
    ('general', 'GENERAL'),
    ('premium', 'PREMIUM'),
)

VACANCY_STATUS = (
    ('active', 'ACTIVE'),
    ('archived', 'ARCHIVED'),
)

POST_TYPE = (
    ('post', 'POST'),
    ('article', 'ARTICLE'),
    ('vacancy', 'VACANCY'),
    ('case', 'CASE')
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


class BasePost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_posts')
    data = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Notify followers or other relevant users
        followers = User.objects.all()  # Example for followers
        for follower in followers:
            Notification.objects.create(
                user=follower,
                message=f"New post from {User.first_name}: {self.title}"
            )

    class Meta:
        abstract = True


class Post(BasePost):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=250, choices=POST_TYPE, default='post')

    def __str__(self):
        return self.title


class Article(BasePost):
    id = models.IntegerField(primary_key=True)
    direction = models.CharField(max_length=150)
    type = models.CharField(max_length=250, choices=POST_TYPE, default='article')

    def __str__(self):
        return self.title


class Vacancy(BasePost):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=150)
    requirements = models.CharField(max_length=150)
    status = models.CharField(max_length=250, choices=VACANCY_STATUS, default='active')
    type = models.CharField(max_length=250, choices=POST_TYPE, default='vacancy')

    def __str__(self):
        return self.title


class Case(BasePost):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=150)
    condition = models.CharField(max_length=150)
    status = models.CharField(max_length=250, choices=VACANCY_STATUS, default='active')
    type = models.CharField(max_length=250, choices=POST_TYPE, default='case')

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
