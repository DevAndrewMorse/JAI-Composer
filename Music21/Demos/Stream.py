# Testing a note stream
# Chapter 4:
# URL: http://web.mit.edu/music21/doc/usersGuide/usersGuide_04_stream1.html

import music21

# Create note objects
# Note: Can't repeat used objects
note_1 = note.Note("D#4")
note_2 = note.Note("F4")
note_3 = note.Note("F#4")
note_3.duration.type = 'half'

note_4 = note.Note("F4")
note_5 = note.Note("C#4")
note_6 = note.Note("F#3")
note_6.duration.type = 'half'
r1 = note.Rest(type = 'quarter')

note_7 = note.Note("D#4")
note_8 = note.Note("F4")
note_9 = note.Note("F#4")
note_9.duration.type = 'quarter'

# Create element (stream), for storing note objects
stream = stream.Stream()

# Store note objects in stream
stream.append(note_1)
stream.append(note_2)
stream.append(note_3)

stream.append(note_4)
stream.append(note_5)
stream.append(note_6)
stream.append(r1)
stream.append(note_7)
stream.append(note_8)
stream.append(note_9)


# Check stream length to test that all objects are loaded
len(stream)

# Show text output of notes
stream.show('text')

# Show sheet music of note objects
stream.show()

# Play MIDI note objects
stream.show('midi')


'''

I'll be back ;)
                    ______
                     <((((((\\\
                     /      . }\
                     ;--..--._|}
  (\                 '--/\--'  )
   \\                | '-'  :'|
    \\               . -==- .-|
     \\               \.__.'   \--._
     [\\          __.--|       //  _/'--.
     \ \\       .'-._ ('-----'/ __/      \
      \ \\     /   __>|      | '--.       |
       \ \\   |   \   |     /    /       /
        \ '\ /     \  |     |  _/       /
         \  \       \ |     | /        /
          \  \      \        /

'''
