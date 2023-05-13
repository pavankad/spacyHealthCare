import en_ner_bc5cdr_md

class medical_entity_extract():

    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        return en_ner_bc5cdr_md.load()

    def extract_diag_entities(self, text):
        extracted_doc = self.model(text)
        entities = []
        # Extract Diag entities
        for ent in extracted_doc.ents:
            if (ent.label_ == "DISEASE"):
                entities.append({'text': ent.text})
        return entities


    # Helper function to verify model output
    def display_model_output(self, model, text):
        print("TEXT", "START", "END", "ENTITY TYPE")
        entities = []
        for ent in doc.ents:
            if (ent.label_ == "DISEASE"):
                entities.append({'text': ent.text})
                print(ent.text, ent.start_char, ent.end_char, ent.label_)






