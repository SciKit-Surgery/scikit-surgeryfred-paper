default : surgeryfred-paper.pdf

EXTERNALS = acronyms.tex \
	    spmpsci.bst \
	    surgeryfred-paper.bib \
	    spie.cls

INPUTS = surgeryfred-paper.tex \
	 abstract_250.tex \
	 introduction.tex \
	 methods.tex \
	 results.tex \
	 discussion.tex \
	 acknowledgements.tex \

FIGURES = 	

surgeryfred-paper.dvi : surgeryfred-paper.tex $(EXTERNALS) $(INPUTS) $(FIGURES)
	latex -halt-on-error surgeryfred-paper.tex 
	bibtex surgeryfred-paper
	latex -halt-on-error surgeryfred-paper
	latex -halt-on-error surgeryfred-paper

%.pdf : %.dvi
	dvipdf $<

%.eps : %.png
	convert $< $@

clean:
	rm *.acr *.aux *.dvi *.glo *.ist *.lof *.log *.lot *.toc *.pdf *.ps *.out *.blg *.bbl

