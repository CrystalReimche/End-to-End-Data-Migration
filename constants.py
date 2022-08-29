import configparser


def read_config():
    """
    Creates a ConfigParser object
    :return: obj
    """
    config = configparser.ConfigParser()
    config.read('inputconfig.ini')
    return config


config = read_config()

FIXEDWIDTH = config['BOOLFIXEDWIDTH']['fixed_width']


if config['HEADER']['CREATE_HEADER'] == 'false':
    INCLUDES_HEADER = header = None

if config['DELIMITER']['delimiter'] == 'space':
    DELIMITER = ' '
else:
    DELIMITER = config['DELIMITER']['delimiter']

# Creating constants for each field fixed width

# Header
H_FULL_NAME = config['HEADER']['FULL_NAME']
H_FIRST_NAME = config['HEADER']['FIRST_NAME']
H_LAST_NAME = config['HEADER']['LAST_NAME']
H_STREET = config['HEADER']['STREET']
H_CITY = config['HEADER']['CITY']
H_STATE = config['HEADER']['STATE']
H_ZIP = config['HEADER']['ZIP']
H_PHONE = config['HEADER']['PHONE']

# Full Name
SPLIT_FULL_NAME = config['FULLNAME']['SPLIT_FULL_NAME']
FULL_NAME = int(config['FULLNAME']['FULL_NAME'])
FULLNAME_PADDING_SIDE = config['FULLNAME']['PADDING_SIDE']
if config['FULLNAME']['PADDING_CHAR'] == 'space':
    FULLNAME_PADDING_CHAR = ' '
else:
    FULLNAME_PADDING_CHAR = config['FULLNAME']['PADDING_CHAR']

# First Name
FIRST_NAME = int(config['FIRSTNAME']['FIRST_NAME'])
FN_PADDING_SIDE = config['FIRSTNAME']['PADDING_SIDE']
if config['FIRSTNAME']['PADDING_CHAR'] == 'space':
    FN_PADDING_CHAR = ' '
else:
    FN_PADDING_CHAR = config['FIRSTNAME']['PADDING_CHAR']

# Last Name
LAST_NAME = int(config['LASTNAME']['LAST_NAME'])
LN_PADDING_SIDE = config['LASTNAME']['PADDING_SIDE']
if config['LASTNAME']['PADDING_CHAR'] == 'space':
    LN_PADDING_CHAR = ' '
else:
    LN_PADDING_CHAR = config['LASTNAME']['PADDING_CHAR']

# Street
STREET = int(config['STREET']['STREET'])
STR_PADDING_SIDE = config['STREET']['PADDING_SIDE']
if config['STREET']['PADDING_CHAR'] == 'space':
    STR_PADDING_CHAR = ' '
else:
    STR_PADDING_CHAR = config['STREET']['PADDING_CHAR']

# City
CITY = int(config['CITY']['CITY'])
C_PADDING_SIDE = config['CITY']['PADDING_SIDE']
if config['CITY']['PADDING_CHAR'] == 'space':
    C_PADDING_CHAR = ' '
else:
    C_PADDING_CHAR = config['CITY']['PADDING_CHAR']

# State
STATE = int(config['STATE']['STATE'])
STATE_PADDING_SIDE = config['STATE']['PADDING_SIDE']
if config['STATE']['PADDING_CHAR'] == 'space':
    STATE_PADDING_CHAR = ' '
else:
    STATE_PADDING_CHAR = config['STATE']['PADDING_CHAR']

# Zip
ZIP = int(config['ZIPCODE']['ZIP'])
ZIP_PADDING_SIDE = config['ZIPCODE']['PADDING_SIDE']
if config['ZIPCODE']['PADDING_CHAR'] == 'space':
    ZIP_PADDING_CHAR = ' '
else:
    ZIP_PADDING_CHAR = config['ZIPCODE']['PADDING_CHAR']

# Phone
PHONE = int(config['PHONE']['PHONE'])
PHONE_PADDING_SIDE = config['PHONE']['PADDING_SIDE']
if config['PHONE']['PADDING_CHAR'] == 'space':
    PHONE_PADDING_CHAR = ' '
else:
    PHONE_PADDING_CHAR = config['PHONE']['PADDING_CHAR']
PHONE_STRIP_CHAR = config['PHONE']['STRIP_CHAR']
if config['PHONE']['REPLACE_CHAR_WITH'] == 'no space':
    PHONE_REPLACE_CHAR = ''
else:
    PHONE_REPLACE_CHAR = config['PHONE']['REPLACE_CHAR_WITH']
