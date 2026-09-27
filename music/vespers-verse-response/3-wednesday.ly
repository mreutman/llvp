\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-c5"
  \melodyDefaults

  a\breve \hideNotes a4 a a a a a a a a\unHideNotes a g4 f g4. g4 g2 \bar "|"

  g\breve \hideNotes g4 g g g g \unHideNotes g e c d2 \fine
}

text = \lyricmode {
  Dò -- mi -- ne, mi -- se -- ri -- còr -- di -- a tu -- a
  sub -- se -- qvé -- tur me
  
  òm -- ni -- bus di -- é -- bus vi -- tae me -- ae.
}

\header {
  title = "Versus et Responsorium"
  subtitle = \markup { \sans "Feria Qvarta" }
  opus = \markup { \sans "Tonus 1" }
  piece = \markup { \sans "Psalmus 2" }
  tagline = #f
}

\include "../template-post.ly"

\markup \vspace #2

% 3. Block of Stanzas / Text Below
\markup {
  \fill-line {
    \column {
      \line { "In tono primo: " }

      \vspace #1

      \line { \sans\tiny "V, " "Dòmine, misericòrdia tua subseqvétur me, òmnibus diébus vitae meae." }
      \line { \sans\tiny "R, " "Dòmine, misericòrdia tua subseqvétur me, òmnibus diébus vitae meae." }

      \vspace #1

      \line { \sans\tiny "V. " "Dòminus rèġit me, et nìhil déerit mìhi. In loco pâscuae ìbi me collocávit." }
      \line { \sans\tiny "R. " "Dòmine, misericòrdia tua subseqvétur me, òmnibus diébus vitae meae." }

      \vspace #1

      \line { \sans\tiny "V. " "Dòmine, misericòrdia tua subseqvétur me." }
      \line { \sans\tiny "R. " "Òmnibus diébus vitae meae." }
    }
  }
}
