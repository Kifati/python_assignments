import tkinter as tk
import webbrowser

def open_faq():
    course = course_var.get()
    sources = sources_var.get()

    if not course or not sources:
        status_label.config(text="Please select both course and source.", fg="red")
        return

    if sources == "Instagram Ads":
        url = "https://help.instagram.com/561062241952036"
    elif sources == "YouTube Ads":
        url = "https://support.google.com/youtube/thread/677314/🔍-youtube-faqs-need-help-start-here?hl=en"
    elif sources == "Google Ads":
        url = "https://policies.google.com/faq?hl=en-US"
    else:
        status_label.config(text="Invalid source selection.", fg="red")
        return

    webbrowser.open_new_tab(url)
    status_label.config(text=f"Navigating to the FAQ page for {sources}...", fg="green")

def main():
    global course_var, sources_var, status_label

    root = tk.Tk()
    root.title("Games Survey Form")
    root.geometry("400x250")

    course_label = tk.Label(root, text="Select Game:", bg="lightblue")
    course_label.pack(pady=10)

    course_var = tk.StringVar()
    course_var.set("Valorant")  # Default course selection
    courses = ["Valorant", "CS:GO", "Apex Legends", "Overwatch", "Warzone", "Rainbow Six: Siege"]

    course_menu = tk.OptionMenu(root, course_var, *courses,)
    course_menu.pack(pady=5)

    sources_label = tk.Label(root, text="Where did you come to know about the game?",bg="lightblue")
    sources_label.pack(pady=10)

    sources_var = tk.StringVar()
    sources_var.set("Instagram Ads")  # Default source selection
    sources = ["Instagram Ads", "YouTube Ads", "Google Ads"]

    sources_menu = tk.OptionMenu(root, sources_var, *sources)
    sources_menu.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", command=open_faq, bg="lightblue", activebackground="blue")
    submit_button.pack(pady=20)

    status_label = tk.Label(root, text="", fg="green")
    status_label.pack(pady=5)
    root.configure(bg="cyan")
    root.mainloop()
main()
