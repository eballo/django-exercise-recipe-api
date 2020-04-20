# Generated by Django 2.1.15 on 2020-04-19 16:47

from django.db import migrations, models
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=recipe.models.recipe_image_file_path),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipe.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='recipe',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='recipe.Tag'),
        ),
    ]