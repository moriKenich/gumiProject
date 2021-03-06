# Generated by Django 3.2.5 on 2022-04-25 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='シリーズ')),
            ],
        ),
        migrations.CreateModel(
            name='Hard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardness', models.CharField(max_length=20, verbose_name='硬さ')),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('makername', models.CharField(max_length=20, verbose_name='メーカー')),
            ],
        ),
        migrations.CreateModel(
            name='Powder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powderis', models.CharField(max_length=20, verbose_name='パウダー')),
            ],
        ),
        migrations.CreateModel(
            name='GumiPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='商品名')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('url', models.TextField(verbose_name='URL')),
                ('image', models.ImageField(upload_to='photos', verbose_name='イメージ')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('price', models.IntegerField(verbose_name='定価')),
                ('weight', models.IntegerField(verbose_name='重量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gumi.category', verbose_name='シリーズ')),
                ('hard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gumi.hard', verbose_name='硬さ')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gumi.maker', verbose_name='メーカー')),
                ('powder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gumi.powder', verbose_name='パウダー')),
            ],
        ),
    ]
