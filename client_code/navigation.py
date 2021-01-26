# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
from .AddMeasurementComponent import AddMeasurementComponent
from .HomeAnonComponent import HomeAnonComponent
from .CompareComponent import CompareComponent
from .AccountComponent import AccountComponent
from .HomeDetailsComponent import HomeDetailsComponent
from .SetHeightComponent import SetHeightComponent

home_form = None

def get_form():
  if home_form is None:
    raise Exception("You must set the home form first.")
  return home_form
  
def go_add():
  set_title("Add Measurement")
  form = get_form()
  form.load_component(AddMeasurementComponent())
  form.set_active_nav("add")

def go_home():
  set_title("")
  form = get_form()
  form.load_component(HomeAnonComponent())
  form.set_active_nav("home")

def go_compare():
  set_title("Compare")
  form = get_form()
  form.load_component(CompareComponent())
  form.set_active_nav("compare")

def go_account():
  set_title("Your account")
  form = get_form()
  form.load_component(AccountComponent())
  form.set_active_nav("account")

def set_title(text):
  form = get_form()
  base_title = form.base_title
  if text:
    form.label_title.text = "".join([base_title, " - ", text])
  else:
    form.label_title.text = base_title