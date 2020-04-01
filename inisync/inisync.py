import argparse
import configparser
from shutil import copyfile
from configobj import ConfigObj

# CLI options
parser = argparse.ArgumentParser(description='Sync values from a source INI file to one or more target INI files.')
parser.add_argument('source', metavar='src', type=str,
                   help='Source filename')
parser.add_argument('target', metavar='dst', type=str, nargs='+',
                   help='Target filename')
parser.add_argument('--section', '-s', metavar='section', type=str, required=True,
                   help='Sectionname in INI file')
parser.add_argument('--option', '-o', metavar='option', type=str, required=True,
                   help='Optionname in INI file')
parser.add_argument('--create', '-c', action="store_true",
                    help='Add Key in destination file if it does not exist.')
parser.add_argument('--skip-backup', action="store_true",
                    help='Skip creation of target file backups.')
args = parser.parse_args()


def main():
  source = configparser.ConfigParser()
  source.read(args.source)
  target = configparser.ConfigParser()
  target.read(args.target)

  # check source and read source value
  if not source.has_option(args.section, args.option):
    print(f'Provided option "{args.option}" in section "{args.section}" not existant in SOURCE file!')
    exit(1)
  value = source.get(args.section, args.option)
  
  # check if each target has option or create option is set
  for target_file in args.target:
    target.read(target_file)
    if not (args.create or target.has_option(args.section, args.option)):
      print(f'Provided option "{args.option}" in section "{args.section}" not existant in TARGET file!')
      exit(1)

  # update each target file
  for target_file in args.target:
    if not args.skip_backup:
      backup(target_file)
      
    print(f'Setting value "{value}" to option "[{args.section}]{args.option}" in file "{target_file}"...')
    config = ConfigObj(target_file)
    config[args.section][args.option] = value
    config.write()

  print("done.")

def backup(target_file: str):
  copyfile(target_file, target_file + '.bak')
  print("Backup file created: " + target_file + ".bak")
