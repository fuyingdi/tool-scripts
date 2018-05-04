from element_screenshot import shot_element
from print_to_pdf import combine_to_pdf
import yaml

with open('target.yaml', "r") as f:
    target = yaml.load(f)
# print(target['target']
for target in target['target']:
    print('working on page %s ' % target['url'])
    shot_element(target['url'], target['element_name'])

combine_to_pdf('image')
