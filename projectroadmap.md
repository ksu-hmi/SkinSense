# 📍 Project Roadmap – SkinSense 

This roadmap tracks the key milestones and tasks for the development of SkinSense – a personal skincare tracker and ingredient guide designed to help users make more informed skincare decisions. The project spans 3 sprints.

---

## 🚀 Sprint 1: Setup & Exploration

**Goals:**

- Set up the project repository  
- Review related repositories  
- Begin outlining features and structure  

**Tasks:**

- ✅ Fork and clone the `radiant` repository into the `ksu-hmi` GitHub organization  
- ✅ Upload core files from `radiant` to `references/radiant/` inside `SkinSense`  
- ✅ Evaluate the structure and code of the `radiant` repo  
- ✅ Create initial project folders: `routines/`, `ingredients/`, `images/`  
- ✅ Create and structure `README.md`  
- ✅ Assign open source license (MIT)  
- ✅ Set up `projectroadmap.md` with Sprint 1 tasks  

**Exploration Notes:**

- The `radiant` repo helped me understand how Streamlit can handle user input forms and layout.  
- The `skincare-routine-helper` repo provided ideas for how to organize skincare data and product info.  
- Only essential files were included in my repo to keep things clean.  
- Future interface layout ideas may be inspired by these references.  

---

## 🚀 Sprint 2: Development Progress

**Goals:**

- Build the routine logging form  
- Implement ingredient lookup  
- Begin product lookup functionality  

**Tasks:**

- ✅ Implement Streamlit form for logging routines (morning/evening, products used, reactions, skin type)  
- ✅ Save routine logs to `routines/routine_log.csv`  
- ✅ Add download button for routine logs  
- ✅ Create ingredient lookup with predefined ingredient info  
- ✅ Add product lookup based on `product_ingredients.csv`  
- ✅ Display product ingredients and scores  
- ✅ Style headers and buttons with custom CSS  
- ✅ Add routine form and ingredient lookup sections to the app  

**Progress Notes:**

- The routine logging form is functional and saves entries correctly.  
- Ingredient lookup provides helpful information for common skincare ingredients.  
- Product lookup displays ingredients and scores from the CSV file.  
- Custom CSS enhances the visual appeal of the app.  

---

## 🚀 Sprint 3: Enhancements & Finalization

**Goals:**

- Integrate product images  
- Refine UI styling  
- Update product database  
- Finalize routine logging features  

**Tasks:**

- ✅ Added support for displaying product images (PNG and JPG) from the `images/` folder  
- ✅ Adjusted image rendering to use `width=300` for consistent display sizing   
- ✅ Changed SkinSense title color to peach  
- ✅ Expanded `product_ingredients.csv` to 25 total products  
- ✅ Confirmed CSV product names match filenames for image display  
- ✅ Improved routine logging and file path structure  
- ✅ Cleaned unused files and verified app.py is in root, not `routines/`  
- ✅ Verified ingredient dictionary fully covers all ingredients from CSV  
- ✅ Maintained organized commit messages throughout updates  

**Progress Notes:**

- Product images display beautifully during product lookup  
- Interface styling is simpler, sleeker, and peach-themed  
- Users now have access to a wider product and ingredient selection  
- All changes are saved, committed, and GitHub-ready  

---
