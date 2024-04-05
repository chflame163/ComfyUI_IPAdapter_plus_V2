'''Change ComfyUI_IPAdapter_plus Node Name to V2
by chflame@163.com'''

import os

orig_file_name = 'IPAdapterPlus.py'
dist_file_name = 'IPAdapterPlusV2.py'
orig_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), orig_file_name)
dist_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dist_file_name)

with open(orig_file_path, "r") as f:
    content = f.read()

class_name_mapping_list = [
    "IPAdapter","IPAdapterSimple",
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
]

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