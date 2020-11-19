from django.urls import path

from .views import (
    PollView,
    PollDetailsView,
    QuestionView,
    QuestionDetailsView,
    ChoicesView,
    ChoiceDetailsView,
    AnswerView
)


app_name = "polls_api"

urlpatterns = [
    # polls/ GET - Список всех опросов
    # polls/ POST - Создать новый опрос
    path('polls/', PollView.as_view()),

    # polls/<int:pk>/ GET - Детальная информация об опросе
    # polls/<int:pk>/ PUT - Изменить опрос
    # polls/<int:pk>/ DELETE - Удалить опрос
    path('polls/<int:pk>/', PollDetailsView.as_view()),

    # polls/<int:poll_pk>/questions/ GET - Список всех вопросов в указанном опросе
    # polls/<int:poll_pk>/questions/ POST - Создать новый вопрос
    path('polls/<int:poll_pk>/questions/', QuestionView.as_view()),

    # polls/<int:poll_pk>/questions/<int:pk>/ GET - Детальная информация о вопросе
    # polls/<int:poll_pk>/questions/<int:pk>/ PUT - Изменить вопрос
    # polls/<int:poll_pk>/questions/<int:pk>/ DELETE - Удалить вопрос
    path('polls/<int:poll_pk>/questions/<int:pk>/', QuestionDetailsView.as_view()),

    # polls/<int:poll_pk>/questions/<int:question_pk>/choices/ GET - Список всех вариантов ответов выбранного вопроса
    # polls/<int:poll_pk>/questions/<int:question_pk>/choices/ POST - Создать новый вариант ответа
    path('polls/<int:poll_pk>/questions/<int:question_pk>/choices/', ChoicesView.as_view()),

    # polls/<int:poll_pk>/questions/<int:question_pk>/choices/<int:pk>/ GET - Детальная информация о варианте ответа
    # polls/<int:poll_pk>/questions/<int:question_pk>/choices/<int:pk>/ PUT - Изменить вариант ответа
    # polls/<int:poll_pk>/questions/<int:question_pk>/choices/<int:pk>/ DELETE - Удалить вариант ответа
    path('polls/<int:poll_pk>/questions/<int:question_pk>/choices/<int:pk>/', ChoiceDetailsView.as_view()),

    # answers/<int:user_id>/ GET - Список всех ответов на опросы для указанного пользователя
    path('answers/<int:user_id>/', AnswerView.as_view()),

    # polls/<int:pk>/answer/ POST - Отправить ответы на опрос
    path('polls/<int:pk>/answer/', AnswerView.as_view()),
]