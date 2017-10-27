from django.db import models
from ..login_app.models import User, UserManager

import datetime  



class TripManager(models.Manager):
    print('================VALIDATING TRIP==================')
    def validate(self, post_data, user_id):
        print(post_data)
        errors = []
        if len(post_data['destination']) < 2 or len(post_data['description']) < 2:
            errors.append('Destination and description must be filled out!')

        if post_data['from_date'] == '' or post_data['to_date'] == '':
            errors.append('From and to date must be completed')

        # fromDate = post_data['from_date'].str
        # if post_data['from_date'] == '' or datetime.datetime.strptime(post_data['date'], '%Y-%m-%d') < datetime.datetime.now():
        #     errors.append("The past is gone! Set date for the future :)...")
        today = datetime.datetime.now()
        today = datetime.datetime.strftime(today, '%Y-%m-%d' )

        print(today)
        print(post_data['to_date'])

        if post_data['from_date'] < today or post_data['to_date'] < post_data['from_date']:
            errors.append('Invalid Scheduling!')

        if not errors:
            user = User.objects.get(id=user_id)
            new_trip = Trip.objects.create(destination=post_data['destination'], description=post_data['description'], 
                                            from_date=post_data['from_date'], to_date=post_data['to_date'])

            new_trip.users.add(user)
            print('User ID: {}'.format(user))
            print(new_trip)
            return new_trip
        print(errors)
        return errors
        



class Trip(models.Model):
    users = models.ManyToManyField(User, related_name='trips')
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = TripManager()


