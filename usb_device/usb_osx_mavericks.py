import subprocess
from xml.dom import minidom
import dateutil.parser

def parse_node(child):
	get_value = lambda n : n.firstChild.nodeValue
	
	if child.tagName == "string":
		return get_value(child);
	elif child.tagName == "true":
		return True
	elif child.tagName == "integer":
		return int(get_value(child))
	elif child.tagName == "real":
		return float(get_value(child))
	elif child.tagName == "date":
		return dateutil.parser.parse(get_value(child))
	elif child.tagName == "array":
		lst = [];
		for ch in child.childNodes:
			if ch.nodeType == ch.ELEMENT_NODE:
				lst.append(parse_node(ch))
		return lst;
		
	elif child.tagName == "dict":
		key = None;
		dct = {};
		for ch in child.childNodes:
			if ch.nodeType == ch.ELEMENT_NODE:
				if ch.tagName == "key":
					key = get_value(ch);
				else:
					dct[key] = parse_node(ch)
		return dct;
	else:
		print("??? Node")
		print(child);
		return None;


import kindle
kindleFactory = kindle.KindleFactory();

def node_to_kindle(node):
	to_fs = {};
	to_fs["MS-DOS FAT32"] = "fat32";


	dev =  kindle.KindleDevice();
	snum = node["serial_num"];
	kindleFactory.create(snum,dev)

	for json_vol in node["volumes"]:
		volume = kindle.KindleVolume( json_vol["mount_point"], json_vol["bsd_name"],to_fs[json_vol["file_system"]]);
		volume.set_space(json_vol["size_in_bytes"],json_vol["free_space_in_bytes"],kindle.DiskUnit.BYTES);
		if json_vol["writable"] == "no":
			volume.read_only();
		dev.add_volume(volume);
	print(repr(dev))
	return dev;
		
class OSXMavericksUSBDeviceInterface:
	
	def init(self):
		cmd = ["system_profiler","-xml","SPUSBDataType"]
		results = subprocess.check_output(cmd);
		result_obj = minidom.parseString(results);
		nodes = result_obj.getElementsByTagName("dict")
		nodes_dict = map(parse_node,nodes)
		self.kindles = [];
		for node in nodes_dict:
			if "_name" in node and node["_name"] == "Amazon Kindle":
				self.kindles.append(node_to_kindle(node));
	
	def get_kindles(self):
		return self.kindles

	def __init__(self):
		self.init();

osx = OSXMavericksUSBDeviceInterface()

kindles = osx.get_kindles();
kindle = kindles[0];
vol = kindle.select_volume("disk2s1");
files = vol.list_files();
for f in files:
	print(f)

print("=======");
files = vol.list_files("documents");

for f in files:
	print(f)


