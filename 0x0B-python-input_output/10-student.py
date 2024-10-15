#!/usr/bin/python3
class Student:
    """Class that defines a student."""
    
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        
        Args:
            attrs (list): A list of attribute names to include in the output.
        
        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__.copy()
        
        return {key: value for key, value in self.__dict__.items() if key in attrs}
