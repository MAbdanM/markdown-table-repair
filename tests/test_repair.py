import unittest
from markdown_table_repair import repair

class TestMarkdownTableRepair(unittest.TestCase):
    def test_basic_repair(self):
        input_md = """| Header1 | Header2 |  Header3 |\n|---|---|---|\nValue1  | Value2 | Value3"""
        expected_md = """| Header1 | Header2 | Header3 |\n| --- | --- | --- |\n| Value1 | Value2 | Value3 |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_inconsistent_columns(self):
        input_md = """| Header1 | Header2 |\n|---|---|\nValue1  | Value2 | Value3"""
        expected_md = """| Header1 | Header2 |  |\n| --- | --- | --- |\n| Value1 | Value2 | Value3 |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_no_separator(self):
        input_md = """ Header1 | Header2 | \nValue1  | Value2 |"""
        expected_md = """| Header1 | Header2 |\n| --- | --- |\n| Value1 | Value2 |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_empty_table(self):
        input_md = """| Header1 | Header2 | Header3 |\n| --- | --- | --- |"""
        expected_md = """| Header1 | Header2 | Header3 |\n| --- | --- | --- |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_unclosed_table(self):
        input_md = """| Header1 | Header2 | Header3  \n|---|---|--- \nValue1 | Value2 | Value3"""
        expected_md = """| Header1 | Header2 | Header3 |\n| --- | --- | --- |\n| Value1 | Value2 | Value3 |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_extra_whitespace(self):
        input_md = """| Header1 |   Header2   | Header3 |\n|---|---|---|\nValue1  |  Value2  |  Value3  |"""
        expected_md = """| Header1 | Header2 | Header3 |\n| --- | --- | --- |\n| Value1 | Value2 | Value3 |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_standard_non_malformed(self):
        input_md = """| Name | Age | Country |\n| --- | --- | --- |\n| Alice | 30 | USA |\n| Bob | 25 | UK |"""
        expected_md = input_md  # No repair is needed for standard markdown
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_multiline_cells(self):
        input_md = """| Header1 | Header2 |\n|---|---|\nValue1  | This is a long value that spans multiple lines\nValue2  | Another multiline value\nValue3  | Yet another value"""
        expected_md = """| Header1 | Header2 |\n| --- | --- |\n| Value1 | This is a long value that spans multiple lines |\n| Value2 | Another multiline value |\n| Value3 | Yet another value |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_empty_cells(self):
        input_md = """| Header1 | Header2 | Header3 |\n|---|---|---|\nValue1  |  | Value3\n|  | Value2 | Value3\n| Value1 | Value2 |   |"""
        expected_md = """| Header1 | Header2 | Header3 |\n| --- | --- | --- |\n| Value1 |  | Value3 |\n|  | Value2 | Value3 |\n| Value1 | Value2 |  |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

    def test_nested_pipe_in_cell(self):
        input_md = """| Header1 | Header2 |\n|---|---|\nValue1  | This|is|nested|pipe\nValue2  | Another|nested|cell|value"""
        expected_md = """| Header1 | Header2 |  |  |  |\n| --- | --- | --- | --- | --- |\n| Value1 | This | is | nested | pipe |\n| Value2 | Another | nested | cell | value |"""
        repaired_md = repair(input_md)
        self.assertEqual(str(repaired_md), expected_md)

if __name__ == '__main__':
    unittest.main()
