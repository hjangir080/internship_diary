import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 10 - 14/06/2024
Successfully resolved collaboration issues and explored new tools.

- **Agent Collaboration:**
  - **Issue Resolution:** Got the agents collaborating with each other, resolving the error.
  - **Program Functionality:** Ensured the program can access all tools, tasks, and agents properly.
  - **Input Parsing Issue:** Encountered an issue with how the input is being parsed and passed along.

- **Assistant's Playground:**
  - **Exploration:** Explored the Assistant's Playground on the OpenAI platform.
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_10",
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