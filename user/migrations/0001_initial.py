# Generated by Django 2.1.1 on 2018-09-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=True, to='user.Products')),
                ('user', models.ForeignKey(on_delete=True, to='user.User')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='products',
            field=models.ManyToManyField(through='user.UserProducts', to='user.Products'),
        ),
    ]