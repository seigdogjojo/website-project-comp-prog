from ._anvil_designer import HOMETemplate
from anvil import *
from ..ITEMS import ITEMS

class HOME(HOMETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  def items_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(ITEMS())
