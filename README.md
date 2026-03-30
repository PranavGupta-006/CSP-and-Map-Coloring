# CSP and Map Coloring Assignment

## Overview

Assignment - 4

This repo contains implementations of classic **Constraint Satisfaction Problems (CSPs)** using Python3. Each problem demonstrates how constraints, variables, and domains can be modeled and solved using backtracking and search techniques.

The problems included are:

1. Map Coloring – Australia
2. Map Coloring – Telangana (33 districts)
3. Sudoku Solver
4. Cryptarithmetic Puzzle (TWO + TWO = FOUR)

---

## 1. Map Coloring – Australia

### Problem Description

The goal is to color the seven regions of Australia:
WA, NT, Q, SA, NSW, V, T

Each region must be assigned a color such that:

* No two adjacent regions share the same color

### CSP Formulation

* Variables: Regions
* Domain: {Red, Green, Blue}
* Constraints: Adjacent regions must have different colors

### Approach

A backtracking algorithm is used:

* Select an unassigned region
* Try assigning a valid color
* Check constraints with neighbors
* Backtrack if a conflict occurs

---

## 2. Map Coloring – Telangana (33 Districts)

### Problem Description

Extend the map coloring problem to the 33 districts of Telangana.

### CSP Formulation

* Variables: Districts
* Domain: {Red, Green, Blue, Yellow}
* Constraints: Neighboring districts cannot share the same color

### Approach

* Represent districts as a graph using adjacency lists
* Apply backtracking search
* Ensure all constraints are satisfied before assigning colors

---

## 3. Sudoku Solver

### Problem Description

Solve a 9×9 Sudoku puzzle where:

* Each row contains digits 1–9 without repetition
* Each column contains digits 1–9 without repetition
* Each 3×3 subgrid contains digits 1–9 without repetition

### CSP Formulation

* Variables: 81 cells
* Domain: {1–9}
* Constraints:

  * Row constraint (all different)
  * Column constraint (all different)
  * Subgrid constraint (all different)

### Approach

* Use backtracking search
* For each empty cell:

  * Try digits 1–9
  * Check row, column, and subgrid validity
* Backtrack if no valid number is found

---

## 4. Cryptarithmetic Puzzle (TWO + TWO = FOUR)

### Problem Description

Each letter represents a unique digit. The goal is to find digits such that:

```
  T W O
+ T W O
--------
F O U R
```

### Constraints

* Each letter maps to a unique digit
* No leading digit can be zero (T ≠ 0, F ≠ 0)
* The arithmetic equation must be correct

### Approach

* Generate permutations of digits
* Assign digits to letters
* Check if the equation holds
* Stop when a valid solution is found

---

## Installation and Setup

### Install Python

#### Windows

1. Go to https://www.python.org/downloads/
2. Download the latest version
3. Run the installer
4. Enable "Add Python to PATH"
5. Verify installation:

   ```
   python --version
   ```

#### macOS

Python may already be installed.

Check:

```
python3 --version
```

If not installed:

```
brew install python
```

#### Linux (Ubuntu/Debian)

```
sudo apt update
sudo apt install python3
```

Verify:

```
python3 --version
```

---

## Running the Programs

### Step 1: Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Run a specific problem

#### Map Coloring (Australia)

```
python3 MapColoringAustralia.py
```

#### Telangana Map Coloring

```
python3 MapColoringTelangana.py
```

#### Sudoku Solver

```
python3 SudokuCSP.py
```

#### Cryptarithmetic Puzzle

```
python3 CryptAnalysisCSP.py
```

---

## Output

Each program prints the solution in the terminal:

* Map coloring: dictionary of regions/districts and assigned colors
* Sudoku: solved grid
* Cryptarithmetic: mapping of letters to digits

---

## Key Concepts Demonstrated

* Constraint Satisfaction Problems (CSP)
* Backtracking search
* Constraint checking
* Graph representation
* Logical inference

---

## Notes

* No external libraries are required
* All implementations use standard Python

---
