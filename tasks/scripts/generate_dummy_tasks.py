from tasks.models import Task
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
import random

# Ensure you have at least one user in your database
user = User.objects.get(username="test")

if not user:
    print("No users found. Please create a user first.")
else:
    # Dummy data for tasks
    titles = [
        "Complete project report",
        "Buy groceries",
        "Prepare presentation slides",
        "Clean the house",
        "Plan weekend trip",
        "Fix the bug in the app",
        "Call the plumber",
        "Organize team meeting",
        "Write a blog post",
        "Read a new book"
    ]

    descriptions = [
        "This task needs to be completed by the end of the week.",
        "Don't forget to buy milk, eggs, and bread.",
        "Slides should include key points and visuals.",
        "Focus on the living room and kitchen.",
        "Decide on the destination and book tickets.",
        "Check the error logs and fix the issue.",
        "The kitchen sink is leaking.",
        "Discuss project updates and next steps.",
        "Write about the latest trends in technology.",
        "Start with the first chapter of the book."
    ]

    statuses = ["P", "IP", "C"]
    priorities = ["L", "M", "H"]
    categories = ["W", "P", "H"]

    # Generate 10 dummy tasks
    for i in range(10):
        Task.objects.create(
            user=user,
            title=titles[i],
            description=descriptions[i],
            created=now(),
            due_date=now() + timedelta(days=random.randint(1, 10)),
            status=random.choice(statuses),
            priority=random.choice(priorities),
            category=random.choice(categories)
        )

    print("10 dummy tasks have been created!")