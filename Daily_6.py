import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 6 - 10/06/2024
On the sixth day, I delved into the intricacies of word embeddings and planned a new project.

- **Word Embeddings Study:**
  - **Exploration:** Looked into various word embedding techniques, including Word2Vec, GloVe, FastText, and ELMo.
  - **Understanding:** Learned how these models deduce relations and context from textual data.

- **Project Planning:**
  - **Sea Route Optimization:** Began outlining a sea route optimization project using Dijkstra or A* algorithms and CrewAI agents, along with RAG.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_6",
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
                    me.text("Posts - Daily")
def navigate_home(e: me.ClickEvent):
    me.navigate("/")