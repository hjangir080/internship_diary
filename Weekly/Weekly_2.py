import mesop as me

SAMPLE_MARKDOWN = """
### Weekly Internship Summary

#### Week 2 (10/06/2024 - 14/06/2024)

**Summary:**
This week, I delved deeper into Docker, working on converting a Flask application to a Docker image and starting the OpenDevin software using Docker. I also explored CrewAI's documentation, developed a simple chatbot, and created a multi-agent tool integrating the Open Meteo API for weather and sea wave conditions. Additionally, I undertook a guided project to understand and implement LangChain and RAG, creating a program to embed and query PDFs.

- **Accomplishments:**
    - **Advanced AI Projects:** Developed a multi-agent tool with CrewAI, integrating the Open Meteo API and creating detailed reports.
    - **LangChain Implementation:** Successfully created a program to upload, parse, and embed PDFs using OpenAI API and LangChain tools.
    - **Tool Integration:** Ensured that various AI tools and agents worked together seamlessly, resolving multi-agent collaboration issues.

- **Challenges:**
    - **Data Processing:** Encountered significant challenges with processing large datasets, especially when creating graphs using NetworkX. The system's RAM limitations caused execution to stop.
    - **Multi-Agent Collaboration:** Ensuring seamless interaction among multiple AI agents and integrating various APIs was complex.
    - **LangChain and RAG:** Understanding and implementing LangChain and RAG for text chunking and embedding was intricate.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Weekly_2",
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