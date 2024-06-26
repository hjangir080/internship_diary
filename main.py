import os
import sys
from dataclasses import dataclass

import mesop as me

import Chatbot.chatbot as chatbot

import Projects.Projects as Projects

import Daily.Daily_1 as Daily_1 
import Daily.Daily_2 as Daily_2
import Daily.Daily_3 as Daily_3
import Daily.Daily_4 as Daily_4
import Daily.Daily_5 as Daily_5
import Daily.Daily_6 as Daily_6
import Daily.Daily_7 as Daily_7
import Daily.Daily_8 as Daily_8
import Daily.Daily_9 as Daily_9
import Daily.Daily_10 as Daily_10
import Daily.Daily_11 as Daily_11
import Daily.Daily_12 as Daily_12
import Daily.Daily_13 as Daily_13
import Daily.Daily_14 as Daily_14
import Daily.Daily_15 as Daily_15
import Daily.Daily_16 as Daily_16
import Daily.Daily_17 as Daily_17

import Weekly.Weekly_1 as Weekly_1
import Weekly.Weekly_2 as Weekly_2
import Weekly.Weekly_3 as Weekly_3
import Weekly.Weekly_4 as Weekly_4

# Ensure the current directory is in the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

@dataclass
class Example:
    name: str
    image_url: str

@dataclass
class Section:
    name: str
    examples: list[Example]

FIRST_SECTIONS = [
    Section(
        name="Daily Report",
        examples=[
            Example(name="Daily_1", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_2", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_3", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_4", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_5", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_6", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_7", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_8", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_9", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_10", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_11", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_12", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_13", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_14", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_15", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_16", image_url="https://i.ibb.co/y44gLtv/june.png"),
            Example(name="Daily_17", image_url="https://i.ibb.co/y44gLtv/june.png"),
        ],
    ),
    Section(
        name="Weekly Report",
        examples=[
            Example(name="Weekly_1", image_url="https://i.ibb.co/bR4wxq4/june-weekly.png"),
            Example(name="Weekly_2", image_url="https://i.ibb.co/bR4wxq4/june-weekly.png"),
            Example(name="Weekly_3", image_url="https://i.ibb.co/bR4wxq4/june-weekly.png"),
            Example(name="Weekly_4", image_url="https://i.ibb.co/bR4wxq4/june-weekly.png"),
        ],
    ),
    Section(
        name="Projects",
        examples=[
            Example(name="Projects", image_url="https://i.ibb.co/xGFPhX6/projects.webp"),
        ],
    ),
    Section(
        name="Chatbot",
        examples=[
            Example(name="chatbot", image_url="https://i.ibb.co/MgJ3Gdc/chatbot.jpg"),
        ],
    ),
]

BORDER_SIDE = me.BorderSide(
    style="solid",
    width=1,
    color="#dcdcdc",
)

@me.page(
    title="My Blog Posts",
    security_policy=me.SecurityPolicy(allowed_iframe_parents=["https://google.github.io"]),
)
def main_page():
    header()
    with me.box(style=me.Style(flex_grow=1, display="flex",height="91%", overflow_y="auto", overflow_x="auto")):
        if is_desktop():
            side_menu()
        with me.box(style=me.Style(
            width="calc(100% - 150px)" if is_desktop() else "100%",
            display="flex",
            gap=24,
            flex_direction="column",
            padding=me.Padding.all(24),
            overflow_y="auto",
            background="#F7F4F3",
        )):
            for section in FIRST_SECTIONS:
                section_box(section)

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
            # margin=me.Margin(left=12, right=12, bottom=12),
            font_size=24,
            color="#BFACC8",
        )):
            with me.box(style=me.Style(display="flex")):
                with me.box(style=me.Style(display="flex", cursor="pointer"), on_click=navigate_home):
                    me.text("Internship", style=me.Style(font_weight=700, margin=me.Margin(right=8)))
                    me.text("Diary")

def navigate_home(e: me.ClickEvent):
    me.navigate("/")

def side_menu():
    with me.box(style=me.Style(
        padding=me.Padding.all(12),
        width=250,
        flex_grow=0,
        line_height="1.5",
        border=me.Border(right=BORDER_SIDE),
        overflow_x="hidden",
        height="calc(100vh - 50px)",
        overflow_y="auto",
        background="#1C2541",
    )):
        for section in FIRST_SECTIONS:
            nav_section(section)
        with me.box(style=me.Style(margin=me.Margin.symmetric(horizontal=-16, vertical=16))):
            me.divider()

def nav_section(section: Section):
    with me.box(style=me.Style(margin=me.Margin(bottom=12))):
        me.text(section.name, style=me.Style(font_weight=700,color="#BFACC8"))
        for example in section.examples:
            example_name = format_example_name(example.name)
            path = f"/post/{example.name}"
            with me.box(style=me.Style(color="#88BBC5", cursor="pointer"), on_click=set_demo, key=path):
                me.text(example_name)

def set_demo(e: me.ClickEvent):
    me.navigate(e.key)

def section_box(section: Section):
    with me.box(style=me.Style(margin=me.Margin(bottom=28))):
        me.text(
            section.name,
            style=me.Style(font_weight=500, font_size=20, margin=me.Margin(bottom=16)),
        )
        with me.box(style=me.Style(
            display="flex",
            flex_direction="row",
            flex_wrap="wrap",
            gap=28,
        )):
            for example in section.examples:
                example_card(example)

def example_card(example: Example):
    with me.box(
        key=example.name,
        on_click=navigate_example_card,
        style=me.Style(
            border=me.Border.all(BORDER_SIDE),
            box_shadow="rgba(0, 0, 0, 0.2) 0px 3px 1px -2px, rgba(0, 0, 0, 0.14) 0px 2px 2px, rgba(0, 0, 0, 0.12) 0px 1px 5px",
            cursor="pointer",
            width="min(100%, 150px)",
            border_radius=12,
            background="#FBF5E5",
        ),
    ):
        image_url = example.image_url
        me.box(style=me.Style(
            background=f'url("{image_url}") center / cover',
            height=112,
            width=150,
            border_radius=12,
        ))
        me.text(
            format_example_name(example.name),
            style=me.Style(
                font_weight=500,
                font_size=18,
                padding=me.Padding.all(12),
                border=me.Border(top=BORDER_SIDE),
            ),
        )

@me.page(
    title="Blog Post",
    path="/post/{name}"
)
def post_page(name: str):
    header()
    with me.box(style=me.Style(
        flex_grow=1,
        display="flex",
        flex_direction="column",
        padding=me.Padding.all(24),
        overflow_y="auto",
    )):
        try:
            module = __import__(name)
            content = module.get_content()
        except (ImportError, AttributeError):
            content = "Content not found."
        
        me.text(content, style=me.Style(font_size=18))

def navigate_example_card(e: me.ClickEvent):
    path = "/post/" + e.key
    print(f"Navigating to: {path}")
    me.navigate(path)

def format_example_name(name: str):
    return (
        " ".join(name.split("_"))
        .capitalize()
        .replace("Llm", "LLM")
        .replace(" demo", "")
    )

def is_desktop():
    return me.viewport_size().width > 640
