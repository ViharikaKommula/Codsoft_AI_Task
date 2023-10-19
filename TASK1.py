import tkinter as tk
from tkinter import messagebox
def response_to_user_input(user_input):
    rules = {
        'hello': 'Hello! How may I assist you todayl?',
        'how are you': 'I am a bot, but thanks for asking!',
        'bye': 'Bye! Please rate your experience (0-10):',
        'thank you': "You're welcome!",
        'what can you do': 'I can answer the questions asked by you.',
        'what is your favorite color': "My favorite color is pink.",
        'do you have a favorite food': "As a chatbot, I do not have any favorite foods.",
        'what is your favorite movie': "I do not have any favorite movies but horror, action and mystery are some genres you should try.",
        'what is your favorite book': "I do not have a specific favorite book",
        'what is your favorite song': "I don't have a favorite song.",
        'what is your favorite animal': "I don't have a favorite animal.",
        'what is your favorite place': "I don't have a favorite place.",
        'what is your favorite thing to do': "I don't have a favorite thing to do.",
        'what is your favorite person': "As a chatbot, I do not have a favorite person",
        'what is your biggest accomplishment': "I don't have a biggest accomplishment."
    }
    for rule, response in rules.items():
        if rule in user_input.lower():
            return response
    return "I'm not sure how to respond to that."
def send_message(event=None):
    user_input = input_box.get()
    bot_reply = response_to_user_input(user_input)
    message_listbox.insert(tk.END, f"User: {user_input}")
    message_listbox.insert(tk.END, f"Bot: {bot_reply}")
    input_box.delete(0, tk.END)
    if 'Bye! Please rate your experience (0-10):' in bot_reply:
        feedback_scale.pack()
def feedback_response():
    rating = feedback_scale.get()
    messagebox.showinfo("Feedback", f"Thank you for your feedback. You rated your experience as: {rating}/10")
    root.destroy()
def update_input_box(*args):
    selected_option = selected_rule.get()
    input_box.delete(0, tk.END)
    input_box.insert(tk.END, selected_option)
    send_message()
root = tk.Tk()
root.title("Chatbot with Feedback")
root.geometry("400x400")
message_listbox = tk.Listbox(root, width=50, height=15)
message_listbox.pack()
rules = [
    'Hello',
    'How are you',
    'Bye',
    'Thank you',
    'What can you do',
    'What is your favorite color',
    'Do you have a favorite food',
    'What is your favorite movie',
    'What is your favorite book',
    'What is your favorite song',
    'What is your favorite animal',
    'What is your favorite place',
    'What is your favorite thing to do',
    'What is your favorite person',
    'What is your biggest accomplishment'
]
selected_rule = tk.StringVar(root)
selected_rule.set(rules[0])  # Set the default rule
rule_menu = tk.OptionMenu(root, selected_rule, *rules)
rule_menu.pack()
selected_rule.trace('w', lambda *args: update_input_box())  # Bind dropdown selection to update_input_box function
input_box = tk.Entry(root, width=50)
input_box.pack()
input_box.bind("<Return>", send_message)  # Binds the Enter key to send_message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()
feedback_scale = tk.Scale(root, from_=0, to=10, orient='horizontal', label="Rate your experience:")
feedback_scale.pack()
feedback_button = tk.Button(root, text="Submit Feedback", command=feedback_response)
feedback_button.pack()
root.mainloop()