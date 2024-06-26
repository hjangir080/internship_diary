import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 3 - 05/06/2024

**CrewAI Multi-Agent Tool**

Today, I enhanced my work with CrewAI by developing a multi-agent tool. I integrated the Open Meteo API to get accurate hourly weather and sea wave conditions based on user-provided latitude and longitude values. These coordinates were then used by three agents: a researcher, a navigator, and a doctor. 

- The researcher found historical cases in the same area.
- The navigator identified all possible paths taken by the ship.
- The doctor diagnosed potential illnesses and injuries among survivors, listing necessary medical supplies.

These inputs, combined with OpenAI API and Serper API integrations, were compiled into a comprehensive report, which I then converted into a PDF.

- **Topics Learned:**
    - CrewAI multi-agent development
    - Open Meteo API integration
    - Historical case research via agents
    - Navigation pathfinding via agents
    - Medical diagnosis of potential diseases and supply listing via agents and google search
    - PDF report generation
"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Daily_3",
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