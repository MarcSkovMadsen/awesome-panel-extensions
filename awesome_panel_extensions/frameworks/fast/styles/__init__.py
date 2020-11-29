"""Functionality for styling according to Fast.design"""
import pathlib
from typing import Dict

import param

_ROOT = pathlib.Path(__file__).parent.parent / "assets/css"
_CSS_FILES = [
    "fast_root.css",
    "fast_bokeh.css",
    "fast_bokeh_slickgrid.css",
    "fast_panel.css",
    "fast_panel_dataframe.css",
    "fast_panel_widgets.css",
    "fast_panel_markdown.css",
    "fast_awesome.css",
]
_DEFAULT_ROOT_FILE = "fast_root_default.css"
_DARK_ROOT_FILE = "fast_root_dark.css"

COLLAPSED_SVG_ICON = """
<svg style="stroke: #E62F63" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="collapsed-icon">
            <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M9 5.44446V12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
""".replace(
    "\n", ""
)

EXPANDED_SVG_ICON = """
<svg style="stroke: #E62F63" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="expanded-icon">
    <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
    <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
""".replace(
    "\n", ""
)


def read_fast_css(theme: str = "default") -> str:
    """Returns the Fast Base CSS

    Args:
        theme (str, optional): "default" or "dark". Defaults to "default".

    Returns:
        str: [description]
    """
    theme = theme.lower()
    if theme == "dark":
        theme_root_file = _DARK_ROOT_FILE
    else:
        theme_root_file = _DEFAULT_ROOT_FILE
    css_files = [*_CSS_FILES, theme_root_file]
    css_list = [(_ROOT / file).read_text() for file in css_files]

    return "\n".join(css_list)


DEFAULT_CSS = read_fast_css(theme="default")
DARK_CSS = read_fast_css(theme="dark")


class FastStyle(param.Parameterized):
    """The FastStyle class provides the different colors and icons used to style the Fast
    Templates"""

    background_color = param.Color(default="#ffffff")
    color = param.Color(default="#00aa41")
    accent_base_color = param.Color("#E1477E")
    neutral_fill_card_rest = param.Color("#F7F7F7")
    neutral_focus = param.Color("#888888")
    neutral_foreground_rest = param.Color("#2B2B2B")
    expanded_icon = param.String(EXPANDED_SVG_ICON)
    collapsed_icon = param.String(COLLAPSED_SVG_ICON)
    font = param.String(default="Open Sans, sans-serif")
    header_color = param.Color("#ffffff")
    header_background = param.Color("#1B5E20")

    def create_bokeh_theme(self) -> Dict:
        """Returns a custom bokeh theme based on the style parameters

        Returns:
            Dict: A Bokeh Theme
        """

        return {
            "attrs": {
                "Figure": {
                    "background_fill_color": self.background_color,
                    "border_fill_color": self.neutral_fill_card_rest,
                    "border_fill_alpha": 0,
                    "outline_line_color": self.neutral_focus,
                    "outline_line_alpha": 0.5,
                    "outline_line_width": 1,
                },
                "Grid": {"grid_line_color": self.neutral_focus, "grid_line_alpha": 0.25},
                "Axis": {
                    "major_tick_line_alpha": 0,
                    "major_tick_line_color": self.neutral_foreground_rest,
                    "minor_tick_line_alpha": 0,
                    "minor_tick_line_color": self.neutral_foreground_rest,
                    "axis_line_alpha": 0,
                    "axis_line_color": self.neutral_foreground_rest,
                    "major_label_text_color": self.neutral_foreground_rest,
                    "major_label_text_font": self.font,
                    "major_label_text_font_size": "1.025em",
                    "axis_label_standoff": 10,
                    "axis_label_text_color": self.neutral_foreground_rest,
                    "axis_label_text_font": self.font,
                    "axis_label_text_font_size": "1.25em",
                    "axis_label_text_font_style": "normal",
                },
                "Legend": {
                    "spacing": 8,
                    "glyph_width": 15,
                    "label_standoff": 8,
                    "label_text_color": self.neutral_foreground_rest,
                    "label_text_font": self.font,
                    "label_text_font_size": "1.025em",
                    "border_line_alpha": 0,
                    "background_fill_alpha": 0.25,
                    # "background_fill_color": FAST_DARK_75,
                },
                "ColorBar": {
                    "title_text_color": self.neutral_foreground_rest,
                    "title_text_font": self.font,
                    "title_text_font_size": "1.025em",
                    "title_text_font_style": "normal",
                    "major_label_text_color": self.neutral_foreground_rest,
                    "major_label_text_font": self.font,
                    "major_label_text_font_size": "1.025em",
                    # "background_fill_color": FAST_DARK_75,
                    "major_tick_line_alpha": 0,
                    "bar_line_alpha": 0,
                },
                "Title": {
                    "text_color": self.neutral_foreground_rest,
                    "text_font": self.font,
                    "text_font_size": "1.15em",
                },
            }
        }


DEFAULT_STYLE = FastStyle()
DARK_STYLE = FastStyle(
    background_color="#181818",
    color="#ffffff",
    neutral_fill_card_rest="#212121",
    neutral_focus="#717171",
    neutral_foreground_rest="#e5e5e5",
)
DEFAULT_BOKEH_THEME = DEFAULT_STYLE.create_bokeh_theme()
DARK_BOKEH_THEME = DARK_STYLE.create_bokeh_theme()
