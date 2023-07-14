from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

import html

import re

# Path to your `.ged` file
#file_path = 'mini.ged'
file_path = 'out.ged'

# Initialize the parser
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False) # Disable strict parsing


root_child_elements = gedcom_parser.get_root_child_elements()

parishes = dict()

förs = 0

count = 0
children_count = 0
# Iterate through all root child elements
for element in root_child_elements:

    # Is the `element` an actual `IndividualElement`? (Allows usage of extra functions such as `surname_match` and `get_name`.)
    if isinstance(element, IndividualElement):

        # Get all individuals whose surname matches "Doe"

        #if element.surname_match('Bäckstrand'):

            # Unpack the name tuple
        (first, last) = element.get_name()

        children = element.get_child_elements()

        children_count += len(children)

        # print(f"Val: {dir(element)}")
        # print(f"Val: {element.get_multi_line_value()}")

        for c in children:
            # print(c.get_tag() + " " + c.get_value())
            if c.get_tag() == "FAMC":
                # print(c.get_tag() + " " + c.get_value())
                pass
            if c.get_tag() == "SOUR":
                # print(f"---------------------------\nDATA: {c.get_value()}")

                cl = c.get_child_elements()
                for v in cl:
                    # print("SOUR:" + v.get_tag() + " " + v.get_value())

                    if v.get_tag() == "DATA":
                        for k in v.get_child_elements():
                            # print("#" + k.get_tag() + ":" + k.get_value())
                            if k.get_tag() == "TEXT":
                                totalText = k.get_value()
                                for p in k.get_child_elements():
                                    # print("%%" + p.get_tag())
                                    if p.get_tag() == "CONC":
                                        totalText += p.get_value()
                                if "Land" in totalText and "Bok" in totalText:
                                    htmlText = totalText.replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").replace("<br>", "\n").replace("\t", "\r\n")
                                    # print(htmlText)

                                    # for hit in re.finditer(r'Församling(\w+)Rad(\d+)e', htmlText):
                                    for hit in re.finditer(r'Församling([^\n]+)', htmlText):
                                        print(f"Församling: {hit.group(1)}")
                                        prsh = hit.group(1)

                                        prsh = re.sub(r'(.*)Rad(\d+)', r'\1', prsh)
                                        prsh = re.sub(r'(.*)Se hushållsmedlemmar', r'\1', prsh)
                                        prsh = re.sub(r'(.*)e hushållsmedlemmar', r'\1', prsh)
                                        if len(prsh) < 2:
                                            print("§§§§§§§§§" + hit.group(1))

                                        if prsh in parishes:
                                            parishes[prsh] += 1
                                        else:
                                            parishes[prsh] = 1
                                        förs += 1
                                    #print("§" + html.unescape(htmlText))


        if len(first) > 0 and len(last) > 9:
            # print(first + " " + last)
            count += 1

        # break
print(f"Count: {count} {children_count}")

# print(parishes)
print(förs)
for p, u in parishes.items():
    if u >2:
        print(p, u)
print(len(parishes))