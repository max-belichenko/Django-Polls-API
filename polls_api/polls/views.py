from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    Poll,
    Question,
    Choice,
    Answer,
)
from .serializers import (
    PollSerializer,
    QuestionSerializer,
    ChoiceSerializer,
    AnswerSerializer,
)


class IsGetOrIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':     # Не запрашивать аутентификацию, если пришёл GET-запрос
            return True
        else:                           # Запрашивать аутентификацию для всех остальных типов запросов
            return bool(request.user and request.user.is_staff)


class PollView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PollSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            poll_object = serializer.save()

            return Response({'success': f'Poll {poll_object} created successfully'})


class PollDetailsView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, pk):
        poll_object = get_object_or_404(Poll.objects.all(), pk=pk)
        poll_serializer = PollSerializer(poll_object)
        questions = Question.objects.filter(poll=pk)
        questions_serializer = QuestionSerializer(questions, many=True)

        return Response({'poll': poll_serializer.data, 'questions': questions_serializer.data})

    def put(self, request, pk):
        poll_object = get_object_or_404(Poll.objects.all(), pk=pk)
        serializer = PollSerializer(instance=poll_object, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            poll_object = serializer.save()

            return Response({'success': f'Poll {poll_object} updated successfully'})

    def delete(self, request, pk):
        poll_object = get_object_or_404(Poll.objects.all(), pk=pk)
        poll_object.delete()

        return Response({'message': f'Poll with id {pk} has been deleted'}, status=204)


class QuestionView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, poll_pk):
        questions = Question.objects.filter(poll=poll_pk)
        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data)

    def post(self, request, poll_pk):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            question_object = serializer.save()

            return Response({'success': f'Question {question_object} created successfully'})


class QuestionDetailsView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, poll_pk, pk):
        question_object = get_object_or_404(Question.objects.all(), pk=pk)
        question_serializer = QuestionSerializer(question_object)
        choices = Choice.objects.filter(question=pk)
        choices_serializer = ChoiceSerializer(choices, many=True)

        return Response({'question': question_serializer.data, 'choices': choices_serializer.data})

    def put(self, request, poll_pk, pk):
        question_object = get_object_or_404(Question.objects.all(), pk=pk)
        serializer = QuestionSerializer(instance=question_object, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            question_object = serializer.save()

            return Response({'success': f'Question {question_object} updated successfully'})

    def delete(self, request, poll_pk, pk):
        question_object = get_object_or_404(Question.objects.all(), pk=pk)
        question_object.delete()

        return Response({'message': f'Question with id {pk} has been deleted'}, status=204)


class ChoicesView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, poll_pk, question_pk):
        choices = Choice.objects.filter(question=question_pk)
        serializer = ChoiceSerializer(choices, many=True)

        return Response(serializer.data)

    def post(self, request, poll_pk, question_pk):
        serializer = ChoiceSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            choice_object = serializer.save()

            return Response({'success': f'Choice {choice_object} created successfully'})


class ChoiceDetailsView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, poll_pk, question_pk, pk):
        choice_object = get_object_or_404(Choice.objects.all(), pk=pk)
        choice_serializer = ChoiceSerializer(choice_object)

        return Response({'choice': choice_serializer.data})

    def put(self, request, poll_pk, question_pk, pk):
        choice_object = get_object_or_404(Choice.objects.all(), pk=pk)
        serializer = ChoiceSerializer(instance=choice_object, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            choice_object = serializer.save()

            return Response({'success': f'Choice {choice_object} updated successfully'})

    def delete(self, request, poll_pk, question_pk, pk):
        choice_object = get_object_or_404(Choice.objects.all(), pk=pk)
        choice_object.delete()

        return Response({'message': f'Choice with id {pk} has been deleted'}, status=204)


class AnswerView(APIView):

    def get(self, request, user_id):
        answers = Answer.objects.filter(user_id=user_id)
        serializer = AnswerSerializer(answers, many=True)

        return Response(serializer.data)

    def post(self, request, pk):
        serializer = AnswerSerializer(data=request.data, many=True)

        if serializer.is_valid(raise_exception=True):
            answer_object = serializer.save()

            return Response({'success': f'Answer {answer_object} created successfully'})