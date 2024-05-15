#!/usr/bin/python3
"""Defines a command interpreter class"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Initialise a command interpreter class.

    Attributes:
        prompt (str): command interpreter.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """command will do nothing"""
        pass

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF signal to exit the program."""
        print ("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
