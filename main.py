from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(name="Jordan", available_start="08:00", available_end="12:00")

    mochi = Pet(name="Mochi", species="dog", age=3)
    luna = Pet(name="Luna", species="cat", age=2)

    owner.add_pet(mochi)
    owner.add_pet(luna)

    owner.add_task_to_pet("Mochi", Task("Morning walk", 30, "high"))
    owner.add_task_to_pet("Mochi", Task("Feed breakfast", 15, "medium"))
    owner.add_task_to_pet("Luna", Task("Play session", 20, "high"))
    owner.add_task_to_pet("Luna", Task("Medicine", 10, "high"))

    scheduler = Scheduler()
    plan = scheduler.build_daily_plan(owner)

    print("Today's Schedule")
    print("================")
    for task in plan:
        print(f"{task.scheduled_time} | {task.description} | {task.priority} | {task.duration_minutes} min")

    print("\nPlan Summary")
    print("------------")
    print(scheduler.explain_plan(plan))


if __name__ == "__main__":
    main()
