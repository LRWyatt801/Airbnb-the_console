#!/usr/bin/python3

import cmd


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
        pass
    
if __name__ == '__main__':
    """This is the engine that makes the
    console work:
    cmdloop() makes prompt vroom-vroom"""
    HBNBCommand().cmdloop()
