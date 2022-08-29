import csv
import fw_to_csv
from constants import *
import csv_to_fw
import pandas as pd
from helper_functions import *


def main():
    # check if input file is fixed width
    if not config.getboolean('BOOLFIXEDWIDTH', 'fixed_width'):
        # CSV input file name
        user_file = 'Sample Run - CSV to FW\\csv.csv'
        # fixed width output file name
        output_file = 'Sample Run - CSV to FW\\fix_width_output.txt'

        # open and read input file
        with open(user_file, 'r') as csv_file:
            # check if user wants a header created
            if config.getboolean('HEADER', 'CREATE_HEADER'):
                # open and write headers to output file
                with open(output_file, 'w') as final_file:
                    if config.getboolean('FULLNAME', 'SPLIT_FULL_NAME'):
                        final_file.write(write_firstname_header(H_FIRST_NAME))
                        final_file.write(write_lastname_header(H_LAST_NAME))
                    else:
                        final_file.write((write_fullname_header(H_FULL_NAME)))
                    final_file.write(write_street_header(H_STREET))
                    final_file.write(write_city_header(H_CITY))
                    final_file.write(write_state_header(H_STATE))
                    final_file.write(write_zip_header(H_ZIP))
                    final_file.write(write_phone_header(H_PHONE))
                    final_file.write('\n')
                # open and append to output file
                with open(output_file, 'a') as final_file:
                    # create a csv reader object and pass in the input file and the delimiter set in .ini file
                    csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
                    # iterate every row - each row is a list
                    for line in csv_reader:
                        # pass each element of the list into the class
                        csvtofw = csv_to_fw.CSVtoFW(line[0], line[1], line[2], line[3], line[4], line[5])
                        # call each method from the CSVtoFW object and write the return to the output file
                        write_all_rows(final_file, csvtofw)
            else:
                # open and write to output file
                with open(output_file, 'w') as final_file:
                    # create a csv reader object and pass in the input file and the delimiter set in .ini file
                    csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
                    # iterate every row - each row is a list
                    for line in csv_reader:
                        # pass each element of the list into the class
                        csvtofw = csv_to_fw.CSVtoFW(line[0], line[1], line[2], line[3], line[4], line[5])
                        # call each method from the CSVtoFW object and write the return to the output file
                        write_all_rows(final_file, csvtofw)
    # else input file is fixed width
    else:
        # fixed width input file name
        fw_user_file = 'Sample Run - FW to CSV\\fixwidth.txt'
        # temporary file that pandas writes to
        pandas_fw_to_csv_output_file = 'new.txt'
        # list of int tuples that specify where each column starts and ends
        col_specification = setup_fixwidth_columns()
        # pandas reading fixed width file and storing the data frame
        data = pd.read_fwf(fw_user_file, sep=DELIMITER, header=None, colspecs=col_specification)

        # write data frame to temporary file in CSV format using the user specified delimiter
        data.to_csv(pandas_fw_to_csv_output_file, sep=DELIMITER, index=False, header=None)

        # final output file
        fw_to_csv_output_file = 'Sample Run - FW to CSV\\FW_to_CSV.txt'

        # open and read temporary CSV file written by pandas
        with open(pandas_fw_to_csv_output_file, 'r') as csv_file:
            # open and write to final output file
            with open(fw_to_csv_output_file, 'w') as final_file:
                # create a csv reader object, pass in the temporary file and the delimiter set in .ini file
                csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
                # if header is to be created on output file
                if config.getboolean('HEADER', 'CREATE_HEADER'):
                    # write headers
                    if config.getboolean('FULLNAME', 'SPLIT_FULL_NAME'):
                        final_file.write(H_FIRST_NAME + DELIMITER)
                        final_file.write(H_LAST_NAME + DELIMITER)
                    else:
                        final_file.write(H_FULL_NAME + DELIMITER)
                    final_file.write(H_STREET + DELIMITER)
                    final_file.write(H_CITY + DELIMITER)
                    final_file.write(H_STATE + DELIMITER)
                    final_file.write(H_ZIP + DELIMITER)
                    final_file.write(H_PHONE)
                    final_file.write('\n')
                    # iterate every row - each row is a list
                    for line in csv_reader:
                        # pass each element of the list into the class
                        fwtocsv = fw_to_csv.FWtoCSV(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                        # call each method from the FWtoCSV object and write the return to the output file
                        write_all_rows(final_file, fwtocsv)

                else:
                    # iterate every row - each row is a list
                    for line in csv_reader:
                        # pass each element of the list into the class
                        fwtocsv = fw_to_csv.FWtoCSV(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                        # call each method from the FWtoCSV object and write the return to the output file
                        write_all_rows(final_file, fwtocsv)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
