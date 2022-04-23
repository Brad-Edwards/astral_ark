#!/usr/local/bin/python3

import json

f = open("../data/oracle-cards.json")
data = json.load(f)

# Get all types and subtypes and add them to their respective files
# Generate types and subtypes code snippets
with open("../data/types.txt", "w", encoding="utf-8") as g:
    with open("../data/subtypes.txt", "w", encoding="utf-8") as h:
        with open("../data/code.txt", "w", encoding="utf-8") as i:
            types = set()
            subtypes = set()
            for card in data:
                type_lines = card["type_line"].split("//")
                for line in type_lines:
                    stripped_line = line.strip()
                    ts = stripped_line.split(" — ")
                    types.add(ts[0])
                    if len(ts) == 2:
                        subtypes.add(ts[1])

            types_list = list(types)
            types_list.sort()
            subtypes_list = list(subtypes)
            subtypes_list.sort()

            # Types
            type_constants = list()
            type_choices = list()
            for st in types:
                y = (
                    st.upper().replace(" ", "").replace("'", "").replace(",", "")
                    + " = "
                    + '"'
                    + st
                    + '"'
                )
                type_constants.append(y)
                type_choices.append("    (" + (y.split(" = "))[0] + ', "' + st + '"),')

            type_constants.sort()
            type_choices.sort()
            type_choices.insert(0, "TYPES_CHOICES = [")
            type_choices.append("]")
            type_constants.append("")
            type_code = type_constants
            type_code.extend(type_choices)

            # Subypes
            subtypes_constants = list()
            subtypes_choices = list()
            for st in subtypes:
                c = (
                    st.upper().replace(" ", "").replace("'", "").replace(",", "")
                    + " = "
                    + '"'
                    + st
                    + '"'
                )
                subtypes_constants.append(c)
                subtypes_choices.append(
                    "    (" + (c.split(" = "))[0] + ', "' + st + '"),'
                )

            subtypes_constants.sort()
            subtypes_choices.sort()
            subtypes_choices.insert(0, "SUBTYPES_CHOICES = [")
            subtypes_choices.append("]")
            subtypes_constants.append("")
            subtypes_code = subtypes_constants
            subtypes_code.extend(subtypes_choices)

            code = type_code
            code.append("")
            code.extend(subtypes_code)

            g.writelines("\n".join(types_list))
            h.writelines("\n".join(subtypes_list))
            i.writelines("\n".join(code))

f.close()
