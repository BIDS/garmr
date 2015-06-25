import morepath
from more.static import StaticApp
import bowerstatic

class App(StaticApp):
    pass

bower = bowerstatic.Bower()

components = bower.components(
  'components',
  bowerstatic.module_relative_path('bower_components'))

local = bower.local_components('local', components)

local.component(bowerstatic.module_relative_path('static'), version=None)

@App.static_components()
def get_static_components():
    return local

def main():
   morepath.autosetup()
   wsgi = App()
   morepath.run(wsgi)