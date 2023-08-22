#!/usr/bin/python3
"""Console module for HBNB"""

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

# Dictionary to map class names to their corresponding classes
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class HBNBCommand(cmd.Cmd):
    """HBNH console class"""
    prompt = '(hbnb) '  # Console prompt

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """Overrides the emptyline method"""
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _token_value_parser(self, args):
        """Creates a dictionary from a list of strings"""
        new_dictionary = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                token = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dictionary[token] = value
        return new_dictionary

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dictionary = self._token_value_parser(args[1:])
            instance = classes[args[0]](**new_dictionary)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    # ... (other methods)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
