import logging
# to change the basic congiuration ->
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%y %H:%M:%S')
                    # this is from the python documentation
# loggin levels:
logging.debug("This is a debug message")
logging.info("this is an info message")
logging.warning("This is a warning message")
logging.error("this is an error message")
logging.critical("This is a critical message")

#  they indicate the severity of the events

# to stop propagation -> logger.propagae = False

# this is a complex topic that needs futher studying. will touch on it next week.

# capturing stack trace. useful for troubleshooting issues:
try:
    a = [1, 2, 3]
    val = a[4] # this will raise an index error
except IndexError as e:
    # logging.error(e)
    logging.error(e, exc_info= True)


# if we don't know what kind of error we raise but want to have the traceback:
import traceback

try:
    a = [1, 2, 3]
    val = a[4] 
except:
    logging.error("the errir is %s", traceback.format_exc())

