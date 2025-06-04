class NegativeNumberException(Exception):
    """Exception raised for errors in the input if it is a negative number."""
    
    def __init__(self, value,message="Negative number is not allowed."):
        self.value = value
        self.message = message
        super().__init__(f"{message} Value: {value}")
    
   