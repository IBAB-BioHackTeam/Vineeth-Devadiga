from dnaops.seqops import SeqOps

myseq1 =SeqOps("atgctatacgrnrtgacagt")
print(myseq1.isvalid)
print(myseq1.countcytosine)
print(myseq1.countambiguousbases)
print(myseq1.countguanine)
print(myseq1.wholelength)
from dnaops import seqanalysis as sa

sa.k_mer_breakdown("ATAGTGCATGCATCGATAGCTA",3)

print(sa.first_motif("ATGCATGCATGCATGCCCC","ATGC"))

print(sa.all_motif("ATGCATGAGTAAGAGAGAGATAGCATATG","ATG"))

print(sa.total_gc_content("ATCGCGCCGCGCGCGCGGCGCGCGCGCGCGCGCG"))

print(sa.total_at_content("ATCGCGCCGCGCGCGCGGCGCGCGCGCGCGCGCG"))

sa.print_base_frequency("atgctacactcgtgatgctgactgctgactgcatgactgcatgactgactgcatgctgactgactgact")

sa.percent_report_base("atcgatcgtcaaaaaaaaaaatgactgcatgactgactgcatgactg")

seqres="ATGCATNNNNNNNGCTGTGACAGATGACACAGTCGCTGACGCTGTACGCTGACGCTGACACGCTGCTGATCNGCATNNat"

print(sa.find_restriction_site_6mer(seqres))

print(sa.gc_content_range("ATATATATATTATATTAT",1,10))

print(sa.gc_content_range("CGCGCGGCGCGCGCGCGGCGCGCGCG",1,10))

print(sa.gc_content_range("ATGCATGCATGCATGC",1,5))

sa.check_palindrome("ATGCAT")


from dnaops import transform as tr

ex="ATGATGACAGATCAGATNAGATCANNNNNATGACGTAC"
print(tr.getreverse(ex))
print(tr.getcomplement(ex))
print(tr.getreversecomplement(ex))
print(tr.getupper_standard(ex))
print(tr.replace_base_with_complement(ex,"A"))

