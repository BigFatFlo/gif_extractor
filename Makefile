UI_NAME := mainwindow
UI_CLASS := ui_$(UI_NAME).py
UI_QRC := $(UI_NAME)_rc.py

all: $(UI_CLASS) $(UI_QRC)

$(UI_CLASS): $(UI_NAME).ui
	pyside2-uic $< > $@

$(UI_QRC): $(UI_NAME).qrc
	pyside2-rcc $< > $@

clean:
	@$(RM) -f *.jpg
.PHONY: clean
