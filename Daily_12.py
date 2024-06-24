import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 12 - 19/06/2024
Began learning about the Chat Completion API by OpenAI and developed a library bot.

- **Chat Completion API:**
  - **Learning:** Started learning about the Chat Completion API by OpenAI.
  - **Library Bot Development:** Created a simple chatbot using the Chat Completion API and the Internet Archive API. The bot can provide information about any book or music in the database by its ID, incorporating chat completion along with function calling.
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_12",
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