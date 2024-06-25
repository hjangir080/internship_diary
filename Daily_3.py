import mesop as me

SAMPLE_MARKDOWN = """
### Internship Diary

#### Day 3 - 05/06/2024
The third day was focused on enhancing the multi-agent system using CrewAI for rescue operations.

- **CrewAI Multi-Agent Tool Development:**
  - **Open Meteo API Integration:** Integrated the Open Meteo API for accurate hourly weather and sea wave conditions.
  - **Designing Agents:** Created agents (researcher, navigator, doctor) for rescue operations, each performing specific tasks:
    - **Researcher:** Finds older cases near the same area.
    - **Navigator:** Finds all possible paths taken by the ship.
    - **Doctor:** Diagnoses possible illnesses and injuries and lists needed medical supplies.
  - **Report Generation:** Integrated OpenAI API and Serper API to compile a comprehensive report and convert it to a PDF.

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