"""
 ██▓ ██▓███   ▄▄▄      ▓█████▄  ▄▄▄       ██▓███  ▄▄▄█████▓▓█████  ██▀███
▓██▒▓██░  ██▒▒████▄    ▒██▀ ██▌▒████▄    ▓██░  ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒▒██  ▀█▄  ░██   █▌▒██  ▀█▄  ▓██░ ██▓▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒░██▄▄▄▄██ ░▓█▄   ▌░██▄▄▄▄██ ▒██▄█▓▒ ▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄
░██░▒██▒ ░  ░ ▓█   ▓██▒░▒████▓  ▓█   ▓██▒▒██▒ ░  ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒  ▒▒   ▓▒█░▒▓▒░ ░  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░▒ ░       ▒   ▒▒ ░ ░ ▒  ▒   ▒   ▒▒ ░░▒ ░         ░     ░ ░  ░  ░▒ ░ ▒░
 ▒ ░░░         ░   ▒    ░ ░  ░   ░   ▒   ░░         ░         ░     ░░   ░
 ░                 ░  ░   ░          ░  ░                     ░  ░   ░
                        ░
             · -—+ IPAdapter Plus Extension for ComfyUI +—- ·
             Brought to you by Matteo "Matt3o/Cubiq" Spinelli
             https://github.com/cubiq/ComfyUI_IPAdapter_plus/
"""

from .IPAdapterPlusV2 import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
class_mappings = NODE_CLASS_MAPPINGS
display_name_mappings = NODE_DISPLAY_NAME_MAPPINGS
from .layer_weights_slider import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
NODE_CLASS_MAPPINGS.update(class_mappings)
NODE_DISPLAY_NAME_MAPPINGS.update(display_name_mappings)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
