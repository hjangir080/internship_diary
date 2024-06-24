import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 2 - 04/06/2024
On the second day, I continued my exploration of Docker and started integrating it with other technologies.

- **Docker and Flask Integration:**
  - **Docker Images:** Worked more on Docker images, converting a Flask application into a Docker image.
  - **OpenDevin Software:** Used the Docker image to start and use OpenDevin software, learning about API keys and different GPT versions.

- **CrewAI Documentation:**
  - **Simple Chatbot:** Reviewed CrewAI documentation and created a simple chatbot that takes input for roles, tasks, and goals, and uses GoogleSerperTool to find relevant articles and present the gathered information.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_2",
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