.PHONY: all clean

DIRS=bin/tempest

run: tempest
	mame -window -rompath bin/ tempest

tempest: sources
	$(shell mkdir -p $(DIRS))
	expect pdp11_build/tempest.exp
	./utils/extract_binary.py

sources:
	./utils/create_source_disk.py

all: run

clean:
	-rm bin/binaries/*
	-rm bin/tempest/*
