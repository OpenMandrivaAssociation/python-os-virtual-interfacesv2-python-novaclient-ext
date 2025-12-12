Name:		python-os-virtual-interfacesv2-python-novaclient-ext
Version:	0.20
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/o/os-virtual-interfacesv2-python-novaclient-ext/os_virtual_interfacesv2_python_novaclient_ext-%{version}.tar.gz
Summary:	Adds Virtual Interfaces support to python-novaclient
URL:		https://pypi.org/project/os-virtual-interfacesv2-python-novaclient-ext/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Adds Virtual Interfaces support to python-novaclient

%files
%{py_sitedir}/os_virtual_interfacesv2_python_novaclient_ext.py
%{py_sitedir}/os_virtual_interfacesv2_python_novaclient_ext-*.*-info
