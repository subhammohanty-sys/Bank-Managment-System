Project Statement: Student Bank Application

1. Project Overview

Basically, I built this console-based banking simulation using Python. The main idea was to show that I can work with file handling, Object-Oriented Programming (OOP), and persistent data without needing to set up a massive database server. It’s a lightweight way to handle banking logic right from the terminal.

2. The Problem

One of the big issues with standard command-line scripts is that they usually store data in variables (RAM). That means the second you close the program, everything—your balance, your history—is gone. I wanted to fix that. My goal was to build a system where the data actually sticks around, so when you come back later, your account is exactly how you left it.

3. How It Works

To solve the data loss problem, I used Python's json module to create a simple file-based database.

Where Data Goes: All user info gets saved into a local file called accounts_db.json.

Logging In: When someone tries to log in, the code checks that file to verify the username and password.

Handling Money:

Read: As soon as you log in, the app pulls the freshest data from the file.

Process: It does the math in memory (like adding a deposit).

Write: This is the important part—it writes the changes back to the file immediately. This ensures that even if the program crashes right after, the transaction is saved.

4. Key Features

Sign Up: You can register a new username (it checks to make sure it's unique).

It Remembers You: Data loads automatically on start and saves automatically on update.

Safety Checks: You can't withdraw money you don't have; the system blocks overdrafts.

History: It keeps a running log of every deposit and withdrawal, stamped with the exact time it happened.

5. Conclusion

Overall, this project takes basic scripting to the next level by adding real persistence. It bridges the gap between writing code that just "runs" and building an application that actually maintains state, acting like a functional prototype for a banking backend.