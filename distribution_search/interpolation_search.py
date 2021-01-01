# Author: Matthew Woolley
# Email: matt.wool@live.com.au


def _interpolate_index(element, min_idx, max_idx, min_value, max_value):

    if (value_range := max_value - min_value) == 0:
        return min_idx

    normalised_interpolated_value = (element - min_value) / value_range
    delta_idx = max_idx - min_idx
    return int(normalised_interpolated_value * delta_idx) + min_idx


def _interpolation_search_recursive(
    array: list, element, min_idx: int, max_idx: int
) -> int:

    if (
        min_idx > max_idx
        or element < (min_value := array[min_idx])
        or element > (max_value := array[max_idx])
    ):
        raise ValueError(f"'{element}' is not in list")

    interpol_idx = _interpolate_index(element, min_idx, max_idx, min_value, max_value)
    interpol_val = array[interpol_idx]

    if element == interpol_val:
        while (temp_interpol_idx := interpol_idx - 1) >= 0 and array[
            temp_interpol_idx
        ] == element:
            interpol_idx = temp_interpol_idx
        return interpol_idx

    if element < interpol_val:
        return _interpolation_search_recursive(
            array, element, min_idx, interpol_idx - 1
        )
    else:
        return _interpolation_search_recursive(
            array, element, interpol_idx + 1, max_idx
        )


def interpolation_search(array: list, element) -> int:

    return _interpolation_search_recursive(array, element, 0, len(array) - 1)
