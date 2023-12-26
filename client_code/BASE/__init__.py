from ._anvil_designer import BASETemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..HOME import HOME
from ..MYCART import MYCART

class BASE(BASETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.change_sign_in_text()
    self.content_panel.add_component(HOME())

    # Any code you write here will run before the form opens.
  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.signin.text = email
    else:
      self.signin.text = "Sign in"

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(HOME())

  def cart_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MYCART())

  def signin_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
     logout = confirm("Would you like to logout?")
     if logout:
       anvil.users.logout()
       self.content_panel.clear()
       self.content_panel.add_component(HOME())    
    else:
       anvil.users.login_with_form()
    self.change_sign_in_text()
    
