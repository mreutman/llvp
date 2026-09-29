\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-c5"
  \melodyDefaults

  g4 g g4. g4 g g4. e4 e4. e4 f g2 \bar "|"  \break

  a4 a a4. a b b g2 \fine
}

text = \lyricmode {
  Ec -- ċe nunc be -- ne -- dí -- ċi -- te Dò -- mi -- num,

  om -- nes ser -- vi Dò -- mi -- ni.
}

\header {
  title = "Versus et Responsorium"
  subtitle = \markup { \sans "Feria Secunda" }
  opus = \markup { \sans "Tonus 8" }
  piece = \markup { \sans "Psalmus 133" }
  tagline = #f
}

\include "../template-post.ly"

\markup \vspace #2

\markup {
  \fill-line {
    \column {
      \line { "In tono octávo: " }

      \vspace #1

      \line { \sans\tiny "V, " "Ecċe nunc benedíċite Dòminum, omnes servi Dòmini." }
      \line { \sans\tiny "R, " "Ecċe nunc benedíċite Dòminum, omnes servi Dòmini." }

      \vspace #1

      \line { \sans\tiny "V. " "Qvi statis in dòmu Dòmini, in átriis dòmůs Dei nostri." }
      \line { \sans\tiny "R, " "Ecċe nunc benedíċite Dòminum, omnes servi Dòmini." }

      \vspace #1

      \line { \sans\tiny "V, " "Ecċe nunc benedíċite Dòminum." }
      \line { \sans\tiny "R, " "Omnes servi Dòmini." }
    }
  }
}
