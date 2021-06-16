def add_record(data_table , entity_dict):
    a=entity_dict["uid"]
    data_table[a]=entity_dict
    return data_table


def search_record(data_table, entity_id):
    return data_table[entity_id]


def update_record(data_table, entity_id, key , value):
    if (data_table[entity_id]).has_key(key):
        data_table[entity_id][key]=value
        return data_table
    else:
        return None


def delete_record(data_table, entity_id):
    data_table.pop(entity_id)
    return data_table