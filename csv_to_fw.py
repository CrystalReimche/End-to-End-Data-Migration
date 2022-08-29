from helper_functions import *
from constants import *


class CSVtoFW:
    """
    This is a class for converting CSV to fixed width documents

    Attributes:
        None
    """

    def __init__(self, full_name, street, city, state, zip_code, phone):
        """
        creating a constructor to assign input data to parameters
        Args:
            full_name: string
            street: string
            city: string
            state: string
            zip_code: string
            phone: string
        """

        self.full_name = full_name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

    def return_full_name(self):
        """
        Counts characters in first element.
        If char count > column width (defined in .ini file), truncate.
        If char count < column width, pad left or right with given char based on .ini file
        :return: string
        """

        char_count = get_char_count(self.full_name)
        if char_count > FULL_NAME:
            return self[0:FULL_NAME]
        elif char_count < FULL_NAME:
            if FN_PADDING_SIDE == 'left':
                return self.full_name.rjust(FULL_NAME, FULLNAME_PADDING_CHAR)
            else:
                return self.full_name.ljust(FULL_NAME, FULLNAME_PADDING_CHAR)
        else:
            return self.full_name

    def return_first_name(self):
        """
        Splits the full name anywhere there is a space.
        Counts characters in first element.
        If char count > column width (defined in .ini file), truncate.
        If char count < column width, pad left or right with given char based on .ini file
        :return: string
        """

        # splits full name anywhere there is a space
        name_combo = self.full_name.split(' ')

        char_count = get_char_count(name_combo[0])
        if char_count > FIRST_NAME:
            return self[0:FIRST_NAME]
        elif char_count < FIRST_NAME:
            if FN_PADDING_SIDE == 'left':
                return name_combo[0].rjust(FIRST_NAME, FN_PADDING_CHAR)
            else:
                return name_combo[0].ljust(FIRST_NAME, FN_PADDING_CHAR)
        else:
            return name_combo[0]

    def return_last_name(self):
        """
        Counts characters in given string.
        If char count > column width (defined in .ini file), truncate.
        If char count < column width, pad left or right with given char based on .ini file
        :return: string
        """

        # returns number of spaces in company contact
        name_spaces = check_space(self.full_name)
        # splits full name anywhere there is a space
        name_combo = self.full_name.split(' ')
        # if there is only one space in the contact, return second element
        if name_spaces == 1:
            char_count = get_char_count(name_combo[1])
            if char_count > LAST_NAME:
                return self[0:LAST_NAME]
            elif char_count < LAST_NAME:
                if LN_PADDING_SIDE == 'left':
                    return name_combo[1].rjust(LAST_NAME, LN_PADDING_CHAR)
                else:
                    return name_combo[1].ljust(LAST_NAME, LN_PADDING_CHAR)
            else:
                return name_combo[1]
        else:
            char_count = get_char_count(name_combo[-1])
            if char_count > LAST_NAME:
                return self[0:LAST_NAME]
            elif char_count < LAST_NAME:
                if LN_PADDING_SIDE == 'left':
                    return name_combo[1].rjust(LAST_NAME, LN_PADDING_CHAR)
                else:
                    return name_combo[1].ljust(LAST_NAME, LN_PADDING_CHAR)
            else:
                return name_combo[1]

    def return_street(self):
        """
        Counts characters in given string.
        If char count > column width (defined in .ini file), truncate.
        If char count < column width, pad left or right with given char based on .ini file
        :return: string
        """

        char_count = get_char_count(self.street)
        if char_count > STREET:
            return self[0:STREET]
        elif char_count < STREET:
            if STR_PADDING_CHAR == 'left':
                return self.street.rjust(STREET, STR_PADDING_CHAR)
            else:
                return self.street.ljust(STREET, STR_PADDING_CHAR)
        else:
            return self.street

    def return_city(self):
        """
        Counts characters in given string.
        If char count > column width (defined in .ini file), truncate.
        If char count < column width, pad left or right with given char based on .ini file
        :return: string
        """

        char_count = get_char_count(self.city)
        if char_count > CITY:
            return self[0:CITY]
        elif char_count < CITY:
            if C_PADDING_SIDE == 'left':
                return self.city.rjust(CITY, C_PADDING_CHAR)
            else:
                return self.city.ljust(CITY, C_PADDING_CHAR)
        else:
            return self.city

    def return_state(self):
        """
        Returns two letter abbreviation of full US territory state.
        If given state is not US recognized, XX is returned.
        :return: string
        """

        return state_to_abbrev(self.state)

    def return_zip(self):
        """
        Counts characters in given string.
        If char count > column width (defined in .ini file), truncate.
        If char count < column width, pad left or right with given char based on .ini file
        :return: string
        """

        char_count = get_char_count(self.zip_code)
        if char_count > ZIP:
            return self[0:ZIP]
        elif char_count < ZIP:
            return ZIP_PADDING_CHAR * ZIP
        else:
            return self.zip_code

    def return_phone(self):
        """
        Strips specified char and replaced with specified char (defined in .ini file).
        Counts characters in given string.
        If char count > column width (defined in .ini file), truncate.
        If char count == column width, return string.
        If char count < column width, return error because missing phone digits.
        :return:
        """

        phone_stripped = remove_hyphen(self.phone, PHONE_STRIP_CHAR, PHONE_REPLACE_CHAR)
        phone_count = get_char_count(phone_stripped)
        if phone_count > PHONE:
            return self[0:PHONE]
        elif phone_count == PHONE:
            return phone_stripped
        else:
            return 'ERROR'
