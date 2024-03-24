### Tokenizes Uniprot sequences using Q4SS data from AlphaFold ###

import json
import urllib.request

ss_types = ["BEND", "HELX", "STRN", "TURN"]

def getAFsentence(uniprotAC):

    url = "https://rest.uniprot.org/uniprotkb/search?query=" + uniprotAC + "&fields=cc_function"
    with urllib.request.urlopen(url) as url:
        uniprot = json.load(url)
    try:
        func = uniprot["results"][0]["comments"][0]["texts"][0]["value"]

        # AF url for API request
        url = "https://alphafold.ebi.ac.uk/api/prediction/" + uniprotAC + "?key=AIzaSyCeurAJz7ZGjPQUtEaerUkBZ3TaBkXrY94"
        
        # Get sequence/CIF-url from alphafold.ebi.ac.uk
        with urllib.request.urlopen(url) as url:
            alphaDB = json.load(url)
        seq = alphaDB[0]['uniprotSequence']
        cifUrl = alphaDB[0]['cifUrl']
        
        # Get CIF file from alphafold.ebi.ac.uk
        alphaCif = urllib.request.urlopen(cifUrl)
        # Create residue index for sentence splitting
        sent_idx = []
        for line in alphaCif:
            line = line.decode()
            # Begin extraction of DSSP information
            for ss in ss_types:
                if ss in line and "DSSP" not in line:
                    sent_idx.append(int(line.split(" ")[2]))

        # Split sequence by DSSP index
        sent = [seq[i:j] for i,j in zip([0] + sent_idx, sent_idx + [None])]
        # Convert list to space-separated string
        return " ".join(sent), func

    except IndexError:
        return "Protein function not yet annotated on UniProt"
    

def getUniprotFunc(uniprotAC):
    url = "https://rest.uniprot.org/uniprotkb/search?query=" + uniprotAC + "&fields=cc_function"
    with urllib.request.urlopen(url) as url:
        uniprot = json.load(url)
    try:
        func = uniprot["results"][0]["comments"][0]["texts"][0]["value"]
        return func
    except IndexError:
        return "Protein function not yet annotated on UniProt"
