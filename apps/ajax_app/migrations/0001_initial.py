# Generated by Django 3.2.8 on 2021-10-10 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='update')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='quantity')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'product',
                'db_table': 'tbl_product',
            },
        ),
    ]
