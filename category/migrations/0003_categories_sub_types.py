# Generated by Django 2.2.6 on 2019-10-11 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20191011_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='sub_types',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.SubCategories'),
        ),
    ]