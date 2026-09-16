import tkinter as tk
from tkinter import messagebox, ttk
import time

class EduBuddyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EduBuddy AI - Socratic Prototype")
        self.root.geometry("420x650")
        self.root.configure(bg="#121212")
        
        self.current_step = 1
        self.max_steps = 10
        self.user_topic = "Python Arrays"
        self.difficulty_score = 5
        
        self.ai_doubts = {
            "ai": [
                "Interesting pivot to AI! For level 1, what is the core difference between Machine Learning and a traditional rule-based Python script?",
                "Level 2: When training an AI model, why do we split data into training and validation sets? What happens if we don't?",
                "Level 3: If an AI model gets 100% accuracy on training data but fails on real world data, what went wrong?",
                "Level 4: How does a Neural Network node decide to pass information? What is the purpose of an activation function?",
                "Level 5: Wow, you know your stuff. In deep learning architectures like Transformers, what exactly does the 'Self-Attention' mechanism do?",
                "Level 6: Let's scale up. How do you prevent exploding gradients during backpropagation in a very deep neural network?",
                "Level 7: If you were deploying an LLM locally on an edge device with low RAM, what optimization techniques would you apply?",
                "Level 8: Real-world case: Explain how a contrastive loss function works in self-supervised computer vision models.",
                "Level 9: How do you mathematically guarantee convergence when training generative adversarial networks (GANs)?",
                "Level 10: Elite Level! How would you design a distributed training pipeline across 1000 GPUs to avoid parameter sync bottlenecks?"
            ],
            "python": [
                "For level 1, why does a dictionary search run faster than checking a list one item at a time?",
                "Level 2: What is the spatial complexity when allocating a dynamic hash map versus a fixed array structure?",
                "Level 3: How do you manage memory collisions when multiple keys resolve to the exact same hash index?",
                "Level 4: Deep test: How does Python handle memory allocation under the hood when a dictionary grows beyond its initial buffer size?"
            ]
        }
        
        self.create_styles()
        self.show_welcome_screen()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TButton", font=("Helvetica", 11, "bold"), background="#1E1E1E", foreground="#FFFFFF", borderwidth=0)
        self.style.map("TButton", background=[('active', '#333333')])

    def clrscr(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clrscr()
        header = tk.Label(self.root, text="⏰ 6:00 AM REFLECTION", font=("Helvetica", 14, "bold"), fg="#BB86FC", bg="#121212", pady=20)
        header.pack()
        
        info_card = tk.Label(self.root, text="Scheduled Block Finished:\n5:00 AM - 6:00 AM [Python Basic Arrays]", 
                             font=("Helvetica", 11), fg="#E0E0E0", bg="#1E1E1E", bd=10, relief="flat", width=35, height=3)
        info_card.pack(pady=10)

        prompt_lbl = tk.Label(self.root, text="🤖 AI Learner:\n'Hey teacher! Explain what you learned,\nor type a different topic if you changed your plan!'", 
                              font=("Helvetica", 11, "italic"), fg="#03DAC6", bg="#121212", justify="center")
        prompt_lbl.pack(pady=20)

        self.text_input = tk.Text(self.root, height=8, width=38, bg="#1E1E1E", fg="#FFFFFF", insertbackground="white", font=("Helvetica", 11), bd=2, relief="solid")
        self.text_input.pack(pady=10)
        self.text_input.insert(tk.END, "Actually, I changed my mind. I read about Artificial Intelligence models instead...")

        submit_btn = ttk.Button(self.root, text="SUBMIT EXPLANATION", command=self.process_initial_input)
        submit_btn.pack(pady=20)

    def process_initial_input(self):
        user_raw_text = self.text_input.get("1.0", tk.END).lower().strip()
        if "artificial intelligence" in user_raw_text or "ai" in user_raw_text or "model" in user_raw_text:
            self.user_topic = "ai"
        else:
            self.user_topic = "python"
        self.current_step = 1
        self.show_socratic_loop_screen()

    def show_socratic_loop_screen(self):
        self.clrscr()
        prog_text = f"Socratic Depth: Level {self.current_step} / {self.max_steps}"
        header = tk.Label(self.root, text=prog_text, font=("Helvetica", 12, "bold"), fg="#BB86FC", bg="#121212", pady=15)
        header.pack()
        
        questions = self.ai_doubts[self.user_topic]
        q_idx = min(self.current_step - 1, len(questions) - 1)
        current_question = questions[q_idx]

        doubt_lbl = tk.Label(self.root, text=f"🧑‍🎓 AI Learner Persona Says:\n\n\"{current_question}\"", 
                             font=("Helvetica", 11), fg="#E0E0E0", bg="#1E1E1E", wraplength=350, justify="left", pady=20, padx=15, bd=1, relief="solid")
        doubt_lbl.pack(pady=15, fill="x", padx=20)

        reply_lbl = tk.Label(self.root, text="Your Answer / Explanation:", font=("Helvetica", 10, "bold"), fg="#888888", bg="#121212")
        reply_lbl.pack(anchor="w", padx=25)

        self.loop_input = tk.Text(self.root, height=6, width=38, bg="#1E1E1E", fg="#FFFFFF", insertbackground="white", font=("Helvetica", 11), bd=1, relief="solid")
        self.loop_input.pack(pady=5)

        btn_frame = tk.Frame(self.root, bg="#121212")
        btn_frame.pack(pady=25)

        next_btn = ttk.Button(btn_frame, text="SUBMIT ANSWER", command=self.evaluate_loop_answer)
        next_btn.grid(row=0, column=0, padx=10)

        quit_btn = ttk.Button(btn_frame, text="SHOW RESULTS", command=self.show_final_results)
        quit_btn.grid(row=0, column=1, padx=10)

    def evaluate_loop_answer(self):
        answer_text = self.loop_input.get("1.0", tk.END).strip().lower()
        if not answer_text:
            messagebox.showwarning("Empty Answer", "Please provide a quick logic answer to clear your student's doubt!")
            return

        if "don't know" in answer_text or "wrong" in answer_text or "skip" in answer_text or len(answer_text) < 8:
            self.difficulty_score -= 1
            proceed = messagebox.askyesno("Struggling Detected", "It looks like you're running into a mental wall on this level.\n\nWould you like to continue onto the next question anyway?")
            if not proceed:
                self.show_final_results()
                return
        else:
            self.difficulty_score += 1
            
        self.current_step += 1
        if self.current_step > self.max_steps:
            self.show_final_results()
        else:
            self.show_socratic_loop_screen()

    def show_final_results(self):
        self.clrscr()
        header = tk.Label(self.root, text="🏆 SESSION COMPLETE", font=("Helvetica", 14, "bold"), fg="#03DAC6", bg="#121212", pady=25)
        header.pack()

        final_rating = max(10, min(100, int((self.difficulty_score / (self.current_step + 3)) * 100)))
        stats_box = tk.Label(self.root, 
                             text=f"Topic Studied: {self.user_topic.upper()}\n"
                                  f"Socratic Levels Cleared: {self.current_step - 1}\n"
                                  f"Concept Retention Accuracy: {final_rating}%\n\n"
                                  f"🔗 Macro Placement Progress: +1.45%", 
                             font=("Helvetica", 12), fg="#FFFFFF", bg="#1E1E1E", bd=15, relief="flat", justify="left")
        stats_box.pack(pady=20, padx=30, fill="x")

        greet_lbl = tk.Label(self.root, text="👋 Awesome teaching session today!\nYour career progress records have been synced.\nHave a wonderful day ahead!", 
                             font=("Helvetica", 11, "italic"), fg="#BB86FC", bg="#121212", justify="center")
        greet_lbl.pack(pady=30)

        exit_btn = ttk.Button(self.root, text="CLOSE APP & LOG OFF", command=self.root.quit)
        exit_btn.pack(pady=10)

if __name__ == "__main__":
    window = tk.Tk()
    app = EduBuddyApp(window)
    window.mainloop()
      
