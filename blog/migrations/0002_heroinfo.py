# Generated by Django 3.2 on 2021-05-26 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('hcomment', models.CharField(max_length=128)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.bookinfo')),
            ],
        ),
    ]
