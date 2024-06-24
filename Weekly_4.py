import mesop as me

SAMPLE_MARKDOWN = """
### Weekly Internship Summary

#### Week 2 (10/06/2024 - 14/06/2024)
The second week was focused on advancing projects, learning new tools, and overcoming technical challenges. Here’s a comprehensive summary of the week:

- **Word Embeddings Study (Day 6):**
  - Explored various word embedding techniques such as Word2Vec, GloVe, FastText, and ELMo, understanding their role in deducing relations and context.
  - Began planning a sea route optimization project using Dijkstra or A* algorithms and CrewAI agents.

- **Route Optimization Project (

Day 7):**
  - Used GeoPandas for data reading and integrated CrewAI agents, tasks, and tools.
  - Encountered challenges with data processing due to RAM limitations when creating a graph using NetworkX.

- **Graph Creation and Pathfinding (Day 8):**
  - Successfully created a graph using NetworkX and found a path, although the entire dataset could not be processed.
  - Explored the Assistant API.

- **Multi-Agent Collaboration (Day 9):**
  - Ensured all tools work together properly but faced challenges with multi-agent collaboration.

- **Agent Collaboration and New Tools (Day 10):**
  - Resolved agent collaboration issues and ensured the program can access all tools, tasks, and agents properly.
  - Encountered and began addressing an issue with input parsing and passing.
  - Explored the Assistant's Playground on the OpenAI platform.

### Challenges Faced in Week 2
- **Data Processing Limits:** Encountered significant challenges with data processing limits due to the RAM being completely used up when creating a graph using NetworkX from a very large dataset.
- **Agent Collaboration Issues:** Initially faced difficulties in establishing effective multi-agent collaboration where the agents did not respond well when called through the multi-agent system. This was later resolved.
- **Input Parsing Problems:** After resolving collaboration issues, encountered problems with how the input is being parsed and passed along within the program.
- **Optimization Project Complexity:** The sea route optimization project required detailed planning and integration of multiple tools, leading to challenges in execution due to data processing constraints.

"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Weekly_4",
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