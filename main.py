from tkinter import *

root = Tk()
root.title("SkillGap AI")
root.geometry("500x400")

def analyze():

    role = role_entry.get().lower()
    skills = skills_entry.get().lower().split(",")

    if role == "data analyst":
        required = ["python", "sql", "excel"]

    elif role == "cyber security":
        required = ["networking", "linux", "python"]

    else:
        result.config(text="Role Not Found")
        return

    missing = []

    for skill in required:
        if skill not in skills:
            missing.append(skill)

    output = "Missing Skills:\n"

    for skill in missing:
        output += skill + "\n"

    result.config(text=output)

heading = Label(
    root,
    text="SkillGap AI",
    font=("Arial",20,"bold")
)
heading.pack(pady=10)# Pady is liye use krte hai widgets ke beech thoda space aa jayega aur GUI saaf dikhe

Label(root,text="Target Role").pack()#pack() widget ko window me display aur arrange karne ke liye use hota hai

role_entry = Entry(root,width=30)
role_entry.pack()

Label(root,text="Your Skills").pack()

skills_entry = Entry(root,width=40)
skills_entry.pack()

Button(
    root,
    text="Analyze",
    command=analyze
).pack(pady=10)

result = Label(
    root,
    text="",
    font=("Arial",12)
)
result.pack()

root.mainloop()