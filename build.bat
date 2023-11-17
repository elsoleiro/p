@ECHO OFF

ECHO Starting build process
pip install --force-reinstall build && python -m build && pip install --force-reinstall dist\pmodels-0.0.0-py3-none-any.whl
