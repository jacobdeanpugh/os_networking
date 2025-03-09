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

### Command Usage:

Before scanning any files, the database must be initalized

```bash
malware_detector update
```

To scan a single file:

```
malware_detector scan --file <file_path>
```

To scan a directory:

```bash
malware_detector scan --directory <directory_path>
```

To scan a directory recursively

```bash
malware_detector scan --directory <directory_path> --recursive
```

To scan a zip file:

```
malware_detector scan --zip <zip_path> --password<Default:none>
```
