from pawpal_system import Pet, Task


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
