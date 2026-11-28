#(ly:font-config-add-font "/home/anon/Git/llvp/books/common/fonts/CormorantUpright2/CormorantUpright2-Regular.ttf")
#(ly:font-config-add-font "/home/anon/Git/llvp/books/common/fonts/EBGaramond/static/EBGaramond-Regular.ttf")
#(ly:font-config-add-font "/home/anon/Git/llvp/books/common/fonts/EBGaramond/static/EBGaramond-Italic.ttf")

%#(ly:font-config-display-fonts)

\paper {
  % New property assignment syntax for 2.24+
  property-defaults.fonts.serif = "CormorantUpright2"
  property-defaults.fonts.sans  = "EBGaramond"
  property-defaults.fonts.typewriter = "monospace"

  top-margin = 0.5\in
  bottom-margin = 0.5\in
  left-margin = 1.0\in
  right-margin = 1.0\in

  score-system-spacing.padding = #5
  system-system-spacing = #'((basic-distance . 13))
  %ragged-bottom = ##t
}

melodyDefaults = {
  \key c \major
  \time 4/4
  \cadenzaOn
  %\dynamicUp
  \stemNeutral
  \omit Staff.TimeSignature
  %\omit Stem
  \set melismaBusyProperties = #'()
  \override Staff.BarLine.hair-thickness = #3
  \override Staff.BarLine.thick-thickness = #6
  \override Stem.thickness = #1
  \override Lyrics.LyricSpace.minimum-distance = #2.0
  %\override NoteHead.style = #'petrucci
  \override Staff.Rest.style = #'neomensural
}

% Default to ##t across all scores
raggedLastSetting = ##t
