# protok
A tokenizer for protein amino acid sequences based on DeepMind-computed secondary structure.

## Functions:
* getAFsentence(uniprotAC):
returns secondary structure tokenization and uniprot functional annotation for protein with given UniProtAC (accession code)

### Example usage:
```python
from alpha_cif_parse import getAFsentence()
getAFsentence("P00686")
```
output:
```python
('ETP AEKFQRQHM DT EHS TASS S NY CNLMMKAR DMT SGRCKP L NTFIHE PK SVVDA VCHQ E NVTCK NG RT NC YKSN SRL SITNCRQTG ASK Y PN CQY ETSNLNKQI IVACEG QYV PVHFDAYV', "Endonuclease that catalyzes the cleavage of RNA on the 3' side of pyrimidine nucleotides. Acts on single-stranded and double-stranded RNA (By similarity)")
```
