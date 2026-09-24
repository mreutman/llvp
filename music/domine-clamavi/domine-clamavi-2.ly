\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-f"
  \melodyDefaults
  %\tempo 4 = 80
  % 1
  \allowBreak
  d,\breve \hideNotes d4 d d d \unHideNotes d c d2 \bar "|"

  f\breve \hideNotes f4 f f \unHideNotes
  \shape #'((0 . 0)(0 . 0.75)(0 . 0.75)(0 . 0)) Slur
  f( e) d e2 \bar "|"

  f\breve \hideNotes f4 f f \unHideNotes f e f g2 \bar "|"
  f\breve \hideNotes f4 f f \unHideNotes f( d) f e2 \bar "|"
  d\breve \hideNotes d4 d \unHideNotes d a c d2 \bar "|"
  e\breve \hideNotes e4 e e e \unHideNotes e c d2 \bar "||"

  % - - - - -

  d\breve \hideNotes d4 d d d d d \unHideNotes d c d2 \bar "|"
  f\breve \hideNotes f4 f f f f f \unHideNotes f e d e2 \bar "|"
  f\breve \hideNotes f4 f f f f f \unHideNotes f e f g2 \bar "|"
  f\breve \hideNotes f4 f f f \unHideNotes f d f e2 \bar "|"
  d\breve \hideNotes d4 d d \unHideNotes d a c d2 \bar "|"
  e\breve \hideNotes e4 e e \unHideNotes e c d2 \bar "||"
  
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
  ex -- áu -- di me, Dò -- mi -- ne.
}

\header {
  title = "Domine Clamavi"
  opus = \markup { \sans "Tonus 2" }
  tagline = #f
}

\include "../template-post.ly"
