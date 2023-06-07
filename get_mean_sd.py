
import argparse
import pandas as pd

HELPTEXT='''
Read in a .csv with age and grip strength columns and print the mean / std
'''

## parse intputs
parser = argparse.ArgumentParser(description=HELPTEXT)
parser.add_argument('--csv', help='path to global .csv file', required=True)

## extract arguments
args = parser.parse_args()

## extract the input
input = args.csv

## load the data 
df = pd.read_csv(input)

## compute the mean
mnAge = df['age'].mean()
mnGst = df['grip_strength'].mean()

## compute the std
sdAge = df.['age'].std()
sdGst = df['grip_strength'].std()

## print the output
print(f"Mean +/- std Age:           {mnAge} +/- {sdAge}")
print(f"Mean +/- std Grip Strength: {mnGst} +/- {sdGst}")

