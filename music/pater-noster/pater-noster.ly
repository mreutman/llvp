\version "2.24.0"
\include "../template-pre.ly"

melody = \relative c' {
  \clef "blackmensural-c4"
  \melodyDefaults
  % 1
  g4 a b b4. \bar "'"
  % 2
  a4 c b a g2 \bar ","
  % 3
  a4 g a b a( g) g( a) b a( b) a2 \bar "|"
  % 4
  b4 c b b a b a g2 \bar ","
  % 5
  b4 b a b a a g2 \bar ","
  % 6
  a4 g a b a( g) g( a) b a( b) a2 \bar "|"
  % 7
  g4 a b b4. \bar "'"
  % 8
  b4 a b c b4. \bar "'"
  % 9
  b4 a b a g g2 \bar "|"
  % 10
  a4 g a b c b b a b a g2 \bar ","
  % 11
  a4 g a b a b a a g a b a g a a2 \bar "|"
  % 12
  e4 g a a b a a a g a a( g) g2 \bar "|"
  % 13
  g4 a a a a b a^\markup \sans "ret."( g) g2 \fine
}

text = \lyricmode {
  \markup { \concat { \fontsize #4 "P" \tied-lyric #"" "a" } }
  -- ter nos -- ter                                                      % 1

  qui es in çoe -- līs,                                               % 2

  san -- cti -- fi -- cé -- tur __ _ no _ -- men tu _ -- um;                       % 3

  ad -- vèn -- i -- at rêg -- num tu -- um;                                   % 4

  fi -- at vo -- lùn -- tas tu -- a,                                        % 5

  si -- cut in çoe -- lo __ _ et __ _ in ter _ -- ra.                           % 6

  Pa -- nem nos -- trum                                                 % 7

  quo -- ti -- di -- á -- num                                               % 8

  da no -- bīs hó -- di -- e;                                             % 9

  et di -- mìt -- te no -- bīs dé -- bi -- ta nos -- tra,                       % 10

  si -- cut et nos di -- mìt -- ti -- mus de -- bi -- tó -- ri -- bus nos -- trīs,    % 11

  et ne nos in -- dú -- ças in temp -- ta -- zi -- ó _ -- nem,                  % 12

  sed lí -- be -- ra nos a Mà _ -- lo.                                    % 13
}

\header {
  title = "PÀTER NOSTER"
  opus = \markup { \sans \smallCaps "melódia oriģináli" }
  tagline = #f
}

\include "../template-post.ly"
