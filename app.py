import streamlit as st
import csv
import os
import pandas as pd
import base64

# --- Page Configuration ---
st.set_page_config(page_title="SkinSense", layout="centered")

# Function to set background image
def set_background(jpg_file):
    with open(jpg_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the background image
set_background("images/background.jpg")

# --- Custom Styling ---
st.markdown("""
    <style>
        h1 {
            color: #FF7F50 !important;  /* Peach/Dark Coral */
            text-align: center;
        }
        h4 {
            color: #000000;
            text-align: center;
        }
        div.stButton > button {
            background-color: #9370DB;
            color: white;
            border-radius: 8px;
            font-size: 20px;
            width: 100%;
        }
        textarea, input[type="text"] {
            background-color: #ffffff;
            color: black;
            border-radius: 8px;
        }
        .stTabs [role="tab"] {
            font-weight: bold;
            font-size: 22px;
            color: black !important;
        }
        .stTabs [aria-selected="true"] {
            border-bottom: 3px solid #FF7F50;
        }
    </style>
""", unsafe_allow_html=True)

# --- Load Product CSV ---
try:
    product_data = pd.read_csv('ingredients/product_ingredients.csv')
    product_data['product_name_clean'] = product_data['product_name'].str.lower().str.strip()
except:
    product_data = None

# --- Tabs ---
tabs = st.tabs(["\U0001F4D6 Welcome", "\U0001F50D Ingredient & Product Search", "\U0001F9F4 Log Your Routine"])

# --- Welcome Page ---
with tabs[0]:
    st.markdown("<h1>SkinSense</h1>", unsafe_allow_html=True)
    st.markdown("<h4>Track your skincare routines and explore ingredients</h4>", unsafe_allow_html=True)
    st.markdown("""
        <div style='color: black; font-size: 17px;'>
        This app helps you track your skincare routines and learn about products and ingredients.
        <br><br>
        Use the tabs above to explore features!
        </div>
    """, unsafe_allow_html=True)

# --- Ingredient & Product Lookup ---
with tabs[1]:
    st.subheader("Look Up Skincare Ingredients")
    st.caption("Tip: Try 'niacinamide', 'salicylic acid', etc.")

    ingredient_info = {
        "hyaluronic acid": "Helps retain skin moisture and plumps the skin.",
        "niacinamide": "Minimizes pores, balances oil, and brightens skin.",
        "retinol": "Increases cell turnover and smooths fine lines.",
        "salicylic acid": "Clears pores and treats acne.",
        "vitamin c": "Brightens skin and helps reduce dark spots.",
        "glycerin": "Hydrates and softens the skin.",
        "ceramides": "Support skin barrier and prevent moisture loss.",
        "zinc oxide": "Soothes irritation and provides sun protection.",
        "benzoyl peroxide": "Kills acne-causing bacteria.",
        "azelaic acid": "Brightens tone and reduces blemishes.",
        "lactic acid": "Gently exfoliates and hydrates.",
        "kojic acid": "Lightens dark spots and uneven tone.",
        "shea butter": "Moisturizes deeply and softens skin.",
        "panthenol": "Soothes and repairs dry skin.",
        "tea tree oil": "Fights acne-causing bacteria.",
        "urea": "Improves skin texture and hydration.",
        "squalane": "Restores moisture without heaviness.",
        "amino acids": "Support skin elasticity and balance.",
        "dimethicone": "Smooths and protects the skin barrier.",
        "allantoin": "Soothes irritated skin.",
        "green tea extract": "Rich in antioxidants and calms redness.",
        "sorbitol": "Humectant that maintains moisture.",
        "betaine": "Gentle hydrator that balances oil.",
        "peptides": "Support collagen and firmness.",
        "sodium hyaluronate": "Hydrates and plumps at a deeper level.",
        "aloe vera": "Soothes and hydrates skin.",
        "aqua": "Water, the base of most skincare products.",
        "avobenzone": "Chemical sunscreen that protects against UVA rays.",
        "butylene glycol": "Moisturizing agent that helps other ingredients penetrate skin.",
        "caprylic/capric triglyceride": "Derived from coconut oil, used to moisturize.",
        "cetearyl alcohol": "Softens skin and stabilizes formulations.",
        "cetyl alcohol": "Conditions and softens skin.",
        "cholesterol": "Supports skin barrier.",
        "citric acid": "Exfoliates and adjusts product pH.",
        "coco-betaine": "Cleansing agent from coconut oil.",
        "colloidal oatmeal": "Soothes dry or sensitive skin.",
        "cucumber extract": "Hydrates and reduces puffiness.",
        "glacial glycoprotein": "Protects and retains moisture.",
        "glycolic acid": "Promotes glow and exfoliates.",
        "homosalate": "UVB absorber in sunscreen.",
        "light reflecting minerals": "Adds glow, blurs imperfections.",
        "mannitol": "Moisturizer and antioxidant.",
        "octocrylene": "Stabilizes sunscreen.",
        "petrolatum": "Locks in moisture.",
        "propylene glycol": "Helps retain moisture and enhances absorption.",
        "snail secretion filtrate": "Hydrates and improves texture.",
        "sodium pca": "Maintains hydration.",
        "sorbitan oleate": "Emulsifier for blending ingredients.",
        "soy extract": "Brightens and evens tone.",
        "stearyl alcohol": "Conditions the skin.",
        "tasmanian pepperberry": "Reduces exfoliant irritation.",
        "vitamin b5": "Hydrates skin.",
        "vitamin e": "Antioxidant protector.",
        "water": "Main base in products.",
        "zinc pca": "Reduces oil, calms acne."
    }

    ingredient_query = st.text_input("Enter Ingredient Name")
    if ingredient_query:
        search = ingredient_query.strip().lower()
        if search in ingredient_info:
            st.success(ingredient_info[search])
        else:
            st.warning("Ingredient not found. Try another term or check spelling.")

    st.markdown("---")
    st.subheader("Look Up Product Ingredients and Score")
    st.caption("Tip: Try a product like 'The Ordinary Niacinamide' or 'CeraVe Moisturizing Cream'")

    if product_data is not None:
        product_query = st.text_input("Enter Product Name")
        if product_query:
            query_clean = product_query.strip().lower()
            match = product_data[product_data['product_name_clean'] == query_clean]
            if not match.empty:
                ingredients = match.iloc[0]['ingredients']
                score = match.iloc[0]['score'] if 'score' in match.columns else 4.6
                st.success("Ingredients: " + ingredients)
                st.info("Overall Score: " + str(score) + " / 5")
                st.markdown("**What Does the Score Mean?**")
                st.markdown(
                    "- 4.8 – 5.0 → Excellent: Gentle, effective, and loved by most users  \n"
                    "- 4.5 – 4.7 → Great: High-quality, widely recommended  \n"
                    "- 4.2 – 4.4 → Good: Well-formulated with minor drawbacks  \n"
                    "- Below 4.2 → Fair: Mixed reviews or contains common irritants"
                )

                base_name = match.iloc[0]["product_name"]
                image_path_jpg = "images/" + base_name + ".jpg"
                image_path_png = "images/" + base_name + ".png"
                if os.path.isfile(image_path_jpg):
                    st.image(image_path_jpg, caption="Product Image", width=300)
                elif os.path.isfile(image_path_png):
                    st.image(image_path_png, caption="Product Image", width=300)
            else:
                st.warning("Product not found. Please check the spelling.")
    else:
        st.error("Product database not loaded properly.")

# --- Log Routine Tab ---
with tabs[2]:
    st.subheader("Log Your Skincare Routine")

    with st.form("routine_form"):
        routine_type = st.radio("Routine Type", ["Morning", "Evening"])
        products_used = st.text_area("Products Used (one per line)")
        skin_reaction = st.text_area("Any Skin Reactions or Notes?")
        skin_type = st.selectbox("Skin Type", ["Normal", "Oily", "Dry", "Combination", "Sensitive"])
        submitted = st.form_submit_button("Submit Routine")

    if submitted:
        st.success("Your skincare routine was successfully saved.")
        st.write("Routine:", routine_type)
        st.write("Products Used:", products_used)
        st.write("Skin Reaction Notes:", skin_reaction)
        st.write("Skin Type:", skin_type)

        file_exists = os.path.isfile('routines/routine_log.csv')
        with open('routines/routine_log.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Routine Type", "Products Used", "Skin Reaction", "Skin Type"])
            writer.writerow([routine_type, products_used, skin_reaction, skin_type])

    if os.path.exists('routines/routine_log.csv'):
        with open('routines/routine_log.csv', 'rb') as f:
            st.download_button("Download Routine Log", f, file_name="routine_log.csv")

st.markdown("---")
st.caption("© 2025 SkinSense. Built with Streamlit.")