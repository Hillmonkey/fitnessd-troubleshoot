from ._anvil_designer import HomeFormTemplate
from anvil import *
from .. import navigation
import sys

class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.base_title = self.label_title.text
    navigation.home_form = self
    navigation.go_home()
    
  def link_add_click(self, **event_args):
    navigation.go_add()
    
  def link_home_click(self, **event_args):
    navigation.go_home()
      
  def link_compare_click(self, **event_args):
    navigation.go_compare()
    
  def link_account_click(self, **event_args):
    navigation.go_account()

  def link_register_click(self, **event_args):
    navigation.go_home()

  def link_login_click(self, **event_args):
    navigation.go_home()
    
  def link_logout_click(self, **event_args):
    navigation.go_home()
    
  def set_active_nav(self, state):
    self.link_home.role = "selected" if state == "home" else None
    self.link_add.role = "selected" if state == "add" else None
    self.link_compare.role = "selected" if state == "compare" else None

    
  def load_component(self, cmpt):
    #print("DEBUG: load_component")
    #print("Cmpt: "+ str(cmpt))
    self.column_panel_content.clear()
    self.column_panel_content.add_component(cmpt)







