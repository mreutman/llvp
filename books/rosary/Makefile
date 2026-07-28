all: tex pdf

DIR_TMP := ./tmp
DIR_ORA := ./text/prayers

TXT2TEX := ./scripts/txt2tex

tex:
	mkdir -p $(DIR_TMP)
	$(TXT2TEX) -f -a $(DIR_ORA)/ave-maria.txt > $(DIR_TMP)/ave-maria.tex
	$(TXT2TEX) -f    $(DIR_ORA)/axion-estin.txt > $(DIR_TMP)/axion-estin.tex
	$(TXT2TEX)    -a $(DIR_ORA)/gloria-patri.txt > $(DIR_TMP)/gloria-patri.tex
	$(TXT2TEX)       $(DIR_ORA)/gloria-tibi.txt > $(DIR_TMP)/gloria-tibi.tex
	$(TXT2TEX) -f    $(DIR_ORA)/labia-mea-aperies.txt > $(DIR_TMP)/labia-mea-aperies.tex
	$(TXT2TEX) -f -a $(DIR_ORA)/pater-noster.txt > $(DIR_TMP)/pater-noster.tex
	$(TXT2TEX) -f -a $(DIR_ORA)/per-oraziones-sanctorum-patrum.txt > $(DIR_TMP)/per-oraziones-sanctorum-patrum.tex
	$(TXT2TEX) -f    $(DIR_ORA)/salve-regina.txt > $(DIR_TMP)/salve-regina.tex
	$(TXT2TEX) -f -a $(DIR_ORA)/symbolum-apostolorum.txt > $(DIR_TMP)/symbolum-apostolorum.tex
	
	./text/rosarium/generate-rosarium.py \
		./text/rosarium/rosarium.csv > $(DIR_TMP)/rosarium.tex 

pdf:
	xelatex -halt-on-error -shell-escape ./rosary.tex

clean:
	rm -fv generated
	rm -fv rosary.aux
	rm -fv rosary.log
	rm -fv rosary.pdf
	rm -fv rosary.log
