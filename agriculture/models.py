from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category, max_length=50, null=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=50, db_index=True, default='')

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        ordering = ['category']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Expenses(models.Model):
    description = models.TextField(max_length=500, blank=False)
    category = models.ForeignKey(
        Category, null=True, max_length=50, on_delete=models.SET_NULL
    )
    subcategory = models.ForeignKey(
        Subcategory, max_length=50, null=True, on_delete=models.SET_NULL
    )
    amount = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Expenses'
        verbose_name_plural = 'Expenses'

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description


class Revenue(models.Model):
    description = models.TextField(max_length=500, blank=False)
    category = models.ForeignKey(
        Category, max_length=50, null=True, on_delete=models.SET_NULL
    )
    subcategory = models.ForeignKey(
        Subcategory, max_length=50, null=True, on_delete=models.SET_NULL
    )
    amount = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Revenue'
        verbose_name_plural = 'Revenue'

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
