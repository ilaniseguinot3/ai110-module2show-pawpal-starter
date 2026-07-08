from datetime import date, timedelta

from pawpal_system import Pet, Scheduler, Task


def test_task_completion_updates_status():
    task = Task(description="Morning walk", duration_minutes=30, priority="high")

    task.mark_complete()

    assert task.completed is True


def test_adding_task_to_pet_increases_task_count():
    pet = Pet(name="Mochi", species="dog")
    task = Task(description="Feed breakfast", duration_minutes=15, priority="medium")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Feed breakfast"


def test_recurring_task_creates_next_occurrence_after_completion():
    task = Task(description="Daily meds", duration_minutes=10, priority="high", frequency="daily")
    task.mark_complete()

    assert task.completed is True
    assert task.next_due_date == date.today() + timedelta(days=1)


def test_scheduler_detects_conflicting_task_times():
    scheduler = Scheduler()
    first_task = Task(description="Morning walk", duration_minutes=30, priority="high")
    second_task = Task(description="Feed breakfast", duration_minutes=20, priority="medium")
    first_task.scheduled_time = "09:00"
    second_task.scheduled_time = "09:00"

    warnings = scheduler.detect_conflicts([first_task, second_task])

    assert len(warnings) == 1
    assert "Conflict" in warnings[0]
