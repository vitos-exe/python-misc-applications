#imports dataclass for convinience and json for saving and getting data from a file
from dataclasses import dataclass
import json

#defining contact dataclass
@dataclass
class Contact:

    first_name: str
    second_name: str
    phone_number: str
    description: str

    #method for converting contact to list
    def to_list(self) -> list[str]:
        return [
            self.first_name,
            self.second_name,
            self.phone_number,
            self.description
        ]

    #overriding __str__ for convinient representing contact to the user
    def __str__(self) -> str:
        return (f"\nFirst name: {self.first_name}\n"
        f"Second name: {self.second_name}\n"
        f"Phone number: {self.phone_number}\n"
        f"Description: {self.description}\n")

#data base class
class Database:

    #constructor takes a file's path as an input and fetches all contacts from it then stores it in the list 
    def __init__(self,path: str) -> None:
        self.path = path
        try:
            with open(path, 'r') as f:
                self.elements = [Contact(*c) for c in json.load(f)]
        except:
            self.elements = []

    #method for adding a new contact to contact list
    def add(self, *args: list[str]) -> None:
        self.elements.append(Contact(*args))

    #method that searches contact with passed name
    def search(self, name: str) -> Contact:
        returned = None
        for c in self.elements:
            if c.first_name == name or c.second_name == name:
                returned = c
        return returned
    
    #method for deleting passed contact
    def delete(self, c: Contact) -> None:
        self.elements.remove(c)

    #overriding __str__ for convinient representing database to the user
    def __str__(self) -> str:
        if self.elements:
            return "\n".join([f"{c.first_name} {c.second_name}" for c in self.elements])
        return "No contacts"

    #destructor saves contact list in the file when database object is garbage collected
    def __del__(self) -> None:
        with open(self.path, 'w') as f:
            json.dump([c.to_list() for c in self.elements], f, indent = 4)