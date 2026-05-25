import customtkinter as ctk
from tkinter import messagebox
import json
import os


class IssueReport:

    def __init__(self, name, category, location, description, issue):
        self.name = name
        self.category = category
        self.location = location
        self.description = description
        self.issue = issue

    def to_dictionary(self):
        return {
            "name": self.name,
            "category": self.category,
            "location": self.location,
            "description": self.description,
            "issue": self.issue
        }


class SchoolIssueApp:

    def __init__(self, root):

        #window
        self.root = root
        self.root.title("Kaitiaki School Issue Reporter")
        self.root.geometry("700x600")

        #file storage
        self.file_name = "reports.json"

        #heading
        title_label = ctk.CTkLabel(
            root,
            text="Kaitiaki School Issue Reporter",
            font=("Arial", 31, "bold")
        )
        title_label.pack(pady=10)

        #te reo maori
        maori_label = ctk.CTkLabel(
            root,
            text="Help care for our kura (school).",
            font=("Arial", 19)
        )
        maori_label.pack()

        #name label
        name_label = ctk.CTkLabel(
            root,
            text="Your Name:",
            font=("Arial", 16)
        )
        name_label.pack()

        #name entry
        self.name_entry = ctk.CTkEntry(
            root,
            placeholder_text="Enter your name here...",
            width=300
        )
        self.name_entry.pack(pady=5)

        #issue label
        issue_label = ctk.CTkLabel(
            root,
            text="Describe the Issue:",
            font=("Arial", 16)
        )
        issue_label.pack()

        #issue entry
        self.issue_entry = ctk.CTkEntry(
            root,
            placeholder_text="Describe the issue...",
            width=300
        )
        self.issue_entry.pack(pady=5)


#run app
root = ctk.CTk()
app = SchoolIssueApp(root)
root.mainloop()