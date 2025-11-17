import streamlit as st
from agent import analyze_argument

st.title("🧠 AI Argument Strength Analyzer")
st.write("Enter any argument and the AI will rate its strength, detect fallacies, and suggest improvements.")

text = st.text_area("Enter your argument:", height=150)

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter an argument before analyzing.")
    else:
        result = analyze_argument(text)

        st.subheader("📌 Argument Strength")
        st.success(result["strength"])

        st.subheader("⚠️ Logical Fallacies Found")
        if result["fallacies"]:
            for f in result["fallacies"]:
                st.error(f"• {f}")
        else:
            st.info("No major fallacies detected.")

        st.subheader("💡 Suggestions to Improve Argument")
        st.write(result["suggestion"])
