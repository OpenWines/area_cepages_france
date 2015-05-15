import re
from pprint import pprint as pp
from collections import Counter
from lxml import etree
from glob import glob
from unicsv import csv

list_files = glob('output_*.xml')

for file_input in list_files:
    filename = file_input.split('.')[0]
    with open(filename + '.csv', 'wb') as csvfile:
        output_file = csv.writer(
            csvfile,
            delimiter=';',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )

        # output from pdftohtml -noframes -s -xml t_scep_fr.pdf output.xml
        doc = etree.parse(file_input)
        font_size = '5'
        if (file_input in ['output_06.xml',
                           'output_07.xml',
                           'output_08.xml',
                           'output_09.xml']):
            font_size = '0'
        text_tags = doc.xpath('//pdf2xml/page/text[@font="' + font_size + '"]')

        left_right = {
            "left": [],
            "right": []
        }

        # On devine
        vals = [tag.attrib['left'] for tag in text_tags]
        c = Counter(vals)
        couple_sep = [c.most_common()[0][0], c.most_common()[1][0]]
        if (file_input in ['output_09.xml']):
            couple_sep = ['30', '473']  # 2013

        new_tags = []
        for tag in text_tags:
            if tag.attrib['left'] in couple_sep:
                if tag.getnext() is not None and tag.getnext().attrib[
                        'left'] in couple_sep:
                    tag.text = tag.text + " " + tag.getnext().text
                    new_tags.append(tag)
                elif tag.getprevious() is not None and tag.getprevious().attrib['left'] in couple_sep:
                    pass
                else:
                    new_tags.append(tag)
            else:
                new_tags.append(tag)
        for tag in new_tags:
            if tag.attrib['left'] == couple_sep[0]:
                left_right['left'].append(tag.text)
            elif tag.attrib['left'] == couple_sep[1]:
                left_right['right'].append(tag.text)
            elif int(tag.attrib['left']) > int(couple_sep[0]) and int(
                tag.attrib['left']
            ) < int(couple_sep[1]):
                left_right['left'].append(tag.text)
            else:
                left_right['right'].append(tag.text)
        source = left_right['left']
        source = [
            i.encode('utf-8').replace(
                u'\xa0',
                ''
            ).replace(
                u' ',
                ''
            ) if re.match(
                r"^[\d \xa0]*$",
                i
            ) is not None else i.encode('utf-8').replace(
                u'%',
                ''
            ).replace(u',', '.') for i in source]

        for i in range(0, len(source)):
            if i % 3 == 0:
                line = source[i:i + 3]
                line.append('20' + filename.replace('output_', ''))
                output_file.writerow(line)
