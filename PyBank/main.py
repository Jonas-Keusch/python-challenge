import os
import csv

CSV_PATH = os.path.join('Resources', 'budget_data.csv')

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile: