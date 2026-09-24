\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-c5"
  \melodyDefaults
  %\tempo 4 = 80
  % 1
  a\breve \hideNotes a4 a a \unHideNotes a4. g4 f g2 \bar "|"

  g\breve \hideNotes g4 g g \unHideNotes 
  \shape #'((0 . 0)(0 . 1.0)(0 . 1.0)(0 . 0)) Slur
  g4.( f4) g a2 \bar "|"

  bes\breve \hideNotes b4 b b \unHideNotes b4. g4 b a2 \bar "|"

  c\breve \hideNotes c4 c c \unHideNotes
  \shape #'((0 . 0)(0 . 0.75)(0 . 0.75)(0 . 0)) Slur
  c4.( a4) f g2 \bar "|"

  f\breve \hideNotes f4 f \unHideNotes f4. g4 g f2 \bar "|"

  g\breve \hideNotes g4 g g \unHideNotes g e c d2 \bar "||"

  % - - - -

  a'\breve \hideNotes a4 a a a \unHideNotes a4. a4 g f g2 \bar "|"

  g\breve \hideNotes g4 g g g \break g g \unHideNotes g4. f4 g a2 \bar "|"

  bes\breve \hideNotes b4 b b b b b \unHideNotes b g b a2 \bar "|"

  c\breve \hideNotes c4 c c c \unHideNotes c4. a4 f g2 \bar "|"

  f\breve \hideNotes f4 f f \unHideNotes f4. f4 g f2 \bar "|"

  g\breve \hideNotes g4 g g \unHideNotes
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
  qu -- um cla -- má -- ve -- ro ad te.

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
