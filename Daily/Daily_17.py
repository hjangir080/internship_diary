import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 17 - 26/06/2024

**Chat History Retention and Asynchronization**

Today, I made significant progress on the internship diary website. To enhance its performance, I integrated gevent to make the website asynchronous. This improvement will ensure that the site can handle multiple tasks simultaneously, making it more efficient and responsive. I also spent time organizing the repository structure. A well-organized repository not only makes the codebase easier to navigate but also helps in maintaining the project in the long run.
Ensuring the chatbot could access the history of the chat was another critical task for the day. This feature will allow the chatbot to provide more contextually accurate responses by referring to past interactions. Finally, I uploaded all the updates to GitHub, and thus finished the project.
I will keep updating the blogs till my internship gets over.

- **Topics Learned:**
    - Gevent for asynchronous operations
    - Repository organization
    - Chatbot history/session
        
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_17",
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