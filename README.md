# Building Tempest for Fun

## You Will Need
.. to install a few things:
```
sudo apt install simh expect mame build-essential
```

## Now You Can Build and Play
```
make
```

Or you can just build:
```
make tempest
```

## How Does This Work?
We're creating a PDP-11 cartridge disk from the files in the [`src`](./src) directory, launching
a PDP-11 emulator, and then assembling and linking the sources on the disk. After that we copy
all the files from the disk to our local system and extract the ROMs from one of those files (`ALEXEC.LDA`).
Once we have those ROMS we use `mame` to play them.

## Do You Want To Know More?
[This Related Repository](https://github.com/mwenge/tempest) has more information about the contents of the 
Tempest sources and how we turn them into workings ROMs.
