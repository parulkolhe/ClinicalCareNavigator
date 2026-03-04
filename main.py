def generate_followup(symptoms,predicted_diseases,disease_map):

    asked=set(symptoms)

    question_scores={}

    for d in predicted_diseases:

        disease=d["disease"]

        disease_symptoms=disease_map[disease]["symptoms"]

        for s in disease_symptoms:

            if s not in asked:

                question_scores[s]=question_scores.get(s,0)+1

    ranked=sorted(question_scores.items(),key=lambda x:x[1],reverse=True)

    questions=[]

    for symptom,_ in ranked[:3]:

        questions.append(f"Are you experiencing {symptom.replace('_',' ')}?")

    return questions