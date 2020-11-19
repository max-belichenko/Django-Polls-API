# Generated by Django 2.2.10 on 2020-11-18 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('TX', 'Ответ текстом'), ('OC', 'Выбор одного варианта'), ('MC', 'Выбор нескольких вариантов')], max_length=255, verbose_name='Тип вопроса')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Вариант ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question')),
            ],
        ),
    ]
