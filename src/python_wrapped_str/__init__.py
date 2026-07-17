"""WrappedStr / string helpers (aka MutableStr in some docs/tests)."""
from python_wrapped_str.string_util import (
    CaseInsensitiveWrappedStr,
    WrappedStr,
    compare_and_format,
    first_char_diff_index,
    format_text,
    generate_diff_marker_line,
    insert_newlines,
    ireplace,
    is_non_empty_string,
    is_string_like,
    normalize_string,
    striprtf,
)

__all__ = [
    "CaseInsensitiveWrappedStr",
    "WrappedStr",
    "compare_and_format",
    "first_char_diff_index",
    "format_text",
    "generate_diff_marker_line",
    "insert_newlines",
    "ireplace",
    "is_non_empty_string",
    "is_string_like",
    "normalize_string",
    "striprtf",
]
