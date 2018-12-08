from music21 import *

# Testing chord outputs

# Middle C chord
c_Chord = chord.Chord("C4 E4 G4")

# Sheet music ouput
c_Chord.show()

# MIDI ouput
c_Chord.show('midi')

# Print chord
print(c_Chord)

# Loop through each note in chord
for note in c_Chord:
	print(note)
	
