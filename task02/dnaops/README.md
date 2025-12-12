This package and modules in it contain all the basic functions for DNA 
seqops (class type)
- wholelength
- countguanine/countadenine/countcytosine/countthymine
- countambiguousbases
- isvalid
- countpurine/countpyrimidine
- replace_invalid_with_N

transform (function type)
- getcomplement(seq)
- getreverse(seq)
- getreversecomplement(seq)
- getupper_standard(seq)
- replace_base_with_complement(seq,base)

seqanalysis (function type)
- total_gc_content(seq)
- total_at_content(seq)
- gc_content_range(seq,range_start,range_end)
- check_palindrome(seq)
- find_restriction_site_6mer(sequence)
- print_base_frequency(seq)
- percent_report_base(seq)
- first_motif(seq,motif)
- all_motif(seq,motif)
- k_mer_breakdown(seq,L)
