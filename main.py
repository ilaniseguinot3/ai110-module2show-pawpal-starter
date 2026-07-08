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

    # Create overlapping tasks to demonstrate conflict detection
    overlapping_walk = Task("Overlapping walk", 20, "high")
    overlapping_play = Task("Overlapping play", 15, "high")
    owner.add_task_to_pet("Mochi", overlapping_walk)
    owner.add_task_to_pet("Luna", overlapping_play)

    # Add tasks out of order to show sorting and filtering
    owner.add_task_to_pet("Mochi", Task("Evening check-in", 10, "low"))
    owner.add_task_to_pet("Luna", Task("Brush fur", 15, "medium"))

    scheduler = Scheduler()
    unsorted_tasks = owner.get_all_tasks()
    sorted_by_time = scheduler.sort_by_time(unsorted_tasks)
    pending_tasks = scheduler.filter_tasks(unsorted_tasks, completed=False)

    print("Today's Schedule")
    print("================")
    for task in sorted_by_time:
        print(f"{task.scheduled_time or 'unscheduled'} | {task.description} | {task.priority} | {task.duration_minutes} min")

    print("\nPending Tasks")
    print("-------------")
    for task in pending_tasks:
        print(f"- {task.description} ({task.priority})")

    plan = scheduler.build_daily_plan(owner)
    overlapping_walk.scheduled_time = "09:00"
    overlapping_play.scheduled_time = "09:00"
    conflicts = scheduler.detect_conflicts(plan)

    print("\nPlan Summary")
    print("------------")
    print(scheduler.explain_plan(plan))

    if conflicts:
        print("\nWarnings")
        print("--------")
        for warning in conflicts:
            print(warning)


if __name__ == "__main__":
    main()
