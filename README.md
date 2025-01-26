# Statistics Calculator

## Purpose of this README
This student-project is for learning purposes. This submission requested other students refactor their code and take a shot at improving it. All changes are explain below.

## Overview
This Python script was refactored to improve its functionality, error handling, and user experience. The main goal was to create a more robust, maintainable, and user-friendly application for calculating mean and median from user input.

## Changes Made:

### 1. **Modular Input Handling**
- **Before**: Directly used `input()` for each number, which was repetitive and error-prone.
- **After**: Introduced a function `get_nums()` to handle input collection, ensuring only valid integers are accepted and providing appropriate feedback for incorrect inputs.

### 2. **Function Generalization**
- **Before**: Functions like `mean_Of_Group` and `median_Of_Group` were hardcoded for five numbers.
- **After**: Changed to accept variable number of arguments via `*args`, making them reusable for any number of inputs.

### 3. **Error Management**
- **Before**: Little to no error handling, with potential for runtime errors.
- **After**: Added try-except blocks to manage ValueError exceptions from invalid inputs or operations, improving robustness.

### 4. **User Interaction Refinement**
- **Before**: Harsh messages for user mistakes.
- **After**: More polite and instructive user prompts, providing clear instructions and feedback.

### 5. **Code Structure**
- **Before**: Mixed program flow and function definitions, with repetitive code for user choice.
- **After**: Encapsulated logic into functions, reducing redundancy and improving code clarity. Introduced a loop for choice selection to allow multiple tries without harsh feedback.

### 6. **Naming Conventions**
- **Before**: Mixed case in function names.
- **After**: Adopted Python's PEP 8 naming convention for consistency (`snake_case`).

## How to Use:
- Run the script.
- Enter five numbers when prompted.
- Choose between 'mean' or 'median' to see the result.

This refactoring aims at making the code more maintainable, less prone to errors, and providing a better user experience.
