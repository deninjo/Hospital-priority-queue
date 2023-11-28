import tkinter as tk
from tkinter import messagebox
from priority_queue import Patient, PriorityQueue

class HospitalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Priority Queue")

        self.priority_queue = PriorityQueue()

        self.name_label = tk.Label(master, text="Patient Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.age_label = tk.Label(master, text="Patient Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)

        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.enqueue_button = tk.Button(master, text="Add Patient", command=self.enqueue_patient)
        self.enqueue_button.grid(row=2, column=0, padx=10, pady=10)

        self.dequeue_button = tk.Button(master, text="Process Patient", command=self.dequeue_patient)
        self.dequeue_button.grid(row=2, column=1, padx=10, pady=10)

        self.peek_button = tk.Button(master, text="Peek", command=self.peek_patient)
        self.peek_button.grid(row=2, column=2, padx=10, pady=10)

        self.is_empty_button = tk.Button(master, text="Is Empty", command=self.is_empty_queue)
        self.is_empty_button.grid(row=2, column=3, padx=10, pady=10)

        self.size_button = tk.Button(master, text="Size", command=self.get_queue_size)
        self.size_button.grid(row=2, column=4, padx=10, pady=10)

        self.update_button = tk.Button(master, text="Update Patient", command=self.update_patient)
        self.update_button.grid(row=2, column=5, padx=10, pady=10)

        self.remove_button = tk.Button(master, text="Remove Patient", command=self.remove_patient)
        self.remove_button.grid(row=2, column=6, padx=10, pady=10)

        self.display_text = tk.Text(master, height=10, width=40)
        self.display_text.grid(row=3, column=0, columnspan=7, padx=10, pady=10)

        self.update_display()

    def enqueue_patient(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        patient = Patient(name, age)
        self.priority_queue.enqueue(patient)
        self.update_display()

    def dequeue_patient(self):
        patient = self.priority_queue.dequeue()
        if patient is not None:
            self.update_display()

    def peek_patient(self):
        patient = self.priority_queue.peek()
        if patient is not None:
            messagebox.showinfo("Peeked Patient", f"The patient at the front of the queue is:\n{str(patient)}")
        else:
            messagebox.showinfo("Peeked Patient", "The queue is empty.")

    def is_empty_queue(self):
        is_empty = self.priority_queue.is_empty()
        messagebox.showinfo("Is Empty", f"The queue is {'empty' if is_empty else 'not empty'}.")

    def get_queue_size(self):
        size = self.priority_queue.size()
        messagebox.showinfo("Queue Size", f"The size of the queue is: {size}")

    def update_patient(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        self.priority_queue.update(name, age)
        self.update_display()

    def remove_patient(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        try:
            self.priority_queue.remove(name, age)
            self.update_display()
        except ValueError:
            messagebox.showinfo("Error", "No such patient!")

    def update_display(self):
        self.display_text.delete(1.0, tk.END)
        for i, patient in enumerate(self.priority_queue.queue, start=1):
            self.display_text.insert(tk.END, f"Patient {i}: {str(patient)}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
