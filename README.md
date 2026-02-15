# Cricket Performance Analysis Using NumPy (Python)

## Project Description

The Cricket Performance Analysis project is a Python application that uses the NumPy library to analyze players' runs scored across multiple matches.
The program performs multi-dimensional array operations to calculate total and average runs per player, match-wise statistics, identify best and worst performers, detect consistent players, and apply bonus runs with value limits.

This project demonstrates practical matrix-based data analysis using NumPy and is suitable for beginners learning sports analytics and numerical computing in Python.

The application executes once and displays all computed results in the terminal.

---

## Features

* Store player scores using a 2D NumPy array
* Calculate total runs per player
* Calculate average runs per player
* Calculate total runs per match
* Identify highest score per match
* Determine best and worst performing players
* Identify consistent players based on average score
* Apply bonus runs and limit final scores

---

## Concepts Used

### Python Fundamentals

* Variables
* Data types (int, float)
* Output formatting

### NumPy Concepts

* Multi-dimensional arrays
* Axis-based aggregation (sum and mean)
* Maximum value detection using max()
* Index identification using argmax() and argmin()
* Conditional filtering using where()
* Element-wise operations
* Data clipping using clip()

### Programming Concepts

* Sports performance analysis
* Matrix-based computation
* Statistical evaluation
* Bulk data transformation
* Logical performance classification

---

## Project Structure

```
cricket-performance-analysis/
│
├── cricket_analysis.py
└── README.md
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on the system
* NumPy library installed

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the following command:

```
python cricket_analysis.py
```

---

## Operations Performed

```
1. Display player score matrix
2. Calculate total runs per player
3. Calculate average runs per player
4. Calculate total runs per match
5. Identify highest score per match
6. Determine best and worst player
7. Identify consistent players (average >= 50)
8. Add bonus runs
9. Limit scores between 0 and 100
```

---

## Sample Output

```
Total runs per player: [270 285 160 385]
Average runs per player: [54. 57. 32. 77.]
Best player index: 3
Worst player index: 2
Consistent players (avg >= 50): [0 1 3]
```

---

## Edge Cases Handled

* Accurate axis-based aggregation
* Proper identification of highest and lowest performers
* Consistency evaluation based on threshold
* Bonus marks applied without exceeding maximum limit
* Valid score range enforcement

---

## Author

Meet Tailor

Python Programming Learner

---

## License

This project is created for learning and educational purposes only.

---

## Project Status

Completed

Last Updates: 2026
