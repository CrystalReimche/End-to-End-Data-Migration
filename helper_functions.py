import string

from constants import *


def write_all_rows(output_file, class_name):
    """
    Writing each row into output file
    :param output_file: file name that is being written to
    :param class_name: class object
    :return: string
    """

    # Check if full name will be split
    if config.getboolean('FULLNAME', 'SPLIT_FULL_NAME'):
        output_file.write(class_name.return_first_name())
        output_file.write(class_name.return_last_name())
    else:
        output_file.write(class_name.return_full_name())
    output_file.write(class_name.return_street())
    output_file.write(class_name.return_city())
    output_file.write(class_name.return_state())
    output_file.write(class_name.return_zip())
    output_file.write(class_name.return_phone())
    output_file.write('\n')


def write_fullname_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > FULL_NAME:
        return self[0:FULL_NAME]
    elif char_count < FULL_NAME:
        if FULLNAME_PADDING_SIDE == 'left':
            return self.rjust(FULL_NAME, ' ')
        else:
            return self.ljust(FULL_NAME, ' ')
    else:
        return self


def write_firstname_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > FIRST_NAME:
        return self[0:FIRST_NAME]
    elif char_count < FIRST_NAME:
        if FN_PADDING_SIDE == 'left':
            return self.rjust(FIRST_NAME, ' ')
        else:
            return self.ljust(FIRST_NAME, ' ')
    else:
        return self


def write_lastname_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > LAST_NAME:
        return self[0:LAST_NAME]
    elif char_count < LAST_NAME:
        if LN_PADDING_SIDE == 'left':
            return self.rjust(LAST_NAME, ' ')
        else:
            return self.ljust(LAST_NAME, ' ')
    else:
        return self


def write_street_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > STREET:
        return self[0:STREET]
    elif char_count < STREET:
        if STR_PADDING_CHAR == 'left':
            return self.rjust(STREET, ' ')
        else:
            return self.ljust(STREET, ' ')
    else:
        return self


def write_city_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > CITY:
        return self[0:CITY]
    elif char_count < CITY:
        if C_PADDING_SIDE == 'left':
            return self.rjust(CITY, ' ')
        else:
            return self.ljust(CITY, ' ')
    else:
        return self


def write_state_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > STATE:
        return self[0:STATE]
    elif char_count < STATE:
        if STATE_PADDING_SIDE == 'left':
            return self.rjust(STATE, ' ')
        else:
            return self.ljust(STATE, ' ')
    else:
        return self


def write_zip_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > ZIP:
        return self[0:ZIP]
    elif char_count < ZIP:
        if ZIP_PADDING_SIDE == 'left':
            return self.rjust(ZIP, ' ')
        else:
            return self.ljust(ZIP, ' ')
    else:
        return self


def write_phone_header(self):
    """
    Take header string name, applies user defined padding side
    :param self: header string name
    :return: string
    """

    char_count = get_char_count(self)
    if char_count > PHONE:
        return self[0:PHONE]
    elif char_count < PHONE:
        if PHONE_PADDING_SIDE == 'left':
            return self.rjust(PHONE, ' ')
        else:
            return self.ljust(PHONE, ' ')
    else:
        return self


def setup_fixwidth_columns():
    """
    Creates a list of integer tuples based on column widths specified in .ini file.
    For example: [(0, 15), (16, 26), (27, 57), (58, 78)]
    :return: list of int tuples
    """

    return [(0, FIRST_NAME),
            (FIRST_NAME + 1, FIRST_NAME + 1 + LAST_NAME),
            (FIRST_NAME + LAST_NAME + 2, FIRST_NAME + LAST_NAME + 2 + STREET),
            (FIRST_NAME + LAST_NAME + STREET + 3, FIRST_NAME + LAST_NAME + STREET + 3 + CITY),
            (FIRST_NAME + LAST_NAME + STREET + CITY + 4, FIRST_NAME + LAST_NAME + STREET + CITY + 4 + STATE),
            (FIRST_NAME + LAST_NAME + STREET + CITY + STATE + 5,
             FIRST_NAME + LAST_NAME + STREET + CITY + STATE + 5 + ZIP),
            (FIRST_NAME + LAST_NAME + STREET + CITY + STATE + ZIP + 6,
             FIRST_NAME + LAST_NAME + STREET + CITY + STATE + ZIP + 6 + PHONE)]


def check_space(self):
    """ Counts how many spaces there are in the given string
    :param self: string obj
    :return: int of spaces in string obj
    """

    count = 0
    # loop through each char until it reaches the end of the given string
    for i in range(0, len(self)):
        # Check each char if space or not
        if self[i] == " ":
            # If there is a space, increase counter
            count += 1
    return count


def get_char_count(self):
    """
    Counts how many characters within the given string
    :param self: string obj
    :return: int
    """

    count = 0
    for _ in self:
        count += 1
    return count


def remove_hyphen(self, strip, replace_with):
    """
    Replaces a specified character with another specified character
    :param self: string obj
    :param strip: single char
    :param replace_with: single char
    :return: string
    """

    return self.replace(strip, replace_with)


def remove_punctuations(self):
    """
    Removes the following punctuation from string: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
    :param self: string obj
    :return: string
    """
    for char in self:
        if char in string.punctuation:
            self = self.replace(char, '')
    return self + DELIMITER


def state_to_abbrev(self):
    """
    Returns two letter abbreviation of given state
    :param self: string obj
    :return: string
    """

    if self in us_state_to_abbrev:
        return us_state_to_abbrev.get(self)
    else:
        return STATE_PADDING_CHAR * 2


def abbrev_to_state(self):
    """
    Returns full state name by passing in the two letter abbreviation of given state
    :param self: string obj
    :return: string
    """

    full_state = dict((v, k) for k, v in us_state_to_abbrev.items())
    if self in full_state:
        return full_state.get(self)
    else:
        return STATE_PADDING_CHAR * 2


# dictionary containing all US territories and the respected abbreviation
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
