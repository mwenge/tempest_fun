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

## Tempest:T2K Edition
There is fun to be had. The 'T2K Edition' contains:
* The first 32 levels from Tempest 2000 (the original Tempest only has 16!).
* Inspiring messages after you complete each level.

[![Tempest: 2K Edition](http://img.youtube.com/vi/qDXQXmQkNSQ/0.jpg)](http://www.youtube.com/watch?v=qDXQXmQkNSQ "Tempest: 2K Edition")

To try it out you can do:

```
git checkout tempest_2k
make
```
Or you can [download it from the releases page](https://github.com/mwenge/tempest_fun/releases/edit/v0.01).

## How Does This Work?
We're creating a PDP-11 cartridge disk from the files in the [`src`](./src) directory, launching
a PDP-11 emulator, and then assembling and linking the sources on the disk. After that we copy
all the files from the emulated disk to our local system and extract the ROMs from one of those files (`ALEXEC.LDA`).
Once we have those ROMS we use `mame` to play them.

## Do You Want To Know More?
[This Related Repository](https://github.com/mwenge/tempest) has more information about the contents of the 
Tempest sources and how we turn them into working ROMs.
