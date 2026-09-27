\version "2.26.0"
\include "../template-pre.ly"

raggedLastSetting = ##f

melody = \relative c' {
  \clef "petrucci-c4"
  \melodyDefaults

  d4 d4. d4 d4. d4 b4. b4 d2 \bar "|"

  c4 c c c4. c4 c c a4. a4 a a a b g g g g2 \fine
}

text = \lyricmode {

  De -- us, su -- sċèp -- tor me -- us es.
 
  De -- us me -- us, mi -- se -- ri -- còr -- di -- a e -- jus
  prae -- vè -- ni -- et me.

}

\header {
  title = "Versus et Responsorium"
  subtitle = \markup { \sans "Sabbatum" }
  opus = \markup { \sans "Tonus 7" }
  piece = \markup { \sans "Psalmus 58" }
  tagline = #f
}

\include "../template-post.ly"

\markup \vspace #2

\markup {
  \fill-line {
    \column {
      \line { "In tono sèptimo: " }

      \vspace #1

      \line { \sans\tiny "V, " "Deus, susċèptor meus es. Deus meus, misericòrdia ejus praevèniet me." }
      \line { \sans\tiny "R, " "Deus, susċèptor meus es. Deus meus, misericòrdia ejus praevèniet me." }

      \vspace #1

      \line { \sans\tiny "V. " "Éripe me de inimícis meis, Deus meus, et ab insurġèntibus in me líbera me." }
      \line { \sans\tiny "R, " "Deus, susċèptor meus es. Deus meus, misericòrdia ejus praevèniet me." }

      \vspace #1

      \line { \sans\tiny "V, " "Deus, susċèptor meus es." }
      \line { \sans\tiny "R, " "Deus meus, misericòrdia ejus praevèniet me." }
    }
  }
}
