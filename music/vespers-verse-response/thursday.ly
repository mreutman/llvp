\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-c4"
  \melodyDefaults

  c4 c4. c4 a a a a a c c c c \bar "|"  \break

  a4 a a g4. g4 g a f4. f4 f f2 \fine
}

text = \lyricmode {
  De -- us, in nó -- mi -- ne tu -- o sal -- vum me fac,
  
  et in vir -- tú -- te tu -- a jú -- di -- ca me.
}

\header {
  title = "Versus et Responsorium"
  subtitle = \markup { \sans "Feria Qvinta" }
  opus = \markup { \sans "Tonus 5" }
  piece = \markup { \sans "Psalmus 53" }
  tagline = #f
}

\include "../template-post.ly"

\markup \vspace #2

\markup {
  \fill-line {
    \column {
      \line { "In tono qvinto: " }

      \vspace #1

      \line { \sans\tiny "V, " "Deus, in nómine tuo salvum me fac, et in virtúte tua júdica me." }
      \line { \sans\tiny "R, " "Deus, in nómine tuo salvum me fac, et in virtúte tua júdica me." }

      \vspace #1

      \line { \sans\tiny "V. " "Deus exáudi oraziónem meam; áuribus pèrċipe verba oris mei." }
      \line { \sans\tiny "R, " "Deus, in nómine tuo salvum me fac, et in virtúte tua júdica me." }

      \vspace #1

      \line { \sans\tiny "V, " "Deus, in nómine tuo salvum me fac." }
      \line { \sans\tiny "R, " "Et in virtúte tua júdica me." }
    }
  }
}
