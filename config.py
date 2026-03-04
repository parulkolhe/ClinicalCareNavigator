def calculate_risk(disease):

    emergency={
    "heart_attack",
    "stroke",
    "cardiac_arrest",
    "pulmonary_embolism"
    }

    high={
    "pneumonia",
    "appendicitis",
    "sepsis"
    }

    if disease in emergency:
        return "emergency"

    if disease in high:
        return "high"

    return "moderate"