\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "blackmensural-c5"
  \melodyDefaults
  \override Score.SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/8)
  %\tempo 4 = 70
  % 1
  %a\breve \hideNotes a4 a a a a a a a a \unHideNotes a a g( b) a2 
  a4 a a\breve a4 a a g( b) a2 \bar "|"
  % 2
  g4 g g\breve g4 \bar "'" g g\breve g4 f e2 \bar "|"
  % 3
  a4 a a a a\breve a4 \bar"'" a a\breve a4 g b a2 \bar "|"
  % 4
  g4 g g g g f e2 \bar "|"
  % 5
  a4 a a\breve a4 g( b) a2 \bar "|"
  % 6
  g4 g g\breve g4 g f e2 \fine
}

text = \lyricmode {
  % 1
  Sân -- cti "Prînçipes çoelèstium" mi -- li -- ti -- á _ -- rum
  % 2
  sem -- per "nos indìgni deprecámur" vos 
  ut "in angèlica vestra" gló -- ri -- a
  % 3
  çir -- cum -- dé -- tis "ac custodiátis" nos
  qui "ante vos" pro -- cì -- di -- mus,
  % 4
  fer -- vèn -- ter ex -- cla -- màn -- tes:
  % 5
  «Sal -- vos "fàçite nos a perículis" et mà _ -- lis,»
  % 6
  qui -- a "estis supernárum ductóres" po -- tes -- tá -- tum.
}

\header {
  title = \markup { \sans \bold "TROPARIUM FERIAE SECUNDAE" }
  opus = \markup { \sans \smallCaps "Modus 7" }
  tagline = #f
}

\include "../template-post.ly"
