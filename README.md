# scEVAL
scRNA-seq benchmark for your AI coding agent

### Roadmap
1) prepare case_1 and case_0
2) prepare all bioturing cases
3) organise all books and papers and tools from scMagic repo read_me
4) implement eval metric/metrics for the dataset/ each case

### Metrics
Suggested metrics to compare how well your AI can replicate the scRNA-seq analysis:
1) some metric between two cell type annotations* (*how many cells or each type)
2) some NLP metric between research conclusions
3) expert sourced evaluation of research conclusions (note: expert can be a human or a machine)
4) 

### About the benchmark 
The benchmark is a collection of scRNA-seq datasets and their analysis. Each dataset is a case. Each case has a research question and a research conclusion. The research conclusion is a summary of the analysis of the dataset.

Dataset is a .json file that looks like this:
```python
{'case_id': 1,
 'case_name': 'Case 1: Cell type identification',
 'case_description': 'Identify cell types in a single cell RNA-seq dataset',
 'path_to_inputs': 'path/to/inputs',
 'research_question': 'What are the cell types in this dataset?',
 'research_conclusion': 'path/to/outputs',
 'source_link': 'link/to/data',
 'case_data': 'path/to/data', 
 'eval_metric': 'metric_name',}
 ```
