This repository contains scripts and data for the bioinformatic analysis used in the article "Dissecting multitrophic interactions: the relationships among Entomophthora, their dipteran hosts, and associated bacteria."
1. MultiSPLIT.py - script used for splitting amplicon reads based on the targetted marker gene
2. LSD.py - wrapper script that merges forward and reverse reads and converts them to a FASTA format based on a PHRED score of at least 30. Then, the script dereplicates, denoises, assigns taxonomy, and clusters sequences based on their 97% similarity. This results in a table with read counts, their classification to OTUs, and their taxonomic designations across the samples.
3. QUACK.py - a decontamination script that further splits sequences based on their taxonomical assignment and provides a table for further manual processing. Reads assigned as contaminants based on their presence in negative samples or by their taxonomic labels (e.g., reads coming from mitochondria, chloroplasts, archaea) are removed, while the reads of quantification spike-ins are kept for manual bacterial abundance estimation.

   Additionally, processed data was visualised using this Processing script: Barplot_visualisation_script.pyde
4. Supplementary_Tables.xlsx containing data visualized in figures.
   Supplementary table legends:
   S1_Primer_seqs - list of used primers along with their sequences, PCR setup, and PCR cycling conditions 
   S2_Collections - list of collection samples with descriptions, coordinates, and descriptions of sites and dates of collection
   S3_Specimens - list of all specimens with unique IDs, collection sites, morphology and COI-based taxonomy, COI barcode sequences, and numbers of amplicon reads in each targeted marker region
   S4_COI_zOTUs - table of COI zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S5_16S_zOTUs - table of 16S (bacterial) zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S6_18S_zOTUs - table of 18S (fungal) zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S7_ITS2_zOTUs - table of ITS2 (fungal) zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S8_emITS1_zOTUs - table of Entomophthora-specific ITS1 zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S9_emITS2_zOTUs - table of Entomophthora-specific ITS2 zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S10_emMCM7_zOTUs - table of Entomophthora-specific MCM7 zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S11_emEF1a_zOTUs - table of Entomophthora-specific EF1ɑ zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample
   S12_emRPB2_zOTUs - table of Entomophthora-specific RPB2 zOTUs with taxonomic assignment and numbers of amplicon reads for each insect sample

   
