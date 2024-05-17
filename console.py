#!/usr/bin/python3
"""Defines a command interpreter class"""
import cmd
import sys
import json
import os
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Initialise a command interpreter class.

    Attributes:
        prompt (str): command interpreter.
    """
    prompt = "(hbnb) "

    def emptyline(self, arg):
        """command will do nothing"""
        pass

    def do_create(self, arg):
        """create a new instance"""
        if len(arg) == 0:
            print("** class name missing ** (ex: $ create )")
            return
        new_a = None
        if arg:
            args_list = args_list.split()
            if len(args_list) == 1:
                if arg in self.classes.keys():
                    new_a = self.classes[arg]()
                    new_a.save()
                    print(new_a.id)
                else:
                    print("** class doesn't exist ** (ex: $ create MyModel )")

    def do_show(self, arg):
        """Create a new instance called show"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg.split() not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) > 1:
            k = arg.split[0] + '.' + arg.split[0]
            if k in storage.all():
                n = storage.all()
                print(i[k])
            else:
                print("** no instance found **")
        else:
            print("** instance is missing **")

    def do_destory(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        arg = arg.split()
        all_instance = storage.all()
        if len(arg) == 0:
            print([str(a) for a in all_instance.values()])
        elif arg not in classes:
            print("**class doesn't exist**")
        else:
            print([str(a) for b, a in all_instance.items() if arg in b])

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if__name__ == '__main__':
    HBNBCommand().cmdloop()
