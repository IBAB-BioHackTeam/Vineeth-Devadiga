# This module has functions to do task like finding the complement, reverse, reverse complement, convert to uppercase and standerdize (atgcn only)

def getcomplement(seq):
    complement=""
    for base in seq:
        if base.upper()=="A":
            complement+="T"
        elif base.upper()=="T":
            complement+="A"
        elif base.upper()=="G":
            complement+="C"
        elif base.upper()=="C":
            complement+="G"
        else:
            complement+=base
    return complement

def getreverse(seq):
    return "".join(reversed(seq))

def getreversecomplement(seq):
    complement=""
    for base in seq:
        if base.upper()=="A":
            complement+="T"
        elif base.upper()=="T":
            complement+="A"
        elif base.upper()=="G":
            complement+="C"
        elif base.upper()=="C":
            complement+="G"
        else:
            complement+=base
    return "".join(reversed(complement))

def getupper_standard(seq):
    standard=""
    for base in seq.upper():
        if base not in ["A",'T',"G",'C',"N"]:
            standard+="N"
        else:
            standard+=base
    return standard.upper()

def replace_base_with_complement(seq,base):
    replaced=""
    complement_base=""
    if base.upper()=="A":
        complement_base+="T"
    elif base.upper()=="T":
        complement_base=="A"
    elif base.upper()=="G":
        complement_base=="C"
    elif base.upper()=="C":
        complement_base=="G"
    else:
        complement_base=="N"
    for nucleotide in seq.upper():
        if nucleotide == base:
            replaced+=complement_base
        else:
            replaced+=nucleotide
    return

