# Generated by Django 4.2.2 on 2023-06-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_datavisualization_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datavisualization',
            name='added',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='impact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='pestle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='published',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='sector',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='source',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='start_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='topic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datavisualization',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
