class Patient(object):
    gender = str()
    age = float()
    symptom_onset = str()
    hosp_visit_date = str()
    id_status = int()

    def __init__(self, gender, age, symptom_onset, hosp_visit_date, id_status):
        self.gender = gender
        self.age = age
        self.symptom_onset = symptom_onset
        self.hosp_visit_date = hosp_visit_date
        self.id_status = id_status

    def __str__(self):
        return "gender: {0}\nage: {1}\nsymptom_onset: {2}\n\
hosp_visit_date: {3}\nid_status: {4}".format(self.gender, self.age, self.symptom_onset, self.hosp_visit_date,
                                             self.id_status)
