from pathlib import Path
import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import time

# --- CONFIGURATION ---
st.set_page_config(
    page_title="CV Digital | Ndiaye NIANG",
    page_icon="✨",
    layout="wide"
)

# --- CHEMINS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "portrait.png"

# --- DONNEES ---
NAME = "Ndiaye NIANG"
DESCRIPTION = "Data Scientist | Expert en Analyse Prédictive"
EMAIL = "ndiayeniang8@gmail.com"
TEL = "07 67 67 76 67"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ndiaye-niang-b51336172",
    "GitHub": "https://github.com/ndiaye429/"
}

# --- FONCTIONS UTILITAIRES ---
def load_css():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

def typewriter_effect(text, speed=0.05, container=None):
    """Affiche un texte avec effet machine à écrire"""
    target = container or st.empty()
    full_text = ""
    for char in str(text):
        full_text += char
        target.markdown(full_text, unsafe_allow_html=True)
        time.sleep(speed)
    return full_text

# --- SECTIONS ---
def profile_section():
    col1, col2 = st.columns([1, 2], gap="medium")
    
    with col1:
        img_base64 = image_to_base64(profile_pic)
        st.markdown(
            f'<div class="profile-container"><img src="data:image/png;base64,{img_base64}" class="profile-img animate-float"></div>',
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(f'<h1 class="gradient-text">{NAME}</h1>', unsafe_allow_html=True)
        typewriter_effect(f'<p class="hero-subtitle">{DESCRIPTION}</p>', 0.03)

        col_a, col_b = st.columns(2)
        with col_a:
            with open(resume_file, "rb") as pdf_file:
                st.download_button(
                    "📄 Télécharger CV",
                    pdf_file,
                    "CV_Ndiaye_NIANG.pdf",
                    "application/pdf",
                    key="download_cv"
                )
        with col_b:
            if st.button("📫 Contact", key="contact_btn"):
                st.markdown(f'<div class="contact-info animate-pulse">{EMAIL}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="contact-info animate-pulse">{TEL}</div>', unsafe_allow_html=True)

        
        st.markdown('<div class="social-container">', unsafe_allow_html=True)
        cols = st.columns(len(SOCIAL_MEDIA))
        for i, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[i].markdown(
                f'<a href="{link}" target="_blank" class="hover-move-effect"><button class="moving-text-btn">{platform}</button></a>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

def section_with_typewriter(title, content, icon=""):
    """Crée une section avec titre animé et contenu statique"""
    full_title = f'<h2><span class="icon">{icon}</span> {title}</h2>'
    card_template = f'<div class="section-card">{{content}}</div>'
    
    # Conteneur principal
    container = st.empty()
    
    # Animation du titre seul d'abord
    animated_title = typewriter_effect(full_title, 0.05, container)
    
    # Affichage final avec le contenu
    container.markdown(
        card_template.format(content=f"{animated_title}{content}"), 
        unsafe_allow_html=True
    )


def professional_experience():
    content = """
    <div class="experience-item">
        <h3>EPSILON, Paris, Consultant Data scientist: Mission en interne</h3>
        <p class="period">Février 2025 - Avril 2025</p>
        <ul class="fixed-list">
            <li class="highlight-item">Conception d'un dashboard interactif pour suivre et analyser l'empreinte carbone des projets internes d'Epsilon, en mettant en avant les émissions de CO2 en fonction de la localisation et du marché.</li>
            <li class="highlight-item"> Les données couvrent les émissions liées aux services GCP utilisés, réparties par mois, région, service, et catégorie d'usage.</li>
        </ul>
    </div>
    <div class="experience-item">
        <h3>EPSILON, Paris, Consultant Data scientist: Mission chez ENGIE</h3>
        <p class="period">Avril 2023 - Aujourd'hui</p>
        <ul class="fixed-list">
            <li class="highlight-item">Identification stratégique des clients et prospects pour des campagnes de prospection par courrier, réglementaires, commerciales et d'enquêtes de satisfaction.</li>
            <li class="highlight-item">Alimentation optimisée des bases de données pour maximiser l'efficacité des campagnes et la clarté des visualisations.</li>
            <li class="highlight-item">Analyse détaillée des campagnes de prospection et de commercialisation (taux de distribution et taux de conversion).</li>
            <li class="highlight-item">Assurer une confiance absolue des équipes métiers dans la qualité des données tout en fournissant des extractions précises et hautement pertinentes.</li>
            <li class="highlight-item">Implémentation d'algorithmes automatisés sur mesure, adaptés aux besoins spécifiques des métiers.</li>
        </ul>
    </div>
    <div class="experience-item">
        <h3>EPSILON, Paris, Consultant Data scientist: Projet en interne</h3>
        <p class="period">Avril 2023 - Juillet 2023</p>
        <p class="highlight-item">
        Extraction Thématique et Analyse Sémantique des Verbatims à l'aide de Modèles de Langage Naturel.
        </p>
        <p class="highlight-item">
        Dans le cadre d’une analyse sémantique approfondie, j’ai conçu et déployé un pipeline de traitement de données textuelles basé sur des modèles avancés de NLP pour identifier les thèmes clés dans un corpus de verbatims.        
        </p>
        <ul class="fixed-list">
            <li class="highlight-item">Nettoyage et normalisation : Suppression des éléments non pertinents (caractères spéciaux, stopwords) et uniformisation linguistique (lemmatisation, tokenisation).</li>
            <li class="highlight-item">Représentation vectorielle : Conversion des textes en vecteurs numériques à l’aide d’un modèle d’embedding, optimisant la capture des relations sémantiques et contextuelles des mots.</li>
            <li class="highlight-item">Entraînement de BERT, un modèle de langage bidirectionnel, pour extraire les thèmes principaux et sous-jacents des verbatims.</li>
            <li class="highlight-item">Analyse non supervisée (clustering sémantique) pour organiser et structurer les données autour des thématiques récurrentes.</li>
            <li class="highlight-item">Validation des résultats avec des métriques pertinentes (cohérence thématique, pertinence des clusters).</li>
            <li class="highlight-item">Identification des tendances majeures et des insights exploitables pour orienter des décisions stratégiques.</li>
            <li class="highlight-item">Création d’un cadre réplicable pour l’analyse future de données textuelles à grande échelle.</li>
        </ul>
    </div>
    <div class="experience-item">
        <h3>ELECTRE, Paris, Data scientist</h3>
        <p class="period">Septembre 2020 - Septembre 2021</p>
        <ul class="fixed-list">
            <li class="highlight-item">Aider la direction Data Services à enrichir le moteur de recherche avec les nouveaux mots clés utilisés par les clients</li>
            <li class="highlight-item">Mise en place d’un moteur de recommandation d’ouvrages en construisant un modèle de machine learning basé sur le NLP regroupant les ouvrages similaires</li>
        </ul>
    </div>
    <div class="experience-item">
        <h3>(LAMA) UMR 8050 CNRS, Stage Data scientist</h3>
        <p class="period">Avril 2019 - Septembre 2019</p>
        <p class="highlight-item">
        Etude du fonctionnement de l'apprentissage des arbres de décisions
        </p>
        <ul class="fixed-list">
            <li class="highlight-item">Analyse des concepts fondamentaux des arbres de décision (nœuds, règles de division, feuilles).</li>
            <li class="highlight-item">Implémentation d'un arbre de décision à partir de zéro en Python (ou avec scikit-learn).</li>
            <li class="highlight-item">Optimisation des hyperparamètres (profondeur maximale, critère de division, etc.) pour améliorer la performance.</li>
            <li class="highlight-item">Évaluation des performances via des métriques comme la précision, le rappel et la matrice de confusion.</li>
            <li class="highlight-item">Comparaison avec d'autres algorithmes (Random Forest, SVM) pour analyser les avantages et les limites.</li>
            <li class="highlight-item">Visualisation des arbres (avec matplotlib) pour interpréter les décisions.</li>
        </ul>
    </div>
    """
    section_with_typewriter("Expérience Professionnelle", content, "💼")

def academic_background():
    content = """
    <div class="experience-item">
        <h3>ENSAI, Rennes, Mastère Spécialisé Data Science pour la connaissance client (Conférence des grandes écoles)</h3>
        <p class="period">Septembre 2020 - Septembre 2021</p>
        <ul class="fixed-list">
            <li class="highlight-item"> Machine learning, Statistique, Traitement des données</li>
            <li class="highlight-item">Econométrie panel, Analyse géospatial, Marketing</li>
            <li class="highlight-item">Data visualisation, Python, R</li>
            <li class="highlight-item">Mesure de satisfaction client, NLP, scoring client </li>
        </ul>
    </div>
    <div class="experience-item">
        <h3>UPEM Champs-Sur-Marne, Master 2 Probabilités et statistiques des nouvelles données</h3>
        <p class="period">Septembre 2018 - Septembre 2019</p>
        <ul class="fixed-list">
            <li class="highlight-item">Machine learning, Statististique en grandes dimensions</li>
            <li class="highlight-item">Big data, Architecture hadoop, AWS, GCP, Azure</li>
            <li class="highlight-item">Sql, Python, R</li>
            <li class="highlight-item">Actuariat, Calcul stochastique</li>
        </ul>
    </div>
    <div class="experience-item">
        <h3>UPEC Créteil, Master 1 Mathématiques et applications</h3>
        <p class="period">Septembre 2017 – Juillet 2018</p>
        <ul class="fixed-list">
            <li class="highlight-item">Probabilités, Statististique</li>
            <li class="highlight-item">Finance, Analyse</li>
            <li class="highlight-item">Python, R, Matlab</li>
            <li class="highlight-item">Anglais</li>
        </ul>
    </div>
    <div class="experience-item">
        <h3>Université de Thiès Sénégal, L3 Mathématiques et Informatiques</h3>
        <p class="period">Septembre 2014 - Juillet 2015</p>
        <ul class="fixed-list">
            <li class="highlight-item">Mesure et intégrations, Probabilités</li>
            <li class="highlight-item">Analyse de donneés, optimisation</li>
            <li class="highlight-item">SQL, Base de données relationnelles</li>
            <li class="highlight-item">Programmation Java, Réseau, HTML, CSS</li>
        </ul>
    </div>
    """
    section_with_typewriter("Parcours Académique", content, "🎓")

def skills_section():
    content = """
    <ul class="fixed-list">
        <li class="highlight-item">Python, Pyspark, R</li>
        <li class="highlight-item">C/C++, Java</li>
        <li class="highlight-item">Power BI, Tableau, Excel</li>
        <li class="highlight-item">SQL, Nosql</li>
        <li class="highlight-item">HTML / CSS / Javascript</li>
        <li class="highlight-item">Matplotlib, Seaborn, Scipy</li>
        <li class="highlight-item">Streamlit, Django, Flask</li>
        <li class="highlight-item">Scikit-learn, Numpy, Pandas, Keras, TensorFlow</li>
        <li class="highlight-item">Hadoop, Spark, cloudera</li>
        <li class="highlight-item">Git, Gitlab, Linux</li>
        <li class="highlight-item">AWS, GCP, Microsoft azure, Dataiku</li>
        <li class="highlight-item">Data Visualization, NLP, Statistiques</li>
        <li class="highlight-item">Machine Learning, Deep Learning, IA  Générative</li>
    </ul>
    """
    section_with_typewriter("Compétences Techniques", content, "🛠️")

def certifications_section():
    content = """
        <p><a href="http://verify.skilljar.com/c/6csshpcgm3mp" class="hover-move-effect"><button class="moving-text-btn">Dataiku Core Designer Certificate</button></a></p>
        <p><a href="http://verify.skilljar.com/c/qn5omcm53ot3" class="hover-move-effect"><button class="moving-text-btn">Dataiku Avanced Designer Certificate</button></a></p>
        <p><a href="http://verify.skilljar.com/c/py5z6b6gieyo" class="hover-move-effect"><button class="moving-text-btn">Dataiku ML Practitioner Certificate</button></a></p>
        <p><a href="https://learn.microsoft.com/api/credentials/share/fr-fr/NdiayeNiang-1906/5C8649F7E5B7ACCB?sharingId" class="hover-move-effect"><button class="moving-text-btn">Power BI Data Analyst Associate</button></a></p>
    """
    section_with_typewriter("Certifications", content, "📜")

def projects_section():
    content = """
        <p><a href="https://modify-compress-files.streamlit.app/" class="hover-move-effect"><button class="moving-text-btn">Application de compression et de fusion de fichiers</button></a></p>
        <p><a href="https://github.com/ndiaye429/Mes_Projets_Machine_learning/blob/master/Classification_images/Projet_Resaux_de_neurones_CNN_Notebook.ipynb" class="hover-move-effect"><button class="moving-text-btn">Classification d'images</button></a></p>
        <p><a href="https://github.com/ndiaye429/Mes_Projets_Machine_learning/blob/master/G%C3%A9n%C3%A9ration_de_l%C3%A9gende/generation_de_legende.ipynb" class="hover-move-effect"><button class="moving-text-btn">Génération de légende</button></a></p>
        <p><a href="https://github.com/ndiaye429/Mes_Projets_Machine_learning/blob/master/NLP/Projet_Analyse_de_la_satisfaction_client.ipynb" class="hover-move-effect"><button class="moving-text-btn">Analyse de la satisfaction client</button></a></p>
        <p><a href="https://github.com/ndiaye429/Mes_Projets_Machine_learning/blob/master/Projet_Scoring/Projet_Scoring_Ciblage.ipynb" class="hover-move-effect"><button class="moving-text-btn">Prédiction des clients à risque de résiliation</button></a></p>
        <p><a href="https://github.com/ndiaye429/Mes_Projets_Machine_learning/blob/master/Projet_S%C3%A9rie_Temporelle/Projet_S%C3%A9rie_Temporelle_Notebook.ipynb" class="hover-move-effect"><button class="moving-text-btn">Série temporelle</button></a></p>             
    """
    section_with_typewriter("Projets Réalisés", content, "🏆")

def badges_section():
    content = """
        <p><a href="https://partner.cloudskillsboost.google/public_profiles/5f17274e-e266-4e31-a83f-481b1fb4e35b/badges/12951694?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share" class="hover-move-effect"><button class="moving-text-btn">Introduction to AI and Machine Learning on Google Cloud</button></a></p>
        <p><a href="https://partner.cloudskillsboost.google/public_profiles/5f17274e-e266-4e31-a83f-481b1fb4e35b/badges/12897014?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share" class="hover-move-effect"><button class="moving-text-btn">Introduction to Data Engineering on Google Cloud </button></a></p>
        <p><a href="https://partner.cloudskillsboost.google/public_profiles/5f17274e-e266-4e31-a83f-481b1fb4e35b/badges/10286871?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share" class="hover-move-effect"><button class="moving-text-btn">Innovating with Google Cloud Artificial Intelligence</button></a></p>
        <p><a href="https://partner.cloudskillsboost.google/public_profiles/5f17274e-e266-4e31-a83f-481b1fb4e35b/badges/16307819" class="hover-move-effect"><button class="moving-text-btn">Preparing for Your Associate Cloud Engineer Journey</button></a></p>
        <p><a href="https://partner.cloudskillsboost.google/public_profiles/5f17274e-e266-4e31-a83f-481b1fb4e35b/badges/16464755" class="hover-move-effect"><button class="moving-text-btn">Preparing for your Professional Data Engineer Journey</button></a></p>
    """
    section_with_typewriter("Badges", content, "🏅")

# --- APPLICATION PRINCIPALE ---
def main():
    load_css()
    profile_section()
    
    # Première ligne
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        professional_experience()
        certifications_section()
    
    with col2:
        skills_section()
        academic_background()
        projects_section()
        badges_section()

if __name__ == "__main__":
    main()   