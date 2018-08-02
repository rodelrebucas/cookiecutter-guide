# script thats runs before generating the project
# can be a pre check for the variables
# must return non zero to success generating project files
# e.g. directory_name

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.directory_name}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The directory_name (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

#Exit to cancel project
sys.exit(1)