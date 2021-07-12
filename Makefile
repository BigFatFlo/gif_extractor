UI_NAME := mainwindow
UI_CLASS := ui_$(UI_NAME).py

all: $(UI_CLASS) $(UI_QRC)

$(UI_CLASS): $(UI_NAME).ui
	pyside2-uic $< > $@

clean:
	@$(RM) -f *.jpg
.PHONY: clean
