import os
import cv2
import streamlit as st
from PIL import Image

from utils.detector import detect
from utils.llm import generate_report

# ====================================================
# PAGE CONFIG
# ====================================================

st.set_page_config(
    page_title="Industrial Quality Assurance",
    page_icon="🏭",
    layout="wide"
)

# ====================================================
# CSS
# ====================================================

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:58px;
    font-weight:700;
    color:#1565C0;
    margin-bottom:5px;
}

.sub-title{
    text-align:center;
    font-size:18px;
    color:gray;
}

.center-radio{
    display:flex;
    justify-content:center;
}

</style>
""", unsafe_allow_html=True)

# ====================================================
# HEADER
# ====================================================

st.markdown(
    '<p class="main-title">🏭 AI-Powered Industrial Quality Assurance</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Detect steel surface defects using YOLOv8 and generate professional inspection reports using Llama 3.2</p>',
    unsafe_allow_html=True
)

st.divider()

# ====================================================
# INPUT METHOD
# ====================================================

st.markdown(
    "<h5 style='text-align:center; color:#555;'>Choose Input Method</h5>",
    unsafe_allow_html=True
)

input_method = st.radio(
    "",
    [
        "📂 Upload Image",
        "📷 Capture Image",
        "✍️ Enter Defect Name"
    ],
    horizontal=True
)

st.divider()

# ====================================================
# FUNCTION TO PROCESS IMAGE
# ====================================================

def process_image(uploaded_file):

    os.makedirs("uploads", exist_ok=True)

    image_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    image = Image.open(image_path)

    results = detect(image_path)

    detections = []

    for box in results[0].boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        class_name = results[0].names[class_id]

        detections.append(
            f"{class_name} ({confidence*100:.1f}%)"
        )

    annotated = results[0].plot()

    annotated = cv2.cvtColor(
        annotated,
        cv2.COLOR_BGR2RGB
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original Image")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("Detected Defects")

        st.image(
            annotated,
            use_container_width=True
        )

    st.divider()

    st.subheader("Detected Defects")

    if len(detections) == 0:

        st.success("✅ No defects detected.")

    else:

        for defect in detections:

            st.write("•", defect)

    st.divider()

    st.subheader("📋 Inspection Report")

    if len(detections) == 0:

        st.info("No report generated because no defects were detected.")

    else:

        with st.spinner("Generating AI report..."):

            report = generate_report(
                "\n".join(detections)
            )

        st.markdown(report)


# ====================================================
# OPTION 1
# ====================================================

if input_method == "📂 Upload Image":

    uploaded_file = st.file_uploader(
        "Upload a steel surface image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        process_image(uploaded_file)

# ====================================================
# OPTION 2
# ====================================================

elif input_method == "📷 Capture Image":

    captured_image = st.camera_input(
        "Capture a steel surface image"
    )

    if captured_image is not None:

        process_image(captured_image)

# ====================================================
# OPTION 3
# ====================================================

else:

    st.subheader("Enter Defect Information")

    defect = st.selectbox(
        "Select Defect",
        [
            "Scratch",
            "Pitted Surface",
            "Inclusion",
            "Crazing",
            "Rolled-in Scale",
            "Patches"
        ]
    )

    confidence = st.slider(
        "Confidence (%)",
        50,
        100,
        95
    )

    if st.button("Generate Report"):

        detections = f"{defect} ({confidence}%)"

        with st.spinner("Generating AI report..."):

            report = generate_report(detections)

        st.subheader("📋 Inspection Report")

        st.markdown(report)