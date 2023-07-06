"""Events for :py:mod:`pyglet.window`.

See :py:class:`~pyglet.window.Window` for a description of the window event types.
"""

import sys

from pyglet.window import key
from pyglet.window import mouse


class WindowEventLogger:
    """Print all events to a file.

    When this event handler is added to a window it prints out all events
    and their parameters; useful for debugging or discovering which events
    you need to handle.

    Example::

        win = window.Window()
        event_logger = WindowEventLogger()
        win.push_handlers(event_logger)

    """
    def __init__(self, logfile=None):
        """Create a `WindowEventLogger` which writes to `logfile`.

        :Parameters:
            `logfile` : file-like object
                The file to write to.  If unspecified, stdout will be used.

        """
        if logfile is None:
            logfile = sys.stdout
        self.file = logfile

    def on_key_press(self, symbol, modifiers):
        print('on_key_press(symbol=%s, modifiers=%s)' % (
            key.symbol_string(symbol), key.modifiers_string(modifiers)), file=self.file)

    def on_key_release(self, symbol, modifiers):
        print('on_key_release(symbol=%s, modifiers=%s)' % (
            key.symbol_string(symbol), key.modifiers_string(modifiers)), file=self.file)

    def on_text(self, text):
        print('on_text(text=%r)' % text, file=self.file)

    def on_text_motion(self, motion):
        print('on_text_motion(motion=%s)' % (
            key.motion_string(motion)), file=self.file)

    def on_text_motion_select(self, motion):
        print('on_text_motion_select(motion=%s)' % (
            key.motion_string(motion)), file=self.file)

    def on_mouse_motion(self, x, y, dx, dy):
        print('on_mouse_motion(x=%d, y=%d, dx=%d, dy=%d)' % (
            x, y, dx, dy), file=self.file)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print('on_mouse_drag(x=%d, y=%d, dx=%d, dy=%d, buttons=%s, modifiers=%s)' % (
              x, y, dx, dy, mouse.buttons_string(buttons), key.modifiers_string(modifiers)),
              file=self.file)

    def on_mouse_press(self, x, y, button, modifiers):
        print('on_mouse_press(x=%d, y=%d, button=%r, modifiers=%s)' % (
            x, y, mouse.buttons_string(button), key.modifiers_string(modifiers)), file=self.file)

    def on_mouse_release(self, x, y, button, modifiers):
        print('on_mouse_release(x=%d, y=%d, button=%r, modifiers=%s)' % (
            x, y, mouse.buttons_string(button), key.modifiers_string(modifiers)), file=self.file)

    def on_mouse_scroll(self, x, y, dx, dy):
        print('on_mouse_scroll(x=%f, y=%f, dx=%f, dy=%f)' % (
            x, y, dx, dy), file=self.file)

    def on_close(self):
        print('on_close()', file=self.file)

    def on_mouse_enter(self, x, y):
        print('on_mouse_enter(x=%d, y=%d)' % (x, y), file=self.file)

    def on_mouse_leave(self, x, y):
        print('on_mouse_leave(x=%d, y=%d)' % (x, y), file=self.file)

    def on_expose(self):
        print('on_expose()', file=self.file)

    def on_resize(self, width, height):
        print('on_resize(width=%d, height=%d)' % (width, height), file=self.file)

    def on_move(self, x, y):
        print('on_move(x=%d, y=%d)' % (x, y), file=self.file)

    def on_activate(self):
        print('on_activate()', file=self.file)

    def on_deactivate(self):
        print('on_deactivate()', file=self.file)

    def on_show(self):
        print('on_show()', file=self.file)

    def on_hide(self):
        print('on_hide()', file=self.file)

    def on_context_lost(self):
        print('on_context_lost()', file=self.file)

    def on_context_state_lost(self):
        print('on_context_state_lost()', file=self.file)

    def on_draw(self):
        print('on_draw()', file=self.file)
