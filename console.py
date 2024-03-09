#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter.
"""
import re
import cmd
from models import storage

from models.base_model import BaseModel

current_classes = {'BaseModel': BaseModel}

class HBNBCommand(cmd.Cmd):
    """
    Represents the command line interpreter for handling commands.

    Inherits from cmd.Cmd to utilize the framework for interpreting and processing command line inputs.
    Manages application data and interfaces with the storage engine through provided commands.
    """

    prompt = "(hbnb) "

    def precmd(self, line):
        """
        Preprocess commands before execution.

        Allows for alternate command syntax and handles command preprocessing.
        """
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line)
        if not match_list:
            return super().precmd(line)

        match_tuple = match_list[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])
        else:
            args = match_tuple[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", match_tuple[2]))
            else:
                match_json = re.findall(r"{.*}", match_tuple[2])
                if (match_json):
                    return "{} {} {} {}".format(
                        match_tuple[1], match_tuple[0],
                        re.sub("[\"\']", "", args[0]),
                        re.sub("\'", "\"", match_json[0]))
                return "{} {} {} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

    def do_help(self, arg):
        """
        To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """
        Inbuilt EOF command to catch errors.
        """
        print("")
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Override default `empty line + return` behavior.
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()