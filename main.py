#!/usb/bin/python
import usb_iface

iface = usb_iface.USBInterface("pyusb");
#iface = USBInterface("python-libusb1");
kindles = iface.get_kindles();
print(kindles)
iface.close();
