from helper_functions import *
from constants import *

class FWtoCSV:
    """
    This is class for converting fixed width documents to CSV

    Attributes:
        None
    """
    def __init__(self, first_name, last_name, street, city, state, zip_code, phone):
        """ creating a constructor to assign input data to parameters """
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

    def return_full_name(self):
        """
        Takes in string object for full name
        If string is padded by any punctuations, it gets removed
        :returns: string
        """

        for char in self.first_name:
            if char in string.punctuation:
                self.first_name = self.first_name.replace(char, '')
        f_name = self.first_name

        for char in self.last_name:
            if char in string.punctuation:
                self.last_name = self.last_name.replace(char, '')
        l_name = self.last_name

        return f_name + ' ' + l_name + DELIMITER

    def return_first_name(self):
        """
        Takes in string object for first name.
        If string is padded by any punctuations, it gets removed
        :return: string
        """
        return remove_punctuations(self.first_name)
        # return self.first_name + DELIMITER

    def return_last_name(self):
        """
        Takes in string object for last name.
        If string is padded by any punctuations, it gets removed
        :return: string
        """

        return remove_punctuations(self.last_name)

    def return_street(self):
        """
        Takes in string object for street.
        If string is padded by any punctuations, it gets removed
        :return: string
        """

        return remove_punctuations(self.street)

    def return_city(self):
        """
        Takes in string object for city.
        If string is padded by any punctuations, it gets removed
        :return: string
        """

        return remove_punctuations(self.city)

    def return_state(self):
        """
        Takes in two letter abbreviated state name.
        Returns full state name.
        :return: string
        """

        return abbrev_to_state(self.state) + DELIMITER

    def return_zip(self):
        """
        Takes in string object for zip.
        :return: string
        """

        return str(self.zip_code) + DELIMITER

    def return_phone(self):
        """
        Takes in string object for phone and returns phone with dashes.
        :return: string
        """

        phone = '-'.join([self.phone[:3], self.phone[4:7], self.phone[6:]])
        return str(phone)
