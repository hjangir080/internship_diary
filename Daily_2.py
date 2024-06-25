import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 2 - 04/06/2024

**Docker Images and CrewAI Chatbot**

Today's focus was on Docker images. I converted a Flask application into a Docker image, which was a great hands-on experience. Using this Docker image, I started and used the OpenDevin software, learning about API keys and different versions of GPTs in the process.

I also explored CrewAI's documentation and developed a simple chatbot. The chatbot could take inputs such as role, task, and goal, and then use the GoogleSerperTool to search the internet for relevant articles, presenting the gathered information as required.

- **Topics Learned:**
    - Docker image creation
    - Flask application Docker conversion
    - OpenDevin software usage
    - API keys and GPT versions
    - CrewAI documentation and chatbot development
    - GoogleSerperTool integration
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_2",
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