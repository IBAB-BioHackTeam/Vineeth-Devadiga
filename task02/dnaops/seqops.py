# This module has functions that does basic python operations like returning the length of the DNA sequence, count each nucleotide(A,T,G,C) sequarately, count amniguous bases (anything not ATGCN), Validate DNA (valid only if base is A/T/G/C/N) returns true/false, replace invalid characters with "N", return number of purines (A+G), return number of puridines (T+C).

class SeqOps:
    def __init__(self,sequence):
        self.sequence=sequence
    @property
    def wholelength(self):
        return len(self.sequence)
    @property
    def countguanine(self):
        gcount=0
        for base in self.sequence:
            if (base)=="g" or (base)=="G":
                gcount+=1
        return gcount 
    @property
    def countadenine(self):
        acount=0
        for base in self.sequence:
            if (base)=="a" or (base)=="A":
                acount+=1
        return acount   
    @property
    def countcytosine(self):
        ccount=0
        for base in self.sequence:
            if (base)=="c" or (base)=="C":
                ccount+=1
        return ccount 
    @property
    def countthymine(self):
        tcount=0
        for base in self.sequence:
            if (base)=="t" or (base)=="T":
                tcount+=1
        return tcount 
    @property
    def countambiguousbases(self):
        nonatgccount=0
        for base in self.sequence:
            if base not in ["A","T","G","C","c","a","t","g","n","N"]:
                nonatgccount+=1
        return nonatgccount 
    @property
    def isvalid(self):
        valid=True
        for base in self.sequence:
            if base not in ["A","T","G","C","c","a","t","g","n","N"]:
                valid=False
                break
        return valid
    @property
    def countpurine(self):
        purinecount=0
        for base in self.sequence:
            if base in ["A","G","a","g"]:
                purinecount+=1
        return purinecount         
    @property
    def countpyrimidine(self):
        pyrimidinecount=0
        for base in self.sequence:
            if base in ["T","C","t","c"]:
                pyrimidinecount+=1
        return pyrimidinecount
    @property
    def replace_invalid_with_N(self):
        replaced=""
        for base in self.sequence:
            if base not in ["A","T","G","C","c","a","t","g","n","N"]:
                replaced+="n"
            else:
                replaced+=base
        return replaced.upper()

