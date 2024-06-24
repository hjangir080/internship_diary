import mesop as me

SAMPLE_MARKDOWN = """
### Weekly Internship Summary

#### Week 1 (03/06/2024 - 07/06/2024)
The first week of my internship was highly productive, filled with learning and practical application of various technologies. Here’s a comprehensive summary of the week:

- **Day 1 Achievements:**
  - Set up and configured MongoDB, integrated it with Python using PyMongo, and performed CRUD operations.
  - Learned about Docker, installed it, and created and hosted a Docker image.
  - Briefly explored several AI studios and GPT models, and learned about RAG and Word2Vec.

- **Docker and Flask Integration (Day 2):**
  - Continued working on Docker by converting a Flask application into a Docker image.
  - Used the Docker image to start and use OpenDevin software, gaining knowledge about API keys and GPT versions.
  - Reviewed CrewAI documentation and created a simple chatbot using GoogleSerperTool to search the internet and present relevant information.

- **CrewAI Multi-Agent Tool Development (Day 3):**
  - Developed a multi-agent tool using CrewAI, integrating the Open Meteo API for accurate hourly weather and sea wave conditions.
  - Designed agents (researcher, navigator, doctor) for rescue operations, integrating OpenAI API and Serper API to compile comprehensive reports and convert them to PDFs.

- **AI Agent Courses and Projects (Day 4):**
  - Worked on CrewAI multi-agent programs and completed a course by CrewAI and DeepLearning.AI.
  - Created and uploaded projects to GitHub, learning key elements of AI agents, agent tools, well-defined tasks, and multi-agent collaboration.

- **LangChain and RAG Exploration (Day 5):**
  - Studied LangChain and RAG principles and their applications.
  - Completed a guided project using these tools with Google API and OpenAI to parse, embed, and query PDFs.
  - Began exploring hosting and deployment, and briefly reviewed Hugging Face.

### Challenges Faced in Week 1
- **Docker Learning Curve:** Initially challenging to understand and set up Docker.
- **API Key Management:** Understanding and managing API keys while working with OpenDevin software.
- **CrewAI Documentation Navigation:** Navigating and comprehending the extensive CrewAI documentation to create a functional chatbot.
- **Multi-Agent Integration:** Ensuring seamless integration and communication between multiple agents and APIs in the rescue operation tool.
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Weekly_1",
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
                    me.text("Posts - Weekly")
def navigate_home(e: me.ClickEvent):
    me.navigate("/")