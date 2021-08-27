#!/usr/bin/env python3
##################
# CompareTwoSets #
##################
ver = 1.0
print(f"--- CompareTwoSets {ver} ---")
# First Set
Set1Label = input("Enter a name for the first set: [Set1] ") or "Set1"
Set1file = input("Enter a filename for {}: [Set1.txt] ".format(Set1Label)) or "Set1.txt"
Set1 = set(line.strip() for line in open(Set1file))
# Second Set
Set2Label = input("Enter a name for the second set: [Set2] ") or "Set2"
Set2file = input("Enter a filename for {}: [Set2.txt] ".format(Set2Label)) or "Set2.txt"
Set2 = set(line.strip() for line in open(Set2file))
# Do diff
Set1DiffSet2 = Set1.difference(Set2)
Set2DiffSet1 = Set2.difference(Set1)
# Print counts
print(f"\n{Set1Label} contains {len(Set1)} items.\n{Set2Label} contains {len(Set2)} items.\nDelta: {len(Set1) - len(Set2)}\n")
# Sets to CSVs
Set1DiffSet2CSV = ', '.join(Set1DiffSet2)
Set2DiffSet1CSV = ', '.join(Set2DiffSet1)
# Print diff
print(f"{Set1Label} items not in {Set2Label} ({len(Set1DiffSet2)}):\n {Set1DiffSet2CSV}\n")
print(f"{Set2Label} items not in {Set1Label} ({len(Set2DiffSet1)}):\n {Set2DiffSet1CSV}\n")
