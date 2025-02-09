# 2025-ITELEC2-LAB003
Week 02 - Python Variables, Operators and I/O Statements

Laboratory # 03 - Guided Coding Exercise: Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 03 - Guided Coding Exercise: Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)**

   **Objective:**
   This exercise aims to solidify your understanding of variable declaration, data types (integers, floats, and strings), the crucial concept of case-sensitivity in Python, and best practices for variable naming. You will learn how to create variables, assign values of different types, observe how Python distinguishes between variables based on their case, and write code that is more readable and maintainable.

   **Desired Output:**
   ```txt
   Integer (count): 10
   Integer (Count): 15
   Integer (total_count): 20
   Decimal: 3.14
   Text: Hello, Python!
   Boolean: True
   None Value: None
   ```
   *Note: The output now includes two variables—count and Count—to clearly demonstrate Python’s case-sensitivity.*

   **Folder Structure and Naming Conventions**
   - Required Filename: exercise_01.py
   - Location: Save this file in the root directory of your project or designated repository folder.
   - Header Comments: Include your name, course code (e.g., ITELEC2), and a brief description of the exercise at the top of your script.

   **Notable Observations (to be discussed after completing the exercise):**
- Case-Sensitivity: Python distinguishes between identifiers by case. For instance, count and Count are two completely different variables.
- Literals vs. Variables: 
   - Literals are the direct values written in the code (e.g., 10, 3.14, "Hello, Python!").
   - Variables are names that store these values, and they can be reassigned over time.
- f-strings and Inline Arithmetic: f-strings allow you to embed expressions directly within string literals. For example:
   ```python
   print(f"Sum: {num1 + num2:.2f}")
   ```
   Here, num1 + num2 is calculated on the fly, and the result is formatted to two decimal places using the :.2f specifier.
- Variable Naming: Consistent and descriptive variable names enhance code clarity. This exercise reinforces the importance of following Python naming conventions (using snake_case, avoiding reserved keywords, etc.).

   **Python Best Practices for Variable Naming**
   - Descriptive Names: Use clear and descriptive names (e.g., count, total_count, decimal_value) rather than single-letter names, unless in short loops or temporary contexts.
   - Snake Case Convention: Adopt snake_case (all lowercase with underscores) for variable names, which is standard in Python.
   - Avoid Reserved Keywords: Never use Python’s reserved words (such as if, else, while, for) as variable names.
   - Consistency: Maintain consistency in your naming conventions throughout your codebase.
   - Valid Naming Rules: Variable names should start with a letter or an underscore and can include numbers after the first character.

****
   
   **Step-by-Step Instructions:**

   1. Setup:
   - Open your preferred Python environment or text editor.
   - Create a new Python script named exercise_01.py.
   - Create Header Comments: At the top of the file, include your details
   ```python
   # Your Name
   # ITELEC2
   # Laboratory #03 – Guided Coding Exercise:
   # Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)
   
   ```
      
   2. Declare Variables with Numeric Literals:
   - Create a variable named count and assign it the integer literal 10.
   - To demonstrate case-sensitivity, create another variable named Count (with an uppercase "C") and assign it the integer literal 15.
   - Create a variable named decimal_value and assign it the floating-point literal 3.14.
   ```python
   count = 10                   # 'count' is assigned 10 (integer literal)
   Count = 15                   # 'Count' (different from 'count') is assigned 15
   decimal_value = 3.14         # 'decimal_value' is assigned 3.14 (float literal)
   ```
      
   3. Declare a Variable with a String Literal:
   - Create a variable named message and assign it the string literal "Hello, Python!"
   ```python
   message = "Hello, Python!"   # String literal
   ```

   4. Declare a Variable with a Boolean Literal:
   - Create a variable named is_active and assign it the boolean literal True.
   ```python
   is_active = True             # Boolean literal
   ```

   5. Declare a Variable with the None Literal:
   - Create a variable named result and assign it the None literal.
   ```python
   result = None                # None literal represents absence of value
   ```

   6. Additional Variable Assignment:
   - Create a variable named total_count and assign it the integer literal 20
   ```python
   total_count = 20             # Another integer literal assignment
   ```

   7. Display the Variable Values:
   - Use the print() function to output each variable with descriptive labels.
   - Additionally, demonstrate inline arithmetic using f-strings:
   ```python
   print("Integer (count):", count)
   print("Integer (Count):", Count)
   print("Integer (total_count):", total_count)
   print("Decimal:", decimal_value)
   print("Text:", message)
   print("Boolean:", is_active)
   print("None Value:", result)
   
   # Example of inline arithmetic with formatting using an f-string:
   num1 = 5
   num2 = 3
   print(f"Sum: {num1 + num2:.2f}")  # The result (8.00) is formatted to 2 decimal places
   ```
         
   8. Run the code:
   - Save the file and execute your script in the terminal:
   ```bash
   python exercise_01.py
   ```
   - Verify that your output matches the desired output specified above.

   9. Observe the output: Compare your output with the "Desired Output" shown above.
   10. Discussion and Reflection:
   - Review how count and Count are treated as two separate variables due to Python's case-sensitivity.
   - Discuss the distinction between literals and variables: literals are fixed values, while variables serve as placeholders that can be reassigned.
   - Reflect on the power of f-strings to compute expressions inline and apply format specifiers for a clean output.
   - Emphasize the importance of following consistent naming conventions for readability and maintenance.

**Conclusion**
By completing this exercise, you will have:
- Developed a solid understanding of variable declaration and the assignment of literals in Python.
- Demonstrated the concept of case-sensitivity by using similar identifiers that differ only in case.
- Gained experience in using Python’s f-strings to perform inline arithmetic operations with format specifiers.
- Adopted best practices for naming variables to ensure your code is clear, readable, and maintainable.
- Reflected on the importance of distinguishing between literals and variables, which is crucial for writing robust Python programs.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
   ```bash
   git status
   ```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
   ```bash
   git add .
   ```
   
3. Commit your changes:
   Write a meaningful commit message:
   
   ```bash
   git commit -m "Submitting Python Week 02 - Session 01 - Exercise 01"
   ```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
   ```bash
   git push origin main
   ```
