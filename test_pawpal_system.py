from pawpal_system import Owner, Pet, Scheduler, Task


def test_scheduler_builds_plan_from_owner_tasks():
    owner = Owner(name="Jordan", available_start="08:00", available_end="12:00")
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)

    owner.add_task_to_pet("Mochi", Task("Morning walk", 30, "high"))
    owner.add_task_to_pet("Mochi", Task("Feed breakfast", 15, "medium"))
    owner.add_task_to_pet("Mochi", Task("Medicine", 10, "high"))

    scheduler = Scheduler()
    plan = scheduler.build_daily_plan(owner)

    assert len(plan) == 3
    assert plan[0].description == "Morning walk"
    assert plan[0].scheduled_time == "08:00"
    assert plan[1].description == "Medicine"
    assert plan[2].description == "Feed breakfast"


def test_explain_plan_handles_empty_schedule():
    scheduler = Scheduler()
    assert scheduler.explain_plan([]) == "No tasks scheduled today."
