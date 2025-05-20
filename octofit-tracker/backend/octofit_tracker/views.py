from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET', 'POST'])
def api_root(request, format=None):
    base_urls = [
        'https://zany-engine-74qqxqx6rxxhwr9r-8000.app.github.dev/',
        'http://localhost:8000/'
    ]
    return Response({
        'users': [base_url + 'api/users/?format=api' for base_url in base_urls],
        'teams': [base_url + 'api/teams/?format=api' for base_url in base_urls],
        'activities': [base_url + 'api/activities/?format=api' for base_url in base_urls],
        'leaderboard': [base_url + 'api/leaderboard/?format=api' for base_url in base_urls],
        'workouts': [base_url + 'api/workouts/?format=api' for base_url in base_urls]
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
