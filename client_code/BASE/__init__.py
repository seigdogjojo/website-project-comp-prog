from ._anvil_designer import BASETemplate
from anvil import *
from ..HOME import HOME
class BASE(BASETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(HOME())

    # Any code you write here will run before the form opens.