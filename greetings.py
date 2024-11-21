from experta import *


class Greetings(KnowledgeEngine):
    def __init__(
        self, symptom_map, if_not_matched, get_treatments, get_details, symptoms
    ):
        self.symptom_map = symptom_map
        self.if_not_matched = if_not_matched
        self.get_details = get_details
        self.get_treatments = get_treatments
        self.symptoms = symptoms
        KnowledgeEngine.__init__(self)

    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_disease")
        for symptom, value in self.symptoms.items():
            yield Fact(**{symptom: value})

    # different rules checking for each disease match
    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="low"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="high"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_1(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="high"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="low"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_2(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="low"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="low"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_4(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="low"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="high"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="low"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_5(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="low"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_6(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def disease_7(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="low"),
        Fact(blurred_vision="low"),
    )
    def disease_8(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="low"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="low"),
    )
    def disease_9(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="low"),
        Fact(blurred_vision="no"),
    )
    def disease_10(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="high"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def disease_11(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="yes"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="high"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_12(self):
        self.declare(Fact(disease="Hypothermia"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="high"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="high"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_13(self):
        self.declare(Fact(disease="Coronavirus"))

    # when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="find_disease"), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        id_disease = disease
        disease_details = self.get_details(id_disease)
        treatments = self.get_treatments(id_disease)
        result = {
            "disease": id_disease,
            "details": disease_details,
            "treatments": treatments,
            "matched": True,
        }
        self.result = result  # Store the result in the class

    @Rule(
        Fact(action="find_disease"),
        Fact(headache=MATCH.headache),
        Fact(back_pain=MATCH.back_pain),
        Fact(chest_pain=MATCH.chest_pain),
        Fact(cough=MATCH.cough),
        Fact(fainting=MATCH.fainting),
        Fact(sore_throat=MATCH.sore_throat),
        Fact(fatigue=MATCH.fatigue),
        Fact(low_body_temp=MATCH.low_body_temp),
        Fact(restlessness=MATCH.restlessness),
        Fact(fever=MATCH.fever),
        Fact(sunken_eyes=MATCH.sunken_eyes),
        Fact(nausea=MATCH.nausea),
        Fact(blurred_vision=MATCH.blurred_vision),
        NOT(Fact(disease=MATCH.disease)),
        salience=-999,
    )
    def not_matched(
        self,
        headache,
        back_pain,
        chest_pain,
        cough,
        fainting,
        sore_throat,
        fatigue,
        low_body_temp,
        restlessness,
        fever,
        sunken_eyes,
        nausea,
        blurred_vision,
    ):
        lis = [
            headache,
            back_pain,
            chest_pain,
            cough,
            fainting,
            sore_throat,
            fatigue,
            low_body_temp,
            restlessness,
            fever,
            sunken_eyes,
            nausea,
            blurred_vision,
        ]
        max_count = 0
        max_disease = ""
        for key, val in self.symptom_map.items():
            count = sum(1 for i, j in zip(eval(key), lis) if i == j and j != "no")
            if count > max_count:
                max_count = count
                max_disease = val
        if max_disease:
            disease_details = self.get_details(max_disease)
            treatments = self.get_treatments(max_disease)
            result = {
                "disease": max_disease,
                "details": disease_details,
                "treatments": treatments,
                "matched": False,
            }
            self.result = result  # Store the result in the class
