from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel),
            User.objects.create_user(email='captain@marvel.com', username='captain', team=marvel),
            User.objects.create_user(email='batman@dc.com', username='batman', team=dc),
            User.objects.create_user(email='superman@dc.com', username='superman', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30),
            Activity.objects.create(user=users[1], type='cycle', duration=45),
            Activity.objects.create(user=users[2], type='swim', duration=60),
            Activity.objects.create(user=users[3], type='walk', duration=20),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout'),
            Workout.objects.create(name='Strength Builder', description='Strength training routine'),
        ]

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
