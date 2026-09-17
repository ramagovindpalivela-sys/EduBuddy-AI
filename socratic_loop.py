import tkinter as tk
from tkinter import messagebox, ttk

def run_socratic_interaction(app):
    app.clrscr()
    
    # Progress Bar UI calculation
    p_frame = tk.Frame(app.root, bg="#333333", height=6)
    p_frame.pack(fill="x", pady=(0, 15))
    fill_w = int((app.current_step / app.max_steps) * 430)
    tk.Frame(p_frame, bg="#03DAC6", height=6, width=fill_w).place(x=0, y=0)

    tk.Label(app.root, text=f"SOCRATIC DIFFICULTY CHECK: LEVEL {app.current_step} / {app.max_steps}", 
             font=("Helvetica", 11, "bold"), fg="#BB86FC", bg="#121212").pack(pady=5)
    
    questions = app.ai_doubts[app.user_topic]
    q_idx = min(app.current_step - 1, len(questions) - 1)
    active_doubt = questions[q_idx]

    # The Socratic Doubt Box Layout
    card = tk.Frame(app.root, bg="#1E1E1E", bd=1, relief="solid")
    card.pack(padx=20, fill="x", pady=15)
    tk.Label(card, text="🧑‍🎓 Curious Learner Agent:", font=("Helvetica", 10, "bold"), fg="#03DAC6", bg="#1E1E1E", padx=10, pady=5).pack(anchor="w")
    tk.Label(card, text=f'"{active_doubt}"', font=("Helvetica", 11, "italic"), fg="#FFFFFF", bg="#1E1E1E", wraplength=340, justify="left", padx=15, pady=10).pack(anchor="w")

    tk.Label(app.root, text="Articulate Your Answer Logic:", font=("Helvetica", 10, "bold"), fg="#888888", bg="#121212").pack(anchor="w", padx=25, pady=(10,0))
    app.interactive_entry = tk.Text(app.root, height=5, width=38, bg="#1E1E1E", fg="#FFFFFF", font=("Helvetica", 11), bd=1, relief="solid")
    app.interactive_entry.pack(pady=5)

    a_frame = tk.Frame(app.root, bg="#121212")
    a_frame.pack(pady=20)
    ttk.Button(a_frame, text="SUBMIT RESPONSE", style="Accent.TButton", command=lambda: evaluate_step(app)).grid(row=0, column=0, padx=10)
    ttk.Button(a_frame, text="SEE SCORES", style="Dark.TButton", command=lambda: show_results(app)).grid(row=0, column=1, padx=10)

def evaluate_step(app):
    ans = app.interactive_entry.get("1.0", tk.END).strip().lower()
    if not ans:
        app.play_sound("alert")
        return

    if "don't know" in ans or "wrong" in ans or len(ans) < 7:
        app.play_sound("alert")
        app.difficulty_score -= 1
        go_on = messagebox.askyesno("Roadblock", "Struggling detected. Continue to next level or show results?")
        if not go_on:
            show_results(app)
            return
    else:
        app.play_sound("success")
        app.difficulty_score += 1

    app.current_step += 1
    if app.current_step > app.max_steps:
        show_results(app)
    else:
        run_socratic_interaction(app)

def show_results(app):
    app.clrscr()
    app.play_sound("success")
    tk.Label(app.root, text="🏆 SESSION ANALYSIS REPORT", font=("Helvetica", 14, "bold"), fg="#03DAC6", bg="#121212", pady=25).pack()

    panel = tk.Frame(app.root, bg="#1E1E1E", bd=1, relief="solid")
    panel.pack(padx=25, fill="x", pady=10)
    pct = max(15, min(100, int((app.difficulty_score / (app.current_step + 3)) * 100)))

    tk.Label(panel, text=f"Student Profile: {app.student_name}\nTarget Goal: {app.macro_goal}\nAccuracy: {pct}%", 
             font=("Helvetica", 11), fg="#E0E0E0", bg="#1E1E1E", justify="left", padx=15, pady=15).pack()

    m_box = tk.Label(app.root, text="🔗 Hour-to-Career Link Matrix:\n🏆 Placement Readiness Progress Boosted by +2.25%!", font=("Helvetica", 10, "bold"), fg="#03DAC6", bg="#1E1E1E", bd=10, relief="flat")
    m_box.pack(pady=25, padx=25, fill="x")
    
    ttk.Button(app.root, text="LOG OFF RUNTIME", style="Accent.TButton", command=app.root.quit).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    # Dummy placeholder loop trigger logic execution safeguard
    root.mainloop()
  
