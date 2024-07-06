import mesop as me

SAMPLE_MARKDOWN = """

### Weekly Internship Summary

### Week 4 (24/06/2024 - 28/06/2024)

**Summary:** This week, I focused on developing and hosting an internship diary website using Mesop and Python, ensuring it worked asynchronously and included a chatbot. Additionally, I worked on integrating the Assistant API with the website.

**Accomplishments:**
        - **Internship Diary Website:** Developed and hosted a website for daily and weekly summaries with a chatbot.
        - **Asynchronous Performance:** Integrated Gevent for better asynchronous performance.
        - **Chatbot Improvement:** Improved the chatbot's asynchronous functionality and added output streaming.
        - **API Integration:** Attempted to integrate the Assistant API with the website.

**Challenges:**
        - **Asynchronous Functionality:** Ensuring the website and chatbot could function asynchronously on multiple devices.
        - **Integration Issues:** Struggling to integrate the Assistant API with the Mesop UI.
        - **Output Streaming:** Ensuring the streaming functionality worked seamlessly.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Weekly_4",
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