#!/usr/bin/env python
"""Tools to updates list of data."""


def update_month_index(entries, updated_entry):
    """Update the Monthly index of blog posts.

    Take a dictionaries and adjust its values
    by inserting at the right place.
    """
    new_uri = list(updated_entry)[0]
    try:
        entries[new_uri]['updated'] = updated_entry['updated']
    except Exception:
        entries.update(updated_entry)
    finally:
        return entries
