from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "The Traitor"
    version = "1.0.0"
    author = "DragonEmperor"
    dependencies = ["MagmaLink", "Kolsavdur Core Mod"]

    def mod_load(self):
        ml.find_label("evilending") \
            .search_say("Not the time of dragons or man, but").hook_to("traitor_start")

    def mod_complete(self):
        pass
