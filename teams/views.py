from rest_framework.views import APIView, status, Request, Response
from utils import data_processing
from .models import Team
from django.forms.models import model_to_dict

class TeamView(APIView):
    def post(self, req: Request) -> Response:
        try: 
            data_processing(req.data)
        except Exception as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)

            
        team = Team.objects.create(**req.data)
        converted_teams = model_to_dict(team)
        return Response(converted_teams, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        converted_teams = []
        for team in teams:
            converted_team = model_to_dict(team)
            converted_teams.append(converted_team)
        return Response(converted_teams, status.HTTP_200_OK)
    
class TeamDetailView(APIView):
    def get(self, res: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        converted_team = model_to_dict(found_team)
        return Response(converted_team)
    
    def delete(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        found_team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        for key, value in req.data.items():
            setattr(found_team, key, value)
        found_team.save()
        converted_team = model_to_dict(found_team)
        return Response(converted_team)
        