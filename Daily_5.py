import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 5 - 07/06/2024

**LangChain and RAG Exploration**

Today, I dived into LangChain and RAG, understanding their principles and essence. I undertook a guided project using these tools along with Google API and OpenAI. I learned how LangChain converts and detects text chunks, which are then embedded using APIs to find similarity indices and answer queries. I created a simple program to upload, parse, and embed a PDF using OpenAI API and LangChain tools, allowing me to run queries on it. I also briefly explored Hugging Face.

- **Topics Learned:**
    - LangChain
    - RAG (Retrieval Augmented Generation)
    - Text chunking and embedding
    - Similarity index calculation
    - PDF upload, parsing, and embedding
    - Hugging Face exploration

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_5",
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