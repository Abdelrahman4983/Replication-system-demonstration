from . import model


def generate_item(block):
    msg = f"extract materials(tools, animals, items, equipments, etc.) and suppliers from this text \n\n{block}\n\n and return a json file with this shape ('Materials':[.. , ..], 'Suppliers':[.. , ..]) and be focus and consice."
    response = model.create(
        model="gpt-3.5-turbo",
        temperature = .1,
        messages=[
            {"role":"assistant", "content":msg}
        ]
    )
    return response

def suggest_item(items):
    msg = f"Based on these Items and matrials and suppliers in json file {items} suggest materials(tools, animals, items, equipments, etc.) related to these items and return suggested items as a json file with this structure ('Suggested':[.. , ..]) be focus and consice"
    response = model.create(
        model="gpt-3.5-turbo",
        temperature = .8,
        messages=[
            {"role":"assistant", "content":msg}
        ]
    )
    return response
