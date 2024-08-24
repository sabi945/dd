import difflib

asci = "apple bagus"
bass = "a bagus"

hasil = difflib.SequenceMatcher(None,asci,bass)
hasill_1 = hasil.ratio()
print(hasill_1)