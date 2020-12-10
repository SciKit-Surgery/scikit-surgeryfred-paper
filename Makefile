default : surgeryfred-paper.pdf

EXTERNALS = acronyms.tex \
	    spmpsci.bst \
	    surgeryfred-paper.bib \
	    spie.cls

INPUTS = surgeryfred-paper.tex \
	 abstract_250.tex \
	 introduction.tex \
	 methods.tex \
	 implementation.tex \
	 other_errors.tex \
	 results.tex \
	 discussion.tex \
	 acknowledgements.tex \

FIGURES = scikit-surgeryfred_gui.eps \
	  usability.eps \
	  images/default.eps \
	  dependency_graph.eps \
	  images/anisitropic_error.eps \
	  images/systematic_error.eps

surgeryfred-paper.dvi : surgeryfred-paper.tex $(EXTERNALS) $(INPUTS) $(FIGURES)
	latex -halt-on-error surgeryfred-paper.tex 
	bibtex surgeryfred-paper
	latex -halt-on-error surgeryfred-paper
	latex -halt-on-error surgeryfred-paper

%.pdf : %.dvi
	dvipdf $<

%.eps : %.png
	convert $< $@

%.eps : %.dot
	dot -Tps $< -o $@

dependency_graph.dot :
	wget https://github.com/UCL/scikit-surgeryfred/raw/master/doc/dependency_graph.dot

clean:
	rm *.acr *.aux *.dvi *.glo *.ist *.lof *.log *.lot *.toc *.pdf *.ps *.out *.blg *.bbl

