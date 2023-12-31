0x0B. Python - Input/Output
By: Guillaume
Weight: 1
Date: 7th Nov, 2023
Codes by me: Victor Ukpongette

The objectives of this project is to make me know:

How to open a file
How to write text in a file
How to read the full content of a file
How to read a file line by line
How to move the cursor in a file
How to make sure a file is closed after using it
What is and how to use the with statement
What is JSON
What is serialization
What is deserialization
How to convert a Python data structure to a JSON string
How to convert a JSON string to a Python data structure

--------------------IN MY OWN WORDS----------------------------------------------------------

In Python, inputs and outputs are fundamental concepts used to handle data flow in your programs. Inputs refer to the data or information that is provided to a program, while outputs are the results or responses generated by the program.

HOW TO OPEN A FILE
To open a file in Python, you can use the open() function. The open() function allows you to open files for various purposes such as reading, writing, appending, and more. Here's the basic syntax for opening a file:
#   file = open(filename, mode)
filename is a string that specifies the name of the file you want to open, including the path if necessary.
mode is a string that specifies the purpose for which you are opening the file, such as reading ('r'), writing ('w'), appending ('a'), or a combination of these modes.

Here are some common file modes in Python:

'r': Read (default mode). Opens the file for reading.
'w': Write. Opens the file for writing (creates a new file or truncates an existing file).
'a': Append. Opens the file for writing (creates a new file or appends to an existing file).
'b': Binary mode. Use this mode for binary files, such as images or non-text data.
't': Text mode (default). Use this mode for text files.
'x': Exclusive creation. Opens the file for exclusive creation, raising an error if the file already exists.

HOW TO WRITE TEXT IN A FILE
To write text to a file in Python, you can use the open() function with the 'w' mode (write mode).

HOW TO READ THE FULL CONTENT OF A FILE
To read the full content of a file, you can use the open() function with the 'r' mode (read mode) and then use the read() method to read the entire content of the file. 

WHAT IS JSON
JSON (JavaScript Object Notation) is a lightweight, human-readable data interchange format that is easy for both humans and machines to work with. It is often used for data storage and exchange in various programming languages, including Python, JavaScript, and many others. JSON is a text-based format and is designed to be simple and easy to understand. It is a commonly used format for transmitting data between a server and a web application, for configuration files, and for storing structured data.

Here are some key characteristics of JSON:

Data Structure: JSON represents data as a collection of key-value pairs, similar to dictionaries or objects in many programming languages. It supports various data types, including strings, numbers, booleans, arrays, and nested objects.

Human-Readable: JSON data is easy for humans to read and write, which makes it a popular choice for configuration files and data exchange in web services.

Language Agnostic: JSON is not tied to a specific programming language and can be used in various languages. Most modern programming languages have libraries or modules for working with JSON.

Lightweight: JSON is a lightweight data format with minimal overhead, which makes it efficient for data transmission over networks.

Standardized: JSON is a well-defined format with a clear specification, which contributes to its widespread adoption.

SERIALIZATION AND DESERIALIZATION

Serialization and deserialization are processes used in computer science to convert data structures or objects into a format that can be easily stored, transmitted, or reconstructed.

Serialization:

Serialization is the process of converting complex data structures, objects, or data into a format that can be easily saved to a file, transmitted over a network, or stored in a database. The resulting serialized data is typically a stream of bytes or a string that can be reconstructed later into its original form. Serialization is useful for tasks such as data persistence (e.g., saving objects to disk), network communication (e.g., sending data between different systems), and inter-process communication.

Common use cases for serialization include:

Data Persistence: Saving the state of an application, such as user preferences or game progress, to a file.

Data Transfer: Transmitting data between systems over a network, as is commonly done with web APIs and data exchange formats like JSON and XML.

Object Serialization: Saving complex objects (e.g., instances of classes) so that they can be reconstructed later.

In Python, the pickle module is often used for object serialization. For more general data serialization, the json module is frequently used.

Deserialization:

Deserialization is the reverse process of serialization. It involves taking the serialized data and reconstructing the original data structures or objects. Deserialization is used to read data from files, receive data from a network, or restore objects from a previously serialized state.

Common use cases for deserialization include:

Loading Data: Reading data from files or network streams into memory for processing.

Object Reconstruction: Creating objects from their serialized representations.

API Consumption: Parsing data received from web services and converting it into usable data structures.

In Python, you can use the pickle module to deserialize objects that were serialized with the pickle module. Similarly, you can use the json module to deserialize JSON data into Python data structures.
