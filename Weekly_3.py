import mesop as me

SAMPLE_MARKDOWN = """
### Weekly Internship Summary

#### Week 3 (18/06/2024 - 21/06/2024)

**Summary:**
This week, I completed the code for the route optimization project and uploaded it to GitHub. I also started learning about the Chat Completion API by OpenAI and created a library bot using the Internet Archive API. I worked on its frontend using HTML and CSS, and backend using Flask, ensuring it handled JSON outputs correctly. Finally, I deployed the library bot using Render and explored the Mesop UI framework.

- **Accomplishments:**
    - **Route Optimization Completion:** Finished the code for the route optimization project, successfully uploaded it to GitHub, and demonstrated its functionality using Google Colab.
    - **Library Bot Development:** Created a fully functional library bot using the Internet Archive API, integrating chat completion with function calling.
    - **Successful Deployment:** Deployed the library bot on Render, making it live and accessible.

- **Challenges:**
    - **Complex API Usage:** Working with the Chat Completion API and integrating it with function calling for the library bot required a thorough understanding of API functionalities.
    - **Frontend and Backend Coordination:** Ensuring smooth interaction between the HTML/CSS frontend and Flask backend for the library bot posed several challenges.
    - **Deployment Issues:** Deploying the chatbot using Render and ensuring it was live and functional involved overcoming several technical hurdles.

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