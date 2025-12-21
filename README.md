# CLI Todo App

A simple **command-line todo application** written in Python.

This project was built as a **learning-focused project** to understand:

-   CLI application design

-   Basic data persistence

-   Refactoring and code structure

-   Command dispatch using dictionaries

-   Testing concepts (unit & integration awareness)

-   Git and GitHub workflow

The focus of this project is clarity, learning, and correctness, not feature overload.

---
## Features

- Add tasks
- Delete tasks
- Display tasks in a clean table format
- Persist tasks using a JSON file
- Handle invalid input gracefully
- Simple and readable CLI interface

Each task contains:
- Title
- Date & time when it was created

---

## Requirements

- Python 3.8 or higher
- `tabulate` library

Install dependency:

```bash
pip install tabulate
```
---

## How to Run

```
git clone https://github.com/your-username/cli-todo.git
cd cli-todo
```

```
python main.py
```

### Usage
Want to add, delete, display tasks or exit?

```
+-------+----------------------+---------------------+
| Index | Title                | Date Created        |
+-------+----------------------+---------------------+
| 1     | Buy groceries        | 2025-01-01 10:30:00 |
| 2     | Study Python         | 2025-01-01 11:15:22 |
+-------+----------------------+---------------------+
```

## Design Notes
-   The CLI loop is intentionally simple and readable.

-   Command handling uses a dictionary (command → function) instead of large if/else blocks.

-   Storage logic is separated into its own file for clarity.

-   Interactive CLI code is not unit-tested; logic separation was discussed and understood.

-   The project prioritizes learning trade-offs over premature abstraction.

## Testing
This project focuses on manual testing for CLI interaction.

While formal unit and integration tests are not implemented, the following concepts were explored:

-   When unit testing makes sense

-   Why CLI loops are difficult to unit test

-   Difference between unit tests and integration tests

-   How testability influences design decisions

Testing knowledge gained here will be applied in future projects.

## Learning Outcomes
By building this project, I learned:

-   How to structure a CLI application

-   How to refactor code safely

-   How to think about responsibilities and separation of concerns

-   How testing fits into real projects (practically, not theoretically)

-   How to use Git and GitHub effectively

## License
This project is for learning purposes.
Feel free to use or modify it.