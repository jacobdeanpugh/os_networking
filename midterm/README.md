# Project Outline

## Introduction

### Malware Detection Software

This malware detection Software will implement

**Signature-based detection** - This method will include hashing a suspicious file and comparing it to a database of known malware hashes.

## User Guide

### Python Package Usage:

To **malware_detector** as a python package, do the following:

Setup Python Virtual Enviroment (Linux)

```bash
# Create virtual enviroment
python3 -m venv venv

# Activate virtual enviroment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

Setup Python Virtual Enviroment (Windows)

```bash
# Create virtual enviroment
python -m venv venv

#Activate virtual Enviroment
./venv/scripts/activate

#Install requirements

pip install -r requirements.txt
```

Access commands using the following

```bash
# Linux
python3 malware_dectector -h

# Windows
python malware_detector -h
```

To compile python package into executabel use the following

```bash
pyinstaller --name malware_detector --onefile --add-data "malware_detector/config.yaml:malware_detector" malware_detector/__main__.py
```

### Binary Executable (exe):

A binary executable of **malware_detector** already exists under `dist/malware_detector`

Commands can be run using the following:

```bash
./dist/malware_detector -h
```

The binary file can be moved outside inital directory for use.
