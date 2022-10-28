install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
test:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user --force-reinstall dist/*.whl