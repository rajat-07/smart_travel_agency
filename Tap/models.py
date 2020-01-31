from django.db import models
from jsonfield import JSONField

class City(models.Model):
    name = models.CharField(max_length=20)
    places = JSONField()
    hotels = JSONField()

'''
City = {
    'name' : 'abc',
    'places' : [
        {
            'name' : 'aaa',
            'desc' : 'bbb',
            'reviews' : [
                {
                    'text' : 'balskcjasvsjs',
                    'rating' : 8,
                }
                {
                    'text' : 'balskcjasvsjs',
                    'rating' : 8
                }
            ]
        }
    ]
    'hotels' : [
        {
            'name' : 'aaa',
            'desc' : 'bbb',
            'costperday' : 1910,
            'reviews' : [
                'review1' : {
                    'text' : 'balskcjasvsjs',
                    'rating' : 8,
                }
                'review2' : {
                    'text' : 'balskcjasvsjs',
                    'rating' : 8,
                }
            ]
        }
    ]
}

[{'name' : 'aaa','desc' : 'bbb','costperday' : 1910,'reviews' : ['review1' : {'text' : 'balskcjasvsjs','rating' : 8,},'review2' : {'text' : 'balskcjasvsjs','rating' : 8,}]} ]
'''
