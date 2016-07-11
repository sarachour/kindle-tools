
class KindleIFace:

	def __init__(self,device):
		self.device = device;
		self.width = 0;
		self.height = 0;
		self.ppi = 0;
		self.name = "(unknown)";
		self.code = "";
		self.year = ""

	def __repr__(self):	
		s = "";
		append = lambda x : s + x + "\n"
		s = append(self.name + " ("+str(self.year)+")");
		s = append(str(self.width) + "x"+ str(self.height) + " (ppi="+str(self.ppi)+")");
		return s

class Kindle(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"

class Kindle2(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"


class KindleDX(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"


class KindleKeyboard(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"


class Kindle7(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"


class Kindle4(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"

class Kindle5Touch(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"

class KindlePaperWhite(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"

class KindlePaperWhite2(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle Paper White 2"
		self.code = "kindle_paper_white_2"

class Kindle7(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle 7"
		self.code = "kindle7"


class KindleVoyage(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle Voyage"
		self.code = "kindle_voyage"


class KindlePaperWhite3(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle Paper White 3"
		self.code = "kindle_paper_white_3"
		self.year = 2015;
		self.width = 1080;
		self.height = 1440;
		self.touchscreen = True;
		self.ppi = 300;


class Kindle8(KindleIFace):
	
	def __init__(self,device):
		KindleIFace.__init__(self,device);
		self.name = "Kindle"
		self.code = "kindle"
		self.ppi = 300;

		
class KindleFactory:
	
	def add_spec(self, idlist,cls):
		for x in idlist:
			self.specs[x] = cls;

	def __init__(self)
		## TODO: This is incomplete:
		self.specs = {};
		self.add_spec(["B000"], Kindle)
		self.add_spec(["B002","B003"], Kindle2)
		self.add_spec(["B004","B005","B009"], KindleDX)
		self.add_spec(["B006","B008","B00A"], KindleKeyboard)
		self.add_spec(["B00E","B023","9023"], Kindle4)
		self.add_spec(["B00F","B010","B011","B012"], Kindle5Touch)
		self.add_spec(["B024","B01B","B01C","B01D","B01F","B020"],KindlePaperWhite)
		self.add_spec(["B0D4","90D4","B0D5"], KindlePaperWhite2)
		self.add_spec(["B001","B0C6"],Kindle7)
		self.add_spec(["B00I","B013","BO53","B054"],KindleVoyage)
		self.add_spec(["G090"],KindlePaperWhite3)
		self.add_spec(["B018"],Kindle8);
	
	def from_serial_number(self,serialnumber):
		code = serialnumber[0:4];
		return self.specs[code];

	def create(self,i,device):
		return self.from_serial_number(i)(device)



