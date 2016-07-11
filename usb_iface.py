from kindle import * 
import sys
import os 

from util import error_msg
from util import log_msg 

class LibUSB1Impl:
	name = "python-libusb1"
	
	def __init__(self):
		try:
			import usb1 
			with usb1.USBContext() as context:
				self.ctx = context;	
				self.ctx.open();	
		except ImportError:
				error_msg("you do not have the python library libusb1 installed. try 'pip install libusb1'")

 	def __test_open(self):
		if self.ctx == None:
			error_msg("you have already closed the usb interface.");
		else:
			return;

	def close(self):
		if(self.ctx != None):
			self.ctx.close();
			self.ctx = None;
		else:
			error_msg("you have attempted to close the already closed usb interface")

	def list_devices(self):
		self.__test_open();
		devices = self.ctx.getDeviceList(skip_on_error=False);
		print(str(devices))

def __load_dir_to_env(en,x):
	if not en in os.environ:
		os.environ[en] = x
		return;

	if x in os.environ[en]:
		log_msg('"'+x+'" already exists in $'+en);
	else:
		os.environ[en] += os.pathsep + x;
	


def load_bin_dir(x):
	__load_dir_to_env("DYLD_LIBRARY_PATH",x);
	__load_dir_to_env("LD_LIBRARY_PATH",x);
	print(os.environ["DYLD_LIBRARY_PATH"]);


class PyUSBDevice:
	def __init__(self,device):
		self.impl = device;

class PyUSBImpl:
	name = "pyusb"
	
	kindleFactory = KindleFactory()

	def set_debug(self,is_debug):
		if is_debug:
			os.putenv("PYUSB_DEBUG", "debug")
			os.environ["PYUSB_DEBUG"] = "debug"
		else:
			os.putenv("PYUSB_DEBUG", "")
			os.environ["PYUSB_DEBUG"] = ""
	
		print(os.getenv("PYUSB_DEBUG"));


	def __get_backend(self,backend_lib,explicit_path):
		if(backend_lib.get_backend() != None):
			return backend_lib.get_backend();
		elif (explicit_path != None):
			path = explicit_path
			load_bin_dir(path);
			backend = backend_lib.get_backend();
			print("backend",backend)
			return backend;
		else:
			return None;
			
	def __init__(self):
		self.set_debug(True);
		try:
			import usb.core
			import usb.util
			import usb.backend
		except ImportError:
			error_msg("you do not have pyusb 1.0.0 installed");
			
		try:
			import usb.backend.libusb1 as libusb1_backend
			import usb.backend.libusb0 as libusb0_backend
			backend = self.__get_backend(libusb1_backend,"/opt/local/lib/")
			if(backend == None):
				backend = self.__get_backend(libusb0_backend,None)
			if(backend == None):
				raise usb.core.NoBackendError;
			
			self.set_debug(False)
			
		except usb.core.NoBackendError:
			error_msg("pyusb could not find a backend. Please install libusb1.0 or libusb0.1.");
	
 	# gets kindle devices	
	def get_kindles(self):
		import usb.core;
		import usb.util
		dev = usb.core.find(find_all=True);
		
		kindles = [];
		for device in dev:
			manu = usb.util.get_string(device,device.iManufacturer);	
			prod = usb.util.get_string(device,device.iProduct);
			if(manu == "Amazon" and prod == "Amazon Kindle"):
				ser_num = device.iSerialNumber;
				serialnumber = usb.util.get_string(device,device.iSerialNumber)
				kindle = self.kindleFactory.create(serialnumber,PyUSBDevice(device));
				kindles.append(kindle)

		return kindles;
	
	def close(self):
		return;

	def write_file(self,kindle,path,handle):
		return None;
	
	def get_files(self,kindle):
		return [];
	

		#except usb.core.NoBackendError:
		#	error_msg("you do not appear to have libusb1 or libusb0 installed or python is having a hard time findiing it.");
			
	

class USBInterface:

	def __init__(self,kind):
		if(kind == "python-libusb1"):
			self.impl = LibUSB1Impl();
		elif(kind == "pyusb"):
			self.impl = PyUSBImpl();


	def get_kindles(self):
		return self.impl.get_kindles();

	
	def close(self):
		self.impl.close();
