#!/usr/bin/python3

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The jumping off point for HBNB
    Documented Commands: EOF and quit"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit program\n"""
        if self.file:
            self.file.close()
            self.file = None
        else:
            return True
    
    def do_quit(self, arg):
        """Quit command to exit program\n"""
        return True
    
    def emptyline(self):
        """this overrides the default 
        behavior of hitting enter
        pass is intentional"""
        pass

    ########### CRUD functions

    def do_create():
        """Create a new instance
        of a class. Takes className
        as argument"""
        pass

    def do_show():
        """Prints string representation
        of an instance. Takes arguments 
        className and id"""
        pass

    def do_destroy():
        """Deletes an instance based on
        the className and id"""
        pass

    def do_all():
        """Prints string representation of all instances, 
        optional argument className"""
        pass

    def do_update():
        """Updates an instance based on className and id
        and attribute"""
        pass
    
    ############Help Text

    def help_EOF(self):
        """help text for update"""
        print("Get helpful insight into using the console")

    def help_quit(self):
        """help text for quit"""
        print("Use this to quit the application")

    def help_create(self):
        """help text for create"""
        print(f"Use this to create new instances of a class "
              + f"and returns the new instance's ID\n"
              + f"example: create <className>\n")

    def help_show(self):
        """help text for show"""
        print("this text should override the doc!")

    def help_destroy(self):
        """help text for destroy"""
        print("this text should override the doc!")

    def help_all(self):
        """help text for all"""
        print("this text should override the doc!")

    def help_update(self):
        """help text for update"""
        print("this text should override the doc!")


if __name__ == '__main__':
    """This is the engine that makes the
    console work:
    cmdloop() makes prompt vroom-vroom"""
    HBNBCommand().cmdloop()
