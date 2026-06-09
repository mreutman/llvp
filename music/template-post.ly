\markup \vspace #1

\score {
  <<
    \new Voice = "one" { 
      \autoBeamOff
      %\slurUp
      %\stemUp
      \melody
    }
    \new Lyrics \lyricsto "one" \text
  >>
  \layout { 
    indent = 0\mm
    ragged-last = ##t
    \context {
      \Score
      \override TextScript.font-shape = #'caps
      \override LyricText.font-shape = #'caps
      \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/16)
      \accidentalStyle forget
    }
  }
  \midi { }
}
