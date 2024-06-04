#!/usr/bin/python3
"""This module contains the cmd line function for the console"""

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The jumping off point for HBNB
    Documented Commands: EOF and quit"""
    prompt = '(hbnb) '

    class_map = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }

    def do_EOF(self, arg):
        """EOF command to exit program\n"""
        if self.file:
            self.file.close()
            self.file = None
        else:
            return True

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def emptyline(self):
        """this overrides the default
        behavior of hitting enter
        pass is intentional"""
        pass

    # ---------------------CRUD functions

    def do_create(self, line):
        """Create a new instance
        of a class. Takes className
        as argument"""

        if self.class_is(line, True) and self.class_in_dict(line, True):

            args = line.split()
            class_name = args[0]
            class_obj = self.class_map[class_name]
            new_instance = class_obj()
            print(new_instance.id)

    def do_show(self, line):
        """Prints string representation
        of an instance. Takes arguments
        className and id"""
        if self.class_is(line, True) and self.class_in_dict(line, True):
            if (self.instance_id_is(line, True)
                    and self.instance_id__is_valid(line, True)):
                print("that specific instance")

    def do_destroy(self, line):
        """Deletes an instance based on
        the className and id"""
        if self.class_is(line, True) and self.class_in_dict(line, True):
            if (self.instance_id_is(line, True)
                    and self.instance_id__is_valid(line, True)):
                print("that specific instance destroyed")

    def do_all(self, line):
        """Prints string representation of all instances,
        optional argument className"""

        if not self.class_is(line, False):
            print("EVERYTHING")
        else:
            if self.class_in_dict(line, True):
                args = line.split()
                class_name = args[0]
                print("EVERYTHING in {}".format(class_name))

    def do_update(self, line):
        """Updates an instance based on className and id
        and attribute"""
        if self.class_is(line, True) and self.class_in_dict(line, True):
            if (self.instance_id_is(line, True)
                    and self.instance_id__is_valid(line, True)):
                if (self.attribute_exits(line, True)
                        and self.value_exits(line, True)):
                    args = line.split()
                    print("{} {} updated to {}".format(
                        args[1], args[2], args[3]))

    # ----------------------- Help Text

    def help_EOF(self):
        """help text for update"""
        print(f"\nEOF: \nUse this to quit the application\n")

    def help_quit(self):
        """help text for quit"""
        print(f"\nQuit: \nUse this to quit the application\n")

    def help_create(self):
        """help text for create"""
        print(f"\nCreate: \n"
              + f"Use this to create new instances of a class "
              + f"and returns the new instance's ID\n\n"
              + f"example: create <className>\n"
              + f"1234-1234-1234-1234\n")

    def help_show(self):
        """help text for show"""
        print(f"\nShow: \n"
              + f"Use this to print instances of a class\n\n"
              + f"example: create <className>\n"
              + f"1234-1234-1234-1234\n")

    def help_destroy(self):
        """help text for destroy"""
        print(f"\nDestroy: \n"
              + f"Use this to destroy an instance of a class\n\n"
              + f"example: destroy <className>\n")

    def help_all(self):
        """help text for all"""
        print(f"\nAll: \n"
              + f"Use this to display all instances on record\n"
              + f"optional: pass <className> to filter by class\n\n"
              + f"example: all             // displays all\n"
              + f"example: all <classname> // displays all in class\n")

    def help_update(self):
        """help text for update"""
        print(f"\nUpdate: \n"
              + f"Use this to update an instance of a class\n\n"
              + f"example: update <className> <id> <attr> <value>\n"
              + f"example: update User 1234-1234-1234-1234 "
              + f"email 'moe.szyslak@email.com\n")

    # --------------------------- utils

    def class_is(self, line, err):
        """validator for line"""
        args = line.split()

        if len(args) == 0:
            if err is True:
                print("** class name missing **")
            return False
        else:
            return True

    def class_in_dict(self, line, err):
        """validator for class in line"""
        args = line.split()
        class_name = args[0]
        if class_name not in self.class_map:
            if err is True:
                print("** class doesn't exits **")
            return False
        else:
            return True

    def instance_id_is(self, line, err):
        """checks to see if instance arg is passed"""
        args = line.split()

        if len(args) == 1:
            if err is True:
                print("** instance id missing **")
            return False
        else:
            return True

    def instance_id__is_valid(self, line, err):
        """checks to see if instance id is valid"""
        instance_id_dict = {'1234-1234-1234-1234'}
        args = line.split()

        instance_id = args[1]
        if instance_id not in instance_id_dict:
            if err is True:
                print("** no instance found **")
            return False
        else:
            return True

    def attribute_exits(self, line, err):
        """checks if attribute is passed"""
        args = line.split()
        if len(args) == 2:
            if err is True:
                print("** attribute name missing **")
            return False
        else:
            return True

    def value_exits(self, line, err):
        """checks if value for attribute is passed"""
        args = line.split()
        if len(args) == 3:
            if err is True:
                print("** value missing **")
            return False
        else:
            return True


if __name__ == '__main__':
    """This is the engine that makes the
    console work:
    cmdloop() makes prompt vroom-vroom"""
    HBNBCommand().cmdloop()
