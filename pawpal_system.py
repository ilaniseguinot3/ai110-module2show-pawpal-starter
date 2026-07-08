from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


PRIORITY_RANK = {"low": 0, "medium": 1, "high": 2}


@dataclass
class Task:
    description: str
    duration_minutes: int = 30
    priority: str = "medium"
    scheduled_time: Optional[str] = None
    frequency: str = "once"
    completed: bool = False
    next_due_date: Optional[date] = None

    def mark_complete(self) -> None:
        """Mark the task as completed and create the next recurrence if needed."""
        self.completed = True
        if self.frequency == "daily":
            self.next_due_date = date.today() + timedelta(days=1)
        elif self.frequency == "weekly":
            self.next_due_date = date.today() + timedelta(weeks=1)

    def mark_incomplete(self) -> None:
        """Reset the task to an incomplete state."""
        self.completed = False

    def to_dict(self) -> dict:
        """Return a dictionary representation of the task."""
        return {
            "description": self.description,
            "duration_minutes": self.duration_minutes,
            "priority": self.priority,
            "scheduled_time": self.scheduled_time,
            "frequency": self.frequency,
            "completed": self.completed,
        }


CareTask = Task


@dataclass
class Pet:
    name: str
    species: str = ""
    age: int = 0
    owner: Optional["Owner"] = None
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a task to this pet."""
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        """Return unfinished tasks for this pet."""
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        """Return completed tasks for this pet."""
        return [task for task in self.tasks if task.completed]


@dataclass
class Owner:
    name: str
    email: str = ""
    pets: List[Pet] = field(default_factory=list)
    available_start: str = "08:00"
    available_end: str = "20:00"

    def add_pet(self, pet: Pet) -> None:
        """Register a pet with this owner."""
        pet.owner = self
        self.pets.append(pet)

    def get_pet(self, pet_name: str) -> Optional[Pet]:
        """Find a pet by name."""
        for pet in self.pets:
            if pet.name.lower() == pet_name.lower():
                return pet
        return None

    def add_task_to_pet(self, pet_name: str, task: Task) -> bool:
        """Add a task to the named pet if it exists."""
        pet = self.get_pet(pet_name)
        if pet is None:
            return False
        pet.add_task(task)
        return True

    def get_all_tasks(self) -> List[Task]:
        """Return every task owned by the owner's pets."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def get_pending_tasks(self) -> List[Task]:
        """Return all unfinished tasks across the owner's pets."""
        return [task for task in self.get_all_tasks() if not task.completed]


@dataclass
class Scheduler:
    def collect_tasks(self, owner: Owner) -> List[Task]:
        """Gather pending tasks from the owner's pets."""
        return owner.get_pending_tasks()

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Order tasks by priority and duration."""
        return sorted(
            tasks,
            key=lambda task: (
                -PRIORITY_RANK.get(task.priority.lower(), 1),
                -task.duration_minutes,
                task.description.lower(),
            ),
        )

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by their scheduled time in HH:MM format."""
        return sorted(tasks, key=lambda task: self._to_minutes(task.scheduled_time or "23:59"))

    def filter_tasks(self, tasks: List[Task], *, pet_name: Optional[str] = None, completed: Optional[bool] = None) -> List[Task]:
        """Filter tasks by pet name or completion status."""
        filtered = list(tasks)
        if pet_name is not None:
            filtered = [task for task in filtered if pet_name.lower() in task.description.lower()]
        if completed is not None:
            filtered = [task for task in filtered if task.completed is completed]
        return filtered

    def build_daily_plan(self, owner: Owner) -> List[Task]:
        """Create a simple daily plan that fits within the owner's availability."""
        tasks = self.sort_tasks(self.collect_tasks(owner))
        start_minutes = self._to_minutes(owner.available_start)
        end_minutes = self._to_minutes(owner.available_end)
        current_time = start_minutes
        plan: List[Task] = []

        for task in tasks:
            if current_time + task.duration_minutes > end_minutes:
                continue
            task.scheduled_time = self._to_hhmm(current_time)
            plan.append(task)
            current_time += task.duration_minutes

        return plan

    def explain_plan(self, plan: List[Task]) -> str:
        """Return a human-readable summary of the scheduled plan."""
        if not plan:
            return "No tasks scheduled today."

        lines = [f"Today's plan includes {len(plan)} task(s):"]
        for task in plan:
            time_label = task.scheduled_time or "unscheduled"
            lines.append(f"- {time_label}: {task.description} ({task.duration_minutes} min, {task.priority})")
        return "\n".join(lines)

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return simple warnings for tasks that overlap in time."""
        warnings: List[str] = []
        for index, task in enumerate(tasks):
            if not task.scheduled_time:
                continue
            start = self._to_minutes(task.scheduled_time)
            end = start + task.duration_minutes
            for other in tasks[index + 1 :]:
                if not other.scheduled_time:
                    continue
                other_start = self._to_minutes(other.scheduled_time)
                other_end = other_start + other.duration_minutes
                if start < other_end and other_start < end:
                    warnings.append(
                        f"Conflict: {task.description} overlaps with {other.description} at {task.scheduled_time}."
                    )
        return warnings

    def _to_minutes(self, value: str) -> int:
        hours_str, minutes_str = value.split(":")
        return int(hours_str) * 60 + int(minutes_str)

    def _to_hhmm(self, minutes: int) -> str:
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours:02d}:{mins:02d}"
