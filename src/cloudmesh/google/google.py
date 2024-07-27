from cloudmesh.common.Shell import Shell
from cloudmesh.common.console import Console
import json
from pprint import pprint
import yaml
import os
from cloudmesh.common.util import readfile

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

    def url(self, id):
        return f"https://drive.google.com/file/d/{id}/view"
    
    def download(self, id, filename):
        return f"rclone copy 'drive:{id}' {filename}"
    
    def html_link(self, id, filename):
        return f'<a href="{self.url(id)}"><!-- {filename} -->'

    def __init__(self):
        """
        Initialize the Google class.

        This method prints an initialization message with the class name.

        Args:
            None

        Returns:
            None
        """
        self.cache = None
        
    def list(self, directory, format="csv", c=",", recursive=False):    
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
                url = self.url(id)
                if format == "csv":
                    output += f"{path}{c}{size}{c}{id}{c}{url}\n"
                elif format == "list":
                    output += f"{path.ljust(len_path)}  {str(size).ljust(len_size)} {id.ljust(len_id)}\n"
                elif format == "html":
                    output += self.html_link(id, path) + "\n"
                
            except:
                Console.error (f"error in entry {item}")         
        return output

    def read_cache(self, cache):
        with open(cache, 'r') as file:
            data = json.loads(file.read())
        return data
    
    def dump_cache(self, cache, data):
        with open(cache, 'w') as file:
            return json.dump(data, file, indent=2)



    def info(self, directory, kind="yaml", cache=None, refresh=False, recursive=False): 
        """
        Perform a list operation.

        This method prints a message indicating a list operation along with the provided parameter.

        Args:
            parameter (str): The parameter for the list operation.

        Returns:
            None
        """
        def get_data():
            try:
                if recursive:
                    recursive_flag = "-R"
                else:
                    recursive_flag = ""
                r = Shell.run(f"rclone {recursive_flag} --drive-shared-with-me lsjson '{directory}'")
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


        if directory.startswith("drive:"):
            pass
        else:
            directory = f"drive:{directory}"

        if cache is not None:
            refresh = not os.path.exists(cache) or refresh
        if cache is not None and refresh:
            data = get_data()
            self.dump_cache(cache, data)
        elif cache is not None and not refresh:
            data = self.read_cache(cache)
        elif cache is None:
            data = get_data()

        return data

    def sanitize(self, name):
        return name.replace(" ", "%20").replace(",", "%2C")
    
    def replace(self, cache, prefix, file, verbose=False):
        data = self.read_cache(cache)
        for entry in data:
            path = self.sanitize(entry["Path"])
            name = self.sanitize(entry["Name"])
            
            entry["source"] = '<a href="' + prefix + "/" + path +'">'
            entry["target"] = self.html_link(entry["ID"], name)

        with open("replace.json", "w") as f:
             json.dump(data, f, indent=4)
        
        content = readfile(file)
        
        for entry in data:
            source = entry["source"]
            target = entry["target"]

            if verbose:
                if source in content:
                    print (source, "->", target)
            content = content.replace(source, target)


        print (content)  


        #pprint(data)


        
        #for line in lines:     
        #    print(line)
        return ""

