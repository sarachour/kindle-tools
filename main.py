#!/usb/bin/python
import usb_iface

iface = usb_iface.USBInterface("pyusb");
#iface = USBInterface("python-libusb1");
iface.get_kindles();
