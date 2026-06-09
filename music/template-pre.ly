#(ly:font-config-add-font "/home/anon/Git/studium-sancti-johannis-cassiani/text/books/common/env/fonts/dueblo/mod1/Dueblo-SEMI-EXT-MED.otf")

#(ly:font-config-add-font "/home/anon/Git/studium-sancti-johannis-cassiani/text/books/common/env/fonts/dueblo/mod1/Dueblo-SEMI-EXT-REG.otf")

\paper {
  #(define fonts
    (set-global-fonts
     #:roman "Dueblo SemiSerif Extended Medium"
     #:sans "Dueblo SemiSerif Extended Regular"
    ))

  #(set-paper-size "letter")
  top-margin = 0.5\in
  bottom-margin = 0.5\in
  left-margin = 1.0\in
  right-margin = 1.0\in

  score-system-spacing.padding = #5

  system-system-spacing = #'((basic-distance . 13)) % vertical spacing
  ragged-bottom = ##t
}

melodyDefaults = {
  \key c \major
  \time 4/4
  \cadenzaOn
  \dynamicUp
  \omit Staff.TimeSignature
  \override Staff.BarLine.hair-thickness = #3
  \override Staff.BarLine.thick-thickness = #6
  \omit Stem
  %\override Stem.length = #5
  \override Stem.thickness = #1
  \override Lyrics.LyricSpace.minimum-distance = #3.0
  \set melismaBusyProperties = #'()
  %\override NoteHead.style = #'neomensural
  %\override Flag.stencil = #old-straight-flag
  %\override Score.SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/8)
}
