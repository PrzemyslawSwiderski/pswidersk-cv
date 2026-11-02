import os

import pypandoc
import pytinytex

pytinytex.download_tinytex()

INPUT_MD_FILE = 'src/CV.md'
OUTPUT_DIR = 'build/CV'
OUTPUT_PREFIX = 'Przemyslaw_Swiderski_CV'

os.makedirs(OUTPUT_DIR, exist_ok=True)

pypandoc.convert_file(INPUT_MD_FILE, 'pdf', outputfile=f'{OUTPUT_DIR}/{OUTPUT_PREFIX}.pdf')
pypandoc.convert_file(INPUT_MD_FILE, 'docx', outputfile=f'{OUTPUT_DIR}/{OUTPUT_PREFIX}.docx')
pypandoc.convert_file(INPUT_MD_FILE, 'html', outputfile=f'{OUTPUT_DIR}/{OUTPUT_PREFIX}.html')
