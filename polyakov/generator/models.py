from django.db import models
from django.urls import reverse


class Task1(models.Model):
    title = models.CharField(max_length=100, default='Задание 1', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 1'
        verbose_name_plural = 'Задание 1'


class Task2(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 2'
        verbose_name_plural = 'Задание 2'


class Task3(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 3'
        verbose_name_plural = 'Задания 3'


class Task4(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 4'
        verbose_name_plural = 'Задания 4'


class Task5(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 5'
        verbose_name_plural = 'Задания 5'


class Task6(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 6'
        verbose_name_plural = 'Задания 6'


class Task7(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 7'
        verbose_name_plural = 'Задания 7'


class Task8(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 8'
        verbose_name_plural = 'Задания 8'


class Task9(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 9'
        verbose_name_plural = 'Задания 9'


class Task10(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 10'
        verbose_name_plural = 'Задания 10'


class Task11(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 11'
        verbose_name_plural = 'Задания 11'


class Task12(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 12'
        verbose_name_plural = 'Задания 12'


class Task13(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 13'
        verbose_name_plural = 'Задания 13'


class Task14(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 14'
        verbose_name_plural = 'Задания 14'


class Task15(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 15'
        verbose_name_plural = 'Задания 15'


class Task16(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 16'
        verbose_name_plural = 'Задания 16'


class Task17(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 17'
        verbose_name_plural = 'Задания 17'


class Task18(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 18'
        verbose_name_plural = 'Задания 18'


class Task19(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 19'
        verbose_name_plural = 'Задания 19'


class Task20(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 20'
        verbose_name_plural = 'Задания 20'


class Task21(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 21'
        verbose_name_plural = 'Задания 21'


class Task22(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 22'
        verbose_name_plural = 'Задания 22'


class Task23(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 23'
        verbose_name_plural = 'Задания 23'


class Task24(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 24'
        verbose_name_plural = 'Задания 24'


class Task25(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 25'
        verbose_name_plural = 'Задания 25'


class Task26(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 26'
        verbose_name_plural = 'Задания 26'


class Task27(models.Model):
    title = models.CharField(max_length=100, default='Задание 2', blank=True)
    content = models.TextField(blank=True, verbose_name='Задание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото к заданию')
    answer = models.TextField(verbose_name='Ответ', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл к заданию')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Задание 27'
        verbose_name_plural = 'Задания 27'


class Variant(models.Model):
    title = models.CharField(max_length=100, blank=True)
    task1 = models.ForeignKey(Task1, on_delete=models.PROTECT)
    task2 = models.ForeignKey(Task2, on_delete=models.PROTECT)
    task3 = models.ForeignKey(Task3, on_delete=models.PROTECT)
    task4 = models.ForeignKey(Task4, on_delete=models.PROTECT)
    task5 = models.ForeignKey(Task5, on_delete=models.PROTECT)
    task6 = models.ForeignKey(Task6, on_delete=models.PROTECT)
    task7 = models.ForeignKey(Task7, on_delete=models.PROTECT)
    task8 = models.ForeignKey(Task8, on_delete=models.PROTECT)
    task9 = models.ForeignKey(Task9, on_delete=models.PROTECT)
    task10 = models.ForeignKey(Task10, on_delete=models.PROTECT)
    task11 = models.ForeignKey(Task11, on_delete=models.PROTECT)
    task12 = models.ForeignKey(Task12, on_delete=models.PROTECT)
    task13 = models.ForeignKey(Task13, on_delete=models.PROTECT)
    task14 = models.ForeignKey(Task14, on_delete=models.PROTECT)
    task15 = models.ForeignKey(Task15, on_delete=models.PROTECT)
    task16 = models.ForeignKey(Task16, on_delete=models.PROTECT)
    task17 = models.ForeignKey(Task17, on_delete=models.PROTECT)
    task18 = models.ForeignKey(Task18, on_delete=models.PROTECT)
    task19 = models.ForeignKey(Task19, on_delete=models.PROTECT)
    task20 = models.ForeignKey(Task20, on_delete=models.PROTECT)
    task21 = models.ForeignKey(Task21, on_delete=models.PROTECT)
    task22 = models.ForeignKey(Task22, on_delete=models.PROTECT)
    task23 = models.ForeignKey(Task23, on_delete=models.PROTECT)
    task24 = models.ForeignKey(Task24, on_delete=models.PROTECT)
    task25 = models.ForeignKey(Task25, on_delete=models.PROTECT)
    task26 = models.ForeignKey(Task26, on_delete=models.PROTECT)
    task27 = models.ForeignKey(Task27, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('ready_var', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
