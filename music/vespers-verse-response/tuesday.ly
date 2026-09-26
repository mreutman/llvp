\version "2.26.0"
\include "../template-pre.ly"

raggedLastSetting = ##f

melody = \relative c' {
  \clef "petrucci-c5"
  \melodyDefaults

  a\breve \hideNotes a4 a \unHideNotes a e4. g4 g a2 \bar "|"

  a\breve \hideNotes a4 a a \unHideNotes a g4. a4 a e2 \fine
}

text = \lyricmode {
  Dò -- mi -- nus ex -- áu -- di -- et me
  
  qv -- um cla -- má -- ve -- ro ad e -- um.
}

\header {
  title = "Versus et Responsorium"
  subtitle = \markup { \sans "Feria Tertzia" }
  opus = \markup { \sans "Tonus 4" }
  piece = \markup { \sans "Psalmus 4" }
  tagline = #f
}

\include "../template-post.ly"

\markup \vspace #2

\markup {
  \fill-line {
    \column {
      \line { "In tono qvarto: " }

      \vspace #1

      \line { \sans\tiny "V, " "Dòminus exáudiet me, qvum clamávero ad eum." }
      \line { \sans\tiny "R, " "Dòminus exáudiet me, qvum clamávero ad eum." }

      \vspace #1

      \line { \sans\tiny "V. " "Qvum invocárem, exaudívit me Deus justìzziae meae." }
      \line { \sans\tiny "R, " "Dòminus exáudiet me, qvum clamávero ad eum." }

      \vspace #1

      \line { \sans\tiny "V, " "Dòminus exáudiet me." }
      \line { \sans\tiny "R, " "Qvum clamávero ad eum." }
    }
  }
}
