import logging
import sys

# Function to format error messages
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom Exception Class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Test Exception Handling
if __name__ == "__main__":
    try:
        a = 1 / 0  # Causes ZeroDivisionError
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(str(e), sys)  # Pass the string message


        
