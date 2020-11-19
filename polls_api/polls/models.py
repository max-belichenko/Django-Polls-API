from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    TEXT = 'TX'
    ONLY_CHOICE = 'OC'
    MULTIPLE_CHOICES = 'MC'
    QUESTION_TYPES = [
        (TEXT, 'Ответ текстом'),
        (ONLY_CHOICE, 'Выбор одного варианта'),
        (MULTIPLE_CHOICES, 'Выбор нескольких вариантов'),
    ]

    poll = models.ForeignKey(to=Poll, on_delete=models.CASCADE, related_name='questions')
    type = models.CharField(max_length=255, choices=QUESTION_TYPES, verbose_name='Тип вопроса')
    text = models.TextField(verbose_name='Текст вопроса')

    def __str__(self):
        poll = str(self.poll) if len(str(self.poll)) <= 20 else str(self.poll)[:20] + '...'
        question = str(self.text) if len(str(self.text)) <= 40 else str(self.text)[:40] + '...'
        return f'{poll}: {question}'


class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='choices')
    text = models.TextField(verbose_name='Вариант ответа')

    def __str__(self):
        question = str(self.question) if len(str(self.question)) <= 20 else str(self.question)[:20] + '...'
        choice = str(self.text) if len(str(self.text)) <= 40 else str(self.text)[:40] + '...'
        return f'{question}: {choice}'


class Answer(models.Model):
    user_id = models.PositiveSmallIntegerField()
    question = models.ForeignKey(to=Question, on_delete=models.DO_NOTHING, related_name='answers')
    text_answer = models.TextField(verbose_name='Ответ', blank=True)
    choice_answer = models.ManyToManyField(to=Choice, blank=True, null=True)
