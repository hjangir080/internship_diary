import mesop as me

SAMPLE_MARKDOWN = """

### Weekly Internship Summary

### Week 4 (24/06/2024 - 26/06/2024)

**Summary:** 
In this week, I focused on creating an internship diary website using Mesop and Python. The website allows for uploading daily and weekly summaries and includes a chatbot to answer queries based on these entries. I improved the website's CSS for better design (small changes like color-schemes, sizing, etc), uploaded it to GitHub, and hosted it using Render. I researched how to ensure the website can function asynchronously on multiple devices.

- **Accomplishments:**
    - **Website Creation:** Successfully created an internship diary website using Mesop and Python, with functionalities to upload daily and weekly summaries and a chatbot for querying entries.
    - **Enhanced Design:** Improved the website's CSS for a more appealing and user-friendly interface.
    - **Live Deployment:** Uploaded the website to GitHub and hosted it on Render, ensuring it was live and functional.
    - **Asynchronous Functionality:** Implemented gevent to make the website asynchronous, improving performance and responsiveness.
    - **Repository Organization:** Structured the project repository for better maintainability and ease of navigation.
    - **Chatbot Integration:** Ensured the chatbot could access chat history for better context during interactions.

- **Challenges:**
    - **New UI Framework:** Learning and implementing Mesop, a new UI framework, required significant effort and adaptation.
    - **Website Functionality:** Ensuring that the internship diary website was fully functional, aesthetically pleasing, and could handle asynchronous operations across multiple devices was challenging.
    - **Live Hosting:** Deploying the website using Render and managing live hosting involved troubleshooting several technical issues.

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