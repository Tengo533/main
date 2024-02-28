#Python has a build in ‘logging’ module for creating log files.
import math
import logging

# Log levels: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL

# Configure logger to log any msgs with level greater than debug

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "my_log.txt",

level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')

# create route logger

logger = logging.getLogger()

# test logging msgs to log file


def quadratic_equation(a, b, c):
    logger.debug(f"Passed in values: A={a}, B={b}, C={c}")
    logger.debug("#discriminant")
    #calculate discriminant
    discrim = ((b**2) - 4(a)(c))
    
    value1 = (-b + math.sqrt(discrim))/2(a)
    logger.debug("#calculate value 1")
    # calculate value 1
    value2 = (-b - math.sqrt(discrim))/2(a)
    # calculate value 2
    logger.debug("#calculate value 2")
    return (value1, value2)

value = quadratic_equation(1,2,3)
print(value)