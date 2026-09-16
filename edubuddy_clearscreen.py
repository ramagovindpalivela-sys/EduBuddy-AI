import os
import time

# Custom function to handle modern clear-screen actions across all environments
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global User State Matrix Simulation
USER_PROFILE = {
    "name": "Ananya",
    "macro_goal": "Campus Ready - Junior Backend Engineer",
    "skills": {
        "Python Syntax": 85,
        "Data Structures (Hash Maps)": 20,
        "System Architecture": 10,
        "Technical Communication": 40
    },
    "long_term_progress_pct": 34.5
}

def run_interactive_demo():
    # STEP 1: Morning Alarm Dashboard Screen
    clrscr()
    print("=" * 60)
    print(" ⏰ EDUBUDDY AI: 6:00 AM REFLECTION WINDOW (MOBILE VIEW) ")
    print("=" * 60)
    print("Notification: [Schedule Block Finished: 5:00 AM - 6:00 AM]")
    print("Task Scheduled: Solve Python Array Problem 'Two Sum'\n")
    print("🤖 AI Learner: 'Hey teacher! I saw you just finished your Python block.")
    print("   How would you like to explain today's logic to me?'")
    print("\n   Record 1-Min Audio/Video \n   Text-only Mode")
    print("-" * 60)
    
    choice = input("Select an option (1 or 2): ").strip()
    
    # STEP 2: Input Content Screen
    clrscr()
    print("=" * 60)
    print(" 🎙️ MULTIMODAL KNOWLEDGE TRANSCRIPTION ENGINE")
    print("=" * 60)
    
    if choice == "1":
        print("[🎙️ System Simulation: Audio recording active... User is speaking...]")
        time.sleep(1)
        user_explanation = (
            "I solved it by creating a Python dictionary. As I looped through the list, "
            "I checked if the target minus the current number was already in the dictionary. "
            "If it was, I found the pair! This prevents using a slow double loop inside a loop."
        )
        print(f"\n💬 Transcribed Audio Input:\n   \"{user_explanation}\"")
    else:
        print("🤖 AI Learner: 'No problem! Write down how you understood it in your own words:'")
        user_explanation = input("\n✍️ Your Input: ")

    print("\n" + "-" * 60)
    print("Saving voice buffer... Analyzing semantic structures...")
    input("\n[Press Enter to submit to your AI student...]")

    # STEP 3: The Socratic Peer Interaction Screen
    clrscr()
    print("=" * 60)
    print(" 🧑‍🎓 BECOMING THE TEACHER: AI AGENT RESPONSE ")
    print("=" * 60)
    print("🤖 AI Processing Explanation Logic...")
    time.sleep(1.5)
    
    print("\n🧑‍🎓 AI (Learner Persona):")
    print("   'Oh wow, teacher! That dictionary trick sounds super fast because it avoids nested loops.")
    print("   But I have a genuine doubt... What if our input array has millions of numbers?")
    print("   Won't our dictionary become massive and eat up all the system memory?")
    print("   Where would an engineer use this optimization in a real-world app like an Instagram live-feed filter?'")
    print("-" * 60)
    
    user_answer = input("\n🧠 Answer your student's doubt: ")
    print("\nEvaluating your answer... Connecting components...")
    time.sleep(1.5)

    # STEP 4: Career Analytics Metric Dashboard Screen
    clrscr()
    print("=" * 60)
    print(" 🏆 SESSION VERIFIED! MICRO-TO-MACRO PROGRESS GRAPH ")
    print("=" * 60)
    
    # Allocation calculations for milestone pacing updates
    skill_gain_ds = 12  
    skill_gain_comm = 8 
    macro_boost = round(((skill_gain_ds + skill_gain_comm) / 400) * 100, 2)
    
    USER_PROFILE["skills"]["Data Structures (Hash Maps)"] += skill_gain_ds
    USER_PROFILE["skills"]["Technical Communication"] += skill_gain_comm
    USER_PROFILE["long_term_progress_pct"] += macro_boost
    
    print("📊 Metric Breakdown Updates:")
    print(f"   📈 Data Structures: {USER_PROFILE['skills']['Data Structures (Hash Maps)']}% (+{skill_gain_ds}%)")
    print(f"   📈 Technical Communication: {USER_PROFILE['skills']['Technical Communication']}% (+{skill_gain_comm}%)")
    print(f"\n🔗 Interconnection Matrix Link:")
    print(f"   [1-Hour Problem] ──► Verified Concept Mastery ──► Linked to Weekly Milestone 'Arrays & Hashing'")
    print("\n🎯 Long-Term Alignment Check:")
    print(f"   You are now {USER_PROFILE['long_term_progress_pct']}% closer to your ultimate goal: '{USER_PROFILE['macro_goal']}'!")
    print("=" * 60)
    print("\nDemo Session Completed Successfully.")

if __name__ == "__main__":
    run_interactive_demo()
  
