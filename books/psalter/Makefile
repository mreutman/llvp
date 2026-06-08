all: latex pdf

latex:
	./text/psalmi/generate-tex-psalmi.py > generated-psalmi.tex
	./text/cantica/generate-tex-cantica.py > generated-cantica.tex

pdf:
	xelatex -halt-on-error -shell-escape ./psalter.tex

clean:
	rm -fv generated-psalmi.tex
	rm -fv generated-cantica.tex
	rm -fv psalter.aux
	rm -fv psalter.log
	rm -fv psalter.pdf
	rm -fv psalter.log
