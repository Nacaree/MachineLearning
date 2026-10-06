import pandas as pd
import spacy


# Load the English NER model
nlp = spacy.load("en_core_web_sm")


# Load the dataset created in Chapter 6
data = pd.read_csv("technology_events_2026.csv")


# Store extracted entities
entities = []


# Process every event in the dataset
for _, row in data.iterrows():

    event_id = row["ID"]
    month = row["Month"]
    event_text = row["Event Text"]

    # Pass the text through the NLP model
    doc = nlp(event_text)

    # Extract named entities
    for entity in doc.ents:

        entities.append({
            "Event ID": event_id,
            "Month": month,
            "Entity": entity.text,
            "Entity Type": entity.label_
        })


# Convert extracted entities into a DataFrame
entity_data = pd.DataFrame(entities)


# Save the results
entity_data.to_csv(
    "ner_entities_2026.csv",
    index=False
)


print("NER analysis complete.")
print(f"Total entities found: {len(entity_data)}")
print("Results saved as: ner_entities_2026.csv")