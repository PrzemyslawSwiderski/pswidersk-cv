import pypandoc
import pytinytex

pytinytex.download_tinytex()

pypandoc.convert_file('src/CV.md', 'pdf', outputfile='build/CV.pdf')
# pypandoc.convert_file('src/CV.tex', 'pdf', outputfile='build/CV.pdf')