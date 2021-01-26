from ._anvil_designer import CompareComponentTemplate
from anvil import *

class CompareComponent(CompareComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.