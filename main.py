import flet
from flet import (
    Page,
    TextField,
    FilledButton,
    Image,
    Row,
    IconButton,
    icons,
    theme,
    ProgressBar,
    sleep,
    icons,
    AppBar,
    Column,
    Text,
    GridView,
)
from pytube import YouTube


def main(page: Page):

    # Basic configurations
    page.title = "Flet counter example"
    page.vertical_alignment = "center"
    page.dark_theme = theme.Theme(color_scheme_seed="green")
    page.theme = theme.Theme(color_scheme_seed="green")

    # Change Theme
    def change_theme(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            themeChanger.icon = icons.LIGHT_MODE
        else:
            page.theme_mode = "light"
            themeChanger.icon = icons.DARK_MODE

        page.update()

    # Theme changer Button
    themeChanger = IconButton(icons.DARK_MODE, on_click=change_theme)

    # Define App Bar
    appbar = AppBar(
        title=Text(value="pyDown"),  # type: ignore
        center_title=True,
        actions=[themeChanger],  # type: ignore
    )
    page.appbar = appbar

    # Define url text field
    urlTextField = TextField(value="url")

    def download_video(e):
        yt = YouTube(urlTextField.value)  # type: ignore
        print(yt.title)

    page.add(
        Column(
            [
                Row(
                    [
                        urlTextField,
                        FilledButton(text="Download", on_click=download_video),
                    ],
                    alignment="center",
                ),
                Column([Text(value="fdsfsd")]),
                Column([Text(value="columna2"), Text(value="columna2")]),
                TextField(value="url"),
            ]
        )
    )

    # page.controls.append(t)
    page.update()


flet.app(target=main)
