# This module has functions that can count GC content, AT content, GC content of a perticular user defined region, check for palindrome, find restriction site, find base frequency , find base percentage, first motif , all motif  and kmer breakdown

def total_gc_content(seq):
    cap_seq=seq.upper()
    gc_count=0
    length=len(cap_seq)
    for base in cap_seq:
        if base in ["G","C"]:
            gc_count+=1
    gc_content=gc_count/length*100
    return round(gc_content,4)

def total_at_content(seq):
    cap_seq=seq.upper()
    at_count=0
    length=len(cap_seq)
    for base in cap_seq:
        if base in ["A","T"]:
            at_count+=1
    at_content=at_count/length*100
    return round(at_content,4)   

def gc_content_range(seq,range_start,range_end):
    gc_count=0
    real_start=range_start-1
    real_end=range_end-1
    len=real_end-real_start +1
    for i in range(real_start,real_end+1):
        if seq[i] in ["G","C"]:
            gc_count+=1
    gc_content=gc_count/len*100
    return gc_content

def check_palindrome(seq):
    complement="" 
    for base in seq:
        if base=="A":
            complement="T"+complement
        elif base=="T":
            complement="A"+complement
        elif base=="G":
            complement="C"+complement
        elif base=="C":
            complement="G"+complement
    if complement==seq:
        print(f"{seq} is a palindromic sequence")
    else:
        print(f"{seq} is not a palindromic sequence")


def find_restriction_site_6mer(sequence):
    seq=""
    for base in sequence.upper():
        if base not in ["A","T","G","C","N"]:
            seq+="N"
        else:
            seq+=base
    complement=""
    for base in seq.upper():
        if base=="A":
            complement+="T"
        elif base=="T":
            complement+="A"
        elif base=="G":
            complement+="C"
        elif base=="C":
            complement+="G"
        else:
            complement+="N"

    ressite=False

    for i in range(len(seq)-5):
        if seq[i]==complement[i+5] and seq[i+1]==complement[i+4] and seq[i+2]==complement[i+3]:
            print(f"Restriction site found at {i+1}: {seq[i:i+6]}")
            ressite=True
    if ressite==False:
         print("There are no 6mer pallindromic restriction site in the given sequence.")

def print_base_frequency(seq):
    a=0
    t=0
    g=0
    c=0
    for base in seq.upper():
        if base=="A":
            a+=1
        elif base=="T":
            t+=1
        elif base=="G":
            g+=1
        elif base=="C":
            c+=1
    print(f"A: {a} | T: {t} | G: {g} | C: {c}")

def percent_report_base(seq):
    a=0
    t=0
    g=0
    c=0
    l=len(seq)
    for base in seq.upper():
        if base=="A":
            a+=1
        elif base=="T":
            t+=1
        elif base=="G":
            g+=1
        elif base=="C":
            c+=1
    print(f"A: {a/l*100:.6f}% | T: {t/l*100:.6f}% | G: {g/l*100:.6f}% | C: {c/l*100:.6f}%")

def first_motif(seq,motif):
    L=len(motif)
    for i in range(len(seq)+1-L):
        if seq[i:i+L]==motif:
            return i+1

def all_motif(seq,motif):
    import re
    list= re.finditer(motif,seq)
    found=False
    for m in list:
        print(m.start()+1)
        found=True
    if not found:
        print("no motif found")

def k_mer_breakdown(seq,L):
    for i in range(0,len(seq),L):
        print(seq[i:i+L])


