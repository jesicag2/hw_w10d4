# HW: Recursive Task Listing

'''
Objective: The objective of this assignment is to introduce students to the concept of recursion by implementing a function to list tasks within a nested hierarchy.

Problem Statement: You are tasked with implementing a recursive function to list tasks within a hierarchical structure. Each task can have subtasks, forming a nested hierarchy. Your task is to design and implement a recursive function named list_tasks that traverses through the hierarchy and lists tasks in a structured manner.
'''

# Task 1: Design the Task Listing Function
# Design a Python function named list_tasks that takes a single parameter: task_hierarchy. The task_hierarchy parameter represents the nested hierarchy of tasks, where each task is a dictionary with the following keys:
    # name: Name or description of the task.
    # subtasks: List of subtasks (nested hierarchy), if any.
# The function should traverse through the task hierarchy recursively and list tasks along with their subtasks in a structured format.

# Task 2:  Implement Task Listing Logic
# Implement the task listing logic within the list_tasks function. Use recursion to traverse through the hierarchy and list tasks along with their subtasks. Print each task name and its subtasks (if any) with appropriate indentation to indicate the hierarchy.

# Task 3: Test the Task Scheduler Function
# Test your list_tasks function with various task hierarchies, including nested hierarchies with different levels of depth. Verify that tasks are listed correctly in a structured format.

task_hierarchy_1 = [
    {
        "name": "Project",
        "subtasks": [
            {"name": "Define project scope"},
            {"name": "Create project plan"},
            {"name": "Assign project team",
            "subtasks": [
                {"name": "Identify team members"},
                {"name": "Allocate roles and responsibilities"}
            ]},
            {"name": "Conduct project kickoff meeting"}
        ]
    },
    {
        "name": "Research",
        "subtasks": [
            {"name": "Gather data"},
            {"name": "Analyze data",
            "subtasks": [
                {"name": "Data cleaning"},
                {"name": "Statistical analysis"}
            ]},
            {"name": "Draw conclusions"}
        ]
    }
]

task_hierarchy_2 = [
    {
        "name": "Homework",
        "subtasks": [
            {"name": "Math assignment",
            "subtasks": [
                {"name": "Complete worksheet"},
                {"name": "Study for quiz"}
            ]},
            {"name": "History essay",
            "subtasks": [
                {"name": "Research topic"},
                {"name": "Write essay"}
            ]}
        ]
    },
    {
        "name": "Home project",
        "subtasks": [
            {"name": "Garden renovation",
            "subtasks": [
                {"name": "Design garden layout"},
                {"name": "Purchase plants and materials"}
            ]},
            {"name": "DIY furniture",
            "subtasks": [
                {"name": "Select furniture design"},
                {"name": "Buy materials"},
                {"name": "Assemble furniture"}
            ]}
        ]
    }
]

def list_tasks(task_hierarchy, indent=0):
    for item in task_hierarchy:
        print("  " * indent + item["name"])
        if "subtasks" in item:
            list_tasks(item["subtasks"], indent + 1)


print("Tasks 1:")
list_tasks(task_hierarchy_1)

print("\n")

print("Tasks 2:")
list_tasks(task_hierarchy_2)