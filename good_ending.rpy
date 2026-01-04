label good_ending:
    $ save_name = (_("Traitor - Ending B"))
    play music "mx/slowpiano.ogg"
    show logan tserious flip at left with dissolve
    lg "You do realize that what you did is treason, right? You lost us any chance of future cooperation."
    menu:
        "I know.":
            ed "Normally this would warrent execution. but you might be too useful to kill."
            c "What do you mean?"
        "I want to continue helping humanity.":
            ed "There might be a way to do so."
    ed "We have power for the hospital, but we still need help."
    ed "[player_name], can you remind me what your degree was in?"
    c "It was in biology, Sergeant."
    ed "We will let you live... on one condition."
    c "What is that condition?"
    ed "Now that we have the generator, we can power research facilities and other factories."
    ed "We're running low on antibiotics."
    show logan tthinking flip at left with dissolve
    lg "We've' had enough medicine to survive until now. But now we need the production to increase immediately."
    lg "And these antibiotics... they're complex enough that normal people cannot make them without machines."
    lg "Which we haven't had since the flare. So we need specialists."
    lg "There just aren't enough scientists to keep up with demand."
    Iz "But what about the dragons? They're about to go extinct in a couple of weeks."
    show logan tannoyed flip at left with dissolve
    lg "I don't think the dragons are willing to continue the deal anymore. Not once they find out you stole one."
    ed "I have to agree with Logan. We'll have to make the most of this one generator."
    Iz "..."
    Iz "Fine, I'll do it myself."
    hide izumi with dissolve
    show edmund flip at Move((0.5, 1.0), (1.0, 1.0), 0.5, xanchor = 1.0, yanchor = 1.0) with dissolve
    m "Izumi starts up the portal and goes to the dragons' world."
    show edmund with dissolve
    ed "Sorry about that."
    c "It's alright. I know her anyway."
    ed "Logan, do you mind showing [player_name] the factory?"
    show logan tsmiling flip at left with dissolve
    lg "No, I don't mind."
    stop music fadeout 2
    queue music "mx/movingon.ogg"
    scene kolfactory3 at Pan((0, 360), (0, 0), 4) with fade
    $ renpy.pause(4)
    c "This is the medicine factory?"
    show logan tsmiling with dissolve
    lg " Yep. Right here."
    "???" "Who's there?"
    c "It's [player_name]!"
    show logan tsmiling flip at Move((0.5, 1.0), (0.0, 1.0), 0.5, xanchor = 0.0, yanchor = 1.0) with dissolve
    show martin happy at right with dissolve
    "???" "Oh, Delta! I heard about you."
    show martin serious at right with dissolve
    "???" "Oh sorry, I forgot to introduce myself."
    Mt "My name is Martin, and I came from another city."
    lg "He came here not too long ago."
    lg "And his team has some very skilled workers."
    show martin normal at right with dissolve
    Mt "That's right. And I have some knowledge with chemistry."
    Mt "Just like you, I never thought it would be useful after the solar flare hit, but here I am."
    show logan tserious flip at left with dissolve
    lg "I'm sorry to inturrupt, but we really need those antibiotics."
    show martin serious at right with dissolve
    Mt "Oh, sorry. [player_name], we have work to do!"
    scene black with fade
    nvl clear
    window show
    play sound "mx/mindstream.ogg"
    n "And so we got to work. Me and Martin have been working with the other scientists developing medicine."
    n "Previously, there just wasn't enough energy to produce the necessary amount, so medicine had to be rationed. The factory could not run at full capacity."
    n "Now, with two new workers, and the generator, we could keep up with demand."
    n "Soon, more scientists were out of the hospital."
    n "The generator was damaged from the energy load, but by the time it gave in, there were enough people to find and produce alternative energy sources."
    window hide
    nvl clear
    window show
    $ adinedead = True
    $ annadead = True
    $ loremdead = True
    $ brycedead = True
    $ remydead = True
    $ naomidead = True
    $ sebastiandead = True
    $ maverickdead = True
    n "Unfortunately, the same cannot be said for the dragons."
    n "Izumi tried to save them, but without the underground generator, it wasn't enough."
    n "She ended up using the portal to go back in time and make yet another attempt."
    n "Maybe in another timeline, she was successful."
    n "Maybe, humanity could've gotten more if the deal went through as expected."
    n "Maybe, in another timeline, both worlds can be saved. But not in this one."
    n "But at least you managed to save one world."
    nvl clear
    window hide
    scene black with fade
    stop music fadeout 1
    $ renpy.pause(1)
    show logan smiling with dissolve
    call ml_ending_check("traitor_ending", "good", "You have seen the good ending. Humanity has a bright future ahead of them!")
    scene kolcityplaza with fade
    show logan normal with dissolve
    c "How's the progress on restoring the city?"
    lg "Our engineers are repairing and reverse engineering the generator you brought back."
    lg "Thanks to your efforts, we could save not just the city, but the entire world."
    lg "We're going to have that parade after all."
    lg "[player_name], your name will go down in history as the person who saved humanity."
    lg "Now quickly, let's get to that parade before all the good spots are taken."
    scene black with fade
    play sound "fx/system3.wav"
    s "Dev note: I don't know how to create custom credits, but I can tell you this mod was a solo project."
    s "However, it could not have been possible without Core or MagmaLink. So special thanks to the developers of those tools."
    s "And of course, credit to Saunders for the base game."
    jump ml_main_menu 