import mesop as me

SAMPLE_MARKDOWN = """
### Weekly Internship Summary

#### Week 3 (17/06/2024 - 21/06/2024)
The third week involved completing the route optimization project, learning new APIs, and developing a chatbot with a complete frontend and backend.

- **Route Optimization Project Completion (Day 11):**
  - Finished the sea route optimization project and uploaded it to GitHub.
  - Faced issues with data incompleteness and processing due to the large dataset.

- **Chat Completion API and Library Bot (Day 12):**
  - Learned about the Chat Completion API by OpenAI.
  - Developed a library bot using the Chat Completion API and the Internet Archive API, incorporating chat completion and function calling.

- **Chatbot Development (Day 13):**
  - Completed the library bot with a polished HTML, CSS frontend, and Flask backend.
  - Uploaded the project to GitHub after resolving issues with handling JSON outputs and integrating function results with GPT responses.

- **Chatbot Deployment and UI Framework Exploration (Day 14):**
  - Deployed the chatbot using Render, making it live.
  - Began exploring Mesop, a new UI framework by Google employees.

### Challenges Faced in Week 3
- **Data Incompleteness and Processing Issues:** Encountered challenges with data incompleteness and processing due to the large dataset size while completing the sea route optimization project.
- **Backend Corrections:** Faced and resolved issues with handling JSON outputs in the chatbot backend to ensure proper function result integration with GPT responses.
- **Deployment Challenges:** Successfully deployed the chatbot but had to ensure it worked seamlessly in a live environment.
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Weekly_3",
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
                    me.text("Posts - Weekly")
def navigate_home(e: me.ClickEvent):
    me.navigate("/")