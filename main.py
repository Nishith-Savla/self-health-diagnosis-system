import tkinter as tk
from tkinter import ttk, messagebox
from greetings import Greetings
from experta import Fact

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

#loads the knowledge from .txt files into variables to allow the code to use it
def preprocess():
    #global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()

    for disease in diseases_list:
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()

        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()

        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)

    return symptom_map[str(symptom_list)]


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" % (id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details + "\n")
    print(
        "The common medications and procedures suggested by other real doctors are: \n"
    )
    print(treatments + "\n")

class DiagnosisGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Diagnosis Expert System")
        self.master.geometry("800x600")
        self.master.configure(bg="#f0f0f0")

        self.symptoms = [
            "headache", "back_pain", "chest_pain", "cough", "fainting",
            "sore_throat", "fatigue", "restlessness", "low_body_temp",
            "fever", "sunken_eyes", "nausea", "blurred_vision"
        ]
        self.symptom_vars = {}

        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        title_label = ttk.Label(self.master, text="Medical Diagnosis Expert System", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=20)

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=10)

        categories = {
            "General": ["fatigue", "fever", "nausea"],
            "Head": ["headache", "blurred_vision"],
            "Chest": ["chest_pain", "cough", "sore_throat"],
            "Body": ["back_pain", "restlessness", "low_body_temp"],
            "Other": ["fainting", "sunken_eyes"]
        }

        for category, symptoms in categories.items():
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=category)
            for i, symptom in enumerate(symptoms):
                self.create_symptom_widget(frame, symptom, i)

        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=20)

        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        diagnose_button = ttk.Button(button_frame, text="Diagnose", command=self.diagnose, style="TButton")
        diagnose_button.pack()

        dark_mode_button = ttk.Button(button_frame, text="Toggle Dark Mode", command=self.toggle_dark_mode, style="TButton")
        dark_mode_button.pack(pady=10)

    def create_symptom_widget(self, parent, symptom, row):
        var = tk.StringVar(value="no")
        self.symptom_vars[symptom] = var
        
        symptom_label = ttk.Label(parent, text=symptom.replace("_", " ").title() + ":", font=("Helvetica", 10))
        symptom_label.grid(row=row, column=0, sticky="w", padx=(0, 10), pady=5)
        
        for j, value in enumerate(["No", "Low", "High"]):
            ttk.Radiobutton(parent, text=value, variable=var, value=value.lower()).grid(row=row, column=j+1, padx=5, pady=5)

    def diagnose(self):
        self.show_progress()
        symptoms = {symptom: var.get() for symptom, var in self.symptom_vars.items()}
        engine = Greetings(symptom_map, if_not_matched, get_treatments, get_details, symptoms)
        engine.reset()
        engine.run()
        
        self.master.after(3000, lambda: self.show_results(engine.facts))

    def show_results(self, facts):
        result_window = tk.Toplevel(self.master)
        result_window.title("Diagnosis Results")
        result_window.geometry("600x400")
        result_window.configure(bg="#f0f0f0")

        result_frame = ttk.Frame(result_window)
        result_frame.pack(fill="both", expand=True, padx=20, pady=20)

        result_text = tk.Text(result_frame, wrap=tk.WORD, font=("Helvetica", 12), padx=10, pady=10)
        result_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
        scrollbar.pack(side="right", fill="y")
        result_text.configure(yscrollcommand=scrollbar.set)

        disease = None
        for fact in facts:
            if isinstance(fact, Fact) and fact.template.name == 'disease':
                disease = fact['__value__']
                break

        if disease:
            result_text.insert(tk.END, f"Diagnosed Disease: {disease}\n\n", "title")
            result_text.insert(tk.END, f"Description:\n{get_details(disease)}\n\n", "description")
            result_text.insert(tk.END, f"Recommended Treatments:\n{get_treatments(disease)}", "treatment")
        else:
            # If no specific disease is found, display the most probable disease
            symptoms = {symptom: var.get() for symptom, var in self.symptom_vars.items()}
            max_count = 0
            max_disease = ""
            for key, val in symptom_map.items():
                count = sum(1 for i, j in zip(eval(key), symptoms.values()) if i == j and j != "no")
                if count > max_count:
                    max_count = count
                    max_disease = val
            
            if max_disease:
                result_text.insert(tk.END, f"Most Probable Disease: {max_disease}\n\n", "title")
                result_text.insert(tk.END, f"Description:\n{get_details(max_disease)}\n\n", "description")
                result_text.insert(tk.END, f"Recommended Treatments:\n{get_treatments(max_disease)}", "treatment")
            else:
                result_text.insert(tk.END, "No specific disease was diagnosed based on the provided symptoms.", "title")

        result_text.tag_configure("title", font=("Helvetica", 14, "bold"))
        result_text.tag_configure("description", font=("Helvetica", 12))
        result_text.tag_configure("treatment", font=("Helvetica", 12, "italic"))
        result_text.config(state=tk.DISABLED)

    def show_progress(self):
        progress_window = tk.Toplevel(self.master)
        progress_window.title("Diagnosing...")
        progress_window.geometry("300x100")

        progress_label = ttk.Label(progress_window, text="Analyzing symptoms...", font=("Helvetica", 12))
        progress_label.pack(pady=10)

        progress_bar = ttk.Progressbar(progress_window, length=200, mode="indeterminate")
        progress_bar.pack(pady=10)
        progress_bar.start()

        self.master.after(3000, progress_window.destroy)  # Close after 3 seconds

    def toggle_dark_mode(self):
        if self.style.theme_use() == "clam":
            self.style.theme_use("alt")
            self.master.configure(bg="#2c2c2c")
            self.style.configure("TLabel", background="#2c2c2c", foreground="white")
            self.style.configure("TButton", background="#444444", foreground="white")
            self.style.configure("TNotebook", background="#2c2c2c")
            self.style.configure("TNotebook.Tab", background="#444444", foreground="white")
        else:
            self.style.theme_use("clam")
            self.master.configure(bg="#f0f0f0")
            self.style.configure("TLabel", background="#f0f0f0", foreground="black")
            self.style.configure("TButton", background="#e0e0e0", foreground="black")
            self.style.configure("TNotebook", background="#f0f0f0")
            self.style.configure("TNotebook.Tab", background="#e0e0e0", foreground="black")

#driver function
if __name__ == "__main__":
    preprocess()
    root = tk.Tk()
    app = DiagnosisGUI(root)
    root.mainloop()