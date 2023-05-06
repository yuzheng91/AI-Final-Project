# AI-Final-Project
Generative AI

### Data
Contain all midi files readable from each musician

### Error
Contain midi files that occur error while reading
+ Missing Leading MTrk
  + [The track chunks (type MTrk) are where actual song data is stored](http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html#BM2_3)
+ Key error
  + Key signature message with the invalid value
  + [Key signature conversion table](https://github.com/mido/mido/blob/f23a97427a9c36a1afea4ab4d67338f4741b9edb/mido/midifiles/meta.py#L27)
+ Unable to determine instrument
