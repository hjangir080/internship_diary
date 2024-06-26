import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 6 - 10/06/2024

**Word Embeddings and Sea Route Optimization**

I focused on understanding word embeddings, exploring Word2Vec, GloVe, FastText, and ELMo. I learned how models deduce relations and context. Additionally, I started outlining a sea route optimization project using Dijkstra's algorithm, CrewAI agents, and RAG.

- **Topics Learned:**
    - Word embeddings
    - Relationship and context deduction by models
    - Dijkstra's algorithm
    - CrewAI agents and RAG integration

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_6",
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