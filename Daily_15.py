import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 1 - 03/06/2024
On my first day, I delved into several new technologies and tools, setting a strong foundation for the rest of my internship. Here’s a detailed account of what I accomplished:

- **MongoDB Introduction and Setup:**
  - **Learning MongoDB:** I began by learning the basics of MongoDB, a popular NoSQL database.
  - **Setting Up MongoDB Compass:** Installed and configured MongoDB Compass, a graphical user interface for MongoDB.
  - **Python Integration with PyMongo:** Connected MongoDB with Python using the PyMongo library.
  - **CRUD Operations:** Performed CRUD (Create, Read, Update, Delete) operations on a MongoDB database using Python.
  - **Dataframe Display:** Displayed the database contents in dataframes for better visualization and manipulation.

- **Docker Exploration:**
  - **Learning Docker:** Gained an understanding of Docker, a platform for developing, shipping, and running applications inside containers.
  - **Installing Docker:** Successfully installed Docker on my machine.
  - **Creating and Hosting Docker Images:** Created a Docker image from a repository and hosted it, facilitating easier deployment and management of applications.

- **AI Tools and Concepts:**
  - **AI Studios and GPTs:** Briefly explored various AI studios and GPT (Generative Pre-trained Transformer) models, including:
    - Mistral AI
    - Groq AI
    - Google AI Studio
  - **Retrieval Augmented Generation (RAG):** Introduced to RAG, a technique combining retrieval and generation for improved performance in AI models.
  - **Word2Vec:** Learned about Word2Vec, a method for generating word embeddings that capture semantic meanings of words.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_15",
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