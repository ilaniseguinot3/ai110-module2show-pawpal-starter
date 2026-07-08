import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
if owner_name != st.session_state.owner.name:
    st.session_state.owner.name = owner_name

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add pet and task"):
    if st.session_state.owner.get_pet(pet_name) is None:
        st.session_state.owner.add_pet(Pet(name=pet_name, species=species))
    st.session_state.owner.add_task_to_pet(
        pet_name,
        Task(description=task_title, duration_minutes=int(duration), priority=priority),
    )
    st.success(f"Added {task_title} for {pet_name}.")

st.write("### Current pets and tasks")
if st.session_state.owner.pets:
    for pet in st.session_state.owner.pets:
        st.write(f"**{pet.name}** ({pet.species})")
        if pet.tasks:
            for task in pet.tasks:
                st.write(f"- {task.description} ({task.duration_minutes} min, {task.priority})")
        else:
            st.write("- No tasks yet")
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a daily plan from the tasks stored in session state.")

if st.button("Generate schedule"):
    scheduler = Scheduler()
    plan = scheduler.build_daily_plan(st.session_state.owner)
    if plan:
        st.success("Schedule created!")
        st.write(scheduler.explain_plan(plan))
        for task in plan:
            st.write(f"- {task.scheduled_time}: {task.description} ({task.duration_minutes} min, {task.priority})")
    else:
        st.info("No tasks available yet.")
