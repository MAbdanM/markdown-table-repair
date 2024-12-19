import re
import pandas as pd
from typing import List

def repair(markdown: str):
    # Split and clean lines
    lines = [line.strip() for line in markdown.split('\n') if line.strip()]
    
    # Ensure all rows start and end with `|`
    lines = [line if line.startswith('|') and line.endswith('|') else f"|{line.strip()}|" for line in lines]
    
    # Determine the maximum number of columns
    max_columns = max(len(line.strip('|').split('|')) for line in lines)
    
    # Process header
    header = [cell.strip() for cell in lines[0].strip('|').split('|')] if lines else []
    header.extend([''] * (max_columns - len(header)))
    header_line = '| ' + ' | '.join(header) + ' |'
    separator_line = '| ' + ' | '.join(['---'] * max_columns) + ' |'
    
    # Process data rows
    data_rows = []
    if len(lines) > 1:
        for line in lines[1:]:
            if not re.match(r'^\|[-:\s|]*\|$', line):
                cells = [cell.strip() for cell in line.strip('|').split('|')]
                cells.extend([''] * (max_columns - len(cells)))
                cells = cells[:max_columns]
                data_rows.append('| ' + ' | '.join(cells) + ' |')
    
    # Combine all parts
    repaired_table = '\n'.join([header_line, separator_line] + data_rows)
    
    return RepairedTableMarkdown(repaired_table)

class RepairedTableMarkdown:
    def __init__(self, table: str):
        self.table = table
    
    def __str__(self):
        return self.table
    
    def to_df(self) -> pd.DataFrame:
        # Split the input into lines
        lines = [line.strip() for line in self.table.split('\n') if line.strip()]

        # Extract header and data rows
        header_line = lines[0].strip('|').split('|')
        data_lines = lines[2:]  # Skip header and separator lines

        # Extract data and clean cells
        data = []
        for line in data_lines:
            cells = [cell.strip() for cell in line.strip('|').split('|')]
            # Skip empty lines
            if all(cell == '' for cell in cells):
                continue
            data.append(cells)

        # Create DataFrame
        df = pd.DataFrame(data, columns=header_line)
        return df