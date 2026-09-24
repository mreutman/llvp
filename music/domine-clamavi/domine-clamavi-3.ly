\version "2.26.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "petrucci-c4"
  \melodyDefaults

  b\breve \hideNotes b4 b b \unHideNotes b4. c4 c b2 \bar "|"

  c\breve \hideNotes c4 c c \unHideNotes 
  \shape #'((0 . 0)(0 . 1.0)(0 . 1.0)(0 . 0)) Slur
  c4.( b4) a b2 \bar "|"

  d\breve \hideNotes d4 d d \unHideNotes d4. c4 a b2 \bar "|"

  c\breve \hideNotes c4 c c \unHideNotes
  \shape #'((0 . 0)(0 . 0.75)(0 . 0.75)(0 . 0)) Slur
  c4.( a4) c b2 \bar "|"

  g\breve \hideNotes g4 g \unHideNotes g4. g4 a g2 \bar "|"

  a\breve \hideNotes a4 a a \unHideNotes a g f e2 \bar "||"

  % - - - -

  b'\breve \hideNotes b4 b b b \unHideNotes b4. b4 b c b2 \bar "|"

  c\breve \hideNotes c4 c c c c \break c \unHideNotes c4. b4 a b2 \bar "|"

  d\breve \hideNotes d4 d d d d \unHideNotes d c a b b2 \bar "|"

  c\breve \hideNotes c4 c c c \unHideNotes c4. a4 c b2 \bar "|"

  g\breve \hideNotes g4 g g \unHideNotes g4. g4 a g2 \bar "|"

  a\breve \hideNotes a4 a a \unHideNotes
  \shape #'((0 . 0)(0 . 0.75)(-0.25 . 1.35)(0 . 0)) Slur
  a4.( g4) f e2
  
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
  opus = \markup { \sans "Tonus 3" }
  tagline = #f
}

\include "../template-post.ly"
