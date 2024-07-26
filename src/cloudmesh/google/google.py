class Google:
    """
    Google Class

    This class provides basic functionality for the Google class.

    Methods:
        - __init__(): Initialize the Google class.
        - list(parameter): Print a message indicating a list operation with the provided parameter.

    Usage:
        google_instance = Google()

        # Initialize the Google class
        google_instance.__init__()

        # Perform a list operation
        google_instance.list("example_parameter")

    Author:
        Your Name
    """

    def __init__(self):
        """
        Initialize the Google class.

        This method prints an initialization message with the class name.

        Args:
            None

        Returns:
            None
        """
        print("init {name}".format(name=self.__class__.__name__))

    def list(self, parameter):
        """
        Perform a list operation.

        This method prints a message indicating a list operation along with the provided parameter.

        Args:
            parameter (str): The parameter for the list operation.

        Returns:
            None
        """
        print("list", parameter)
