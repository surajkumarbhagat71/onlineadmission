# Generated by Django 2.2 on 2020-06-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_title', models.CharField(max_length=200)),
                ('cat_description', models.TextField()),
                ('cat_icon', models.CharField(max_length=25)),
                ('cat_date_of_creation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.IntegerField(null=True)),
                ('street', models.TextField()),
                ('city', models.CharField(choices=[('PRNA', 'Purnea'), ('PAT', 'Patna')], max_length=10)),
                ('state', models.CharField(choices=[('BR', 'Bihar'), ('JK', 'jharkhand')], max_length=10)),
                ('secondary_contact', models.IntegerField(blank=True, null=True)),
                ('category', models.ManyToManyField(to='public.Categories')),
            ],
        ),
    ]
