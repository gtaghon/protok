### Tokenizes Uniprot sequences using Q4SS data from AlphaFold ###
import json
import urllib.request

ss_types = ["BEND", "HELX", "STRN", "TURN"]

def getAFsentence(uniprotAC):
    url = f"https://rest.uniprot.org/uniprotkb/search?query={uniprotAC}&fields=cc_function"

    with urllib.request.urlopen(url) as url:
        uniprot = json.load(url)

    try:
        func = uniprot["results"][0]["comments"][0]["texts"][0]["value"]
    except (IndexError, KeyError):
        return "Protein function not yet annotated on UniProt", None

    af_url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprotAC}?key=AIzaSyCeurAJz7ZGjPQUtEaerUkBZ3TaBkXrY94"

    with urllib.request.urlopen(af_url) as url:
        alphaDB = json.load(url)

    seq = alphaDB[0]['uniprotSequence']
    cif_url = alphaDB[0]['cifUrl']

    with urllib.request.urlopen(cif_url) as cif:
        sent_idx = []
        for line in cif:
            line = line.decode()
            for ss in ss_types:
                if ss in line and "DSSP" not in line:
                    sent_idx.append(int(line.split(" ")[2]))

        sent = [seq[i:j] for i, j in zip([0] + sent_idx, sent_idx + [None])]
        tokenized_seq = " ".join(sent)

    return tokenized_seq, func
