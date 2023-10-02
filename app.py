import streamlit as st
import spacy
from spacy import displacy
import json

# Initialize spaCy
nlp = spacy.load("en_core_web_md")

# Define sample data
data = {
    "fruit": ["apple", "pear", "orange"],
    "vegetable": ["broccoli", "spinach", "tomato"],
    "meat": ['beef', 'pork', 'turkey', 'duck']
}

# Streamlit app
st.title('Named Entity Recognition with spaCy')

user_input = st.text_area("Enter text:", "")

if st.button("Process"):
    if user_input:
        # Process the text
        doc = nlp(user_input)
        
        # Visualization options
        options = {
            "colors": {"fruit": "darkorange", "vegetable": "limegreen", "meat": "salmon"},
            "ents": ["fruit", "vegetable", "meat"],
        }

        # JSON serialization with only entity and type
        result_dict = {'entities': []}
        
        for ent in doc.ents:
            ent_data = {
                'entity': ent.text,
                'type': ent.label_
            }
            result_dict['entities'].append(ent_data)
        
        result_json = json.dumps(result_dict, indent=4)

        # Display results
        st.subheader("Named Entities")
        html = displacy.render(doc, style="ent", page=True, minify=True)
        st.write(html, unsafe_allow_html=True)
        st.subheader("Entities in JSON format")
        st.json(result_json)
      
