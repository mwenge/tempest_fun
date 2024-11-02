.PHONY: all clean

DIRS=bin/tempest

run: tempest mame
	mame -window -rompath bin/ -skip_gameinfo -beam_width_min 2.1 tempest

tempest: sources expect pdp11
	$(shell mkdir -p $(DIRS))
	cp pdp11_build/sy_clean.rk05 pdp11_build/sy.rk05
	expect pdp11_build/tempest.exp
	./utils/extract_binary.py

pdp11:
  ifeq (, $(shell which pdp11))
  $(error "pdp11 is not installed, consider doing apt-get install simh")
  endif

expect:
  ifeq (, $(shell which expect))
  $(error "expect is not installed, consider doing apt-get install expect")
  endif

mame:
  ifeq (, $(shell which mame))
  $(error "mame is not installed, consider doing apt-get install mame")
  endif

sources:
	./utils/create_source_disk.py

all: run

clean:
	-rm bin/binaries/*
	-rm bin/tempest/*
