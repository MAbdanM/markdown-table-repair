[![PyPI](https://img.shields.io/pypi/v/markdown-table-repair)](https://pypi.org/project/markdown-table-repair/)
![Python version](https://img.shields.io/badge/python-3.8+-important)

# 🛠️ Markdown Table Repair
```markdown-table-repair``` is a Python package designed to repair and clean malformed Markdown tables and convert them into structured pandas DataFrames. Large language models (LLMs) often generate tables with inconsistent formatting, making it difficult to use the data directly. This package helps by cleaning and structuring these tables into usable DataFrames.

# ✨ Supported Broken Markdown Table Format
- Inconsistent column and header count
```
Header1 | Header2 | 
|---|---|
Value1  | Value2 | Value3
```
- Improperly formatted header 
```
| Header1 | Header2 | Header3  
|---|---|---  
Value1 | Value2 | Value3 |
```
- Missing separator
```
| Header1 | Header2 | Header3
Value1 | Value3
```  
- Unclosed table blocks
```
| Header1 | Header2 | Header3  
|---|---|--- 
Value1 | Value2 | Value3
```
- No separator in header row
```
 Header1 | Header2 | 
 |---|---|
  Value1  | Value2 | Value3
```
- Unnecessary whitespaces
- etc.

# 🔧 Usage
To use the markdown-table-repair package, follow these steps:
1. **Install the Package**
Before using markdown-table-repair, ensure that ```pandas``` is installed.
```
pip install markdown-table-repair  
```
2. **Repair Malformed Tables**
```
import markdown_table_repair as mtr

malformed_table = """| Header1 | Header2 |  Header3 \n|---|---|\n Value1  | Value2 | Value3"""
repaired_table = mtr.repair(malformed_table)
print(repaired_table)
```
3. **Optional - Convert to DataFrame**
```
# If you want to convert the repaired table into a pandas DataFrame

dataframe = repaired_table.to_df()
```
# 🤝 Contributing
Your contributions to this project are welcome! Feel free to fork the repository, create pull requests, and help improve the markdown-table-repair package.

# 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
