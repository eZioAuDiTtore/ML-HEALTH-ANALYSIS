import pandas as pd
import os
from django.contrib.auth.models import User
from pathlib import Path
import csv
import pickle
from .models import symptoms as Symptoms
import numpy as np
BASE_DIR = Path(__file__).resolve().parent.parent
test_data = pd.read_csv(str(BASE_DIR)+'/ml/Testing.csv', sep=',')
test_data = test_data.drop('prognosis', axis=1)
symptoms = list(test_data.columns)
fields = []
description = {}
precautionDictionary = {}
model = pickle.load(open(str(BASE_DIR)+'/ml/model.pkl', 'rb'))

with open(str(BASE_DIR)+'/ml/disease_description.csv', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        disease, desc = row
        description[disease] = desc

with open(str(BASE_DIR)+'/ml/symptom_precaution.csv', encoding="utf8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        _prec = {row[0]: [row[1], row[2], row[3], row[4]]}
        precautionDictionary.update(_prec)
#print(precautionDictionary)
def get_intent(text):
    intents = {"greeting": ["hi", "hello", "hey", "symptoms"], "ask_symptoms": symptoms, "ask_symptoms-no": ["no","No"], "end-chat": ["bye", "thanks", "thankyou", "fine", "okay","ok","thank you"]}
    words = text.lower().split(" ")
    #print(words)
    real_intent = ''
    for word in words:
        for intent in intents:
            #print(intent)
            if word in intents[intent]:
                real_intent = intent
                return real_intent
            elif intent == "ask_symptoms":
                for each_symp in intents[intent]:
                    splitted_symptoms=each_symp.split()
                    if word in splitted_symptoms:
                        real_intent = intent
                        return real_intent


def predict_disease(affected_symps):
    disease = model.predict([np.array(affected_symps)])
    disease = disease[0]
    return disease
#updated symptoms to db
'''
def update_symptoms(request):
    for symptom in symptoms:
        Symptoms(symptom_name=symptom,symptom_desc="").save()

'''
