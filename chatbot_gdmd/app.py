import streamlit as st
from utils import search_all_metadata
from vis import load_emdat_data, plot_disasters_by_year, plot_map

st.set_page_config(page_title="Disaster Data Chatbot", layout="wide")
st.title("🤖 Disaster Data Chatbot + Visualisations")

query = st.text_input("💬 Posez une question ou un mot-clé (ex: inondation, séisme, Afrique...)", "")

if query:
    results = search_all_metadata(query)
    if results:
        st.success(f"{len(results)} jeu(x) de données trouvé(s) :")
        for result in results:
            st.markdown("---")
            st.markdown(f"**📘 Nom :** {result['name']}")
            st.markdown(f"**📝 Description :** {result['description']}")
            st.markdown(f"**🔗 Lien :** [Accéder aux données]({result['url']})")

            if "emdat" in result["name"].lower():
                st.markdown("### 📊 Visualisation des données EM-DAT")
                df = load_emdat_data()
                st.altair_chart(plot_disasters_by_year(df), use_container_width=True)
                st.markdown("### 🗺️ Carte des événements")
                st.pydeck_chart(plot_map(df))
    else:
        st.warning("Aucun jeu de données trouvé pour cette question.")