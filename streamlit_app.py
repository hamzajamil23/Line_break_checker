import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import time
import re
from typing import Generator

def animate_text_line_by_line(text: str) -> Generator[str, None, None]:
    """Generates line-by-line animation with proper spacing."""
    lines = [line.strip() for line in re.split(r'\n+', text) if line.strip()]
    current_lines = []
    
    for line in lines:
        current_lines.append(line)
        yield '\n\n'.join(current_lines)
        time.sleep(0.05)

def main():
    st.set_page_config(
        page_title="Text Line Break Enhancer",
        page_icon="📝",
        layout="wide"
    )

    # Maintain session state for output
    if 'output_text' not in st.session_state:
        st.session_state.output_text = ""

    st.title("Line Break Checker")

    # Two-column layout for input and output
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 📝 Input Text")
        input_text = st.text_area("", height=350, placeholder="Enter your text here...")

        # Centering process button
        if st.button("Process Text ", use_container_width=False):
            if input_text.strip():
                st.session_state.output_text = ""
                for partial_result in animate_text_line_by_line(input_text):
                    st.session_state.output_text = partial_result
                    st.session_state.update()
            else:
                st.warning("Please enter some text to process!")

    with col2:
        st.markdown("### 📜 Output Text")
        
        # Output text area
        output_placeholder = st.empty()
        if st.session_state.output_text:
            output_placeholder.text_area("", st.session_state.output_text, height=310)

            # Custom copy button styling for dark mode
            st.markdown(
                """
                <style>
                .stCopyButton button {
                    background-color: #4CAF50 !important;
                    color: white !important;
                    border-radius: 8px;
                    font-weight: bold;
                }
                .stCopyButton button:hover {
                    background-color: #45a049 !important;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            # Centered copy button
            st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
            st_copy_to_clipboard(st.session_state.output_text, "📋 Copy Output")
            st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

