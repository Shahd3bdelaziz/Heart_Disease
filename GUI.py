import customtkinter as ctk
import tkinter.messagebox as mbox
import requests
import json

def send_request():
    data = {
        "Age": int(age_in.get()),#0
        "Sex": sex_values[sex_in.get()],#1
        "Chest pain type": chest_values[chest_in.get()],#2
        "BP": int(bp_in.get()),#3
        "Cholesterol": int(cholesterol_in.get()),#4
        "FBS over 120": fbs_values[fbs_in.get()],#5
        "EKG results": ekg_values[ekg_in.get()],#6
        "Exercise angina": angina_values[angina_in.get()],#7
        "ST depression": float(st_in.get()),#8
        "Slope of ST": sst_values[sst_in.get()],#9
        "Number of vessels fluro": vessle_values[vessle_in.get()],#10
        "Thallium": thallium_values[thallium_in.get()]#11
    }

    response = requests.post("https://AIUnionTeam.pythonanywhere.com", json=[data])
    #decision_tree_response=response.json()[0]["Decision treee"]
    #eural_network_response=response.json()[0]["Neural Network"]
    mbox.showinfo("Prediction",response.json())

root = ctk.CTk()

root.title("Heart Disease")
root.geometry("820x420")
root.resizable(width=False,height=False)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")



sex_values = {"Male":1, "Female":0}
chest_values = {"Typical angina":1, "Atypical angina":2, "Non-anginal pain":3, "Asymptomatic":4}
fbs_values = {"Over 120":1, "Under 120":0}
ekg_values = {"Normal":0, "ST-T wave abnormality":1, "Left ventricular hypertrophy":2}
angina_values = {"Yes":1, "No":0}
sst_values = {"Up sloping":1, "Flat":2, "Down sloping":3}
vessle_values = {"0":0, "1":1, "2":2, "3":3}
thallium_values = {"Normal":3, "Fixed":6, "Reversable":7}



#Entry widgets
ctk.CTkLabel(root, text="Age",font=("Arial Rounded MT",15,"bold")).grid(row=0, column=0, padx=10, pady=10)
age_in = ctk.CTkEntry(root)
age_in.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(root, text="Blood pressure",font=("Arial Rounded MT",14,"bold")).grid(row=1, column=0, padx=10, pady=10)
bp_in = ctk.CTkEntry(root)
bp_in.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkLabel(root, text="Cholesterol",font=("Arial Rounded MT",14,"bold")).grid(row=2, column=0, padx=10, pady=10)
cholesterol_in = ctk.CTkEntry(root)
cholesterol_in.grid(row=2, column=1, padx=10, pady=10)

ctk.CTkLabel(root, text="ST Depression",font=("Arial Rounded MT",14,"bold")).grid(row=3, column=0, padx=10, pady=10)
st_in = ctk.CTkEntry(root)
st_in.grid(row=3, column=1, padx=10, pady=10)

#OptionMenu widgets
ctk.CTkLabel(root, text="Sex",font=("Arial Rounded MT",15,"bold")).grid(row=0, column=3, padx=10, pady=10)
sex_in = ctk.CTkOptionMenu(root, values=list(sex_values.keys()),width=200)
sex_in.grid(row=0, column=4, padx=10, pady=10)

ctk.CTkLabel(root, text="Chest Pain Type",font=("Arial Rounded MT",14,"bold")).grid(row=1, column=3, padx=10, pady=10)
chest_in = ctk.CTkOptionMenu(root, values=list(chest_values.keys()),width=200)
chest_in.grid(row=1, column=4, padx=10, pady=10)

ctk.CTkLabel(root, text="FBS",font=("Arial Rounded MT",15,"bold")).grid(row=2, column=3, padx=10, pady=10)
fbs_in = ctk.CTkOptionMenu(root, values=list(fbs_values.keys()),width=200)
fbs_in.grid(row=2, column=4, padx=10, pady=10)

ctk.CTkLabel(root, text="EKG Results",font=("Arial Rounded MT",14,"bold")).grid(row=3, column=3, padx=10, pady=10)
ekg_in = ctk.CTkOptionMenu(root, values=list(ekg_values.keys()),width=200)
ekg_in.grid(row=3, column=4, padx=10, pady=10)

ctk.CTkLabel(root, text="Exercise Angina",font=("Arial Rounded MT",14,"bold")).grid(row=4, column=3, padx=10, pady=10)
angina_in = ctk.CTkOptionMenu(root, values=list(angina_values.keys()),width=200)
angina_in.grid(row=4, column=4, padx=10, pady=10)

ctk.CTkLabel(root, text="Slope of ST",font=("Arial Rounded MT",14,"bold")).grid(row=5, column=3, padx=10, pady=10)
sst_in = ctk.CTkOptionMenu(root, values=list(sst_values.keys()),width=200)
sst_in.grid(row=5, column=4, padx=10, pady=10)

ctk.CTkLabel(root, text="Number of Vessels",font=("Arial Rounded MT",14,"bold")).grid(row=4, column=0, padx=10, pady=10)
vessle_in = ctk.CTkOptionMenu(root, values=list(vessle_values.keys()))
vessle_in.grid(row=4, column=1, padx=10, pady=10)

ctk.CTkLabel(root, text="Thallium",font=("Arial Rounded MT",14,"bold")).grid(row=5, column=0, padx=10, pady=10)
thallium_in = ctk.CTkOptionMenu(root, values=list(thallium_values.keys()))
thallium_in.grid(row=5, column=1, padx=10, pady=10)

# Place the button in the middle
prediction_button = ctk.CTkButton(root, text="Prediction",font=("Arial Rounded MT",14,"bold"), height=35,command=send_request)
prediction_button.grid(row=6, column=2,pady=70)

root.mainloop()
