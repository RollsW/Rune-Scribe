# Rune_Scribe
A short python script that translates English (Latin) characters into Anglo Saxon Runes.

The script is a super-simple dict, with a function front end. 

    #set up a text string with whatever we want to convert
     
    text = '''Where now the horse and the rider? Where is the horn that was blowing? 
    Where is the helm and the hauberk, and the bright hair flowing? 
    Where is the hand on the harpstring, and the red fire glowing? 
    Where is the spring and the harvest and the tall corn growing? 
    They have passed like rain on the mountain, like a wind in the meadow; 
    The days have gone down in the West behind the hills into shadow. 
    Who shall gather the smoke of the dead wood burning, 
    Or behold the flowing years from the Sea returning?'''

    # drop it into the function
    runify(text)

    # output
    ᚹᚻᛖᚱᛖ᛫ᚾᚩᚹ᛫ᚦᛖ᛫ᚻᚩᚱᛋᛖ᛫ᚪᚾᛞ᛫ᚦᛖ᛫ᚱᛁᛞᛖᚱ ᛭ ᚹᚻᛖᚱᛖ᛫ᛁᛋ᛫ᚦᛖ᛫ᚻᚩᚱᚾ᛫ᚦᚪᛏ᛫ᚹᚪᛋ᛫ᛒᛚᚩᚹᛝ ᛭ 
    ᚹᚻᛖᚱᛖ᛫ᛁᛋ᛫ᚦᛖ᛫ᚻᛖᛚᛗ᛫ᚪᚾᛞ᛫ᚦᛖ᛫ᚻᚪᚢᛒᛖᚱᛣ ᛬ ᚪᚾᛞ᛫ᚦᛖ᛫ᛒᚱᛁᚸᛏ᛫ᚻᚪᛁᚱ᛫ᚠᛚᚩᚹᛝ ᛭ 
    ᚹᚻᛖᚱᛖ᛫ᛁᛋ᛫ᚦᛖ᛫ᚻᚪᚾᛞ᛫ᚩᚾ᛫ᚦᛖ᛫ᚻᚪᚱᛈᛋᛏᚱᛝ ᛬ ᚪᚾᛞ᛫ᚦᛖ᛫ᚱᛖᛞ᛫ᚠᛁᚱᛖ᛫ᚷᛚᚩᚹᛝ ᛭ 
    ᚹᚻᛖᚱᛖ᛫ᛁᛋ᛫ᚦᛖ᛫ᛋᛈᚱᛝ᛫ᚪᚾᛞ᛫ᚦᛖ᛫ᚻᚪᚱᚡᛖᛋᛏ᛫ᚪᚾᛞ᛫ᚦᛖ᛫ᛏᚪᛚᛚ᛫ᚳᚩᚱᚾ᛫ᚷᚱᚩᚹᛝ ᛭ 
    ᚦᛖᚣ᛫ᚻᚪᚡᛖ᛫ᛈᚪᛋᛋᛖᛞ᛫ᛚᛁᛣᛖ᛫ᚱᚪᛁᚾ᛫ᚩᚾ᛫ᚦᛖ᛫ᛗᚩᚢᚾᛏᚪᛁᚾ ᛬ ᛚᛁᛣᛖ᛫ᚪ᛫ᚹᛁᚾᛞ᛫ᛁᚾ᛫ᚦᛖ᛫ᛗᛠᛞᚩᚹ ᛬ 
    ᚦᛖ᛫ᛞᚪᚣᛋ᛫ᚻᚪᚡᛖ᛫ᚷᚩᚾᛖ᛫ᛞᚩᚹᚾ᛫ᛁᚾ᛫ᚦᛖ᛫ᚹᛖᛋᛏ᛫ᛒᛖᚻᛁᚾᛞ᛫ᚦᛖ᛫ᚻᛁᛚᛚᛋ᛫ᛁᚾᛏᚩ᛫ᛋᚻᚪᛞᚩᚹ ᛭ 
    ᚹᚻᚩ᛫ᛋᚻᚪᛚᛚ᛫ᚷᚪᚦᛖᚱ᛫ᚦᛖ᛫ᛋᛗᚩᛣᛖ᛫ᚩᚠ᛫ᚦᛖ᛫ᛞᛠᛞ᛫ᚹᚩᚩᛞ᛫ᛒᚢᚱᚾᛝ ᛬ 
    ᚩᚱ᛫ᛒᛖᚻᚩᛚᛞ᛫ᚦᛖ᛫ᚠᛚᚩᚹᛝ᛫ᚣᛠᚱᛋ᛫ᚠᚱᚩᛗ᛫ᚦᛖ᛫ᛋᛠ᛫ᚱᛖᛏᚢᚱᚾᛝ ᛭ 

