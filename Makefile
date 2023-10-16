# Makefile

.PHONY: run test

CURRENT_DIR := $(CURDIR)

run:
	python $(CURRENT_DIR)/code/main.py  # Use the current directory and run main.py

test:
	pytest $(CURRENT_DIR)/tests/*

default: test run
