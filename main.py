import xml.etree.ElementTree as ET
import yaml

root = ET.parse("schedule.xml").getroot()


def element_to_dict(element):
    # Имя и атрибуты элемента
    result = {'name': element.tag, 'attributes': {}}

    for name, value in element.attrib.items():
        result['attributes'][name] = value

    # Дочерние элементы
    children = list(element)
    if children:
        result['children'] = [element_to_dict(child) for child in children]
    else:
        result['text'] = element.text.strip() if element.text else None

    return result


xml_dict = element_to_dict(root)

# Конвертация словаря в YAML
yaml_data = yaml.dump(xml_dict, default_flow_style=False)

# Запись YAML-данных в файл
with open('schedule.yaml', 'w') as file:
    file.write(yaml_data)