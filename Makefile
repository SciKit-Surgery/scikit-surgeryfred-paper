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

FIGURES = scikit-surgeryfred_gui.eps \
	  usability.eps \
	  images/default.eps \
	  dependency_graph.eps \
	  images/anisitropic_error.eps \
	  images/systematic_error.eps

FIGURES_PNG = scikit-surgeryfred_gui.png \
	      usability.png \
	      images/default.png \
	      dependency_graph.png \
	      images/anisitropic_error.png \
	      images/systematic_error.png


surgeryfred-paper.dvi : surgeryfred-paper.tex $(EXTERNALS) $(INPUTS) $(FIGURES)
	latex -halt-on-error surgeryfred-paper.tex 
	bibtex surgeryfred-paper
	latex -halt-on-error surgeryfred-paper
	latex -halt-on-error surgeryfred-paper

build/surgeryfred-paper.html : surgeryfred-paper.tex $(EXTERNALS) $(INPUTS) $(FIGURES_PNG)
	latex -halt-on-error surgeryfred-paper.tex
	bibtex surgeryfred-paper
	htlatex surgeryfred-paper.tex "html,html5, charset=utf-8" " -cunihtf -utf8" 
	mv surgeryfred-paper*.html build/
	mv surgeryfred-paper.4ct surgeryfred-paper.4tc build/
	mv surgeryfred-paper.css surgeryfred-paper.idv build/
	mv surgeryfred-paper.lg build/
	mv surgeryfred-paper.tmp surgeryfred-paper.xref build/
	cp $(FIGURES_PNG) build/
	mkdir build/images
	mv build/default.png build/anisitropic_error.png build/systematic_error.png build/images

%.pdf : %.dvi
	dvipdf $<

%.eps : %.png
	convert $< $@

%.png : %.eps 
	gs -dSAFER -dEPSCrop -r600 -sDEVICE=pngalpha -o $@ $<

%.eps : %.dot
	dot -Tps $< -o $@

dependency_graph.dot :
	wget https://github.com/UCL/scikit-surgeryfred/raw/master/doc/dependency_graph.dot

clean:
	rm *.acr *.aux *.dvi *.glo *.ist *.lof *.log *.lot *.toc *.pdf *.ps *.out *.blg *.bbl build/surgeryfred-paper* build/*.png 
	rm -r build/images

