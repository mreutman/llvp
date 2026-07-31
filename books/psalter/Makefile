DIR_TMP := ./tmp
DIR_ORA := ./text/prayers

TXT2TEX := ./scripts/txt2tex

define fntxt2tex
    $(eval $@_FILENAME = $(1))
    $(eval $@_CMDARGS  = $(2))
    $(TXT2TEX) $($@_CMDARGS) $(DIR_ORA)/$($@_FILENAME).txt \
        > $(DIR_TMP)/$($@_FILENAME).tex
endef

all: latex pdf

latex:
	mkdir -p $(DIR_TMP)

	$(call fntxt2tex, gloria-tibi, )
	$(call fntxt2tex, gloria-patri, -a)
	$(call fntxt2tex, labia-mea-aperies, -f)
	$(call fntxt2tex, pater-noster, -f -a)
	$(call fntxt2tex, per-oraziones-sanctorum-patrum, -f -a)
	$(call fntxt2tex, sanctus, )
	$(call fntxt2tex, sanctissima-trinitas, )

	./text/psalmi/generate-tex-psalmi.py > $(DIR_TMP)/psalmi.tex
	./text/cantica/generate-tex-cantica.py > $(DIR_TMP)/cantica.tex

pdf:
	xelatex -halt-on-error -shell-escape ./psalter.tex

clean:
	rm -rfv tmp
	rm -fv psalter.aux
	rm -fv psalter.log
	rm -fv psalter.pdf
	rm -fv psalter.log
