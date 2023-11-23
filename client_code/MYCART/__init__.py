from ._anvil_designer import MYCARTTemplate
from anvil import *

class MYCART(MYCARTTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
