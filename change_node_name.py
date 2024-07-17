'''Change ComfyUI_IPAdapter_plus Node Name to V2
by chflame@163.com'''

import os
import glob

# py file
orig_file_name = 'IPAdapterPlus.py'
dist_file_name = 'IPAdapterPlusV2.py'
orig_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), orig_file_name)
dist_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dist_file_name)
# json files
json_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
json_file_list = glob.glob(json_path + '/*.json')


class_name_mapping_list = [
    "IPAdapter",
    "IPAdapterSimple",
    "IPAdapterAdvanced",
    "IPAdapterBatch",
    "IPAdapterFaceID",
    "IPAAdapterFaceIDBatch",
    "IPAdapterTiled",
    "IPAdapterTiledBatch",
    "IPAdapterEmbeds",
    "IPAdapterUnifiedLoader",
    "IPAdapterUnifiedLoaderFaceID",
    "IPAdapterModelLoader",
    "IPAdapterInsightFaceLoader",
    "IPAdapterEncoder",
    "IPAdapterCombineEmbeds",
    "IPAdapterNoise",
    "PrepImageForClipVision",
    "IPAdapterSaveEmbeds",
    "IPAdapterLoadEmbeds",
    "IPAdapterUnifiedLoaderCommunity",
    "IPAdapterStyleComposition",
    "IPAdapterStyleCompositionBatch",
    "IPAdapterMS",
    "IPAdapterWeights",
    "IPAdapterRegionalConditioning",
    "IPAdapterCombineParams",
    "IPAdapterFromParams",
    "IPAdapterWeightsFromStrategy",
    "IPAdapterPromptScheduleFromWeightsStrategy",
    "IPAdapterCombineWeights",
    "IPAdapterEmbedsBatch",
    "IPAdapterPreciseStyleTransfer",
    "IPAdapterPreciseStyleTransferBatch",
    "IPAdapterPreciseComposition",
    "IPAdapterPreciseCompositionBatch",
    "IPAdapterClipVisionEnhancer"
]

display_name_mapping_list = [
    "IPAdapter",
    "IPAdapter Advanced",
    "IPAdapter Batch (Adv.)",
    "IPAdapter FaceID",
    "IPAdapter FaceID Batch",
    "IPAdapter Tiled",
    "IPAdapter Tiled Batch",
    "IPAdapter Embeds",
    "IPAdapter Unified Loader",
    "IPAdapter Unified Loader FaceID",
    "IPAdapter Model Loader",
    "IPAdapter InsightFace Loader",
    "IPAdapter Encoder",
    "IPAdapter Combine Embeds",
    "IPAdapter Noise",
    "Prep Image For ClipVision",
    "IPAdapter Save Embeds",
    "IPAdapter Load Embeds",
    "IPAdapter Unified Loader Community",
    "IPAdapter Style & Composition SDXL",
    "IPAdapter Style & Composition Batch SDXL",
    "IPAdapter Mad Scientist",
    "IPAdapter Weights",
    "IPAdapter Regional Conditioning",
    "IPAdapter Combine Params",
    "IPAdapter from Params",
    "IPAdapter Weights From Strategy",
    "Prompt Schedule From Weights Strategy",
    "IPAdapter Combine Weights",
    "IPAdapter Embeds Batch",
    "IPAdapter Precise Style Transfer",
    "IPAdapter Precise Style Transfer Batch",
    "IPAdapter Precise Composition",
    "IPAdapter Precise Composition Batch",
    "IPAdapter ClipVision Enhancer"
]

def change_node_name():
    if os.path.exists(orig_file_path):
        with open(orig_file_path, "r") as f:
            content = f.read()
        for class_name in class_name_mapping_list:
            content = content.replace(f'"{class_name}":', f'"{class_name}V2":')
            content = content.replace(f'class {class_name}:', f'class {class_name}V2:')
            content = content.replace(f'class {class_name}(', f'class {class_name}V2(')
            content = content.replace(f'": {class_name},', f'": {class_name}V2,')
            content = content.replace(f'({class_name}):', f'({class_name}V2):')
            content = content.replace(f'class IPAdapterV2(nn.Module):', f'class IPAdapter(nn.Module):')

        for display_name in display_name_mapping_list:
            content = content.replace(f': "{display_name}",', f': "{display_name} V2",')

        with open(dist_file_path, 'w') as f:
            f.write(content)

        os.remove(orig_file_path)

def change_json_name():
    for i in json_file_list:
        with open(i, "r") as f:
            content = f.read()
        for class_name in class_name_mapping_list:
            content = content.replace(f'"{class_name}"', f'"{class_name}V2"')
            # print(f'replace "{class_name}" to "{class_name}V2"')
        with open(i, 'w') as f:
            f.write(content)
        print(f"Change {i} node name to V2, done.")

change_node_name()
change_json_name()