from cloudmesh.google.google import Google
from cloudmesh.common.console import Console
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import banner
#from cloudmesh.common.util import path_expand
from cloudmesh.common.variables import Variables
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
#from cloudmesh.shell.command import map_parameters
from pprint import pprint

class GoogleCommand(PluginCommand):
    # noinspection PyUnusedLocal
    @command
    def do_google(self, args, arguments):
        """
        ::

          Usage:
                google ls DIR [--csv] [--c=CHAR]
                google info DIR [--json|--yaml]
                
          This command does some useful things.

          Arguments:
              DIR   the directory in google
              CHAR  the character to be used for csv separation [default: ,]
              
          Options:
              -f      specify the file

          Description:

            > cms google ls DIR 
            > lists the files in the DIR
            
        """

        variables = Variables()
        variables["debug"] = True

        arguments["json"] = arguments["--json"]
        arguments["yaml"] = arguments["--yaml"]
        arguments["csv"] = arguments["--csv"]
        arguments["c"] = arguments["--c"] or ","

        if arguments.yaml:
            kind = "yaml"
        else:
            kind = "json"
            
        #map_parameters(arguments, "--json", "--yaml")

        VERBOSE(arguments)

        banner(
            "rewriting arguments so we convert to appropriate types for easier handling",
            color="RED",
        )

        # arguments = Parameter.parse(
        #     arguments, parameter="expand", experiment="dict", COMMAND="str"
        # )

        # VERBOSE(arguments)

        banner("showcasing tom simple if parsing based on teh dotdict", color="RED")

        m = Google()

        if arguments.ls:
            r = m.list(arguments.DIR, csv=arguments.csv, c=arguments.c)
            print (r)

        elif arguments.info:
            r = m.info(arguments.DIR, kind=kind)
            if kind == "json":
                pprint(r)
            else:
                print (r)

        return ""
