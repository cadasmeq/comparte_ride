"""Circle App Extra Functions"""
# python
import csv

# model
from cride.circles.models import Circle


def load_data(csv_file):
    '''Load Circles Data from CSV File'''
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            circle = Circle(**row)
            circle.save()
            print(circle.name)