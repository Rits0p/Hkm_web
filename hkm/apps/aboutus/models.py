from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='faculty/')
    experience = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. 5+ Years Experience")
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Order of display on the page")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Faculty Members"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    tools = models.CharField(max_length=255, help_text="e.g. Ps • Ai • Ae • Pr")
    image = models.ImageField(upload_to='portfolios/')
    portfolio_link = models.URLField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Portfolios"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class StudentWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='student_work/thumbnails/', help_text="Main preview image for the card")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Student Work"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class StudentWorkImage(models.Model):
    student_work = models.ForeignKey(StudentWork, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student_work/gallery/')
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.student_work.title}"
