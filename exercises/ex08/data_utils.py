"""Data Utils."""

__author__ = "730515426"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data: dict[str, list[str]], amount: int) -> dict[str, list[str]]:
    """Return an initial subset of each column's values."""
    output: dict[str, list[str]] = {}
    for key in data:
        new_values: list[str] = []
        i: int = 0
        if amount >= len(data):
            output = data
            return output
        while i < amount:
            new_values.append(data[key][i])
            i += 1
        output[key] = new_values
    return output


def select(data: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Select specific values based on column names."""
    output: dict[str, list[str]] = {}
    for name in names:
        output[name] = data[name]
    return output


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two sets of data from different sources."""
    output: dict[str, list[str]] = {}
    for key in table1:
        output[key] = table1[key]
    for key in table2:
        if key in output:
            output[key] += table2[key]
        else:
            output[key] = table2[key]
    return output


def count(initial_list: list[str]) -> dict[str, int]:
    """Produces dictionary of how many times each list element is present."""
    counted_elems: dict[str, int] = {}
    for key in initial_list:
        if key in counted_elems:
            counted_elems[key] += 1
        else:
            counted_elems[key] = 1
    return counted_elems
