# Generated by Django 3.2.9 on 2021-12-02 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0005_question_set_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qpid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Qpaper', to='editor.questionpapers'),
        ),
    ]
