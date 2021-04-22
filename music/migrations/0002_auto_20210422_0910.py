# Generated by Django 3.2 on 2021-04-22 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='band',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='music',
            field=models.ManyToManyField(blank=True, to='music.Music'),
        ),
        migrations.AddField(
            model_name='music',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='music',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.label'),
        ),
    ]