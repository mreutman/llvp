\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-c5"
  \melodyDefaults

  d,4 f4 f f f e4. d4 f f f2 \bar "|"

  a4 a4 a g g a4 f2 f \fine

}

text = \lyricmode {

  Au -- xì -- li -- um me -- um a Dò -- mi -- no,
  
  qvi fe -- ċit ċoe -- lum et ter -- ram.

}

\header {
  title = "Versus et Responsorium"
  subtitle = \markup { \sans "Feria Sexta" }
  opus = \markup { \sans "Tonus 6" }
  piece = \markup { \sans "Psalmus 120" }
  tagline = #f
}

\include "../template-post.ly"

\markup \vspace #2

\markup {
  \fill-line {
    \column {
      \line { "In tono sexto: " }

      \vspace #1

      \line { \sans\tiny "V, " "Auxìlium meum a Dòmino, qvi feċit ċoelum et terram." }
      \line { \sans\tiny "R, " "Auxìlium meum a Dòmino, qvi feċit ċoelum et terram." }

      \vspace #1

      \line { \sans\tiny "V. " "Levávi òculos meos in montes, unde vèniet auxìlium mìhi." }
      \line { \sans\tiny "R, " "Auxìlium meum a Dòmino, qvi feċit ċoelum et terram." }

      \vspace #1

      \line { \sans\tiny "V, " "Auxìlium meum a Dòmino." }
      \line { \sans\tiny "R, " "Qvi feċit ċoelum et terram." }
    }
  }
}
