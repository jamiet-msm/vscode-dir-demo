# Demo


Use a virtualenv. Issue the following:
```bash
python3 -m venv venv \
  && source venv/bin/activate \
  && python3 -m pip install --upgrade pip setuptools wheel \
  && pip install -r requirements.txt
```


## Pre-commit

A pre-commit config file exists in the root of this repository. Run `pip install pre-commit && pre-commit install` to get
setup with it. It is strongly advised to *not* skip this step, pre-commit is a very very useful tool.
