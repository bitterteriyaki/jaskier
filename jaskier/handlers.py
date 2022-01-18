"""
MIT License

Copyright (c) 2022 Caio Alexandre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import datetime
import logging
from logging import Handler, LogRecord
from pathlib import Path
from typing import Iterable, List, Union

from rich import get_console
from rich.table import Table
from rich.highlighter import ReprHighlighter
from rich.console import ConsoleRenderable, RenderableType
from rich.text import Text
from rich.containers import Renderables


__all__ = ('JaskierHandler',)


# TODO:
# - Handle tracebacks (add custom table for tracebacks).
# - Check compatibility with Windows.
# - Add documentation.
# - Add CI/CD and probably tests.
# - Be a rockstar.


KEYWORDS = [
    'GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'PATCH'
]

LEVEL_STYLES = {
    'notset': 'dim',
    'debug': 'green',
    'info': 'blue',
    'warning': 'red',
    'error': 'bold bright_red',
    'critical': 'bold bright_red reverse',
}


class JaskierHandler(Handler):
    """
    """

    __slots__ = ('console', 'highlighter')

    def __init__(self, level: Union[str, int] = logging.NOTSET) -> None:
        super().__init__(level)

        self.console = get_console()
        self.highlighter = ReprHighlighter()

    def render_message(self, record: LogRecord) -> ConsoleRenderable:
        """
        """
        message = record.getMessage()

        text = self.highlighter(Text.from_markup(message))
        text.highlight_words(KEYWORDS, style='yellow')
        return text

    def render_log(
        self,
        message: ConsoleRenderable,
        record: LogRecord
    ) -> ConsoleRenderable:
        """
        """
        time = datetime.datetime.fromtimestamp(record.created)
        level = record.levelname
        path = Path(record.pathname).name

        renderables = [message]
        table = self._create_table(renderables, time, level, path, record)

        return table

    def _get_level_text(self, level: str) -> Text:
        return Text.styled(f'[{level}]', LEVEL_STYLES[level.lower()])

    def _create_table(
        self,
        renderables: Iterable[ConsoleRenderable],
        time: datetime.datetime,
        level: str,
        path: str,
        record: LogRecord
    ) -> Table:
        table = Table.grid(padding=(0, 1))
        table.expand = True

        # Add the log table columns.
        table.add_column(style='dim')
        table.add_column()
        table.add_column(ratio=1, overflow='fold')
        table.add_column(style='dim')

        # Now we have to add the rows for each column.
        rows: List[RenderableType] = []

        rows.append(Text(time.strftime('[%X]')))
        rows.append(self._get_level_text(level))
        rows.append(Renderables(renderables))

        ## Adding path row.
        path_text = Text()
        path_name = record.pathname
        line_no = str(record.lineno)

        path_text.append(path, style=f'link file://{path_name}')
        path_text.append(':')
        path_text.append(line_no, style=f'link file://{path_name}#{line_no}')
        rows.append(path_text)

        table.add_row(*rows)

        return table

    def emit(self, record: LogRecord) -> None:
        renderable_message = self.render_message(record)
        renderable_log = self.render_log(renderable_message, record)

        try:
            self.console.print(renderable_log)
        except Exception:
            self.handleError(record)
