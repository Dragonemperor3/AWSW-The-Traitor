label best_ending:
    $ save_name = (_("Traitor - Ending A"))
    play music "mx/hope_kol.ogg"
    c "Wait."
    show logan tserious flip at left with dissolve
    lg "What is it?"
    c "I have an idea."
    c "We still have a stockpile of weapons, and a generator to power the portal."
    ed "Your point being?"
    c "We might be able to repair our relationship with the dragons."
    show logan tsurprised flip at left with dissolve
    lg "You dont mean...?"
    c "Oh, but I do."
    c "If we can destroy the comet for them, we might have a chance at continuing the deal."
    ed "I think I get what you're saying."
    show logan tnormal flip at left with dissolve
    ed "We have a nuclear arsenal that has never been used. We might be able to help the dragons redirect an asteroid."
    show logan tserious flip at left with dissolve
    lg "But won't the radiation destroy their electronics, the same way the sun destroyed ours?"
    c "Maybe we can find a way around that. They have no satellites, so we only need to protect ground infrastructure."
    show logan tthinking flip at left with dissolve
    lg "It's worth a try. We have nothing to lose."
    lg "How much time do we have?"
    c "Around 2 weeks."
    show logan tserious flip at left with dissolve
    lg "Delta, we're sending you back to tell them the plan."
    ed "We'll send the bombs through tonight. Good luck."
    $ renpy.pause(2)
    jump plan

label plan:
    scene np1x at Pan((569, 360), (569, 0), 4) with fade
    $ renpy.pause(4)
    if brycedead == True or sebastiandead == True: #should not be dead, but a failsafe just in case
        s "You should not be seeing this. Make sure Bryce and Sebastian are alive before getting this ending. Ideally with a bad relationship."
        jump ml_main_menu
    else:
        show bryce sad b with dissolve
        Br "[player_name]? You didn't come back to call me fat again, did you?" 
        #it might not be possible to get the evil ending with a neutral relationship, but the mod still assumes the relationship is bad
        Br "Or take more generators from us?"
        c "Actually no, I'm here to tell you something urgent."
        show bryce brow b with dissolve
        Br "This better be important."
        c "You know about the comet right?"
        show bryce normal b with dissolve
        Br "You mean the one that's going to pass us?"
        c "Actually it won't. It's going right towards us unless we redirect it."
        show bryce laugh b with dissolve
        Br "Ha! Good one! You'd think I'd listen to you after what happened?"
        c "If you don't believe me, point my PDA to the sky."
        show bryce stern b with dissolve
        Br "Maybe you are telling the truth. If you wanted to steal more generators, you wouldn't have come up to me."
        Br "You need to tell the council about this immediately."
        Br "But you will constantly need an escort. We're not letting you off on your own again."
        Br "Sebastian! Come here!"
        show bryce at Move((0.5, 1.0), (1.0, 1.0), 0.5, xanchor = 1.0, yanchor = 1.0) with dissolve
        $ renpy.pause(1)
        show sebastian normal b flip at left with dissolve
        Sb "Yes, chief?"
        Br "Guide [player_name] to Emera's office."
        show sebastian drop b flip at left with dissolve
        Sb "Wh- why are they here?"
        Br "They say they have important news about the comet."
        scene corridor with fade
        m "Well, this is it. Emera's office."
        play sound "fx/knocking1.ogg"
        $ renpy.pause(2)
        Em "Come in!"
        play sound "fx/door/door_open.wav"
        scene emeraroom with fade
        show emera ques at right with dissolve
        show sebastian normal b flip at left with dissolve
        Em "Well, I certainly wasn't expecting [player_name] to come back."
        Sb "They must have an escort to prevent a repeat of what they did the night of the fireworks."
        Em "Sebastian, please wait outside my office. This is a matter between us two."
        Sb "Alright."
        hide sebastian with dissolve
        show emera ques at Move((1.0, 1.0), (0.5, 1.0), 0.5, xanchor = 0.5, yanchor = 1.0) with dissolve
        Em "So, tell me, why are you here?"
        c "That's what I was about to tell you."
        c "That comet will not pass us. It is actually headed right towards us."
        show emera frown with dissolve
        Em "Even if what you say is true, We could not deflect it without the underground generator."
        c "That's why we're sending the one thing we have an abundence of to help."
        show emera ques with dissolve
        Em "And what would that be?"
        c "Hydrogen bombs. We can combine them with the generators you do have to deflect the asteroid. They should come through tonight, through the portal."
        c "I would also suggest protecting the more valuable electronics and backing up as much digital data as possible."
        c "And if you point my PDA at the sky tonight, it should give all the information necessary to deflect it."
        show emera normal with dissolve
        Em "Thank you [player_name]. I will tell this new information to the council. You may leave."
        play sound "fx/door/doorclose.wav"
        scene corridor with fade
        show sebastian normal b with dissolve
        Sb "Well?"
        c "Sebastian, I think we can save this world."
        show sebastian smile b with dissolve
        Sb "That's great!"
        show sebastian normal b with dissolve
        Sb "You still need an escort though."
        scene black with fade
        nvl clear
        window show
        play music "mx/fun.ogg"
        n "As promised, that night, there were giant missiles near the portal, plus a detonator and a note."
        n "The note explained that the warheads were modified to explode at the same time when the detonator was activated."
        n "I kept the detonator in a safe place until it was time to deflect it."
        n "The dragons combined all their generators, while I helped set up the bombs."
        n "Then, the night came. The dragons covered my PDA and a few digital storage devices in lead blankets to protect them."
        n "Combining all their generators, They sent a high-energy laser towards the comet, causing it to burn up. Soon, the order was given to launch the nukes."
        n "When the scientists believed that the nukes were close enough, they told me to press the detonator."
        window hide
        nvl clear
        scene starsr with fade #use this after the detonation
        $ renpy.pause(2)
        window show
        n "There was no mushroom cloud released from the explosion. There was, however, a bright fireball that gave the sky a deep red glow."
        n "The red sky was mesmerizing in a way that could not be described with words."
        n "The laser continued, and after some time, stopped. The scientists declared the comet to be redirected."
        if adinedead == False:
            $ adinestatus = "neutral"
        if annadead == False:
            $ annastatus = "neutral"
        if loremdead == False:
            $ loremstatus = "neutral" #for some goddamn reason, neutral is actually "good" and "good" is impressed
        if remydead == False:
            $ remystatus = "neutral"
        $ brycestatus = "neutral" #you couldn't get here if he was dead, so there's no need to check a second time
        window hide
        nvl clear
        window show
        n "However, the incoming radiation did damage some unprotected infrastructure, and the generators were used up from redirecting the comet. \
            This caused an energy shortage, though it wasn't as severe as human society after the flare."
        n "Thanks to continued cooperation with the humans, though, the dragons made a great recovery."
        n "I've learned my lesson, and started to be more respectful to the dragons."
        n "And you, the player, should check the status screen. There's a surprise for you. ;)"
        nvl clear
        window hide
        scene black with fade
        stop music fadeout 1
        $ renpy.pause(1)
        call ml_ending_check("traitor_ending", "best", "You have seen the best ending! The deal can still go through.")
        play sound "fx/system3.wav"
        s "Dev note: I don't know how to create custom credits, but I can tell you this mod was a solo project."
        s "However, it could not have been possible without Core or MagmaLink. So special thanks to the developers of those tools."
        s "And of course, credit to Saunders for the base game."
        jump ml_main_menu #ends the mod and takes player to the main menu