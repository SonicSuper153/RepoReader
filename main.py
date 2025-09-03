# import asyncio

# try:
#     asyncio.get_running_loop()
# except RuntimeError:
#     asyncio.set_event_loop(asyncio.new_event_loop())


# # app.py
# import streamlit as st
# from app import ReadMe

# # Initialize your ReadMe class
# readme = ReadMe()

# # Streamlit app
# st.set_page_config(page_title="GitHub README Generator", page_icon="📄", layout="centered")

# # Title
# st.title("📄 GitHub README Generator")

# # Description
# st.markdown("""
# Enter a GitHub repository URL below, and we'll generate a neat README for it!
# """)

# # Input box for URL
# url = st.text_input("🔗 GitHub Repository URL", placeholder="https://github.com/username/repo")

# # Button to generate
# if st.button("🚀 Generate README"):
#     if url.strip():
#         with st.spinner("Generating README..."):
#             try:
#                 output = readme.generateReadme(url)
#                 st.success("README Generated!")
#                 st.markdown("### 📄 Generated README")
#                 st.code(output, language="markdown")
#             except Exception as e:
#                 st.error(f"⚠️ Error: {str(e)}")
#     else:
#         st.warning("Please enter a valid GitHub URL.")

# # Footer
# st.markdown("---")
# st.caption("Made with ❤️ using Streamlit")


from app import ReadMe

readme = ReadMe()

url = "https://github.com/SonicSuper153/Tranformer---Architecture"

print(readme.generateReadme(url,"Standard README"))