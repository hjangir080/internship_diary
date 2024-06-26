import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 12 - 19/06/2024

**Chat Completion API and Library Bot**

I began learning about the Chat Completion API by OpenAI and created simple chatbots using it. I developed a library bot utilizing the Internet Archive API, which could provide information about any book or music in the database by its ID. The chatbot combined chat completion with function calling for enhanced functionality.

- **Topics Learned:**
    - Chat Completion API by OpenAI
    - Simple chatbot creation
    - Internet Archive API integration
    - Function calling in chatbots

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_12",
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