from modules import file_handling

FAQS_FILE = "data/faqs.txt"

def add_faq():
    print("==== Add FAQ ====")
    faq_question = input("Enter the FAQ question: ")

    faqs_data = file_handling.read_data(FAQS_FILE)

    if faqs_data:
        faqs = faqs_data.split("\n")
        for faq in faqs:
            if faq_question.lower() == faq.lower():
                print("FAQ already exists.")
                return

    new_faq_data = f"{faq_question}\n"
    file_handling.append_data(FAQS_FILE, new_faq_data)
    print("FAQ added successfully.")

def view_faqs():
    print("==== View FAQs ====")
    faqs_data = file_handling.read_data(FAQS_FILE)

    if faqs_data:
        faqs = faqs_data.split("\n")
        print("Frequently Asked Questions:")
        for faq in faqs:
            print(faq)
    else:
        print("No FAQs found.")
