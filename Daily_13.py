import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 13 - 20/06/2024
Completed the chatbot and worked on its frontend and backend.

- **Chatbot Completion:**
  - **Frontend Development:** Worked on the HTML and CSS for the chatbot’s frontend.
  - **Backend Development:** Used Flask for the backend, making corrections to handle JSON outputs and ensuring function results are properly integrated with GPT responses.
  - **GitHub Upload:** Uploaded the completed project to GitHub.
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_13",
)
def app():
  header()
  with me.box(style=me.Style(margin=me.Margin(left=12))):
      me.markdown(SAMPLE_MARKDOWN)

def header():
    with me.box(style=me.Style(
        border=me.Border(bottom=me.BorderSide(style="solid", width=1, color="#dcdcdc")),
        overflow_x="clip",
    )):
        with me.box(style=me.Style(
            display="flex",
            align_items="end",
            justify_content="space-between",
            margin=me.Margin(left=12, right=12, bottom=12, top=12),
            font_size=24,
        )):
            with me.box(style=me.Style(display="flex")):
                with me.box(style=me.Style(display="flex", cursor="pointer"), on_click=navigate_home):
                    me.text("My Blog", style=me.Style(font_weight=700, margin=me.Margin(right=8)))
                    me.text("Posts - Daily")
def navigate_home(e: me.ClickEvent):
    me.navigate("/")