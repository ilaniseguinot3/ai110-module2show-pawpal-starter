# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Example terminal output from running the demo script:

```text
Today's Schedule
================
08:00 | Morning walk | high | 30 min
08:30 | Play session | high | 20 min
08:50 | Medicine | high | 10 min
09:00 | Feed breakfast | medium | 15 min

Plan Summary
------------
Today's plan includes 4 task(s):
- 08:00: Morning walk (30 min, high)
- 08:30: Play session (20 min, high)
- 08:50: Medicine (10 min, high)
- 09:00: Feed breakfast (15 min, medium)
```

## 🧪 Testing PawPal+

Run the test suite with:

```bash
python -m pytest
```

The tests cover core scheduling behaviors such as task completion, adding tasks to pets, recurring-task scheduling, conflict detection, and chronological sorting.

Example test output:

```text
============================= test session starts ==============================
platform win32 -- Python 3.13.3, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\imspi\codepath\ai110-module2show-pawpal-starter
collected 7 items

test_pawpal_system.py ..                                                 [ 28%]
tests\test_pawpal.py .....                                               [100%]

============================== 7 passed in 0.05s ==============================
```

Confidence level: ★★★★★

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks by their scheduled time in HH:MM format. |
| Filtering | `Scheduler.filter_tasks()` | Filters tasks by completion status or pet-related criteria. |
| Conflict handling | `Scheduler.detect_conflicts()` | Warns when two tasks overlap in time. |
| Recurring tasks | `Task.mark_complete()` | Creates a next occurrence for daily or weekly tasks after completion. |

## 📸 Demo Walkthrough

1. Open the Streamlit app and enter an owner name, pet name, species, and a task such as a walk or medication.
2. Click the add button to create the pet and attach the task to it through the backend owner/pet classes.
3. Generate the schedule to see the scheduler build a daily plan, sort pending tasks by time, and explain the plan.
4. If two tasks overlap, the scheduler surfaces a warning so the owner can adjust the plan before relying on it.
5. The CLI demo script also shows the same behavior in the terminal, including the sorted schedule and recurring-task logic.

Example CLI output from running the demo script:

```text
Today's Schedule
================
08:00 | Morning walk | high | 30 min
08:30 | Play session | high | 20 min
08:50 | Medicine | high | 10 min
09:00 | Feed breakfast | medium | 15 min

Plan Summary
------------
Today's plan includes 4 task(s):
- 08:00: Morning walk (30 min, high)
- 08:30: Play session (20 min, high)
- 08:50: Medicine (10 min, high)
- 09:00: Feed breakfast (15 min, medium)
```
