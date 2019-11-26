# Python Seed App

Inspired by [MarshalJoe](https://github.com/MarshalJoe)

This is a simple skeleton for a generic Python (3.6.5) app. It comes loaded with:

- Project automation with [tox](https://tox.readthedocs.io/en/latest/)
- Test with [pytest](https://pytest.readthedocs.io/en/latest/)
- Style with [pylint](https://pylint.readthedocs.io/en/latest/)

As well a `.gitignore`, `.pylintrc` config file, and simple directory structure employing the `src` pattern.

## Setup

Using Docker:

```bash
# build the image:
docker build -t git-processor .
# Run image:
docker run -it seed-app
```

## Testing

To find out more info about the testing configuration, check out the `tox.ini` file.

```bash
# Run the test suite
tox
# Run the linter:
tox -e lint
```

## Misc Notes

- Make sure and edit the package title in `setup.py` to reflect your app name
- If you have issue with tox and `ModuleNotFoundError`, try set `recreate` to `True` in `tox.ini`.