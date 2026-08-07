from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    # قیمت به صورت اعشاری (مناسب برای دلار یا سیستم‌های دقیق)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="قیمت")
    image = models.ImageField(upload_to='items/', null=True, blank=True, verbose_name="تصویر")

    # زمان ایجاد و بروزرسانی خودکار
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم‌ها"
        ordering = ['-created_at'] # نمایش جدیدترین‌ها در ابتدا

    def __str__(self):
        return self.title
