import yaml
import xml.etree.ElementTree as ET
from datetime import datetime

# Load YAML data
with open('feed.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Create RSS feed XML structure
rss = ET.Element('rss', attrib={'version': '2.0', 
'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

channel = ET.SubElement(rss, 'channel')

# Add channel elements
ET.SubElement(channel, 'title').text = data['title']
ET.SubElement(channel, 'format').text = data['format']
ET.SubElement(channel, 'subtitle').text = data['subtitle']
ET.SubElement(channel, 'itunes:author').text = data['author']
ET.SubElement(channel, 'itunes:image', {'href': data['link'] + data['image']})
ET.SubElement(channel, 'description').text = data['description']
ET.SubElement(channel, 'language').text = data['language']
ET.SubElement(channel, 'link').text = data['link']
ET.SubElement(channel, 'itunes:category', {'text': data['category']})
ET.SubElement(channel, 'lastBuildDate').text = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

# Add items to the channel
for item_data in data['item']:
    item = ET.SubElement(channel, 'item')
    ET.SubElement(item, 'title').text = item_data['title']
    ET.SubElement(item, 'itunes:author').text = data['author']
    ET.SubElement(item, 'description').text = item_data['description']
    ET.SubElement(item, 'pubDate').text = item_data['published']
    ET.SubElement(item, 'enclosure', attrib={'url': data['link'] + item_data['file'], 'type': data['format'], 'length': str(item_data['length'])})
    ET.SubElement(item, 'itunes:duration').text = item_data['duration']

# Create and write the XML file
tree = ET.ElementTree(rss)
tree.write('output_rss.xml', encoding='utf-8', xml_declaration=True)
