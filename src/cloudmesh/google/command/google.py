from cloudmesh.google.google import Google
from cloudmesh.common.console import Console
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import banner
#from cloudmesh.common.util import path_expand
from cloudmesh.common.variables import Variables
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.shell.command import map_parameters
from pprint import pprint
import json

class GoogleCommand(PluginCommand):
    # noinspection PyUnusedLocal
    @command
    def do_google(self, args, arguments):
        """
        ::

          Usage:
                google ls DIR [--csv|--html] [--c=CHAR] 
                google info DIR [--json|--yaml] [--cache=CACHE] [--refresh] [--R]
                google replace --cache=CACHE [--prefix=PREFIX] [--verbose] FILE
                
          This command does some useful things.

          Arguments:
              DIR     the directory in google
              CHAR    the character to be used for csv separation [default: ,]
              FILE    the file on which to replace the prefix
              PREFIX  the URL prefix to be replaced [default: "https://infomall.org"]

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
        if arguments["--csv"]:
            arguments["lsformat"] = "csv"
        elif arguments["--html"]:
            arguments["lsformat"] = "html"
        else:
            arguments["lsformat"] = "list"

        arguments["c"] = arguments["--c"] or ","
        arguments["refresh"] = arguments["--refresh"]
        arguments["verbose"] = arguments["--verbose"]
        arguments["recursive"] = arguments["--R"]

        if arguments.yaml:
            kind = "yaml"
        else:
            kind = "json"
            
        map_parameters(arguments, "cache", "prefix")



        # VERBOSE(arguments)

        # arguments = Parameter.parse(
        #     arguments, parameter="expand", experiment="dict", COMMAND="str"
        # )

        # VERBOSE(arguments)


        m = Google()

        if arguments.ls:
            r = m.list(arguments.DIR, format=arguments["lsformat"], c=arguments.c, recusive=arguments.recursive)
            print (r)

        elif arguments.info:
            r = m.info(arguments.DIR, kind=kind, cache=arguments.cache, refresh=arguments.refresh, recursive=arguments.recursive)
            if kind == "json":
                print(json.dumps(r, indent=2))
            else:
                print (r)

        elif arguments.replace:
            r = m.replace(arguments.cache, arguments.prefix, arguments.FILE, arguments.verbose)
            print (r)

        return ""
