import mesop as me

SAMPLE_MARKDOWN = """
### Weekly Internship Summary

#### Week 1 (03/06/2024 - 07/06/2024)

**Summary:**
In the first week, I focused on setting up and learning the fundamentals of MongoDB and Docker. I connected MongoDB with Python, performed CRUD operations, and displayed data using dataframes. I also created and hosted a Docker image of a repository. Throughout the week, I briefly touched on AI studios like Mistral AI, Groq AI, and Google AI Studio.

- **Accomplishments:**
    - **MongoDB Setup:** Successfully set up MongoDB Compass and connected it with Python.
    - **CRUD Operations:** Performed CRUD operations on MongoDB using Python and displayed data in dataframes.
    - **Docker Mastery:** Created and hosted a Docker image, gaining a solid understanding of Docker.
    - **AI Exploration:** Developed a simple chatbot using CrewAI, integrating various APIs, and got hands-on experience with AI tools.

- **Challenges:**
    - **Learning Curve:** Getting accustomed to MongoDB, Docker, and various AI tools was challenging. There was a steep learning curve, especially in understanding and setting up MongoDB Compass and Docker.
    - **Integration Issues:** Connecting MongoDB with Python using `pymongo` and performing CRUD operations required careful attention to detail.
    - **AI Concepts:** Understanding advanced AI concepts in a short time was demanding.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Weekly_1",
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