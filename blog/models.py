from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone

""" class User(models.Model):
    options = (
        ('unauthorized', 'Unauthorized'),
        ('authorized', 'Authorized')
    )
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    status = models.CharField(max_length=50, choice=options, default='unauthorized')
    realm_roles = models.ForeignKey(User, related_name= 'realm_roles', on_delete = models.CASCADE)
    resources_roles = models.ForeignKey(User, related_name= 'resources_roles', on_delete = models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False) # a user; medic
    admin = models.BooleanField(default=False) # a superuser
    objetcs = models.Manager() # default manager

    def __str__(self) -> str:
        return self.name

    def has_resouces_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_realm_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    class Meta:
        ordering = ('-unauthorized')

        def __str__(self) -> str:
            return self.name """


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self) -> str:
        return self.title
