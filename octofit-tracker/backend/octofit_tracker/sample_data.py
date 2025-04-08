from octofit_tracker.models import User, Team, Activity, Workout

def create_sample_data():
    # Create sample users
    user1 = User.objects.create(username="john_doe", email="john@example.com", first_name="John", last_name="Doe")
    user2 = User.objects.create(username="jane_smith", email="jane@example.com", first_name="Jane", last_name="Smith")

    # Create sample teams
    team1 = Team.objects.create(name="Team Alpha", description="A high-performing team")
    team2 = Team.objects.create(name="Team Beta", description="A team of beginners")

    # Assign users to teams
    team1.members.add(user1)
    team2.members.add(user2)

    # Create sample activities
    activity1 = Activity.objects.create(name="Running", description="Outdoor running activity")
    activity2 = Activity.objects.create(name="Cycling", description="Outdoor cycling activity")

    # Create sample workouts
    Workout.objects.create(user=user1, activity=activity1, duration_minutes=30, calories_burned=300)
    Workout.objects.create(user=user2, activity=activity2, duration_minutes=45, calories_burned=450)

    print("Sample data created successfully!")

if __name__ == "__main__":
    create_sample_data()