\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "blackmensural-c5"
  \melodyDefaults
  %\tempo 4 = 80
  % 1
  f,4 c d 
  \shape #'((0 . 0)(0 . 1.5)(0 . 1.75)(0 . 0)) Slur
  d( a'4. bes4) a2 \bar "'"
  % 2
  a4 g f g4.( a4) a2 \bar "'"
  % 3
  a4 g f g d2 \bar "|"
  % 4
  g4 g a g f4. \bar "'"
  % 5
  e4( f) g f( e) d c( d) d2 \bar "|"
  % 6
  e4 c d f f e f g e g f( e) c( d) d2^\markup \sans "ret."( g) \bar "||"
  % 7
  a4 g a c( b) g4. g4 f g( a) a2 \bar "|"
  % 8
  a4 g f g( f) d f f( e) d( e) d c2 \bar "|"
  % 9
  d4 c d( f) f4.( g4) f e f g( a) f( e4.) \bar "'"
  % 10
  d2^\markup \sans "ret." d
  \fine
}

text = \lyricmode {
  %\markup { \concat { \fontsize #4 "A" \tied-lyric #"" "-" } }
  \markup { \concat { \fontsize #4 "A" } }
  % 1
  -- ve  Ma -- rí _ _ -- a
  % 2
  grá -- zi -- a ple _ -- na
  % 3
  Dò -- mi -- nus te -- cum;
  % 4
  be -- ne -- dìc -- ta tu
  % 5
  in __ _ mu -- li _ -- è -- ri _ -- bus,
  % 6
  et be -- ne -- dìc -- tus frûc -- tus ven -- tris tu -- i, __ _ Įe _ -- sus __ _
  % 7
  Sânc -- ta Ma -- rí _ -- a, Ma -- ter De _ -- i,
  % 8
  o -- ra pro no _ -- bīs pec -- ca _ -- tó _ -- ri -- bus
  % 9
  nunc et in __ _ ho _ -- ra mor -- tis nos _ -- trae. __ _
  % 10
  A -- men.
}

\header {
  title = "AVE MARÍA"
  opus = \markup { \sans \smallCaps "melódia oriģináli" }
  tagline = #f
}

\include "../template-post.ly"
