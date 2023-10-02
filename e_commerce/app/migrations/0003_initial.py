# Generated by Django 4.2.4 on 2023-08-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='media/slider_imgs')),
                ('Discount_deal', models.CharField(choices=[('HOT DEAL', 'HOT DEAL'), ('NEW ARRIVALES', 'NEW ARRIVALES')], max_length=200)),
                ('Sale', models.IntegerField()),
                ('Brand_Name', models.CharField(max_length=200)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=200)),
            ],
        ),
    ]