

class IPA_LayerWeightsSlider:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "layer0": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer1": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer2": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer3": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer4": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer5": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer6": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer7": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer8": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer9": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer10": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
                "layer11": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01, "display": "slider"}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("layer_weights",)
    FUNCTION = 'ipa_layer_weights_slider'
    CATEGORY = 'ipadapter/dev'

    def ipa_layer_weights_slider(self, layer0, layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8, layer9, layer10, layer11):
        ret_str = f"0:{layer0}, 1:{layer1}, 2:{layer2}, 3:{layer3}, 4:{layer4}, 5:{layer5}, 6:{layer6}, 7:{layer7}, 8:{layer8}, 9:{layer9}, 10:{layer10}, 11:{layer11}"

        return (ret_str,)

NODE_CLASS_MAPPINGS = {
    "IPAdapterLayerWeightsSlider": IPA_LayerWeightsSlider
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IPAdapterLayerWeightsSlider": "IPAdapter Layer Weights Slider"
}