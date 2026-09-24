#(ly:font-config-add-font "/home/anon/Git/llvp/books/common/fonts/KJV1611/KJV1611-Regular.otf")
#(ly:font-config-add-font "/home/anon/Git/llvp/books/common/fonts/EBGaramond/static/EBGaramond-Regular.ttf")
#(ly:font-config-add-font "/home/anon/Git/llvp/books/common/fonts/EBGaramond/static/EBGaramond-Italic.ttf")

#(ly:font-config-display-fonts)

\paper {
  % New property assignment syntax for 2.24+
  property-defaults.fonts.serif = "KJV1611"
  property-defaults.fonts.sans  = "EBGaramond"
  property-defaults.fonts.typewriter = "monospace"

  top-margin = 0.5\in
  bottom-margin = 0.5\in
  left-margin = 1.0\in
  right-margin = 1.0\in

  score-system-spacing.padding = #5
  system-system-spacing = #'((basic-distance . 13))
  ragged-bottom = ##t
}

melodyDefaults = {
  \key c \major
  \time 4/4
  \cadenzaOn
  %\dynamicUp
  \stemNeutral
  \omit Staff.TimeSignature
  \set melismaBusyProperties = #'()
  \override Staff.BarLine.hair-thickness = #3
  \override Staff.BarLine.thick-thickness = #6
  \override Stem.thickness = #1
  \override Lyrics.LyricSpace.minimum-distance = #3.0
  \override NoteHead.style = #'petrucci
  \override Staff.Rest.style = #'neomensural
  %\override Score.SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/8)
}
