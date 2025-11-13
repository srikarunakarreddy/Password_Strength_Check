# 🔐 Password Strength Checker

This is a beginner-friendly Python CLI tool that evaluates the strength of a password based on key security criteria. It was built as part of my Python crash course to practice input validation, string handling, and modular function design.

## Features
- Checks for:
  - Minimum length (8 characters)
  - No spaces allowed
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character (from `string.punctuation`)
- Classifies passwords as:
  - **Strong**
  - **Not Strong**
- Provides specific feedback for missing criteria
- Loop-based input: test multiple passwords until you type `"exit"`

## What I Learned
- Writing modular functions with clear logic
- Using Python's `any()` and string methods for validation
- Handling user input in a loop
- Designing CLI tools with user-friendly feedback

## How to Run
Make sure you have Python installed, then run:
```bash
python password_strength_check.py
