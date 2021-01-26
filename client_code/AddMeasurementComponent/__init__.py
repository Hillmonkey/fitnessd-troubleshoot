from ._anvil_designer import AddMeasurementComponentTemplate
from anvil import *
from .. import navigation

class AddMeasurementComponent(AddMeasurementComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.weight = 0
    self.rate = 0
    self.date = None

  def button_save_click(self, **event_args):
    """This method is called when the Add Measurement button is clicked"""
    error = self.sync_data()
    if error:
      self.label_error_msg.text = error
      self.label_error_msg.visible = True
      return
    print("Would have saved the measurement: {} {} {}".format(
          self.weight, self.date, self.rate)
         )
    navigation.go_home()
    
  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    print("home-click")
    print(event_args)
    self.load_component(HomeAnonComponent())
    
  def sync_data(self):
     if not self.text_box_rate.text:
        return"Heart rate is required"
     if not self.text_box_weight.text:
        return "Weight is required."
     if not self.date_of_measurement.date:
        return "Date of measurement is required"
     self.label_error_msg.visible = False
      
     try:
      self.weight = int(self.text_box_weight.text)
      self.rate = int(self.text_box_rate.text)
      self.date = self.date_of_measurement.date
     except TypeError as te:
      return "Invalid format: Could not convert data."
     except Exception as x:
      return "Unknown error {}".format(x)
    
     return None

