#!/usr/bin/python3
"""Module contains BaseModel
BaseModel: defines all common attributes/methods
            for other classes
"""


from datetime import datetime
import uuid


class BaseModel:
    """Defines all common attributes and methods
    for other classes
    """
    def __init__(self) -> None:
        """Initialize instance with random UUID
        and timestamps for created_at and updated_at
        """
        new_id = uuid.uuid4()  # Asign random UUID
        self.id = str(new_id)
        self.created_at = datetime.now()  # Created timestamp
        self.updated_at = datetime.now()  # Update timestamp

    def __str__(self) -> str:
        """Change string representation of class instance to:
        [<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: String representation of class instance
        """
        return ("[{}] ({}) {}"
               .format(
                   self.__class__.__name__,
                   self.id,
                   self.__dict__
               ))
