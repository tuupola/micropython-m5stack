.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Available tasks:"
	@echo "    watch  Upload changed *.py files to /pyboard automatically"
	@echo "    shell  Start an remote shell session"
	@echo "    sync   Copy all *.py files to /pyboard"
	@echo "    reset  Soft reboot the board"
	@echo "    repl   Start a repl session"
	@echo "    deps   Install dependencies with upip"
	@echo ""

watch:
	find . -name "*.py" | entr -c sh -c 'make sync && make reset'

sync:
	#rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32 cp --recursive *.py /pyboard
	rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32 rsync --mirror --verbose ./firmware  /pyboard

shell:
	rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32

repl:
	rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32 repl

reset:
	rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32 repl "~ import machine ~ machine.reset()~"

deps:
	micropython -m upip install -p firmware/lib/ micropython-ili934x

.PHONY: help watch shell repl reset sync deps
