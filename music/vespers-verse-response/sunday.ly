\version "2.26.0"
\include "../template-pre.ly"

raggedLastSetting = ##f

melody = \relative c' {
  \clef "petrucci-c5"
  \melodyDefaults

  f,4. f4 e4. d4 f4. f2 \bar "|"

  d4 a'4. a4 a g4. a4 f2 \fine
}

text = \lyricmode {
  Dò -- mi -- nus reg -- ná -- vit,
  
  de -- cór -- em in -- dú -- tus est.
}

\header {
  title = "Versus et Responsorium"
  subtitle = \markup { \sans "Dominica" }
  opus = \markup { \sans "Tonus 6" }
  piece = \markup { \sans "Psalmus 92" }
  tagline = #f
}

\include "../template-post.ly"

\markup \vspace #2

\markup {
  \fill-line {
    \column {
      \line { "In tono sexto: " }

      \vspace #1

      \line { \sans\tiny "V, " "Dòminus regnávit, decórem indútus est." }
      \line { \sans\tiny "R, " "Dòminus regnávit, decórem indútus est." }

      \vspace #1

      \line { \sans\tiny "V. " "Indútus est Dòminus fortitúdinem, et praeċînxit se." }
      \line { \sans\tiny "R, " "Dòminus regnávit, decórem indútus est." }

      \vspace #1

      \line { \sans\tiny "V. " "Ètenim firmávit orbem terrae, qui non commovébitur." }
      \line { \sans\tiny "R, " "Dòminus regnávit, decórem indútus est." }

      \vspace #1

      \line { \sans\tiny "V. " "Dòmum tuam dèċet sanctitúdo, Dòmine, in longitúdinem diérum." }
      \line { \sans\tiny "R, " "Dòminus regnávit, decórem indútus est." }

      \vspace #1

      \line { \sans\tiny "V, " "Dòminus regnávit." }
      \line { \sans\tiny "R, " "Decórem indútus est." }
    }
  }
}
