PY ?= python
LAB ?= lab00

.PHONY: list status grade handin

list:
	$(PY) tools/course.py list

status:
	$(PY) tools/course.py status

grade:
	$(PY) tools/course.py grade $(LAB)

handin:
	$(PY) tools/course.py handin $(LAB)

