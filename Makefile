.PHONY: test

test:
	python3 -B -m unittest discover -s tests -v
	git diff --check
