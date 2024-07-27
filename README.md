# Tzefa Language Interpreter

## Overview

This project implements an interpreter for a custom programming language called "Tzefa". The interpreter is written in Python and provides functionality for variable management, arithmetic operations, conditional statements, and function calls.

## Project Structure

### Main Files

1. **main.py**
   - Entry point of the program
   - Handles the initial processing of Tzefa code
   - Calls functions from ErrorCorrection and topy modules

2. **topy.py**
   - Contains the `makepyfile` function
   - Responsible for translating Tzefa code into Python code that uses the interpreter

3. **createdpython.py**
   - Contains the main interpreter logic
   - Implements variable management, operations, and execution control
   - Defines key classes like VALUE, LIST, COND, and EERROR

4. **ErrorCorrection.py**
   - Handles error correction and preprocessing of Tzefa code
   - Implements functions like `handelfirstword` and `toline`

5. **test.py** (generated file)
   - Output file created by `topy.py`
   - Contains the translated Python code from Tzefa source

### Additional Components

- **Tzefa-ocr Project** (separate repository)
  - Translates images containing Tzefa code into a format that can be executed by this interpreter
  - Bridges the gap between written/visual Tzefa code and its execution

## Key Components

[... Keep the existing "Key Components" section ...]

## Main Classes

- `VALUE`: Represents basic variable types (INT, STR, BOOLEAN)
  - Attributes: name, value, readable, writable, type
  - Methods: write, read, changeread, changewrite, tostring, makecopy, copyvar

- `LIST`: Implements list functionality with dynamic typing
  - Attributes: size, currentindex, values, types, readable, writable, name, type
  - Methods: addsize, changeindex, placevalue, returnvalue, copybyvalue, tostring

- `COND`: Handles conditional operations
  - Attributes: index, left, right
  - Methods: changecompare, changeleft, changeright, giveresult

- `EERROR`: Custom error handling and reporting
  - Methods: nameerror, makeeindexrror, DIVZEROERROR, doesntexisterror, writeerror, typetointerror, readerror, linelimiterror, overflowerror, cantchangeindexerror, varexistserror, typeerror

- `Stack`: Implements a stack data structure
  - Methods: isempty, push, pop

- `Node`: Used in linked list implementations
  - Attributes: value, next
  - Methods: setnext, setnextnode, getnext, getvalue

## Key Functions

[... Keep the existing "Key Functions" section ...]

## Usage

[... Keep the existing "Usage" section ...]

## Tzefa-ocr Integration

[... Keep the existing "Tzefa-ocr Integration" section ...]

## Note

This README is based on the provided code snippets and additional information about the Tzefa-ocr project. The actual usage and setup instructions may vary depending on the complete project structure and any additional files or dependencies not shown in the provided code.

## Future Developments

- Integrate Tzefa-ocr directly into this project for a seamless image-to-execution pipeline
- Develop a dedicated IDE for Tzefa that incorporates both the OCR and interpreter functionalities