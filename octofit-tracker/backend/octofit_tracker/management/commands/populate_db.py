from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data
from bson import ObjectId

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
        for team, user in zip(teams, users):
            team.members.add(user)

        # Create activities
        activities = [
            Activity(_id=activity['_id'], user=users[i % len(users)], activity_type=activity['activity_type'], duration=activity['duration'])
            for i, activity in enumerate(test_data['activities'])
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=entry['_id'], user=users[i % len(users)], score=entry['score'])
            for i, entry in enumerate(test_data['leaderboard'])
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [Workout(**workout) for workout in test_data['workouts']]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
