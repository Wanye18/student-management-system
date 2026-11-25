
""" Lab 1 .

This is command-line app that keeps a record of each student: their course,
their status, and their marks.

New this lab:
    - the data model: each student is a dictionary, and a list holds them all
    - two pre-built packages: datetime for dates, statistics for averages
    - docstrings and comments that explain the code

Run:
    python student_manager.py
"""

from datetime import date
from statistics import mean

students = [
    {
        "id": 1,
        "name": "Ada Lovelace",
        "email": "ada.lovelace@uni.ac.uk",
        "course": "Software Development",
        "start_date": "2025-09-22",
        "status": "Enrolled",
        "marks": {"Python": 78, "Databases": 65},
    },
    {
        "id": 2,
        "name": "Alan Turing",
        "email": "alan.turing@uni.ac.uk",
        "course": "Data Science",
        "start_date": "2024-09-23",
        "status": "Enrolled",
        "marks": {"Statistics": 55, "Machine Learning": 48},
    },
    {
        "id": 3,
        "name": "Grace Hopper",
        "email": "grace.hopper@uni.ac.uk",
        "course": "Cyber Security",
        "start_date": "2027-01-25",
        "status": "Applied",
        "marks": {},
    },

    {
       "id": 4,
        "name": "Akindigh Dominic",
        "email": "akind@ng.com",
        "course": "Music theory",
        "start_date": "2026-09-23",
        "status": "Enrolled",
        "marks": {"practical": 70, "Theory":80},

    }

    ]

def average(marks: dict[str, int]) -> float | None:
    """Return the average mark, or None if there are no marks yet."""
    if not marks:
        return None
    return round(mean(marks.values()), 1)

def describe_start(start_date: str, today: date) -> str:
    """Return how long ago the course started, or how soon it starts."""
    days = (date.fromisoformat(start_date) - today).days
    # A positive number of days means the start date is still in the future.
    if days > 0:
        return f"starts in {days} days"
    return f"{-days / 365.25:.1f} years"


def show_students(students: list[dict], today: date) -> None:
    """Print the students as a table."""
    print(
        f"{'ID':<4}{'Name':<20}{'Course':<22}"
        f"{'Status':<10}{'Average':<9}{'Studying for'}"
    )
    for student in students:
        mark = average(student["marks"])
        shown = "-" if mark is None else mark
        print(
            f"{student['id']:<4}{student['name']:<20}"
            f"{student['course']:<22}{student['status']:<10}"
            f"{shown:<9}{describe_start(student['start_date'], today)}"
        )
def main() -> None:
    """Show today's date and the class list."""
    today = date.today()
    print(f"Student Management System, {today.strftime('%d %B %Y')}\n")
    show_students(students, today)


if __name__ == "__main__":
    main()

