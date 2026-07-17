# python-wrapped-str

`WrappedStr` / `CaseInsensitiveWrappedStr` and string helpers (`striprtf`, `ireplace`, etc.).

Docs/tests sometimes call this **MutableStr**; the class is an immutable `str` subclass with delegated methods.

## Install

```bash
pip install -e .
pip install git+https://github.com/bodencrouch/python-wrapped-str.git
```

## Origin

Extracted from [PyKotor](https://github.com/bodencrouch/PyKotor) `utility/string_util.py` and `utility/common/misc_string/`. Canonical API is `python_wrapped_str.string_util`; `misc_string` keeps the alternate smaller modules.

## License

LGPL-3.0-or-later
