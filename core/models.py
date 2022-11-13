from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Division(MPTTModel):
    """ Подразделение """

    name = models.CharField(
        max_length=512,
        verbose_name='Название'
    )

    parent = TreeForeignKey(
        'self',
        verbose_name='Родитель',
        related_name='children',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Post(models.Model):
    """ Должность """

    name = models.CharField(
        max_length=512,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'должности'


class Employee(models.Model):
    """ Сотрудник """

    name = models.CharField(
        max_length=512,
        verbose_name='ФИО'
    )

    post = models.ForeignKey(
        Post,
        verbose_name='Должность',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    date_of_admission = models.DateField(
        verbose_name='Дата приема на работу'
    )

    salary = models.FloatField(
        verbose_name='Размер заработной платы'
    )

    division = models.ForeignKey(
        Division,
        related_name=u'division_employee',
        verbose_name='Подразделение',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = u'сотрудники'
