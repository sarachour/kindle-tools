class DiskUnit:
	BYTES = 1;
	KILOBYTES = 2;
	MEGABYTES = 3;
	GIGABYTES = 4;
	
	def __init__(self,qty,unit):
		self.unit = unit;
		self.val = qty;


   	def conv(self,units):
		unit_map = {
			1:1.0,
			2:1000.0,
			3:1000.0*1000,
			4:1000.0*1000*1000
		}
		self.val = self.val*unit_map[self.unit]/unit_map[units]
		self.unit = units;
			
	def __repr__(self):
		unit_map = {
			1:"bytes",
			2:"kb",
			3:"mb",
			4:"gb"
		}
		return str(self.val)+" "+unit_map[self.unit]

class DiskSpace:
	def __init__(self,total,free,unit):
		self.free = DiskUnit(free,unit);
		self.total = DiskUnit(total,unit);
		self.used = DiskUnit(total - free,unit);
		self.used.conv(DiskUnit.GIGABYTES);
		self.free.conv(DiskUnit.GIGABYTES);
		self.total.conv(DiskUnit.GIGABYTES);

	def __repr__(self):
		return str(self.used)+"/"+str(self.total)+"  ("+str(self.free)+" free)"

import os;

class KindleVolume:
	def __init__(self,mountpoint,phys_dev,fs_type):
		self.mnt = mountpoint;
		self.read_only = False;
		self.phys_dev = phys_dev;
		self.fstype = fs_type;

	
	def read_only(self):
		self.read_only = True;

	def set_space(self,total,free,unit):
		self.space = DiskSpace(total,free,unit);
	
	def list_files(self,reldir=None):
		if(reldir == None):
			reldir = "";
		return os.listdir(self.mnt+"/"+reldir);	

	def __repr__(self):
		s = [];
		app = lambda x : s.append(x);
		perm = "+rw"
		if self.read_only:
			perm = "+r"

		app(self.phys_dev+": "+self.mnt + "  ["+self.fstype+", "+perm+"]");
		app(str(self.space));
		return "\n".join(s);

class KindleScreen:

	def __init__(self,width,height,ppi):
		self.width = width;
		self.height = height;
		self.ppi = ppi;

	def __repr__(self):
		s = [];
		app = lambda x : s.append(x);
		app(str(self.width)+"x"+str(self.height)+" px");
		app("["+str(self.ppi)+" ppi]");

		return " ".join(s);
class KindleDevice	:
	def __init__(self):
		self.screen = KindleScreen(0,0,0);
		self.name = None;
		self.code = None;
		self.year = None;
		self.volumes = {};
		self.selected = None;
	
	def add_volume(self,vol):
		self.volumes[vol.phys_dev] = vol;

	def set_screen(self,width,height,ppi):
		self.screen= KindleScreen(width,height,ppi);
	
	def set_info(self,name,code,year):
		self.name = name;
		self.code = code;
		self.year = year;
	
	def select_volume(self,name):
		self.selected = self.volumes[name];
		return self.selected

	def get_volume(self):
		return self.selected;
	
	def __repr__(self):
		s = [];
		app = lambda x : s.append(x);
		app("["+self.code+"]: "+self.name+" ("+str(self.year)+")");
		app("screen:"+str(self.screen));
		app("volumes:");
		for vol in self.volumes:
			app(str(self.volumes[vol]))

		return "\n".join(s);

class KindleIFace:

	def __init__(self):
		self.name = "(unknown)";
		self.code = "";
		self.year = ""
	
	def apply(self,device):
		device.set_screen(self.width,self.height,self.ppi);
		device.set_info(self.name,self.code,self.year);

	def __repr__(self):	
		s = "";
		append = lambda x : s + x + "\n"
		s = append(self.name + " ("+str(self.year)+")");
		s = append(str(self.width) + "x"+ str(self.height) + " (ppi="+str(self.ppi)+")");
		s = append(str(self.device))
		return s

class Kindle(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"

class Kindle2(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"


class KindleDX(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"


class KindleKeyboard(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"


class Kindle7(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"


class Kindle4(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"

class Kindle5Touch(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"

class KindlePaperWhite(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"

class KindlePaperWhite2(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle Paper White 2"
		self.code = "kindle_paper_white_2"

class Kindle7(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle 7"
		self.code = "kindle7"


class KindleVoyage(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle Voyage"
		self.code = "kindle_voyage"


class KindlePaperWhite3(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle Paper White 3"
		self.code = "kindle_paper_white_3"
		self.year = 2015;
		self.width = 1080;
		self.height = 1440;
		self.touchscreen = True;
		self.ppi = 300;


class Kindle8(KindleIFace):
	
	def __init__(self):
		KindleIFace.__init__(self);
		self.name = "Kindle"
		self.code = "kindle"
		self.ppi = 300;

		
class KindleFactory:
	
	def add_spec(self, idlist,cls):
		for x in idlist:
			self.specs[x] = cls;

	def __init__(self):
		## TODO: This is incomplete:
		self.specs = {};
		self.add_spec(["B000"], Kindle())
		self.add_spec(["B002","B003"], Kindle2())
		self.add_spec(["B004","B005","B009"], KindleDX())
		self.add_spec(["B006","B008","B00A"], KindleKeyboard())
		self.add_spec(["B00E","B023","9023"], Kindle4())
		self.add_spec(["B00F","B010","B011","B012"], Kindle5Touch())
		self.add_spec(["B024","B01B","B01C","B01D","B01F","B020"],KindlePaperWhite())
		self.add_spec(["B0D4","90D4","B0D5"], KindlePaperWhite2())
		self.add_spec(["B001","B0C6"],Kindle7())
		self.add_spec(["B00I","B013","BO53","B054"],KindleVoyage())
		self.add_spec(["G090"],KindlePaperWhite3())
		self.add_spec(["B018"],Kindle8());
	
	def from_serial_number(self,serialnumber):
		code = serialnumber[0:4];
		return self.specs[code];

	def create(self,i,device):
		return self.from_serial_number(i).apply(device)



