from ._anvil_designer import ITEMSTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class ITEMS(ITEMSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_items()

    def load_items(self):
      items = anvil.server.call("get_item_details").search()





    



    # Any code you write here will run before the form opens.
