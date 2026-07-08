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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler currently warns about conflicts when two tasks share the same start time, rather than modeling every possible overlap across full durations. This keeps the logic simple, readable, and fast for a small pet-care app, while still catching the most obvious scheduling mistakes without overcomplicating the implementation.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
