from cloudmesh.common.Shell import Shell
from cloudmesh.common.console import Console
import json
from pprint import pprint
import yaml

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
        pass

    def list(self, directory, csv=False, c=","):    
        """
        Perform a list operation.

        This method prints a message indicating a list operation along with the provided parameter.

        Args:
            parameter (str): The parameter for the list operation.

        Returns:
            None
        """
        r = self.info(directory, kind="json")
        output = ""

        len_path = 0
        len_size = 0
        len_id = 0
        for item in r:
            try:
                len_path = max(len(str(item['Path'])), len_path)
                len_size = max(len(str(item['Size'])), len_size)
                len_id = max(len(str(item['ID'])), len_id)
            except:
                Console.error (f"error in entry {item}")         
        

        for item in r:
            try:
                path = item['Path']
                size = item['Size']
                id = item['ID']
                if csv:
                    output += f"{path}{c}{size}{c}{id}\n"
                else:
                    output += f"{path.ljust(len_path)}  {str(size).ljust(len_size)} {id.ljust(len_id)}\n"
                
            except:
                Console.error (f"error in entry {item}")         
        return output


    def info(self, directory, kind="yaml"): 
        """
        Perform a list operation.

        This method prints a message indicating a list operation along with the provided parameter.

        Args:
            parameter (str): The parameter for the list operation.

        Returns:
            None
        """
        print("list", directory, kind)

        if directory.startswith("drive:"):
            pass
        else:
            directory = f"drive:{directory}"

        try:
            r = Shell.run(f"rclone --drive-shared-with-me lsjson '{directory}'")
        except Exception as e:
            print()
            Console.error(f"Directory '{directory}' not found.")
            print()
            return ""
        print (r)
        data = json.loads(r)
    
        if kind == "yaml":
            output = yaml.dump(data, default_flow_style=False)
            data = output
        else:
            pass
        return data
        

