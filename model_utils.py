from backend.engine.decision_graph import triage
from backend.engine.bayesian_model import predict, disease_map
from backend.engine.followup_agent import generate_followup
from backend.agents.doctor_agent import get_doctor


def diagnose(symptoms):

    triage_level = triage(symptoms)

    diseases = predict(symptoms)

    followups = generate_followup(symptoms,diseases,disease_map)

    results=[]

    for d in diseases:

        doctor=get_doctor(d["system"])

        results.append({
            "disease":d["disease"],
            "confidence":d["confidence"],
            "doctor":doctor,
            "risk":d["risk"]
        })

    return{
        "triage":triage_level,
        "results":results,
        "followup_questions":followups
    }