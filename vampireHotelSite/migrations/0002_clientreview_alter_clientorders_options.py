# Generated by Django 4.1.7 on 2023-03-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vampire_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.CharField(max_length=1500)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='clientorders',
            options={'verbose_name': 'Client Order'},
        ),
    ]
