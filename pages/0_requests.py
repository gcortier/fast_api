import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/"


st.title("Ajouter une citation")


# Récupérer les citation
def get_citations():
    response = requests.get(f"{API_URL}/citations")
    return response.json()

citations = get_citations()
st.header(f"Affichages citations ( total :{len(citations)} )")


def modify_citation(citation_id, citation):
  response = requests.put(f"{API_URL}/citation/", json={"citation_id": citation_id, "citation": citation})
  return response.json()


if not citations:
    st.write("Aucune citation disponible.")
else:
    # affichage des citations
    for citation_id, citation in citations.items():
        st.write(f"{citation_id}: {citation}")
        
        
        

    st.subheader("Affichage d'une citation spécifique")
    # Création du sélecteur avec les IDs disponibles
    selected_id = st.selectbox(
        "Sélectionner une citation par ID",
        options=list(citations.keys())
    )
    # Affichage de la citation sélectionnée
    st.write(f"**Citation sélectionnée :{selected_id}** {citations[selected_id]}")


    with st.form("Edition de la citation"):
        citation = st.text_area(f"Modifier la citation", citations[selected_id])
        modify = st.form_submit_button("Modifier la citation")
        if modify:
            
            response = requests.put(f"{API_URL}/citation/{selected_id}", json={"citation_id": selected_id, "citation": citation})
            if response.status_code == 200:
                st.success(f"Citation {selected_id} modifiée avec succès.")
            else:
                st.error(f"Erreur lors de la modification de la citation {selected_id}.")

            
        delete = st.form_submit_button("Supprimer la citation")
        if delete:
            response = requests.delete(f"{API_URL}/citation/{selected_id}")
            if response.status_code == 200:
                st.success(f"Citation {selected_id} supprimée avec succès.")
            else:
                st.error(f"Erreur lors de la suppression de la citation {selected_id}.")


# Fonction pour ajouter une citation
def add_citation(citation):
  response = requests.post(f"{API_URL}/citation/", json={"citation": citation})
  return response.json()


st.header("Ajouter une Citation")
with st.form("add_citation_form"):
  citation = st.text_area("Entrez la nouvelle citation")
  submitted = st.form_submit_button("Ajouter")
  if submitted:
    # Ajout de la citation
    result = add_citation(citation)
    st.write(result)
    