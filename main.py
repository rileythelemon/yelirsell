import customtkinter as ctk
from tkinter import messagebox
import json
import os

#File used to store reports
FILE = "reports.json"


#Load reports from the JSON file
def get_reports():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                return json.load(file)
        except:
            pass
    return []


#Save reports to the JSON file
def save_reports(reports):
    with open(FILE, "w") as file:
        json.dump(reports, file, indent=4)


#Display all reports in the history box
def load_reports():
    history.configure(state="normal")
    history.delete("1.0", "end")

    reports = get_reports()
    report_count = len(reports)  #Integer variable

    for i, report in enumerate(reports, start=1):
        history.insert(
            "end",
            f"Report #{i}\n"
            f"Name: {report['name']}\n"
            f"Issue: {report['issue']}\n"
            f"{'-' * 50}\n"
        )

    history.configure(state="disabled")


#Submit a new issue report
def submit_issue():
    student = name.get().strip()  #String variable
    issue = issue_box.get("1.0", "end").strip()

    #Selection (IF statement)
    if not student or not issue:
        messagebox.showerror(
            "Error",
            "Please complete all fields."
        )
        return

    reports = get_reports()

    reports.append({
        "name": student,
        "issue": issue
    })

    save_reports(reports)

    #Clear input boxes
    name.delete(0, "end")
    issue_box.delete("1.0", "end")

    messagebox.showinfo(
        "Success",
        "Ka pai! Issue submitted successfully."
    )

    load_reports()


#Remove the oldest report
def resolve_issue():
    reports = get_reports()

    #Selection (IF statement)
    if not reports:
        messagebox.showinfo(
            "No Reports",
            "There are no reports to resolve."
        )
        return

    reports.pop(0)

    save_reports(reports)

    messagebox.showinfo(
        "Resolved",
        "Issue marked as resolved."
    )

    load_reports()



#Window Setup

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Kaitiaki School Issue Reporter")
root.geometry("740x730")

#Heading
ctk.CTkLabel(
    root,
    text="Kaitiaki School Issue Reporter",
    font=("Arial", 30, "bold")
).pack(pady=10)

#Maori message
ctk.CTkLabel(
    root,
    text="Ka pai! Help care for our kura (school).",
    font=("Arial", 18)
).pack(pady=5)

#Name input
ctk.CTkLabel(
    root,
    text="Your Name:"
).pack()

name = ctk.CTkEntry(
    root,
    width=300,
    placeholder_text="Enter your name..."
)
name.pack(pady=5)

#Issue input
ctk.CTkLabel(
    root,
    text="Describe the Issue:"
).pack()

issue_box = ctk.CTkTextbox(
    root,
    width=400,
    height=120
)
issue_box.pack(pady=5)

#submit button
ctk.CTkButton(
    root,
    text="Submit Issue",
    command=submit_issue
).pack(pady=10)

#History section
ctk.CTkLabel(
    root,
    text="Report History"
).pack()

history = ctk.CTkTextbox(
    root,
    width=600,
    height=250
)
history.pack(pady=10)

history.configure(state="disabled")

#Resolve button
ctk.CTkButton(
    root,
    text="Resolve Oldest Issue",
    command=resolve_issue
).pack(pady=10)

#Load saved reports when program starts
load_reports()

root.mainloop()
