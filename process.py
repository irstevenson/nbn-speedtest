#!/usr/bin/python

import csv
import json

def process_file( filename ):
    times = set()
    date_values = dict()

    with open( filename, 'rb' ) as csvfile:
        last_row_details = ('', '', '0')

        reader = csv.reader( csvfile )
        next( reader, None ) # skip header row
        for row in reader:
            # process the row
            try:
                row_details = process_row( row, 6 )
            except IndexError: # bad row in CSV - probably due to capture error
                # Bit dodge, as we'll have duplicate entry for a timeslot,
                # however at least we'll have a full set for a day (probably)
                row_details = (last_row_details[0], last_row_details[1], '0')
            else:
                last_row_details = row_details

            # reduce the results
            times.add( row_details[1] )
            date_str = row_details[0]
            value = float( row_details[2] )
            if date_str not in date_values:
                date_values[date_str] = [ value ]
            else:
                date_values[date_str].append( value )

    sorted_values = []
    sorted_dates = sorted( date_values.keys() ) 
    for k in sorted_dates:
        sorted_values.append( date_values[k] )

    return { 'z': sorted_values, # sorted by date
             'y': sorted_dates,
             'x': sorted( times ) }

def process_row( row, value_col ):
    """
    Looks at a processed CSV row returning the date, time and
    then value of the specified column.
    """
    date_time = row[3].split('T')
    # [:5] so that we just get hh:mm
    return (date_time[0], date_time[1][:5], row[value_col])

# !! DELETE ME !!
def quick_test():
    row  = ['2167', 'Internode', 'Hobart', '2017-01-24T23:00:01.949596', '9.757502716624701', '8.346', '23280669.80028002', '3885850.466667056']
    print process_row( row, 6 )

def main():
    #quick_test()
    print json.dumps(
        process_file( 'speedtest.csv' ),
        sort_keys=True, indent=4, separators=(',', ': ') )

if __name__ == '__main__': main()
