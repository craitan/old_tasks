

legendary_materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
trash = {}
condition = True

while condition:
    materials = input().split(' ')
    for x in range(0, len(materials), 2):
        quantity = int(materials[x])
        material = materials[x + 1]

        if material.lower() in ['shards', 'fragments', 'motes']:
            legendary_materials_dict[material.lower()] += quantity
        else:
            if material not in trash:
                trash[material.lower()] = quantity
            else:
                trash[material.lower()] += quantity


