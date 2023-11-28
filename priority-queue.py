class Patient:
    def __init__(self, name, age):
        self.details = (name, age)

    def __str__(self):
        return f"('{self.details[0]}', {self.details[1]})"


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)
        self.queue.sort(key=lambda x: x.details[1], reverse=True)   # the greater the age the greater the priority

    def dequeue(self):
        if not self.is_empty():
            min_key = max(self.queue, key=lambda x: x.details[1])
            self.queue.remove(min_key)
            return min_key
        else:
            return None

    def peek(self):
        if not self.is_empty():
            self.queue.sort(key=lambda x: x.key, reverse=True)
            return self.queue[0]
        else:
            print("Queue is empty. Cannot peek.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def update(self, name, age):
        # Remove the patient with the given name, if present
        self.queue = [patient for patient in self.queue if patient.details[0] != name]

        # Append the patient with the new details to the front of the stack
        self.queue.insert(0, Patient(name, age))

    def remove(self, patient_name, patient_age):
        # Find the index of the patient with the given name and age
        index_to_remove = None
        for i, patient in enumerate(self.queue):
            if patient.details[0] == patient_name and patient.details[1] == patient_age:
                index_to_remove = i
                break

        # If the patient is found, remove it
        if index_to_remove is not None:
            del self.queue[index_to_remove]
        else:
            print("No such patient!")

    def __str__(self):
        return "[" + ", ".join(str(patient) for patient in self.queue) + "]"