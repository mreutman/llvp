\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-c5"
  \melodyDefaults
  %\tempo 4 = 80
  % 1
  a4 a a a a4. g4 f g2 \bar "|"

  g4 g g g 
  \shape #'((0 . 0)(0 . 1.0)(0 . 1.0)(0 . 0)) Slur
  g4.( f4) g a2 \bar "|"

  bes4 b b b b4. g4 b a2 \bar "|"

  c4 c c c
  \shape #'((0 . 0)(0 . 0.75)(0 . 0.75)(0 . 0)) Slur
  c4.( a4) f g2 \bar "|"

  f4 f f f4. g4 g f2 \bar "|"

  g4 g g g g e c d2 \bar "||"

  % - - - -

  a'4 a a a a a4. a4 g f g2 \bar "|"

  g4 g g g4. g4 \break g g g4. f4 g a2 \bar "|"

  bes4 b b b b b b b g b a2 \bar "|"

  c4 c c c c c4. a4 f g2 \bar "|"

  f4 f f f f4. f4 g f2 \bar "|"

  g4 g g g
  \shape #'((0 . 0)(0 . 0.75)(-0.25 . 1.35)(0 . 0)) Slur
  g4.( e4) c d2 \bar "||"
  
  \fine
}

text = \lyricmode {
  Dò -- mi -- ne, cla -- má -- vi ad te;
  ex -- áu -- di me, Dò _ -- mi -- ne.
  Dò -- mi -- ne, cla -- má -- vi ad te;
  ex -- áu -- di me, Dò _ -- mi -- ne.
  In -- tèn -- de vo -- ċi me -- ae,
  qv -- um cla -- má -- ve -- ro ad te.

  Di -- ri -- ġá -- tur or -- á -- zi -- o me -- a
  si -- cut in -- ċèn -- sum in con -- spèc -- tu tu -- o;
  e -- le -- vá -- zi -- o mà -- nu -- um me -- á -- rum
  sa -- cri -- fì -- ċi -- um ves -- per -- tí -- num.
  Dò -- mi -- ne, cla -- má -- vi ad te;
  ex -- áu -- di me, Dò _ -- mi -- ne.
}

\header {
  title = "Domine Clamavi"
  opus = \markup { \sans "Tonus 1" }
  tagline = #f
}

\include "../template-post.ly"
