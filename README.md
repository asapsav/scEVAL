# scEVAL
scRNA-seq benchmark for your AI coding agent

Roadmap:
1) prepare case_1 
2) prepare all bioturing cases
3) organise all books and papers and tools from scMagic repo read_me 

Metrics used to compare completed scRNA-seq analysises:
1) some metric between two cell type annotations* (*how many cells or each type)
2) some NLP metric between research conclusions
3) expert sourced evaluation of research conclusions (note: expert can be a human or a machine)
4) 

Format:
a .json file that looks like this:
{'case_id': 1,
 'case_name': 'Case 1: Cell type identification',
 'case_description': 'Identify cell types in a single cell RNA-seq dataset',
 'path_to_inputs': 'path/to/inputs',
 'research_question': 'What are the cell types in this dataset?',
 'research_conclusion': 'path/to/outputs',
 'source_link': 'link/to/data',
 'case_data': '}
