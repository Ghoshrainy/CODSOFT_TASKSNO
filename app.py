import streamlit as st

from src.image_processor import load_image
from src.caption_generator import ImageCaptionGenerator
from src.story_generator import StoryGenerator
from src.image_analyzer import ImageAnalyzer
from src.object_detector import ObjectDetector


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Image Captioning & Visual Storyteller",
    page_icon="🖼️",
    layout="centered"
)


# ==================================================
# HEADER
# ==================================================

st.title("🖼️ AI Image Captioning & Visual Storyteller")

st.write(
    "Upload an image and let AI understand the scene, "
    "detect objects, generate a caption, analyze the image, "
    "and create a visual story."
)


# ==================================================
# LOAD MODELS
# ==================================================

@st.cache_resource
def load_caption_model():
    return ImageCaptionGenerator()


@st.cache_resource
def load_story_model():
    return StoryGenerator()


@st.cache_resource
def load_object_detector():
    return ObjectDetector()


caption_generator = load_caption_model()

story_generator = load_story_model()

image_analyzer = ImageAnalyzer()

object_detector = load_object_detector()


# ==================================================
# IMAGE UPLOAD
# ==================================================

uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png"]
)


# ==================================================
# MAIN APPLICATION
# ==================================================

if uploaded_file is not None:

    image = load_image(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.divider()


    # ==================================================
    # GENERATE AI ANALYSIS BUTTON
    # ==================================================

    if st.button(
        "🤖 Generate AI Analysis",
        use_container_width=True
    ):


        # ==============================================
        # 1. IMAGE CAPTIONING
        # ==============================================

        with st.spinner(
            "Generating image caption..."
        ):

            caption = caption_generator.generate_caption(
                image
            )


        st.subheader("✨ Generated Caption")

        st.success(caption)


        # ==============================================
        # 2. IMAGE ANALYSIS
        # ==============================================

        with st.spinner(
            "Analyzing image..."
        ):

            analysis = image_analyzer.analyze(
                image,
                caption
            )


        # ==============================================
        # AI SCENE UNDERSTANDING
        # ==============================================

        st.subheader(
            "🧠 AI Scene Understanding"
        )


        # First row

        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "👤 Main Subject",
                analysis["main_subject"]
            )


        with col2:

            st.metric(
                "🌍 Environment",
                analysis["environment"]
            )


        # Second row

        col3, col4 = st.columns(2)


        with col3:

            st.metric(
                "🎬 Activity",
                analysis["activity"]
            )


        with col4:

            st.metric(
                "📸 Scene Type",
                analysis["scene_type"]
            )


        # ==============================================
        # AI OBSERVATION
        # ==============================================

        st.write(
            "### 📝 AI Observation"
        )

        st.info(
            analysis["observation"]
        )


        # ==============================================
        # 3. YOLO OBJECT DETECTION
        # ==============================================

        with st.spinner(
            "Detecting objects using YOLO..."
        ):

            detected_objects = (
                object_detector.detect_objects(
                    image
                )
            )


        st.subheader(
            "🎯 Detected Objects"
        )


        if detected_objects:

            # ------------------------------------------
            # DRAW DETECTIONS
            # ------------------------------------------

            try:

                annotated_image = (
                    object_detector.draw_detections(
                        image
                    )
                )

                st.image(
                    annotated_image,
                    caption="YOLO Object Detection",
                    use_container_width=True
                )

            except AttributeError:

                pass


            # ------------------------------------------
            # REMOVE DUPLICATES
            # ------------------------------------------

            unique_objects = {}


            for obj in detected_objects:

                name = obj["name"]

                confidence = obj["confidence"]


                if (
                    name not in unique_objects
                    or confidence > unique_objects[name]
                ):

                    unique_objects[name] = confidence


            # ------------------------------------------
            # DISPLAY OBJECTS
            # ------------------------------------------

            for name, confidence in (
                unique_objects.items()
            ):

                percentage = confidence * 100


                st.write(
                    f"**{name.title()}** — "
                    f"{percentage:.1f}% confidence"
                )


                st.progress(
                    min(
                        int(percentage),
                        100
                    )
                )


        else:

            st.warning(
                "No recognizable objects detected."
            )


        # ==============================================
        # 4. VISUAL STORY
        # ==============================================

        with st.spinner(
            "Creating visual story..."
        ):

            story = story_generator.generate_story(
                caption=caption,
                subject=analysis["main_subject"],
                environment=analysis["environment"],
                activity=analysis["activity"]
            )


        st.subheader(
            "📖 Visual Story"
        )

        st.write(
            story
        )


        # ==============================================
        # SUCCESS MESSAGE
        # ==============================================

        st.divider()

        st.success(
            "✅ Image analysis completed successfully!"
        )