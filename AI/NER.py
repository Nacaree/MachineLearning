

import spacy

# Step 1: Load the small English NLP model
nlp = spacy.load("en_core_web_sm")

# Step 2: Define the text you want to analyze

text ='Why Apple is looking at buying U.K. startup for $1 billion ?'

doc = nlp(text)

print(f"{'Entity':<20} | {'Label':<10} | {'Description'}")
#print("-" * 60)

# Iterate over the detected entities
for ent in doc.ents:
    print(f"{ent.text:<20} | {ent.label_:<10} | {spacy.explain(ent.label_)}")



# Step 3: Process the text through the NLP pipeline
doc = nlp(text)


# Step 4: Loop through the detected entities and print them
for entity in doc.ents:
    # entity.text is the actual word, entity.label_ is the category
    print(f"Entity: {entity.text} | Type: {entity.label_} ({spacy.explain(entity.label_)})")

    
