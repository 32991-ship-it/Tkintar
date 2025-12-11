import tkinter as tk
from tkinter import ttk, messagebox

def submit():
    # เก็บข้อมูลทั้งหมด
    data = {
        "ชื่อ-สกุล": entry_name.get(),
        "อายุ": entry_age.get(),
        "วันเดือนปีเกิด": entry_birth.get(),
        "เพศ": gender_var.get(),
        "อีเมล": entry_email.get(),
        "เบอร์โทร": entry_phone.get(),
        "ที่อยู่": entry_address.get("1.0", tk.END).strip(),
        "ระดับการศึกษา": combo_edu.get(),
        "สาขาวิชา": entry_major.get(),
        "ประสบการณ์ทำงาน": entry_exp.get("1.0", tk.END).strip(),
        "ทักษะพิเศษ": entry_skill.get("1.0", tk.END).strip()
    }

    # ตรวจสอบว่ามีช่องไหนว่าง
    for key, value in data.items():
        if value == "":
            messagebox.showwarning("คำเตือน", f"กรุณากรอกข้อมูลให้ครบ: {key}")
            return

    # แสดงผลข้อมูล
    result = "\n".join([f"{k}: {v}" for k, v in data.items()])
    messagebox.showinfo("ผลการสมัครงาน", result)


root = tk.Tk()
root.title("ฟอร์มสมัครงาน")
root.geometry("600x800")

# ====== TITLE ======
title = tk.Label(root, text="ฟอร์มสมัครงาน", font=("TH Sarabun New", 26))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(padx=20, pady=10, anchor="w")

# ====== ข้อมูลส่วนตัว ======
tk.Label(frame, text="ข้อมูลส่วนตัว", font=("TH Sarabun New", 30, "bold")).grid(row=0, column=0, sticky="w", pady=10)

tk.Label(frame, text="ชื่อ-สกุล", font=("TH Sarabun New", 18)).grid(row=1, column=0, sticky="w")
entry_name = tk.Entry(frame, width=60)
entry_name.grid(row=1, column=1, pady=3)

tk.Label(frame, text="อายุ", font=("TH Sarabun New", 18)).grid(row=2, column=0, sticky="w")
entry_age = tk.Entry(frame, width=15)
entry_age.grid(row=2, column=1, sticky="w")

tk.Label(frame, text="วันเดือนปีเกิด (DD/MM/YYYY)", font=("TH Sarabun New", 18)).grid(row=3, column=0, sticky="w")
entry_birth = tk.Entry(frame, width=20)
entry_birth.grid(row=3, column=1, sticky="w")

tk.Label(frame, text="เพศ", font=("TH Sarabun New", 18)).grid(row=4, column=0, sticky="w")
gender_var = tk.StringVar(value="ชาย")

tk.Radiobutton(frame, text="ชาย", variable=gender_var, value="ชาย").grid(row=4, column=1, sticky="w")
tk.Radiobutton(frame, text="หญิง", variable=gender_var, value="หญิง").grid(row=4, column=1, sticky="w", padx=60)
tk.Radiobutton(frame, text="อื่น ๆ", variable=gender_var, value="อื่น ๆ").grid(row=4, column=1, sticky="w", padx=120)

tk.Label(frame, text="อีเมล", font=("TH Sarabun New", 18)).grid(row=5, column=0, sticky="w")
entry_email = tk.Entry(frame, width=40)
entry_email.grid(row=5, column=1, pady=3)

tk.Label(frame, text="เบอร์โทร", font=("TH Sarabun New", 18)).grid(row=6, column=0, sticky="w")
entry_phone = tk.Entry(frame, width=40)
entry_phone.grid(row=6, column=1, pady=3)

tk.Label(frame, text="ที่อยู่", font=("TH Sarabun New", 18)).grid(row=7, column=0, sticky="nw")
entry_address = tk.Text(frame, width=40, height=4)
entry_address.grid(row=7, column=1, pady=3)

# ====== ข้อมูลการศึกษา ======
tk.Label(frame, text="ข้อมูลการศึกษา", font=("TH Sarabun New", 20, "bold")).grid(row=8, column=0, sticky="w", pady=15)

tk.Label(frame, text="ระดับการศึกษา", font=("TH Sarabun New", 18)).grid(row=9, column=0, sticky="w")
combo_edu = ttk.Combobox(frame, values=[
    "มัธยมศึกษา", "ปวช.", "ปวส.", "ปริญญาตรี", "ปริญญาโท", "ปริญญาเอก"
], width=37)
combo_edu.grid(row=9, column=1, pady=3)

tk.Label(frame, text="สาขาวิชา", font=("TH Sarabun New", 18)).grid(row=10, column=0, sticky="w")
entry_major = tk.Entry(frame, width=30)
entry_major.grid(row=10, column=1, pady=3)

# ====== ประสบการณ์ทำงาน ======
tk.Label(frame, text="ประสบการณ์ทำงาน", font=("TH Sarabun New", 20, "bold")).grid(row=11, column=0, sticky="w", pady=15)

tk.Label(frame, text="รายละเอียด", font=("TH Sarabun New", 18)).grid(row=12, column=0, sticky="nw")
entry_exp = tk.Text(frame, width=40, height=5)
entry_exp.grid(row=12, column=1, pady=3)

# ====== ทักษะพิเศษ ======
tk.Label(frame, text="ทักษะพิเศษ / ความสามารถ", font=("TH Sarabun New", 20, "bold")).grid(row=13, column=0, sticky="w", pady=15)

entry_skill = tk.Text(frame, width=40, height=4)
entry_skill.grid(row=14, column=1, pady=3)

# ====== ปุ่มส่ง ======
submit_btn = tk.Button(root, text="ส่งใบสมัคร", font=("TH Sarabun New", 15), command=submit, width=20)
submit_btn.pack(pady=20)

root.mainloop()
