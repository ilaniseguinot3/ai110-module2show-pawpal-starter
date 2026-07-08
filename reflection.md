# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

I planned a simple design centered on a pet owner, their pets, the care tasks they need, and a scheduler that turns those tasks into a daily plan. The main goal was to support a few core user actions clearly and consistently.

- What classes did you include, and what responsibilities did you assign to each?

The system uses four main classes to support the app's core workflow:

1. Owner: represents the pet parent, stores basic profile information, and manages the list of pets they care for.
2. Pet: represents an individual animal, stores basic details such as name and species, and holds the tasks associated with that pet.
3. CareTask: represents a single care activity such as a walk, feeding, or medication, including duration, priority, and completion status.
4. Scheduler: evaluates the tasks and produces a daily plan based on the owner's constraints and the tasks' priorities.

These classes support three core actions for users:

1. Add or update pet information so the app knows which pet needs care.
2. Create and edit care tasks such as walks, feeding, or medication, including details like duration and priority.
3. View a generated daily plan that shows today's scheduled tasks and explains why they were chosen.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes. I refined the initial design by making the relationship between Owner and Pet more explicit in the skeleton, with the Owner class managing a list of pets and the Pet class holding its own tasks. I also added a dedicated Scheduler class to separate planning logic from the data objects so the app would be easier to extend later.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler mainly considers task priority, time order, and basic availability windows. It sorts tasks by urgency and scheduled time, filters tasks for the active day, and warns about conflicts when tasks overlap. I prioritized these constraints because they are the most visible to a pet owner and directly support the app's core goal of creating a practical daily plan without requiring a complicated optimization engine.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler currently warns about conflicts when two tasks share the same start time, rather than modeling every possible overlap across full durations. This keeps the logic simple, readable, and fast for a small pet-care app, while still catching the most obvious scheduling mistakes without overcomplicating the implementation.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used the AI assistant throughout the project for design brainstorming, code scaffolding, testing, and refactoring. It was especially helpful when I needed quick drafts of class structures, method signatures, and test cases. Prompts that asked for concrete implementation steps, such as "write a scheduler class for recurring tasks and conflict warnings" or "help me connect the backend logic to Streamlit," were more useful than broad brainstorming prompts.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One example was when the AI suggested a more elaborate scheduling approach with many conditional branches. I rejected that version because it made the backend harder to read and test. Instead, I kept the scheduler focused on a small set of clear rules: sort by priority and time, filter for active tasks, and warn on overlap. I verified the behavior by running the pytest suite and by checking the CLI output from the demo script to ensure the schedule matched the intended logic.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding tasks to pets, recurring-task behavior, conflict detection, and the scheduler's ability to sort tasks by time. These tests were important because they cover the core user actions that make the app useful: creating tasks, seeing them in a logical order, and receiving useful warnings when the schedule becomes overloaded.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that the current scheduler works well for its intended scope because the tests pass and the demo output is readable and consistent. If I had more time, I would test edge cases such as tasks with very long durations, multiple overlapping conflicts, recurring tasks that span weekends or holidays, and more complex owner availability windows.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how the system stayed modular. The backend logic, tests, and Streamlit UI all work together without being tightly coupled, which makes the project easier to understand and extend.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

In a future iteration, I would expand the scheduler to support more realistic constraints such as user-defined time windows, task dependencies, and richer recurring patterns beyond simple daily recurrence.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

A strong system design is still essential even when AI can generate code quickly. The lead architect needs to guide the structure, define clear responsibilities, and verify that the implementation matches the intended behavior rather than simply accepting the most convenient suggestion.
