from ._anvil_designer import BASETemplate
from anvil import *
from ..HOME import HOME
from ..MYCART import MYCART

class BASE(BASETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(HOME())

    # Any code you write here will run before the form opens.

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(HOME())

  def cart_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MYCART())
