import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Magic Booklet Maker", layout="wide")

st.title("✨ Magic Kids Booklet Maker ✨")
st.subheader("Fun 5-page activity booklets for ages 5–10!")

child_name = st.text_input("Child's name (optional)", "")

if st.button("Generate New Booklet! 🎈", type="primary", use_container_width=True):
    with st.spinner("Creating your magical booklet..."):
        theme = random.choice([
            "Space Adventure", "Dinosaur World", "Under the Sea",
            "Magical Forest", "Superheroes", "Jungle Quest", "Robot Friends"
        ])
        
        main_character = random.choice([
            "dinosaur", "unicorn", "robot", "dragon", "panda", "tiger", "fox"
        ])
        
        booklet_id = datetime.now().strftime("%Y%m%d-%H%M%S")
        
        st.success(f"**{theme} Booklet ready!** (ID: {booklet_id})")
        st.balloons()
        
        # Page 1 - Cover
        st.markdown("### Page 1 – Super Cool Cover")
        st.markdown(f"# My {theme} Adventure!")
        if child_name.strip():
            st.markdown(f"### Starring: **{child_name}** and the Amazing {main_character.title()}!")
        else:
            st.markdown(f"### Starring: The Amazing {main_character.title()}!")
        st.markdown("Age 5–10 • Lots of Fun!")
        st.markdown("---")
        
        # Pages 2–5
        activities = [
            ("Coloring", "A big smiling {thing} waving hello! Lots of space to color!"),
            ("Maze", "Help the little {thing} find the hidden treasure!"),
            ("Word Search", "Find these words: star, moon, paw, laser, fin"),
            ("Draw & Finish", "Finish this drawing: half of a funny {thing}")
        ]
        
        for i in range(4):
            act_type, template = random.choice(activities)
            thing = random.choice(["dinosaur", "unicorn", "robot", "dragon", "panda"])
            
            text = template.format(thing=thing)
            
            st.markdown(f"### Page {i+2} – {act_type}")
            st.write(text)
            st.markdown("→ → **Big empty space for drawing / coloring / writing!** ← ←")
            st.markdown("---")
        
        st.info("Tip: You can print this page or take screenshots to make a real mini booklet!")
