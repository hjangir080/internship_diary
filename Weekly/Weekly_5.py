import mesop as me

SAMPLE_MARKDOWN = """
### Weekly Internship Summary

#### Week 5 (01/07/2024 - 05/07/2024)
**Summary:** This week, I attempted to integrate the assistant with HTML and Flask, faced challenges with streaming responses in the UI, and explored reinforcement learning by training a computer to play the Snake game.

**Accomplishments:**
    - **Assistant Integration:** Attempted integrating the assistant with HTML and Flask, exploring SSE clients.
    - **Streaming Responses:** Continued efforts to enable streaming responses in the UI.
    - **Reinforcement Learning Exploration:** Explored reinforcement learning concepts and their applications.
    - **Snake Game Training:** Replicated a model to train a computer to play the Snake game using Python, PyTorch, and Deep Q-Learning.
    - **Machine Learning Study:** Conducted an in-depth study into machine learning, auditing a course by Andrew Ng.

**Challenges:**
    - **Integration Issues:** Continued challenges with integrating the assistant with different UI frameworks.
    - **Streaming Functionality:** Struggled to implement streaming responses in the chatbot UI.
    - **Learning Curve:** Steep learning curve in understanding and implementing reinforcement learning concepts.
    - **Model Replication:** Ensuring accurate replication and training of the Snake game model.
    - **Comprehensive Study:** Balancing the in-depth study of machine learning with practical implementation.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Weekly_5",
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