# Simple INI Sync script

Small Python3 script to update a value from a given source ini file to one or many target ini files.

# Installation

```
pip3 install inisync
```

# Skrip without pip module installation
If you do not want to use the the module, you can download the script from the release page and use it this way:

Download link: [Latest release](https://github.com/wody/inisync/releases/latest/download/inisync.py)

```
python3 inisync.py
```

# Usage

Sync values from a source INI file to one or more target INI files.

```
Sync values from a source INI file to one or more target INI files.

positional arguments:
  src                   Source filename
  dst                   Target filename

optional arguments:
  -h, --help            show this help message and exit
  --section sec, -s sec
                        Sectionname in INI file
  --key key, -k key     Keyname in INI file
  --create, -c          Add Key in destination file if it does not exist.
  --skip-backup         Skip creation of target file backups.
```

To sync to value of key `user` in section `database` from file `a.ini` to `b.ini` you would call:
```
inisync -s database -k user a.ini b.ini
```
