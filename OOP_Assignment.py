# --- Assignment 1: Design Your Own Class ---

# Let's create a class representing a "Book"

class Book:
    """
    Represents a book with title, author, ISBN, and publication year.
    """

    def __init__(self, title, author, isbn, publication_year, genre="Fiction"):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The International Standard Book Number (ISBN) of the book.
            publication_year (int): The year the book was published.
            genre (str): The genre of the book. Defaults to "Fiction".  Added as a default so subclasses don't *require* it.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.genre = genre

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nPublication Year: {self.publication_year}\nGenre: {self.genre}"

    def get_age(self):
        """
        Calculates and returns the age of the book (years since publication).
        """
        import datetime
        current_year = datetime.datetime.now().year
        return current_year - self.publication_year

    def display_info(self):
        """
        Prints the book's information to the console.
        """
        print(self) # Uses the __str__ method for a cleaner output.
        print(f"Age: {self.get_age()} years")


# Inheritance:  Let's create a subclass "Textbook" that inherits from "Book"

class Textbook(Book):
    """
    Represents a textbook, inheriting from the Book class.
    """

    def __init__(self, title, author, isbn, publication_year, subject, grade_level):
        """
        Initializes a Textbook object.

        Args:
            title (str): The title of the textbook.
            author (str): The author of the textbook.
            isbn (str): The ISBN of the textbook.
            publication_year (int): The year the textbook was published.
            subject (str): The subject of the textbook (e.g., "Mathematics", "History").
            grade_level (int): The grade level for which the textbook is intended (e.g., 9, 10, 11).
        """
        super().__init__(title, author, isbn, publication_year, genre="Educational")  # Call the parent class's constructor
        self.subject = subject
        self.grade_level = grade_level

    def __str__(self):
        """
        Returns a string representation of the Textbook object. Overrides the parent's method.
        """
        return super().__str__() + f"\nSubject: {self.subject}\nGrade Level: {self.grade_level}"

    def is_suitable_for_grade(self, grade):
        """
        Checks if the textbook is suitable for a given grade level.

        Args:
            grade (int): The grade level to check.

        Returns:
            bool: True if the textbook is suitable for the grade, False otherwise.
        """
        return self.grade_level == grade  # Simple example, could be more complex



# Example Usage (Creating Book and Textbook objects):

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803", 1979)
print("Book 1 Information:")
book1.display_info()
print("\n")


textbook1 = Textbook("Algebra I", "Robert Blitzer", "978-0134497104", 2018, "Mathematics", 9)
print("Textbook 1 Information:")
textbook1.display_info()

print(f"\nIs Textbook 1 suitable for grade 10? {textbook1.is_suitable_for_grade(10)}")
print(f"Is Textbook 1 suitable for grade 9? {textbook1.is_suitable_for_grade(9)}")


# --- Activity 2: Polymorphism Challenge ---

class Animal:
    """
    Base class for animals.
    """
    def __init__(self, name):
        self.name = name

    def move(self):
        """
        Abstract method for moving.  Subclasses must implement this.
        """
        raise NotImplementedError("Subclasses must implement the move() method.")

    def speak(self):
        """
        Generic speaking method (can be overridden).
        """
        print(f"{self.name} makes a sound.")  # Added a default implementation


class Dog(Animal):
    """
    Represents a dog.
    """
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def move(self):
        """
        Implements the move() method for a dog.
        """
        print(f"{self.name} (a {self.breed}) is running!")

    def speak(self):
      print(f"{self.name} says Woof!")

class Bird(Animal):
    """
    Represents a bird.
    """
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def move(self):
        """
        Implements the move() method for a bird.
        """
        print(f"{self.name} (a {self.species}) is flying!")

    def speak(self):
      print(f"{self.name} tweets!")

class Fish(Animal):
    """
    Represents a fish.
    """
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def move(self):
        """
        Implements the move() method for a fish.
        """
        print(f"{self.name} (a {self.habitat} fish) is swimming!")

    # No need to override speak() if the default is sufficient.


# Example Usage (Polymorphism):

animal_list = [
    Dog("Buddy", "Golden Retriever"),
    Bird("Tweety", "Canary"),
    Fish("Nemo", "Coral Reef")
]

print("\nAnimal Movements:")
for animal in animal_list:
    animal.move()
    animal.speak()
