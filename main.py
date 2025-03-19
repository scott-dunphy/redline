import streamlit as st
from redlines import Redlines
import pandas as pd

def highlight_differences(text1, text2):
    """
    Use Redlines to highlight differences between two texts.
    Returns HTML with deletions and additions highlighted.
    """
    diff = Redlines(text1, text2)
    return diff.output_markdown

def main():
    st.set_page_config(
        page_title="Text Comparison Tool",
        page_icon="📝",
        layout="wide"
    )
    
    st.title("Text Comparison Tool")
    st.markdown("Compare two versions of text and see the differences highlighted")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Text")
        text1 = st.text_area(
            "Enter original text here:",
            height=200,
            key="text1",
            placeholder="Paste original text here..."
        )
    
    with col2:
        st.subheader("Modified Text")
        text2 = st.text_area(
            "Enter modified text here:",
            height=200,
            key="text2",
            placeholder="Paste revised text here..."
        )
    
    if st.button("Compare Texts"):
        if text1 and text2:
            st.subheader("Comparison Result")
            
            # Get highlighted differences
            diff_html = highlight_differences(text1, text2)
            
            # Display highlighted differences
            st.markdown(diff_html, unsafe_allow_html=True)
            
            # Calculate statistics
            total_words_original = len(text1.split())
            total_words_modified = len(text2.split())
            
            # Create simple stats
            stats = {
                "Metric": ["Word Count (Original)", "Word Count (Modified)", "Word Count Difference"],
                "Value": [
                    total_words_original,
                    total_words_modified,
                    total_words_modified - total_words_original
                ]
            }
            
            st.subheader("Text Statistics")
            st.table(pd.DataFrame(stats))
            
            # Additional explanation
            st.info("In the comparison above:  \n"
                   "- **Red strikethrough text** shows content that was removed  \n"
                   "- **Green underlined text** shows content that was added")
        else:
            st.error("Please enter text in both fields to compare.")

    # Add example button to help users get started
    if st.button("Load Example Texts"):
        st.session_state.text1 = "The quick brown fox jumps over the lazy dog. He was very tired after the long jump."
        st.session_state.text2 = "The quick brown fox leaps over the lazy dog. He was exhausted after the long jump."
        st.experimental_rerun()

if __name__ == "__main__":
    main()
