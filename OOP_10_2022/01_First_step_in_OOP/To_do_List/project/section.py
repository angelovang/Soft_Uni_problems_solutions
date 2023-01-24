from Inheritance.Need_for_Speed.project import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task : Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try :
            current_task = next(filter(lambda tsk: tsk.name == task_name , self.tasks))
        except StopIteration :
            return f"Could not find task with the name {task_name}"

        current_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        amount_of_tasks = 0
        for elem in self.tasks:
            if elem.completed:
                self.tasks.remove(elem)
                amount_of_tasks += 1

        return f"Cleared {amount_of_tasks} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        for el in self.tasks:
            result.append(el.details())

        return '\n'.join(result)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

section = Section("Daily tasks")
print(section.add_task(task))

second_task = Task("Make bed", "27/05/2020")
print(section.add_task(second_task))

print(section.complete_task("Make bed"))

print(section.view_section())
print(section.clean_section())
print(section.view_section())