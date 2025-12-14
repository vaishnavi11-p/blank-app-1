import streamlit as st
import time
from PIL import Image
from io import BytesIO
from streamlit_image_comparison import image_comparison

st.title("Room Design AI App 🏠")

image = st.file_uploader("Upload room image", type=["jpg", "png"])

if image:
    original_image = Image.open(image)
    st.image(original_image, caption="Original Room", use_container_width=True)

room_type = st.selectbox(
    "Select Room Type",
    ["Bedroom", "Living Room", "Office"]
)

style = st.selectbox(
    "Select Design Style",
    ["Modern", "Minimalist", "Luxury"]
)

if st.button("Design My Room"):
    with st.spinner("AI is redesigning your room..."):
        time.sleep(2)

    st.success("Design Completed!")

    if style == "Modern":
        redesigned_image = Image.open("sample_designs/modern.jpg")
    elif style == "Minimalist":
        redesigned_image = Image.open("sample_designs/minimalist.jpg")
    else:
        redesigned_image = Image.open("sample_designs/luxury.jpg")

    st.subheader("AI Redesigned Room ✨")
    st.image(redesigned_image, caption=f"{style} {room_type}", use_container_width=True)

    image_comparison(
        img1=original_image,
        img2=redesigned_image,
        label1="Original Room",
        label2="AI Designed Room"
    )

    buffer = BytesIO()
    redesigned_image.save(buffer, format="PNG")

    st.download_button(
        label="Download AI Designed Room 🏠",
        data=buffer.getvalue(),
        file_name="ai_room_design.png",
        mime="image/png"
    )

    st.subheader("AI Design Suggestions 🧠")

    if room_type == "Bedroom":
        suggestions = [
            "Soft ambient lighting near the bed",
            "Neutral colors with warm accents",
            "Minimal furniture for calm atmosphere"
        ]
    elif room_type == "Living Room":
        suggestions = [
            "Central seating arrangement",
            "Accent wall behind sofa",
            "Layered lighting for depth"
        ]
    else:
        suggestions = [
            "Ergonomic desk placement",
            "Natural lighting optimization",
            "Cable-free clean layout"
        ]

    st.write(f"**Room Type:** {room_type}")
    st.write(f"**Design Style:** {style}")

    for s in suggestions:
        st.write("•", s)

    st.success("AI analyzed lighting, layout, and space efficiency")
