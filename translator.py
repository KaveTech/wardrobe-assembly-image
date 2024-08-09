def get_wardrobe(data):
    wardrobe_json = {}

    for i in data:
        if (
            data[i]["product_classification"] == "wardrobe_body_extension"
            or data[i]["product_classification"] == "wardrobe_body_base"
        ):
            design_module_index = (
                data[i]["customisation_details"]["design_module_index"] - 1
            )
            wardrobe_json[design_module_index] = {
                "width": data[i]["customisation_details"]["width"],
                "height": data[i]["customisation_details"]["height"],
            }
    return wardrobe_json


def get_components(data):
    components_json = {}

    for index, i in enumerate(data):
        if data[i]["product_classification"] == "WARDROBE_SHELF_REGULAR":
            design_module_index = (
                data[i]["customisation_details"]["design_module_index"] - 1
            )
            components_json[index] = {
                "body": design_module_index,
                "component": "shelf",
                "height": data[i]["customisation_details"]["assembly_position_Y"],
            }
        if data[i]["product_classification"] == "WARDROBE_DRAWER_SINGLE":
            design_module_index = (
                data[i]["customisation_details"]["design_module_index"] - 1
            )
            components_json[index] = {
                "body": design_module_index,
                "component": "drawer",
                "height": data[i]["customisation_details"]["assembly_position_Y"],
            }
    return components_json
