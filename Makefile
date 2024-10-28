clean:
	rm -rf basespace-python-sdk-v2_protected
	rm -rf dist
	rm -rf build

build-pip-src-package:
	python setup.py sdist

build-pip-package:
	cd ./basespace-python-sdk-v2_protected;	python setup.py sdist
