import mesop as me

SAMPLE_MARKDOWN = """
### Internship Projects

- **[Internship Diary](https://github.com/hjangir080/internship_diary):** A website to upload and view daily and weekly internship summaries, featuring a chatbot for querying entries.
- **[Library ChatBot](https://github.com/hjangir080/Library_ChatBot):** A chatbot that uses the Internet Archive API to provide information about books and music, incorporating chat completion and function calling.
- **[Sea Route Optimization](https://github.com/hjangir080/sea_route_optimization):** A project to optimize sea routes using Dijkstra's algorithm, CrewAI agents, and RAG for accurate routing and rescue operations.
- **[Shipwreck Report](https://github.com/hjangir080/shipwreck_report):** A multi-agent tool that generates detailed reports on shipwreck rescue operations, integrating weather, navigation, and medical insights.

### CrewAI Course Replications

- **[Financial Analysis CrewAI](https://github.com/hjangir080/financial_analysis_crewAI):** A project to perform financial analysis using CrewAI agents.
- **[Event Planning CrewAI](https://github.com/hjangir080/event_planning_crewAI):** A tool to assist in event planning and management with CrewAI agents.
- **[Sales Outreach CrewAI](https://github.com/hjangir080/sales_outreach_crewAI):** A project to enhance sales outreach using CrewAI agents.
- **[Customer Support CrewAI](https://github.com/hjangir080/customer_support_crewAI):** A tool to provide efficient customer support using CrewAI agents.
- **[Article Writer CrewAI](https://github.com/hjangir080/article_writer_crewAI):** A project to assist in article writing and content generation with CrewAI agents.


"""


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/post/Projects",
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
                    me.text("Internship", style=me.Style(font_weight=700, margin=me.Margin(right=8)))
                    me.text("Diary - Projects")
def navigate_home(e: me.ClickEvent):
    me.navigate("/")