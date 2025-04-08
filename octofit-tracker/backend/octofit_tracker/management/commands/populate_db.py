from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
# Adjust the import path for sample_data
from octofit_tracker.sample_data import get_test_data
from bson import ObjectId
# Import timedelta for duration conversion
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Get test data
        test_data = get_test_data()

        # Create users
        users = [User(**user) for user in test_data['users']]
        User.objects.bulk_create(users)

        # Create teams and assign members
        teams = [Team(**team) for team in test_data['teams']]
        Team.objects.bulk_create(teams)
        # Fix the assignment of members to teams
        for team in Team.objects.all():
            team.members.add(*User.objects.all())

        # Create activities
        activities = [
            Activity(**{**activity, 'user': User.objects.first(), 'duration': timedelta(hours=int(activity['duration'].split(':')[0]), minutes=int(activity['duration'].split(':')[1]))})
            for activity in test_data['activities']
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(**{**entry, 'user': User.objects.first()})
            for entry in test_data['leaderboard']
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [Workout(**workout) for workout in test_data['workouts']]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
