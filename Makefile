.PHONY: all clean

DIRS=bin/tempest

run: tempest
  ifeq (, $(shell which mame))
  $(error "mame is not installed, consider doing apt-get install mame")
  endif
	mame -window -rompath bin/ tempest

tempest: sources
	$(shell mkdir -p $(DIRS))
  ifeq (, $(shell which pdp11))
  $(error "pdp11 is not installed, consider doing apt-get install simh")
  endif
  ifeq (, $(shell which expect))
  $(error "expect is not installed, consider doing apt-get install expect")
  endif
	expect pdp11_build/tempest.exp
	./utils/extract_binary.py

sources:
	./utils/create_source_disk.py

all: run

clean:
	-rm bin/binaries/*
	-rm bin/tempest/*
