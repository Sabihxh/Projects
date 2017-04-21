def _create_label_value_structure(cell):

    """
    Create the following structure assuming that label can be missing
    +-----+-----+
    |Label|Value|
    +-----+-----+
    |     |     |
    +-----+-----+

    Input could be: 'label: value; label:value; value; value; ...'
    Output should be: 'label<c>value<r>label<c>value<r><c>value<r><c>value ...'
     """
    rows = []
    for row in (cell or '').split(';'):
        columns = [column.strip() for column in row.split(':')]
        cleaned_columns = []

        for col in columns:
            if col:
                cleaned_columns.append(col)
        columns = cleaned_columns

        if len(columns) == 1 and columns[0]:
            if row.find(':') > -1:
                if row.find(columns[0]) > row.find(':'):
                    # push value to the 2nd column = no label but value is present
                    columns = ['',] + columns
                else:
                    ## else: if there is a label and a colon - do not add this to results
                    ##columns = []
                    pass
            else:
                columns = ['',] + columns

        rows.append('<c>'.join(columns))
    resulting_structure = '<r>'.join(rows)
    return resulting_structure or ''


print _create_label_value_structure('yea, Okaaayy, yeaaaa <r> test <c> ing')








