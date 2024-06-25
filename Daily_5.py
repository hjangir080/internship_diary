import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 5 - 07/06/2024
The final day of the first week was dedicated to exploring new AI tools and completing a guided project.

- **LangChain and RAG Exploration:**
  - **Principles and Applications:** Studied LangChain and RAG principles and their applications.
  - **Guided Project:** Completed a guided project using these tools along with Google API and OpenAI to parse, embed, and query PDFs.
  - **Hosting and Deployment:** Began exploring hosting and deployment options.
  - **Hugging Face:** Briefly reviewed Hugging Face, a popular platform for NLP models.
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_5",
)
def app():
  header()
  with me.box(style=me.Style(margin=me.Margin(left=12),height="91%", overflow_y="auto",background="#F7F4F3")):
      me.markdown(SAMPLE_MARKDOWN)

def header():
    with me.box(style=me.Style(
        background="#1C2541",
        border=me.Border(bottom=me.BorderSide(style="solid", width=1, color="#dcdcdc")),
        overflow_x="clip",
    )):
        with me.box(style=me.Style(
            padding=me.Padding(top=12, right=12, left=12, bottom=12),
            display="flex",
            align_items="end",
            justify_content="space-between",
            # margin=me.Margin(left=12, right=12, bottom=12, top=12),
            font_size=24,
            color="#BFACC8",
        )):
            with me.box(style=me.Style(display="flex")):
                with me.box(style=me.Style(display="flex", cursor="pointer"), on_click=navigate_home):
                    me.text("My Blog", style=me.Style(font_weight=700, margin=me.Margin(right=8)))
                    me.text("Posts - Daily")
def navigate_home(e: me.ClickEvent):
    me.navigate("/")