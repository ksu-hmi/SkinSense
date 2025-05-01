import streamlit as st
import csv
import os
import pandas as pd

# Load updated product CSV
try:
    product_data = pd.read_csv('ingredients/product_ingredients.csv')
    product_data['product_name_clean'] = product_data['product_name'].str.lower().str.strip()
except:
    product_data = None

# --- Page Configuration ---
st.set_page_config(page_title="SkinSense", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
        h1 {
            color: #FFDAB9 !important;  /* Peach */
            text-align: center;
        }
        h4 {
            color: #808080;
            text-align: center;
        }
        div.stButton > button {
            background-color: #9370DB;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            width: 100%;
        }
        textarea, input[type="text"] {
            background-color: #ffffff;
            color: black;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>SkinSense</h1>", unsafe_allow_html=True)
st.markdown("<h4>Track your skincare routines and explore ingredients</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- Section 1: Log Routine ---
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

# --- Ingredient Lookup ---
st.subheader("Look Up Skincare Ingredients")
st.caption("Tip: Type an ingredient name, like 'niacinamide' or 'retinol'.")

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
    "aloe vera": "Soothes and hydrates skin, great for calming redness and irritation.",
    "aqua": "Water, the base of most skincare products.",
    "avobenzone": "Chemical sunscreen that protects against UVA rays.",
    "butylene glycol": "A moisturizing agent that helps other ingredients penetrate skin.",
    "caprylic/capric triglyceride": "Derived from coconut oil, used to moisturize and replenish skin.",
    "cetearyl alcohol": "Fatty alcohol that softens skin and stabilizes formulations.",
    "cetyl alcohol": "Non-drying alcohol that conditions and softens skin.",
    "cholesterol": "Helps support skin barrier and retain moisture.",
    "citric acid": "AHA that helps exfoliate and adjust product pH.",
    "coco-betaine": "Mild cleansing agent derived from coconut oil.",
    "colloidal oatmeal": "Soothes and protects dry, itchy, or sensitive skin.",
    "cucumber extract": "Hydrates and refreshes skin while reducing puffiness.",
    "glacial glycoprotein": "Protects skin from cold weather and retains moisture.",
    "glycolic acid": "Exfoliates dead skin cells and promotes glow.",
    "homosalate": "Sunscreen agent that absorbs UVB rays.",
    "light reflecting minerals": "Add glow or shimmer and help blur imperfections.",
    "mannitol": "Sugar alcohol that acts as a humectant and antioxidant.",
    "octocrylene": "UVB filter that stabilizes other sunscreen ingredients.",
    "petrolatum": "Creates a barrier to lock in moisture and heal dryness.",
    "propylene glycol": "A humectant that helps retain moisture and enhance absorption.",
    "snail secretion filtrate": "Hydrates, heals, and improves skin texture.",
    "sodium pca": "Naturally occurring humectant that helps maintain skin hydration.",
    "sorbitan oleate": "Emulsifier that helps blend ingredients together.",
    "soy extract": "Brightens skin and evens tone with antioxidant effects.",
    "stearyl alcohol": "Fatty alcohol that softens and conditions the skin.",
    "tasmanian pepperberry": "Soothes skin and reduces irritation from exfoliants.",
    "vitamin b5": "Hydrates and helps skin retain moisture.",
    "vitamin e": "Antioxidant that protects skin from environmental stressors.",
    "water": "Primary solvent used in most skincare products.",
    "zinc pca": "Regulates oil and calms acne-prone skin."
}
ingredient_query = st.text_input("Enter Ingredient Name")
if ingredient_query:
    search = ingredient_query.strip().lower()
    if search in ingredient_info:
        st.success(ingredient_info[search])
    else:
        st.warning("Ingredient not found. Try another term or check spelling.")

st.markdown("---")

# --- Product Lookup ---
st.subheader("Look Up Product Ingredients and Score")
st.caption("Tip: Type a product like 'The Ordinary Niacinamide' or 'CeraVe Moisturizing Cream'.")

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

            # Show matching product image if available
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

st.markdown("---")
st.caption("© 2025 SkinSense. Built with Streamlit.")