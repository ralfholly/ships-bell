SHELL:=/bin/bash
MIN_COVERAGE_PERCENTAGE := 100
MAKE := @$(MAKE) --quiet

.PHONY:
all:
	@$(MAKE) pylint

.PHONY:
pylint:
	@pylint3 *.py tests/*.py

.PHONY:
test:
	@$(MAKE) pylint
	@python3 -m unittest discover tests/

.PHONY:
test_cover_run:
	$(MAKE) pylint
	@python3-coverage run -m unittest discover tests/

.PHONY:
test_cover_annotate:
	@python3-coverage annotate

.PHONY:
test_cover_report:
	@python3-coverage report --fail-under $(MIN_COVERAGE_PERCENTAGE)

.PHONY:
test_cover:
	@$(MAKE) test_cover_run
	@$(MAKE) test_cover_annotate
	@$(MAKE) test_cover_report

.PHONY:
clean:
	@find \( -name "*.pyc" -o -name "*.*,cover" \) -delete


