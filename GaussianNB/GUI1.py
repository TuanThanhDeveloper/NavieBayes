import joblib
import tkinter as tk
from tkinter import ttk
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from tkinter.messagebox import showinfo

df = pd.read_csv('income1.csv')

loaded_model = joblib.load('Completed_model1.joblib')
model = loaded_model

enc = OneHotEncoder(handle_unknown='ignore')


def pdf1():
    root.quit()


def pdf():
    if (workclass.get() == " Self-emp"):
        a = 2
    elif (workclass.get() == " Not-worked"):
        a = 0
    elif (workclass.get() == " Private"):
        a = 1
    elif (workclass.get() == " State-gov"):
        a = 3


    if (education.get() == " Bachelors"):
        b = 0
    elif (education.get() == " College"):
        b = 1
    elif (education.get() == " Doctorate"):
        b = 2
    elif (education.get() == " High_school"):
        b = 3
    elif (education.get() == " Masters"):
        b = 4
    elif (education.get() == " Primary_school"):
        b = 5
    elif (education.get() == " Second_school"):
        b = 6
    elif (education.get() == " University"):
        b = 7

    if (marital.get() == " Married"):
        c = 0
    elif (marital.get() == " Single"):
        c = 2
    elif (marital.get() == " Others"):
        c = 1

    if (occupation.get() == " Doctor"):
        d = 0
    elif (occupation.get() == " Managerial"):
        d = 1
    elif (occupation.get() == " Others"):
        d = 2
    elif (occupation.get() == " Protective-serv"):
        d = 4
    elif (occupation.get() == " Sales"):
        d = 5
    elif (occupation.get() == " Shipper"):
        d = 7
    elif (occupation.get() == " Tech-support"):
        d = 7
    elif (occupation.get() == " Pilot"):
        d = 3

    if (race.get() == " Black"):
        e = 0
    elif (race.get() == " Other"):
        e = 1
    elif (race.get() == " White"):
        e = 2
    elif (race.get() == " Yellow"):
        e = 3

    if (sex.get() == " Female"):
        f = 0
    elif (sex.get() == " Male"):
        f = 1

    if (nativecountry.get() == " Canada"):
        g = 0
    elif (nativecountry.get() == " China"):
        g = 1
    elif (nativecountry.get() == " England"):
        g = 2
    elif (nativecountry.get() == " Germany"):
        g = 3
    elif (nativecountry.get() == " India"):
        g = 4
    elif (nativecountry.get() == " Japan"):
        g = 5
    elif (nativecountry.get() == " Philippines"):
        g = 6
    elif (nativecountry.get() == " United-States"):
        g = 7
    elif (nativecountry.get() == " Vietnam"):
        g = 8

    x_pred = [[age.get(), a, b, c, d, e,
               f, hour.get(), g]]
    print(x_pred)


    tp = model.predict(x_pred)
    print(tp)

    if (tp == 1):
        msg = f' Income > 50k $ '
    else:
        msg = f' Income <= 50k $ '

    showinfo(title='Result', message=msg)


root = tk.Tk()
root.title('GaussionNB')

root.geometry('650x650')

# age
age = tk.StringVar()  # --variable

age_label = ttk.Label(root, text="age:")
age_label.pack(fill='x', padx=10, pady=0, expand=True)

age_entry = ttk.Entry(root, textvariable=age)
age_entry.pack(fill='x', padx=10, pady=0, expand=True)
age_entry.focus()

# workclass
workclass = tk.StringVar()  # --variable

workclass_label = ttk.Label(root, text="workclass:")
workclass_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_workclass = list(set(df['workclass']))

workclass_cb = ttk.Combobox(root, textvariable=workclass)
workclass_cb['values'] = datalist_workclass
workclass_cb['state'] = 'readonly'
workclass_cb.pack(fill='x', padx=10, pady=5)

# education
education = tk.StringVar()  # --variable

education_label = ttk.Label(root, text="education:")
education_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_education = list(set(df['education']))

education_cb = ttk.Combobox(root, textvariable=education)
education_cb['values'] = datalist_education
education_cb['state'] = 'readonly'
education_cb.pack(fill='x', padx=10, pady=5)

# marital
marital = tk.StringVar()  # --variable

marital_label = ttk.Label(root, text="marital:")
marital_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_marital = list(set(df['marital_status']))

marital_cb = ttk.Combobox(root, textvariable=marital)
marital_cb['values'] = datalist_marital
marital_cb['state'] = 'readonly'
marital_cb.pack(fill='x', padx=10, pady=5)

# occupation
occupation = tk.StringVar()  # --variable

occupation_label = ttk.Label(root, text="occupation:")
occupation_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_occupation = list(set(df['occupation']))

occupation_cb = ttk.Combobox(root, textvariable=occupation)
occupation_cb['values'] = datalist_occupation
occupation_cb['state'] = 'readonly'
occupation_cb.pack(fill='x', padx=10, pady=5)

# race
race = tk.StringVar()  # --variable

race_label = ttk.Label(root, text="race:")
race_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_race = list(set(df['race']))

race_cb = ttk.Combobox(root, textvariable=race)
race_cb['values'] = datalist_race
race_cb['state'] = 'readonly'
race_cb.pack(fill='x', padx=10, pady=5)

# sex
sex = tk.StringVar()
sex_label = ttk.Label(text="sex:")
sex_label.pack(fill='x', padx=5, pady=0, expand=True)

datalist_sex = list(set(df['sex']))

sex_cb = ttk.Combobox(root, textvariable=sex)
sex_cb['values'] = datalist_sex
sex_cb['state'] = 'readonly'
sex_cb.pack(fill='x', padx=10, pady=5)

# age
hour = tk.StringVar()  # --variable

hour_label = ttk.Label(root, text="hours_per_week:")
hour_label.pack(fill='x', padx=10, pady=0, expand=True)

hour_entry = ttk.Entry(root, textvariable=hour)
hour_entry.pack(fill='x', padx=10, pady=0, expand=True)
hour_entry.focus()

# native_country
nativecountry = tk.StringVar()  # --variable

nativecountry_label = ttk.Label(root, text="native_country:")
nativecountry_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_nativecountry = list(set(df['native_country']))

nativecountry_cb = ttk.Combobox(root, textvariable=nativecountry)
nativecountry_cb['values'] = datalist_nativecountry
nativecountry_cb['state'] = 'readonly'
nativecountry_cb.pack(fill='x', padx=10, pady=5)

# pred button
pred_button = ttk.Button(root, text="Predict", command=pdf)
pred_button.pack(fill='x', expand=True, padx=10, pady=10)

root.mainloop()
